"""LLM-assisted classification with keyword fallback."""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parent.parent


def classify_message(text: str) -> str:
    load_dotenv(_PROJECT_ROOT / ".env")
    text = (text or "").strip()
    if not text:
        return "ARCHIVE"

    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            return _classify_llm(text)
        except Exception:
            pass

    return _classify_rules(text)


def classify_email(subject: str, body: str = "", sender: str = "") -> str:
    blob = f"{subject}\n{body}\n{sender}".strip()
    return classify_message(blob)


def _classify_rules(text: str) -> str:
    from .reader import triage_email

    first, _, rest = text.partition("\n")
    subject = first.strip()[:500]
    remainder = rest.strip()
    return triage_email(subject, remainder or subject)


def _classify_llm(text: str) -> str:
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    system = (
        "You classify construction/project communications into exactly one label: "
        "URGENT, ACTION, FYI, or ARCHIVE. "
        'Return ONLY JSON: {"category":"URGENT|ACTION|FYI|ARCHIVE"}'
    )
    resp = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
        max_tokens=120,
        temperature=0.2,
        system=system,
        messages=[{"role": "user", "content": text[:8000]}],
    )
    raw = "".join(getattr(b, "text", "") or "" for b in resp.content)
    data = json.loads(raw)
    cat = data["category"].upper()
    if cat not in ("URGENT", "ACTION", "FYI", "ARCHIVE"):
        raise ValueError(cat)
    return cat
