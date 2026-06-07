"""LLM-assisted drafting with simple fallback templates."""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent


def draft_response(incoming_text: str, category: str) -> str:
    load_dotenv(_PROJECT_ROOT / ".env")
    incoming_text = (incoming_text or "").strip()
    category = (category or "ARCHIVE").upper()

    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            return _draft_llm(incoming_text, category)
        except Exception as e:
            print("draft_llm exception")
            print(e)
            pass

    return _draft_fallback(incoming_text, category)


def draft_email_reply(*, subject: str, body: str, category: str, sender: str = "") -> str:
    payload = f"Subject: {subject}\nFrom: {sender}\n\n{body}".strip()
    return draft_response(payload, category)


def _draft_fallback(text: str, category: str) -> str:
    print("draft_fallback")
    if category == "URGENT":
        return (
            "Thank you for flagging this urgently. I acknowledge receipt and will coordinate "
            "an immediate response. Please confirm any site constraints or deadlines."
        )
    if category == "ACTION":
        return (
            "Thanks — I’ve logged this as an action item. I’ll follow up with the requested "
            "information or approvals and confirm timelines shortly."
        )
    if category == "FYI":
        return "Thanks for the update — noted for the record."
    return (
        "Thank you for your message. If a specific response or decision is needed, "
        "please highlight the required action and due date."
    )


def _draft_llm(text: str, category: str) -> str:
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    system = (
        "You draft concise, professional construction-management replies. "
        'Return ONLY JSON: {"reply":"...plain text..."}. '
        "Keep under ~180 words unless critical detail requires more."
    )
    user = json.dumps(
        {"incoming": text[:12000], "priority_bucket": category}, ensure_ascii=False
    )
    resp = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
        max_tokens=600,
        temperature=0.4,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    raw = "".join(getattr(b, "text", "") or "" for b in resp.content)
    data = json.loads(raw)
    return str(data["reply"]).strip()
