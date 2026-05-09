from __future__ import annotations

import json
import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

from .contracts import ClassificationResult, Draft, EmailMessage
from .memory import Contact, Memory
from .tone import choose_tone, render_greeting, render_signoff


_SYSTEM = """You draft professional construction-management communications.
You will be given:
- an incoming message (subject/body)
- a classification (category/urgency/kind)
- optional contact metadata and brief message history
- a tone profile (greeting/signoff + style notes)

Write a reply email body (plain text). Keep it actionable and realistic for CEM work.
If information is missing, ask 1-3 specific questions.
Do not invent project facts (dates, drawing numbers, spec sections) unless provided.
Return ONLY valid JSON with keys: subject, body_text.
"""


def _client() -> Anthropic:
    load_dotenv()
    key = os.environ["ANTHROPIC_API_KEY"]
    return Anthropic(api_key=key)


def _load_template(kind: str) -> str | None:
    base = Path(__file__).parent / "templates"
    mapping = {
        "rfi": base / "rfi024-hilal.md",
        "submittal": base / "submittal-transmittal-hilal.md",
        "daily_report": base / "daily-construction-report-hilal.md",
    }
    path = mapping.get(kind)
    if not path or not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def draft_reply(
    *,
    msg: EmailMessage,
    classification: ClassificationResult,
    mem: Memory,
    contact: Contact | None,
    sender_name: str = "CEM501 Agent",
) -> Draft:
    tone = choose_tone(contact)
    greeting = render_greeting(tone, contact=contact)
    signoff = render_signoff(tone, sender_name=sender_name)

    history = []
    if contact:
        for row in mem.get_recent_messages(contact_id=contact.id, limit=6):
            history.append(
                {
                    "direction": row["direction"],
                    "subject": row["subject"],
                    "channel": row["channel"],
                    "sent_at": row["sent_at"],
                    "body_preview": (row["body"] or "")[:300],
                }
            )

    template = _load_template(classification.kind)
    user_payload = {
        "incoming": {
            "subject": msg.subject,
            "from": {"name": msg.from_name, "email": msg.from_email},
            "body": msg.body_text[:7000],
        },
        "classification": {
            "category": classification.category,
            "urgency": classification.urgency,
            "kind": classification.kind,
            "rationale": classification.rationale,
        },
        "contact": {
            "name": contact.name if contact else None,
            "email": contact.email if contact else None,
            "role": contact.role if contact else None,
            "company": contact.company if contact else None,
            "culture_region": contact.culture_region if contact else None,
            "preferred_tone": contact.preferred_tone if contact else None,
        },
        "message_history": history,
        "tone_profile": {
            "preset": tone.preset,
            "style_notes": tone.style_notes,
            "required_greeting": greeting,
            "required_signoff": signoff,
        },
        "optional_template_reference": template,
    }

    try:
        client = _client()
        resp = client.messages.create(
            model=os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-latest"),
            max_tokens=900,
            temperature=0.4,
            system=_SYSTEM,
            messages=[{"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}],
        )

        text = "".join(block.text for block in resp.content if getattr(block, "text", None))
        data = json.loads(text)
        subject = data.get("subject") or f"Re: {msg.subject}"
        body = data["body_text"].strip()
    except Exception:
        subject = f"Re: {msg.subject}"
        body = (
            "Thanks for the message. I’ve reviewed it and will proceed once the following are confirmed:\n"
            "- Please confirm the required scope/standard and any applicable drawing/spec references.\n"
            "- Please confirm your required response date/time.\n\n"
            "Proposed next step: we will prepare a written response and plan with any impacts once confirmed."
        )

    # Enforce greeting/signoff if the model omitted them.
    if not body.lower().startswith(greeting.lower().split()[0]):
        body = f"{greeting}\n\n{body}"
    if signoff.splitlines()[0] not in body:
        body = f"{body}\n\n{signoff}"

    return Draft(
        to_email=(contact.email if contact else msg.from_email),
        subject=subject,
        body_text=body,
        channel="email",
        tone_preset=tone.preset,
    )

