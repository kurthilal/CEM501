from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from telegram import Bot

from .contracts import Draft
from .memory import Memory


@dataclass(frozen=True)
class TelegramConfig:
    token: str
    chat_id: str


def load_telegram_config() -> TelegramConfig:
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN (or BOT_TOKEN/TELEGRAM_TOKEN).")
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    return TelegramConfig(token=token, chat_id=chat_id)


def send_draft_notification(*, draft: Draft, mem: Memory, contact_id: int | None) -> None:
    """
    Minimal HITL: send the draft to a fixed chat for review.
    Approval is out-of-band (user replies manually). We still log the notification.
    """
    cfg = load_telegram_config()
    bot = Bot(cfg.token)
    text = (
        "Draft ready for review:\n\n"
        f"To: {draft.to_email}\n"
        f"Subject: {draft.subject}\n\n"
        f"{draft.body_text[:2500]}"
    )
    bot.send_message(chat_id=cfg.chat_id, text=text)
    mem.log_message(
        contact_id=contact_id,
        direction="sent",
        subject=f"TELEGRAM_REVIEW: {draft.subject}",
        body=text[:4000],
        channel="telegram",
    )

