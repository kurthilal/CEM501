"""Telegram bot: classify → draft → reply. Run: ``python3 -m demo.test_bot`` from ``project/``."""

from __future__ import annotations

import asyncio
import os
import traceback
from pathlib import Path

import httpx
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

from .classifier import classify_message
from .drafter import draft_response
from .memory import Memory
from .photo_vision import describe_photo, guess_media_type

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DEMO_ROOT = Path(__file__).resolve().parent

_BOT_VERSION = "photo-vision-v2"
_TELEGRAM_MAX_MESSAGE_LEN = 4096


def _telegram_chat_allowed(chat_id: int | None) -> bool:
    """If TELEGRAM_CHAT_ID is set, only accept updates from that chat (comma-separated allowed)."""
    raw = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not raw or chat_id is None:
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


def _truncate_telegram_text(text: str, max_len: int = 3800) -> str:
    text = (text or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "…"


def _telegram_text_chunks(text: str, max_len: int = _TELEGRAM_MAX_MESSAGE_LEN) -> list[str]:
    text = text or ""
    if not text.strip():
        return []
    return [text[i : i + max_len] for i in range(0, len(text), max_len)]


async def _reply_in_chat_with_optional_split(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    chat_id: int,
    full_text: str,
):
    """Reply to the incoming message; split into multiple Telegram messages if over the length limit."""
    chunks = _telegram_text_chunks((full_text or "").strip() or "(empty)")
    reply_msg = await update.message.reply_text(chunks[0])
    for extra in chunks[1:]:
        await context.bot.send_message(chat_id=chat_id, text=extra)
    return reply_msg


async def _download_telegram_photo(
    bot_token: str, file_id: str
) -> tuple[bytes, str]:
    """Fetch largest photo bytes from Telegram Bot API."""
    async with httpx.AsyncClient(timeout=90.0) as client:
        gf = await client.get(
            f"https://api.telegram.org/bot{bot_token}/getFile",
            params={"file_id": file_id},
        )
        gf.raise_for_status()
        payload = gf.json()
        if not payload.get("ok"):
            raise RuntimeError(payload.get("description", "getFile failed"))
        file_path = (payload.get("result") or {}).get("file_path")
        if not file_path:
            raise RuntimeError("no file_path")
        media_type = guess_media_type(file_path)
        url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        img = await client.get(url)
        img.raise_for_status()
        return img.content, media_type


async def handle_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if not update.message or not update.message.text:
        return
    msg = update.message
    chat_id = msg.chat_id
    if not _telegram_chat_allowed(chat_id):
        return

    user = msg.from_user
    incoming_text = msg.text
    sender = user.first_name if user else "?"

    mem = Memory()
    mem.insert_telegram_message(
        chat_id=chat_id,
        user_id=user.id if user else None,
        username=user.username if user else None,
        direction="received",
        message_type="text",
        text_content=incoming_text,
        telegram_message_id=msg.message_id,
    )

    category = classify_message(incoming_text)
    print(category)
    draft = draft_response(incoming_text, category)
    print(draft)

    reply_msg = await update.message.reply_text(draft)

    mem.insert_telegram_message(
        chat_id=chat_id,
        user_id=None,
        username="bot",
        direction="sent",
        message_type="text",
        text_content=draft,
        telegram_message_id=reply_msg.message_id if reply_msg else None,
    )
    print(f"[Telegram] {sender} -> {category} -> replied")


async def handle_photo(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if not update.message or not update.message.photo:
        return
    msg = update.message
    chat_id = msg.chat_id
    user = msg.from_user
    sender = user.first_name if user else "?"
    print(f"[Telegram] photo received from {sender} (chat_id={chat_id})")

    if not _telegram_chat_allowed(chat_id):
        print(f"[Telegram] chat {chat_id} not in TELEGRAM_CHAT_ID allowlist; ignoring")
        return

    token = (
        os.getenv("TELEGRAM_BOT_TOKEN")
        or os.getenv("BOT_TOKEN")
        or os.getenv("TELEGRAM_TOKEN")
    )
    if not token:
        try:
            await update.message.reply_text(
                "Bot token missing on server. Set TELEGRAM_BOT_TOKEN in project/.env."
            )
        except Exception:
            pass
        return

    try:
        await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    except Exception:
        pass

    ack_msg = None
    try:
        ack_msg = await update.message.reply_text("Analyzing photo with AI…")
    except Exception as exc:
        print(f"[Telegram] could not send ack: {exc}")

    photos = msg.photo
    best = photos[-1]
    file_ids = [best.file_id]
    caption = (msg.caption or "").strip()

    image_bytes: bytes = b""
    media_type = "image/jpeg"
    try:
        image_bytes, media_type = await _download_telegram_photo(token, best.file_id)
        print(f"[Telegram] downloaded photo: {len(image_bytes)} bytes ({media_type})")
    except Exception as exc:
        print(f"[Telegram] photo download failed: {exc}")

    desc = ""
    tags: list[str] = []
    if image_bytes:
        try:
            analysis = await asyncio.to_thread(describe_photo, image_bytes, media_type)
            desc = (analysis.get("description") or "").strip()
            tags_raw = analysis.get("tags") or []
            if isinstance(tags_raw, list):
                tags = [str(t).strip() for t in tags_raw if str(t).strip()]
            print(f"[Telegram] vision: desc_len={len(desc)} tags={tags}")
        except Exception as exc:
            print(f"[Telegram] describe_photo raised: {exc}")
            traceback.print_exc()
    else:
        desc = "Could not download the photo for analysis."

    if not desc:
        desc = "(No description was generated. Check ANTHROPIC_API_KEY and ANTHROPIC_MODEL.)"

    mem = Memory()
    try:
        mem.insert_telegram_message(
            chat_id=chat_id,
            user_id=user.id if user else None,
            username=user.username if user else None,
            direction="received",
            message_type="photo",
            text_content=caption or None,
            photo_file_ids=file_ids,
            photo_llm_description=desc,
            photo_tags=tags,
            telegram_message_id=msg.message_id,
        )
    except Exception as exc:
        print(f"[Telegram] memory insert failed: {exc}")

    lines = [
        "Photo description:",
        "",
        desc,
    ]
    if tags:
        lines.extend(["", "Tags: " + ", ".join(tags)])
    if caption:
        lines.extend(["", "Your caption: " + caption])
    reply_body = "\n".join(lines)

    try:
        reply_msg = await _reply_in_chat_with_optional_split(
            update, context, chat_id, reply_body
        )
    except Exception as exc:
        print(f"[Telegram] sending photo reply failed: {exc}")
        traceback.print_exc()
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Sorry, I couldn't deliver the photo description: {exc}",
            )
        except Exception:
            pass
        return

    try:
        mem.insert_telegram_message(
            chat_id=chat_id,
            user_id=None,
            username="bot",
            direction="sent",
            message_type="text",
            text_content=reply_body,
            telegram_message_id=reply_msg.message_id if reply_msg else None,
        )
    except Exception as exc:
        print(f"[Telegram] memory insert (reply) failed: {exc}")

    print(f"[Telegram] photo from {sender}: {len(tags)} tags -> replied (desc_len={len(desc)})")


def main() -> None:
    load_dotenv(_PROJECT_ROOT / ".env")

    token = (
        os.getenv("TELEGRAM_BOT_TOKEN")
        or os.getenv("BOT_TOKEN")
        or os.getenv("TELEGRAM_TOKEN")
    )
    if not token:
        raise SystemExit(
            "Set TELEGRAM_BOT_TOKEN (or BOT_TOKEN) in project/.env"
        )

    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print(f"Demo agent bot ({_BOT_VERSION}) is running... (Ctrl+C to stop)")
    print(f"  ANTHROPIC_API_KEY set: {bool(os.getenv('ANTHROPIC_API_KEY'))}")
    print(f"  ANTHROPIC_MODEL: {os.getenv('ANTHROPIC_MODEL', 'claude-sonnet-4-6 (default)')}")
    print(f"  SQLite telegram log: {_DEMO_ROOT / 'memory' / 'memory.db'}")
    app.run_polling()


if __name__ == "__main__":
    main()
