"""
CEM501 demo agent — web dashboard.

Run from ``project/``::

    pip install flask
    python -m demo.web.app

Open http://127.0.0.1:5000 (or set ``WEB_PORT`` in ``project/.env``, e.g. ``WEB_PORT=8081``).
"""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, Response, jsonify, render_template, request

_WEB_DIR = Path(__file__).resolve().parent
_DEMO_DIR = _WEB_DIR.parent
_PROJECT_ROOT = _DEMO_DIR.parent
_MEMORY_DB = _DEMO_DIR / "memory" / "memory.db"

# Load project/.env so WEB_PORT and other vars apply when starting the dev server.
load_dotenv(_PROJECT_ROOT / ".env")

app = Flask(
    __name__,
    template_folder=str(_WEB_DIR / "templates"),
    static_folder=str(_WEB_DIR / "static"),
)


def _memory_conn():
    _MEMORY_DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(_MEMORY_DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify(ok=True, demo=str(_DEMO_DIR))


@app.route("/api/dashboard/summary", methods=["GET"])
def api_dashboard_summary():
    """Aggregate unread emails, pending notifications, and waiting Telegram chats."""
    email_limit = request.args.get("email_limit", default=10, type=int)
    task_limit = request.args.get("task_limit", default=10, type=int)
    tg_limit = request.args.get("tg_limit", default=10, type=int)
    email_limit = max(1, min(email_limit, 30))
    task_limit = max(1, min(task_limit, 50))
    tg_limit = max(1, min(tg_limit, 30))

    unread_emails: list[dict] = []
    email_error: str | None = None
    try:
        from demo.reader import read_unread_emails

        rows = read_unread_emails(n=email_limit)
        for r in rows:
            unread_emails.append(
                {
                    "subject": r.get("subject"),
                    "from_addr": r.get("from_addr"),
                    "from_raw": r.get("from_raw"),
                    "date": r.get("date"),
                    "preview": (r.get("preview") or "")[:300],
                }
            )
    except Exception as exc:
        email_error = str(exc)

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    pending_tasks = mem.list_pending_tasks(limit=task_limit)
    waiting_telegram = mem.list_waiting_telegram_chats(limit=tg_limit)

    return jsonify(
        ok=True,
        unread_emails={
            "count": len(unread_emails),
            "items": unread_emails,
            "error": email_error,
        },
        notifications={
            "count": len(pending_tasks),
            "items": pending_tasks,
        },
        waiting_telegram={
            "count": len(waiting_telegram),
            "items": waiting_telegram,
        },
    )


@app.route("/api/classify", methods=["POST"])
def api_classify():
    from demo.classifier import classify_email, classify_message

    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    subject = (data.get("subject") or "").strip()
    body = (data.get("body") or "").strip()
    sender = (data.get("sender") or "").strip()

    if subject or body or sender:
        category = classify_email(subject=subject or text[:200], body=body or text, sender=sender)
    else:
        category = classify_message(text)

    return jsonify(category=category)


@app.route("/api/draft", methods=["POST"])
def api_draft():
    from demo.drafter import draft_email_reply, draft_response

    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    category = (data.get("category") or "ARCHIVE").upper()
    subject = (data.get("subject") or "").strip()
    body = (data.get("body") or "").strip()
    sender = (data.get("sender") or "").strip()

    if subject or body:
        draft = draft_email_reply(
            subject=subject or "(no subject)",
            body=body or text,
            category=category,
            sender=sender,
        )
    else:
        draft = draft_response(text or "(empty)", category)

    return jsonify(draft=draft, category=category)


@app.route("/api/pipeline", methods=["POST"])
def api_pipeline():
    from demo.classifier import classify_email, classify_message
    from demo.drafter import draft_email_reply, draft_response

    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    subject = (data.get("subject") or "").strip()
    body = (data.get("body") or "").strip()
    sender = (data.get("sender") or "").strip()

    if subject or body or sender:
        category = classify_email(subject=subject or text[:500], body=body or text, sender=sender)
        draft = draft_email_reply(
            subject=subject or text[:200] or "(no subject)",
            body=body or text,
            category=category,
            sender=sender,
        )
    else:
        category = classify_message(text)
        draft = draft_response(text, category)

    return jsonify(category=category, draft=draft)


@app.route("/api/inbox", methods=["GET"])
def api_inbox():
    n = request.args.get("n", default="5", type=int)
    n = max(1, min(n, 50))
    try:
        from demo.reader import read_recent_emails

        rows = read_recent_emails(n=n)
        # Avoid huge payloads
        safe = []
        for r in rows:
            safe.append(
                {
                    "subject": r.get("subject"),
                    "from_addr": r.get("from_addr"),
                    "from_raw": r.get("from_raw"),
                    "date": r.get("date"),
                    "preview": (r.get("preview") or "")[:500],
                }
            )
        return jsonify(ok=True, count=len(safe), emails=safe)
    except Exception as exc:
        return jsonify(ok=False, error=str(exc), emails=[]), 400


@app.route("/api/telegram/messages", methods=["GET"])
def api_telegram_messages():
    """List Telegram messages persisted by ``demo.test_bot`` (newest slice, chronological)."""
    limit = request.args.get("limit", default="150", type=int)
    limit = max(1, min(limit, 500))
    chat_id = request.args.get("chat_id", type=int)

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    rows = mem.list_telegram_messages(chat_id=chat_id, limit=limit)
    return jsonify(ok=True, messages=rows)


@app.route("/api/telegram/chats", methods=["GET"])
def api_telegram_chats():
    """Distinct Telegram chats with activity metadata for the dashboard chat list."""
    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    chats = mem.list_telegram_chats()
    return jsonify(ok=True, chats=chats)


@app.route("/api/telegram/send", methods=["POST"])
def api_telegram_send():
    """
    Send a reply to a known Telegram chat from the web UI.
    Requires ``WEB_ALLOW_SEND=1`` and ``TELEGRAM_BOT_TOKEN`` in ``project/.env``.
    """
    if os.getenv("WEB_ALLOW_SEND") != "1":
        return jsonify(
            ok=False,
            error="Sending disabled. Set WEB_ALLOW_SEND=1 in project/.env to enable.",
        ), 403

    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    raw_chat_id = data.get("chat_id")
    if raw_chat_id is None or not text:
        return jsonify(ok=False, error="Missing chat_id or text"), 400

    try:
        chat_id = int(raw_chat_id)
    except (TypeError, ValueError):
        return jsonify(ok=False, error="Invalid chat_id"), 400

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if not mem.telegram_chat_exists(chat_id):
        return jsonify(ok=False, error="Unknown chat_id"), 404

    try:
        from demo.telegram_sender import send_telegram_message

        message_ids = send_telegram_message(chat_id, text)
    except Exception as exc:
        return jsonify(ok=False, error=str(exc)), 400

    row_id = mem.insert_telegram_message(
        chat_id=chat_id,
        user_id=None,
        username="bot",
        direction="sent",
        message_type="text",
        text_content=text,
        telegram_message_id=message_ids[0] if message_ids else None,
    )

    return jsonify(ok=True, message_ids=message_ids, id=row_id)


@app.route("/api/telegram/file", methods=["GET"])
def api_telegram_file():
    """
    Proxy a Telegram photo by ``file_id`` only if it was stored from an incoming user photo.
    Requires ``TELEGRAM_BOT_TOKEN`` (or aliases) in ``project/.env``.
    """
    file_id = (request.args.get("file_id") or "").strip()
    if not file_id:
        return jsonify(ok=False, error="missing file_id"), 400

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if not mem.telegram_file_id_is_known(file_id):
        return jsonify(ok=False, error="unknown file_id"), 404

    token = (
        os.getenv("TELEGRAM_BOT_TOKEN")
        or os.getenv("BOT_TOKEN")
        or os.getenv("TELEGRAM_TOKEN")
    )
    if not token:
        return jsonify(ok=False, error="Telegram bot token not configured"), 503

    import httpx

    try:
        gf = httpx.get(
            f"https://api.telegram.org/bot{token}/getFile",
            params={"file_id": file_id},
            timeout=30.0,
        )
        gf.raise_for_status()
        payload = gf.json()
        if not payload.get("ok"):
            desc = payload.get("description") or "getFile failed"
            return jsonify(ok=False, error=desc), 502
        result = payload.get("result") or {}
        file_path = result.get("file_path")
        if not file_path:
            return jsonify(ok=False, error="no file_path"), 502
        url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        img = httpx.get(url, timeout=60.0)
        img.raise_for_status()
        content_type = img.headers.get("content-type") or "image/jpeg"
        return Response(img.content, mimetype=content_type)
    except Exception as exc:
        return jsonify(ok=False, error=str(exc)), 502


@app.route("/api/memory/messages", methods=["GET"])
def api_memory_messages():
    limit = request.args.get("limit", default="40", type=int)
    limit = max(1, min(limit, 200))

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    with mem._connect() as conn:
        rows = conn.execute(
            """
            SELECT id, contact_id, direction, subject, channel, sent_at,
                   substr(body, 1, 400) AS body_preview
            FROM message_history
            ORDER BY sent_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    tg_limit = max(limit, 80)
    raw_tg = mem.list_telegram_messages(chat_id=None, limit=tg_limit)
    raw_tg = list(reversed(raw_tg))

    telegram_rows = []
    for r in raw_tg:
        tags_list = r.get("photo_tags") or []
        if not isinstance(tags_list, list):
            tags_list = []
        telegram_rows.append(
            {
                "id": r["id"],
                "chat_id": r["chat_id"],
                "direction": r["direction"],
                "message_type": r["message_type"],
                "created_at": r["created_at"],
                "username": r.get("username") or "",
                "text_preview": (r.get("text_content") or "")[:400],
                "photo_description": (r.get("photo_llm_description") or "")[:400],
                "tags": ", ".join(str(t) for t in tags_list),
            }
        )

    return jsonify(
        ok=True,
        messages=[dict(r) for r in rows],
        telegram_messages=telegram_rows,
    )


@app.route("/api/memory/tasks", methods=["GET"])
def api_memory_tasks():
    limit = request.args.get("limit", default="40", type=int)
    limit = max(1, min(limit, 200))
    if not _MEMORY_DB.exists():
        return jsonify(ok=True, tasks=[])

    with _memory_conn() as conn:
        rows = conn.execute(
            """
            SELECT id, description, due_at, contact_id, status, created_at
            FROM scheduled_tasks
            ORDER BY due_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return jsonify(ok=True, tasks=[dict(r) for r in rows])


@app.route("/api/memory/contacts", methods=["GET"])
def api_memory_contacts():
    limit = request.args.get("limit", default="50", type=int)
    limit = max(1, min(limit, 200))
    if not _MEMORY_DB.exists():
        return jsonify(ok=True, contacts=[])

    with _memory_conn() as conn:
        rows = conn.execute(
            """
            SELECT id, name, email, role, company, created_at
            FROM contacts
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return jsonify(ok=True, contacts=[dict(r) for r in rows])


@app.route("/api/send", methods=["POST"])
def api_send():
    """
    Optional SMTP send — disabled unless WEB_ALLOW_SEND=1 in environment (unsafe on public hosts).
    """
    if os.getenv("WEB_ALLOW_SEND") != "1":
        return jsonify(ok=False, error="Sending disabled. Set WEB_ALLOW_SEND=1 in project/.env to enable."), 403

    data = request.get_json(force=True, silent=True) or {}
    to_email = (data.get("to") or "").strip()
    subject = (data.get("subject") or "").strip()
    body = (data.get("body") or "").strip()
    if not to_email or not subject:
        return jsonify(ok=False, error="Missing to or subject"), 400

    try:
        from demo.sender import send_email

        send_email(to_email=to_email, subject=subject, body=body)
        return jsonify(ok=True)
    except Exception as exc:
        return jsonify(ok=False, error=str(exc)), 400


def main() -> None:
    port = int(os.getenv("WEB_PORT", "5000"))
    print(f"Demo web dashboard: http://127.0.0.1:{port}/  (WEB_PORT from project/.env)")
    app.run(host="127.0.0.1", port=port, debug=True)


if __name__ == "__main__":
    main()
