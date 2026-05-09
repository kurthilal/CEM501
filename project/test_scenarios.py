from __future__ import annotations

import json
import logging
from dataclasses import replace
from datetime import datetime
from pathlib import Path

from .classifier import classify_with_fallback_rules
from .contracts import EmailMessage
from .drafter import draft_reply
from .logging_setup import setup_logging
from .memory import default_memory


log = logging.getLogger("test_scenarios")


def _load_fixture(path: Path) -> EmailMessage:
    data = json.loads(path.read_text(encoding="utf-8"))
    dt = datetime.fromisoformat(data["date"]) if data.get("date") else None
    return EmailMessage(
        message_id=None,
        from_email=data.get("from_email"),
        from_name=data.get("from_name"),
        subject=data["subject"],
        date=dt,
        body_text=data["body_text"],
        snippet=data["body_text"][:200],
        raw_headers={},
        thread_key=(data.get("from_email") or "") + "|" + data["subject"],
    )


def run() -> None:
    setup_logging(log_path=Path(__file__).parent / "logs" / "test_log.txt", verbose=False)
    mem = default_memory()

    fixtures_dir = Path(__file__).parent / "fixtures"
    fixture_paths = [
        fixtures_dir / "scenario_urgent.json",
        fixtures_dir / "scenario_action_rfi.json",
        fixtures_dir / "scenario_fyi_update.json",
    ]

    for fp in fixture_paths:
        msg = _load_fixture(fp)
        contact = mem.get_contact_by_email(msg.from_email) if msg.from_email else None
        if not contact:
            mem.upsert_contact(name=msg.from_name or "Unknown", email=msg.from_email)
            contact = mem.get_contact_by_email(msg.from_email) if msg.from_email else None

        contact_id = contact.id if contact else None
        mem.log_message(contact_id=contact_id, direction="received", subject=msg.subject, body=msg.body_text, channel="email", sent_at=msg.date or datetime.utcnow())

        classification = classify_with_fallback_rules(msg)
        draft = draft_reply(msg=msg, classification=classification, mem=mem, contact=contact)

        mem.log_message(contact_id=contact_id, direction="sent", subject=draft.subject, body=draft.body_text, channel="email", sent_at=datetime.utcnow())

        if classification.category == "URGENT":
            mem.schedule_task(description=f"Follow up urgently on: {msg.subject}", due_at=datetime.utcnow(), contact_id=contact_id)
        elif classification.category == "ACTION":
            mem.schedule_task(description=f"Follow up on action item: {msg.subject}", due_at=datetime.utcnow(), contact_id=contact_id)

        log.info("scenario=%s category=%s urgency=%s kind=%s tone=%s", fp.name, classification.category, classification.urgency, classification.kind, draft.tone_preset)
        log.info("draft_subject=%r", draft.subject)
        log.info("draft_body_preview=%r", draft.body_text[:240])

    log.info("done scenarios=3")


if __name__ == "__main__":
    run()

