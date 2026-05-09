from __future__ import annotations

import json
import os
from dataclasses import asdict

from anthropic import Anthropic
from dotenv import load_dotenv

from .contracts import ClassificationResult, EmailCategory, EmailMessage, Urgency


_SYSTEM = """You are a construction communication triage assistant.
Classify an incoming message into:
- category: URGENT | ACTION | FYI | ARCHIVE
- urgency: high | medium | low
- kind: short snake_case label (e.g. rfi, submittal, schedule, incident, meeting_minutes, general)
Return ONLY valid JSON with keys: category, urgency, kind, rationale.
"""


def _client() -> Anthropic:
    load_dotenv()
    key = os.environ["ANTHROPIC_API_KEY"]
    return Anthropic(api_key=key)


def classify_email(msg: EmailMessage) -> ClassificationResult:
    client = _client()
    user = {
        "subject": msg.subject,
        "from": {"name": msg.from_name, "email": msg.from_email},
        "snippet": msg.snippet,
        "body": msg.body_text[:6000],
    }

    resp = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-latest"),
        max_tokens=300,
        temperature=0.2,
        system=_SYSTEM,
        messages=[{"role": "user", "content": json.dumps(user, ensure_ascii=False)}],
    )

    text = "".join(block.text for block in resp.content if getattr(block, "text", None))
    data = json.loads(text)

    category: EmailCategory = data["category"]
    urgency: Urgency = data["urgency"]
    kind: str = data["kind"]
    rationale: str = data.get("rationale", "")
    return ClassificationResult(category=category, urgency=urgency, kind=kind, rationale=rationale)


def classify_with_fallback_rules(msg: EmailMessage) -> ClassificationResult:
    try:
        return classify_email(msg)
    except Exception:
        from .reader import triage_email

        cat = triage_email(msg.subject, (msg.from_email or msg.from_name or ""))
        urgency: Urgency = "high" if cat == "URGENT" else ("medium" if cat in ("ACTION", "FYI") else "low")
        kind = "general"
        return ClassificationResult(category=cat, urgency=urgency, kind=kind, rationale="fallback_rules")

