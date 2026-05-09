from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal


EmailChannel = Literal["email", "telegram"]
MessageDirection = Literal["sent", "received"]

Urgency = Literal["high", "medium", "low"]
EmailCategory = Literal["URGENT", "ACTION", "FYI", "ARCHIVE"]


@dataclass(frozen=True)
class EmailMessage:
    message_id: str | None
    from_email: str | None
    from_name: str | None
    subject: str
    date: datetime | None
    body_text: str
    snippet: str = ""
    raw_headers: dict[str, str] = field(default_factory=dict)

    # A stable-ish key for grouping messages if Message-ID is missing.
    thread_key: str | None = None


@dataclass(frozen=True)
class ClassificationResult:
    category: EmailCategory
    urgency: Urgency
    kind: str  # e.g., "rfi", "submittal", "schedule", "incident", "general"
    rationale: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Draft:
    to_email: str | None
    subject: str
    body_text: str
    channel: EmailChannel = "email"
    tone_preset: str | None = None
