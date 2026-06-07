"""Vision: describe Telegram photos with Claude (Anthropic), return description + tags."""

from __future__ import annotations

import base64
import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parent.parent


def describe_photo(image_bytes: bytes, media_type: str = "image/jpeg") -> dict[str, Any]:
    """
    Return ``{"description": str, "tags": list[str]}``.

    Without ``ANTHROPIC_API_KEY``, returns a short placeholder and empty tags.
    """
    load_dotenv(_PROJECT_ROOT / ".env")
    media_type = (media_type or "image/jpeg").strip() or "image/jpeg"
    if not image_bytes:
        return {"description": "(empty image)", "tags": []}

    if not os.getenv("ANTHROPIC_API_KEY"):
        return {
            "description": "Photo received. Set ANTHROPIC_API_KEY in project/.env for an AI description.",
            "tags": [],
        }

    try:
        return _describe_llm(image_bytes, media_type)
    except Exception:
        return {
            "description": "Could not analyze this image right now. Try again later.",
            "tags": [],
        }


def _describe_llm(image_bytes: bytes, media_type: str) -> dict[str, Any]:
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    b64 = base64.standard_b64encode(image_bytes).decode("ascii")
    system = (
        "You assist on construction and field communications. "
        "Describe the photo clearly in 2–5 sentences: setting, visible objects, safety or quality notes if obvious. "
        "Stay factual; say when unsure."
    )
    prompt = (
        'Respond with ONLY valid JSON, no markdown: '
        '{"description":"<plain text>","tags":["tag1","tag2"]}. '
        "Use 3–8 short tags (lowercase words or hyphenated phrases)."
    )
    resp = client.messages.create(
        model=model,
        max_tokens=600,
        temperature=0.3,
        system=system,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": b64,
                        },
                    },
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    )
    raw = "".join(getattr(b, "text", "") or "" for b in resp.content)
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.removeprefix("```json").removeprefix("```").strip()
        if "```" in raw:
            raw = raw.split("```", 1)[0].strip()
    data = json.loads(raw)
    desc = (data.get("description") or "").strip()
    tags_raw = data.get("tags") or []
    if isinstance(tags_raw, str):
        tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
    elif isinstance(tags_raw, list):
        tags = [str(t).strip().lower() for t in tags_raw if str(t).strip()]
    else:
        tags = []
    tags = tags[:12]
    if not desc:
        desc = "(No description returned.)"
    return {"description": desc, "tags": tags}


def guess_media_type(file_path: str | None) -> str:
    if not file_path:
        return "image/jpeg"
    lower = file_path.lower()
    if lower.endswith(".png"):
        return "image/png"
    if lower.endswith(".webp"):
        return "image/webp"
    if lower.endswith(".gif"):
        return "image/gif"
    return "image/jpeg"
