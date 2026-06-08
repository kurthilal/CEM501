"""LLM-assisted drafting with simple fallback templates."""

from __future__ import annotations

import json
import os
import re

from dotenv import load_dotenv
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOCIAL_PLATFORMS = ("linkedin", "instagram")


def normalize_social_platform(platform: str | None) -> str:
    raw = (platform or "").strip().lower()
    if raw in SOCIAL_PLATFORMS:
        return raw
    raise ValueError("platform must be linkedin or instagram")


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


def suggest_email_replies(
    *,
    subject: str,
    body: str,
    sender: str = "",
) -> dict[str, object]:
    """Classify an email and return a primary draft plus alternative reply suggestions."""
    from .classifier import classify_email

    subject = (subject or "").strip()
    body = (body or "").strip()
    sender = (sender or "").strip()
    category = classify_email(subject=subject, body=body, sender=sender)
    draft = draft_email_reply(subject=subject, body=body, category=category, sender=sender)
    suggestions = _reply_suggestions(
        subject=subject,
        body=body,
        sender=sender,
        category=category,
        primary=draft,
    )
    return {"category": category, "draft": draft, "suggestions": suggestions}


def _reply_suggestions(
    *,
    subject: str,
    body: str,
    sender: str,
    category: str,
    primary: str,
) -> list[str]:
    load_dotenv(_PROJECT_ROOT / ".env")
    payload = f"Subject: {subject}\nFrom: {sender}\n\n{body}".strip()
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            return _suggestions_llm(payload, category, primary)
        except Exception:
            pass
    return _suggestions_fallback(category, primary)


def _suggestions_fallback(category: str, primary: str) -> list[str]:
    alts: list[str] = []
    if category == "URGENT":
        alts.append(
            "Acknowledged — treating this as urgent. I am mobilizing the team now and will "
            "update you within the hour with next steps."
        )
        alts.append(
            "Received with urgency noted. Please share any immediate site constraints so we "
            "can respond without delay."
        )
    elif category == "ACTION":
        alts.append(
            "Thanks — I have assigned an owner and will confirm deliverables and dates by "
            "end of day."
        )
        alts.append(
            "Noted as an action item. I will review the request and reply with approvals or "
            "questions shortly."
        )
    elif category == "FYI":
        alts.append("Thanks for the heads-up — logged for the project record.")
        alts.append("Appreciate the update. No action required unless you need otherwise.")
    else:
        alts.append(
            "Thank you for your message. Please let me know if a specific decision or "
            "response is required."
        )
        alts.append("Received — please highlight any required action and target date if applicable.")

    unique: list[str] = []
    for text in [primary, *alts]:
        text = text.strip()
        if text and text not in unique:
            unique.append(text)
    return unique[1:3] if len(unique) > 1 else unique[:2]


def _suggestions_llm(text: str, category: str, primary: str) -> list[str]:
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    system = (
        "You suggest concise professional email replies for construction project management. "
        'Return ONLY JSON: {"suggestions":["...","..."]} with exactly 2 alternative replies '
        "(different tone or emphasis, each under 120 words). Do not repeat the primary draft."
    )
    user = json.dumps(
        {
            "incoming": text[:12000],
            "priority_bucket": category,
            "primary_draft": primary[:4000],
        },
        ensure_ascii=False,
    )
    resp = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
        max_tokens=700,
        temperature=0.5,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    raw = "".join(getattr(b, "text", "") or "" for b in resp.content)
    data = json.loads(raw)
    items = data.get("suggestions") or []
    out: list[str] = []
    for item in items:
        s = str(item).strip()
        if s and s not in out and s != primary.strip():
            out.append(s)
        if len(out) >= 2:
            break
    if not out:
        out = _suggestions_fallback(category, primary)
    return out


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


def draft_social_post(*, platform: str, notes: str) -> dict[str, object]:
    """Draft a social media post from rough notes for LinkedIn or Instagram."""
    load_dotenv(_PROJECT_ROOT / ".env")
    plat = normalize_social_platform(platform)
    notes = (notes or "").strip()
    if not notes:
        raise ValueError("Write a few notes or ideas first.")

    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            return _social_llm(platform=plat, notes=notes)
        except Exception:
            pass

    return _social_fallback(platform=plat, notes=notes)


def _social_fallback(*, platform: str, notes: str) -> dict[str, object]:
    hook = notes.split("\n")[0].strip()[:120]
    if platform == "linkedin":
        draft = (
            f"{hook}\n\n"
            f"Here's what I've been thinking about:\n\n{notes}\n\n"
            "What's your take? Drop a comment — I'd love to hear how others handle this."
        )
        suggestions = [
            (
                f"Quick reflection: {hook}\n\n"
                f"{notes}\n\n"
                "#Leadership #ProfessionalGrowth #Learning"
            ),
            (
                f"I used to overlook this — then learned:\n\n{notes}\n\n"
                "Sharing in case it helps someone else this week."
            ),
        ]
    else:
        short = notes.replace("\n", " ").strip()
        if len(short) > 180:
            short = short[:177].rstrip() + "…"
        draft = f"{hook} ✨\n\n{short}\n\n#daily #motivation #worklife"
        suggestions = [
            f"{hook} 💡\n\n{short[:140]}\n\n#instagram #tips #share",
            f"POV: {hook.lower()}\n\n{short[:120]}\n\nSave this for later 📌",
        ]
    return {"platform": platform, "draft": draft.strip(), "suggestions": suggestions[:2]}


def _social_llm(*, platform: str, notes: str) -> dict[str, object]:
    from anthropic import Anthropic

    if platform == "linkedin":
        system = (
            "You write polished LinkedIn posts for a professional audience. "
            "Use a clear hook, short paragraphs, and an optional call-to-action. "
            "Return ONLY JSON: "
            '{"draft":"...","suggestions":["...","..."]} '
            "with exactly 2 alternative caption drafts (different angle or tone). "
            "Each under 220 words. Plain text; hashtags sparingly at the end."
        )
    else:
        system = (
            "You write engaging Instagram captions. "
            "Keep the main draft concise, conversational, and emoji-friendly. "
            "Return ONLY JSON: "
            '{"draft":"...","suggestions":["...","..."]} '
            "with exactly 2 alternative captions (different hook or style). "
            "Each under 120 words. Include a few relevant hashtags."
        )

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    user = json.dumps(
        {"platform": platform, "rough_notes": notes[:8000]},
        ensure_ascii=False,
    )
    resp = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
        max_tokens=900,
        temperature=0.6,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    raw = "".join(getattr(b, "text", "") or "" for b in resp.content)
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    data = json.loads(raw)
    draft = str(data.get("draft") or "").strip()
    if not draft:
        return _social_fallback(platform=platform, notes=notes)
    suggestions: list[str] = []
    for item in data.get("suggestions") or []:
        s = str(item).strip()
        if s and s != draft and s not in suggestions:
            suggestions.append(s)
        if len(suggestions) >= 2:
            break
    if len(suggestions) < 2:
        fallback = _social_fallback(platform=platform, notes=notes)
        for s in fallback["suggestions"]:
            if s not in suggestions and s != draft:
                suggestions.append(str(s))
            if len(suggestions) >= 2:
                break
    return {"platform": platform, "draft": draft, "suggestions": suggestions[:2]}
