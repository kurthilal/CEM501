from __future__ import annotations

import argparse
import logging
from datetime import datetime, timedelta

from .classifier import classify_with_fallback_rules
from .contracts import Draft, EmailMessage
from .drafter import draft_reply
from .logging_setup import setup_logging
from .memory import default_memory
from .reader import read_recent_emails
from .sender import send_email
from .telegram_channel import send_draft_notification


log = logging.getLogger("agent")


def process_once(*, dry_run: bool = True, max_emails: int = 5, telegram_review: bool = False) -> list[Draft]:
    mem = default_memory()
    drafts: list[Draft] = []

    emails = read_recent_emails(n=max_emails)
    for msg in emails:
        contact = mem.get_contact_by_email(msg.from_email) if msg.from_email else None
        if not contact:
            contact_id = mem.upsert_contact(
                name=msg.from_name or (msg.from_email or "Unknown"),
                email=msg.from_email,
                role=None,
                company=None,
                culture_region=None,
                preferred_tone=None,
            )
            contact = mem.get_contact_by_email(msg.from_email) if msg.from_email else None
        contact_id = contact.id if contact else None

        mem.log_message(
            contact_id=contact_id,
            direction="received",
            subject=msg.subject,
            body=msg.body_text[:4000],
            channel="email",
            sent_at=msg.date or datetime.utcnow(),
        )

        classification = classify_with_fallback_rules(msg)
        draft = draft_reply(msg=msg, classification=classification, mem=mem, contact=contact)
        drafts.append(draft)

        if classification.category == "URGENT":
            mem.schedule_task(
                description=f"Follow up urgently on: {msg.subject}",
                due_at=datetime.utcnow() + timedelta(hours=2),
                contact_id=contact_id,
            )
        elif classification.category == "ACTION":
            mem.schedule_task(
                description=f"Follow up on action item: {msg.subject}",
                due_at=datetime.utcnow() + timedelta(hours=48),
                contact_id=contact_id,
            )

        if telegram_review:
            try:
                send_draft_notification(draft=draft, mem=mem, contact_id=contact_id)
                log.info("telegram_review_notified to=%s subject=%r", draft.to_email, draft.subject)
            except Exception as e:
                log.warning("telegram_review_failed err=%r", e)

        if not dry_run and draft.to_email:
            send_email(to_email=draft.to_email, subject=draft.subject, body_text=draft.body_text)
            mem.log_message(
                contact_id=contact_id,
                direction="sent",
                subject=draft.subject,
                body=draft.body_text[:4000],
                channel="email",
                sent_at=datetime.utcnow(),
            )
            log.info("sent_email to=%s subject=%r", draft.to_email, draft.subject)
        else:
            log.info("drafted dry_run=%s to=%s subject=%r", dry_run, draft.to_email, draft.subject)

    return drafts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true", help="Process once then exit.")
    ap.add_argument("--dry-run", action="store_true", help="Draft/store but do not send.")
    ap.add_argument("--telegram-review", action="store_true", help="Send draft to Telegram for human review (optional).")
    ap.add_argument("--max-emails", type=int, default=5)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    setup_logging(log_path=(__file__.replace("agent.py", "logs/agent.log")), verbose=args.verbose)

    if args.once:
        process_once(dry_run=(True if args.dry_run else False), max_emails=args.max_emails, telegram_review=args.telegram_review)
        return

    # Default behavior: single pass for now (scheduler.py provides looped automation).
    process_once(dry_run=(True if args.dry_run else False), max_emails=args.max_emails, telegram_review=args.telegram_review)


if __name__ == "__main__":
    main()
