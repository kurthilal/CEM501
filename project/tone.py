from __future__ import annotations

from dataclasses import dataclass

from .memory import Contact


@dataclass(frozen=True)
class ToneProfile:
    preset: str
    greeting: str
    signoff: str
    style_notes: str


_PRESETS: dict[str, ToneProfile] = {
    "formal": ToneProfile(
        preset="formal",
        greeting="Dear {name},",
        signoff="Sincerely,\n{sender_name}",
        style_notes="Formal, respectful, complete sentences. Avoid slang. Prefer clear structure and polite requests.",
    ),
    "neutral": ToneProfile(
        preset="neutral",
        greeting="Hello {name},",
        signoff="Best regards,\n{sender_name}",
        style_notes="Professional and neutral. Clear action items, no excessive warmth.",
    ),
    "friendly": ToneProfile(
        preset="friendly",
        greeting="Hi {name},",
        signoff="Thanks,\n{sender_name}",
        style_notes="Warm but still professional. Collaborative framing.",
    ),
    "direct": ToneProfile(
        preset="direct",
        greeting="Hello {name},",
        signoff="Regards,\n{sender_name}",
        style_notes="Concise, action-oriented. Bullets where helpful. Ask for dates/decisions explicitly.",
    ),
}


def choose_tone(contact: Contact | None) -> ToneProfile:
    if contact and contact.preferred_tone:
        return _PRESETS.get(contact.preferred_tone, _PRESETS["neutral"])
    return _PRESETS["neutral"]


def render_greeting(profile: ToneProfile, *, contact: Contact | None) -> str:
    name = (contact.name if contact else None) or "there"
    return profile.greeting.format(name=name)


def render_signoff(profile: ToneProfile, *, sender_name: str = "CEM501 Agent") -> str:
    return profile.signoff.format(sender_name=sender_name)

