"""Send Telegram messages via Bot API (web dashboard and other callers)."""

from __future__ import annotations

import os
from typing import Any

import httpx

_TELEGRAM_MAX_MESSAGE_LEN = 4096


def get_bot_token() -> str:
    token = (
        os.getenv("TELEGRAM_BOT_TOKEN")
        or os.getenv("BOT_TOKEN")
        or os.getenv("TELEGRAM_TOKEN")
    )
    if not token:
        raise RuntimeError("Telegram bot token not configured")
    return token


def telegram_chat_allowed(chat_id: int) -> bool:
    """If TELEGRAM_CHAT_ID is set, only allow listed chats (comma-separated)."""
    raw = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not raw:
        return True
    allowed: set[int] = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            allowed.add(int(part))
        except ValueError:
            continue
    return chat_id in allowed


def text_chunks(text: str, max_len: int = _TELEGRAM_MAX_MESSAGE_LEN) -> list[str]:
    text = (text or "").strip()
    if not text:
        return ["(empty)"]
    return [text[i : i + max_len] for i in range(0, len(text), max_len)]


def send_telegram_message(chat_id: int, text: str) -> list[int]:
    """Send plain text to a chat; returns Telegram message_id for each chunk sent."""
    if not telegram_chat_allowed(chat_id):
        raise RuntimeError(f"Chat {chat_id} is not allowed by TELEGRAM_CHAT_ID")

    token = get_bot_token()
    chunks = text_chunks(text)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message_ids: list[int] = []

    with httpx.Client(timeout=30.0) as client:
        for chunk in chunks:
            resp = client.post(url, json={"chat_id": chat_id, "text": chunk})
            resp.raise_for_status()
            payload: dict[str, Any] = resp.json()
            if not payload.get("ok"):
                desc = payload.get("description") or "sendMessage failed"
                raise RuntimeError(str(desc))
            result = payload.get("result") or {}
            mid = result.get("message_id")
            if mid is not None:
                message_ids.append(int(mid))

    return message_ids
