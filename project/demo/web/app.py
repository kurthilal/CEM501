"""
CEM501 demo agent — web dashboard.

Run from ``project/``::

    pip install flask
    python -m demo.web.app

Open http://127.0.0.1:5000 (or set ``WEB_PORT`` in ``project/.env``, e.g. ``WEB_PORT=8081``).
"""

from __future__ import annotations

import os
import re
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
    cal_limit = request.args.get("cal_limit", default=12, type=int)
    cal_days = request.args.get("cal_days", default=7, type=int)
    email_limit = max(1, min(email_limit, 30))
    task_limit = max(1, min(task_limit, 50))
    tg_limit = max(1, min(tg_limit, 30))
    cal_limit = max(1, min(cal_limit, 30))
    cal_days = max(1, min(cal_days, 30))

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
    daily_todos = mem.list_daily_todos(limit=15)
    daily_todo_open = mem.count_open_daily_tasks()

    calendar_items: list[dict] = []
    calendar_error: str | None = None
    calendar_account: str | None = None
    try:
        from demo.calendar_reader import read_upcoming_calendar_events
        from demo.reader import EMAIL_ADDRESS

        calendar_items = read_upcoming_calendar_events(days=cal_days, limit=cal_limit)
        calendar_account = EMAIL_ADDRESS
    except Exception as exc:
        calendar_error = str(exc)

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
        calendar={
            "count": len(calendar_items),
            "items": calendar_items,
            "error": calendar_error,
            "account": calendar_account,
            "days": cal_days,
        },
        daily_todos={
            "open_count": daily_todo_open,
            "count": len(daily_todos),
            "items": daily_todos,
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


@app.route("/api/social/draft", methods=["POST"])
def api_social_draft():
    from demo.drafter import draft_social_post

    data = request.get_json(force=True, silent=True) or {}
    platform = (data.get("platform") or "").strip()
    notes = (data.get("notes") or "").strip()

    try:
        result = draft_social_post(platform=platform, notes=notes)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400

    return jsonify(result)


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
                    "body": (r.get("body") or "")[:4000],
                }
            )
        return jsonify(ok=True, count=len(safe), emails=safe)
    except Exception as exc:
        return jsonify(ok=False, error=str(exc), emails=[]), 400


@app.route("/api/inbox/suggest-reply", methods=["POST"])
def api_inbox_suggest_reply():
    """Classify an email and return LLM/rule-based draft plus alternative suggestions."""
    data = request.get_json(force=True, silent=True) or {}
    subject = (data.get("subject") or "").strip()
    body = (data.get("body") or data.get("preview") or "").strip()
    sender = (data.get("sender") or data.get("from_addr") or data.get("from_raw") or "").strip()
    if not subject and not body:
        return jsonify(ok=False, error="Missing email content"), 400

    from demo.drafter import suggest_email_replies

    result = suggest_email_replies(subject=subject, body=body, sender=sender)
    return jsonify(ok=True, **result)


@app.route("/api/inbox/reply", methods=["POST"])
def api_inbox_reply():
    """Send a reply via SMTP and log it in SQLite. Requires WEB_ALLOW_SEND=1."""
    if os.getenv("WEB_ALLOW_SEND") != "1":
        return jsonify(
            ok=False,
            error="Sending disabled. Set WEB_ALLOW_SEND=1 in project/.env to enable.",
        ), 403

    data = request.get_json(force=True, silent=True) or {}
    to_email = (data.get("to") or data.get("to_email") or data.get("from_addr") or "").strip()
    reply_body = (data.get("reply_body") or data.get("body") or "").strip()
    original_subject = (data.get("subject") or "").strip()
    if not to_email or not reply_body:
        return jsonify(ok=False, error="Missing recipient or reply body"), 400

    subject = (data.get("reply_subject") or "").strip()
    if not subject:
        base = original_subject or "(no subject)"
        subject = base if base.lower().startswith("re:") else f"Re: {base}"

    try:
        from demo.sender import send_email

        send_email(to_email=to_email, subject=subject, body=reply_body)
    except Exception as exc:
        return jsonify(ok=False, error=str(exc)), 400

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    contact_id = mem.upsert_contact(name=to_email.split("@")[0], email=to_email)
    mem.log_message(
        contact_id=contact_id,
        direction="sent",
        subject=subject,
        body=reply_body,
        channel="email",
    )

    return jsonify(ok=True, to=to_email, subject=subject)


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
    """Distinct Telegram chats and groups with activity metadata for the dashboard chat list."""
    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if request.args.get("sync", default="0") == "1":
        _sync_telegram_chats(mem)
    chats = mem.list_telegram_chats()
    groups = sum(1 for c in chats if c.get("is_group"))
    return jsonify(ok=True, chats=chats, count=len(chats), groups=groups)


def _sync_telegram_chats(mem) -> None:
    """Refresh chat/group titles from Telegram ``getChat`` for known chat IDs."""
    token = (
        os.getenv("TELEGRAM_BOT_TOKEN")
        or os.getenv("BOT_TOKEN")
        or os.getenv("TELEGRAM_TOKEN")
    )
    if not token:
        return

    import httpx

    for cid in mem.list_telegram_chat_ids():
        try:
            resp = httpx.get(
                f"https://api.telegram.org/bot{token}/getChat",
                params={"chat_id": cid},
                timeout=20.0,
            )
            resp.raise_for_status()
            payload = resp.json()
            if not payload.get("ok"):
                continue
            result = payload.get("result") or {}
            title = result.get("title")
            if not title:
                first = (result.get("first_name") or "").strip()
                last = (result.get("last_name") or "").strip()
                title = " ".join(p for p in (first, last) if p).strip() or None
            mem.upsert_telegram_chat(
                chat_id=cid,
                chat_type=str(result.get("type") or mem.infer_chat_type(cid)),
                title=title,
                username=result.get("username"),
                is_active=True,
            )
        except Exception:
            continue


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


def _crm_fields(data: dict) -> dict[str, str | None]:
    name = (data.get("name") or "").strip()
    if not name:
        raise ValueError("Name is required")

    def opt(key: str) -> str | None:
        val = (data.get(key) or "").strip()
        return val or None

    from demo.memory import normalize_crm_pipeline_stage

    pipeline_stage = normalize_crm_pipeline_stage(data.get("pipeline_stage"))

    return {
        "name": name,
        "email": opt("email"),
        "phone": opt("phone"),
        "role": opt("role"),
        "company": opt("company"),
        "notes": opt("notes"),
        "pipeline_stage": pipeline_stage,
    }


@app.route("/api/crm/customers", methods=["GET"])
def api_crm_list_customers():
    limit = request.args.get("limit", default=200, type=int)
    limit = max(1, min(limit, 500))
    search = (request.args.get("q") or "").strip() or None

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    customers = mem.list_contacts(limit=limit, search=search)
    return jsonify(ok=True, customers=customers, count=len(customers))


@app.route("/api/crm/customers/<int:customer_id>", methods=["GET"])
def api_crm_get_customer(customer_id: int):
    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    row = mem.get_contact(customer_id)
    if not row:
        return jsonify(ok=False, error="Customer not found"), 404
    return jsonify(ok=True, customer=row)


@app.route("/api/crm/customers", methods=["POST"])
def api_crm_create_customer():
    data = request.get_json(force=True, silent=True) or {}
    try:
        fields = _crm_fields(data)
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    try:
        row_id = mem.create_contact(**fields)
    except sqlite3.IntegrityError:
        return jsonify(ok=False, error="A customer with that email already exists"), 409

    row = mem.get_contact(row_id)
    return jsonify(ok=True, customer=row), 201


@app.route("/api/crm/customers/<int:customer_id>", methods=["PUT"])
def api_crm_update_customer(customer_id: int):
    data = request.get_json(force=True, silent=True) or {}
    try:
        fields = _crm_fields(data)
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if not mem.get_contact(customer_id):
        return jsonify(ok=False, error="Customer not found"), 404

    try:
        mem.update_contact(customer_id, **fields)
    except sqlite3.IntegrityError:
        return jsonify(ok=False, error="A customer with that email already exists"), 409

    row = mem.get_contact(customer_id)
    return jsonify(ok=True, customer=row)


@app.route("/api/crm/customers/<int:customer_id>", methods=["DELETE"])
def api_crm_delete_customer(customer_id: int):
    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if not mem.get_contact(customer_id):
        return jsonify(ok=False, error="Customer not found"), 404

    mem.delete_contact(customer_id)
    return jsonify(ok=True)


@app.route("/api/crm/customers/<int:customer_id>/pipeline", methods=["PATCH"])
def api_crm_update_pipeline(customer_id: int):
    data = request.get_json(force=True, silent=True) or {}
    from demo.memory import Memory, normalize_crm_pipeline_stage

    stage = normalize_crm_pipeline_stage(data.get("pipeline_stage"))
    mem = Memory(db_path=_MEMORY_DB)
    if not mem.get_contact(customer_id):
        return jsonify(ok=False, error="Customer not found"), 404

    mem.update_contact_pipeline_stage(customer_id, stage)
    row = mem.get_contact(customer_id)
    return jsonify(ok=True, customer=row, pipeline_stage=stage)


@app.route("/api/crm/pipeline/stages", methods=["GET"])
def api_crm_pipeline_stages():
    from demo.memory import CRM_PIPELINE_STAGES

    labels = {
        "cold_call": "Cold call",
        "meeting": "Meeting",
        "demo": "Demo",
        "offer": "Offer",
        "accepted": "Accepted",
    }
    stages = [{"id": s, "label": labels[s]} for s in CRM_PIPELINE_STAGES]
    return jsonify(ok=True, stages=stages)


@app.route("/api/calendar/events", methods=["GET"])
def api_calendar_list_events():
    days = request.args.get("days", default=30, type=int)
    limit = request.args.get("limit", default=50, type=int)
    days = max(1, min(days, 60))
    limit = max(1, min(limit, 100))
    try:
        from demo.calendar_reader import read_upcoming_calendar_events
        from demo.reader import EMAIL_ADDRESS

        events = read_upcoming_calendar_events(days=days, limit=limit)
        return jsonify(
            ok=True,
            events=events,
            count=len(events),
            account=EMAIL_ADDRESS,
            days=days,
        )
    except Exception as exc:
        return jsonify(ok=False, error=str(exc), events=[], count=0), 502


@app.route("/api/calendar/events", methods=["POST"])
def api_calendar_create_event():
    """Create a Google Calendar event (invites sent when attendees are listed)."""
    if os.getenv("WEB_ALLOW_SEND") != "1":
        return jsonify(
            ok=False,
            error="Calendar writes disabled. Set WEB_ALLOW_SEND=1 in project/.env to enable.",
        ), 403

    data = request.get_json(force=True, silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify(ok=False, error="Title is required"), 400

    attendees_raw = data.get("attendees") or []
    if isinstance(attendees_raw, str):
        attendees = [a.strip() for a in re.split(r"[,;\n]+", attendees_raw) if a.strip()]
    else:
        attendees = [str(a).strip() for a in attendees_raw if str(a).strip()]

    try:
        from demo.calendar_reader import create_calendar_event

        event = create_calendar_event(
            title=title,
            start=str(data.get("start") or ""),
            end=(data.get("end") or None),
            all_day=bool(data.get("all_day")),
            location=(data.get("location") or None),
            description=(data.get("description") or None),
            attendees=attendees,
        )
        return jsonify(ok=True, event=event), 201
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400
    except Exception as exc:
        return jsonify(ok=False, error=str(exc)), 502


@app.route("/api/todos", methods=["GET"])
def api_list_todos():
    list_date = (request.args.get("day") or "").strip() or None
    include_done = request.args.get("include_done", default="0") == "1"
    limit = request.args.get("limit", default=100, type=int)
    limit = max(1, min(limit, 200))

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    try:
        items = mem.list_daily_todos(
            list_date=list_date,
            include_done=include_done,
            limit=limit,
        )
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400

    open_count = mem.count_open_daily_tasks(list_date=list_date)
    try:
        normalized_day = Memory._normalize_list_date(list_date)
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400
    day = items[0]["list_date"] if items else normalized_day
    return jsonify(
        ok=True,
        todos=items,
        count=len(items),
        open_count=open_count,
        list_date=day,
    )


@app.route("/api/todos", methods=["POST"])
def api_create_todo():
    data = request.get_json(force=True, silent=True) or {}
    content = (data.get("content") or "").strip()
    item_type = (data.get("item_type") or "task").strip().lower()
    list_date = (data.get("list_date") or "").strip() or None

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    try:
        row_id = mem.create_daily_todo(
            content=content,
            item_type=item_type,
            list_date=list_date,
        )
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400

    row = mem.get_daily_todo(row_id)
    return jsonify(ok=True, todo=row), 201


@app.route("/api/todos/<int:todo_id>", methods=["PATCH"])
def api_update_todo(todo_id: int):
    data = request.get_json(force=True, silent=True) or {}
    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if not mem.get_daily_todo(todo_id):
        return jsonify(ok=False, error="Todo not found"), 404

    content = data.get("content")
    is_done = data.get("is_done")
    if is_done is not None:
        is_done = bool(is_done)

    try:
        mem.update_daily_todo(
            todo_id,
            content=content if content is not None else None,
            is_done=is_done if "is_done" in data else None,
        )
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400

    row = mem.get_daily_todo(todo_id)
    return jsonify(ok=True, todo=row)


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def api_delete_todo(todo_id: int):
    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    if not mem.delete_daily_todo(todo_id):
        return jsonify(ok=False, error="Todo not found"), 404
    return jsonify(ok=True)


@app.route("/api/todos/<int:todo_id>/event", methods=["POST"])
def api_todo_create_event(todo_id: int):
    """Create a Google Calendar event from a daily todo item."""
    if os.getenv("WEB_ALLOW_SEND") != "1":
        return jsonify(
            ok=False,
            error="Calendar writes disabled. Set WEB_ALLOW_SEND=1 in project/.env to enable.",
        ), 403

    from demo.memory import Memory

    mem = Memory(db_path=_MEMORY_DB)
    todo = mem.get_daily_todo(todo_id)
    if not todo:
        return jsonify(ok=False, error="Todo not found"), 404

    data = request.get_json(force=True, silent=True) or {}
    title = (data.get("title") or todo.get("content") or "").strip()
    if not title:
        return jsonify(ok=False, error="Title is required"), 400

    attendees_raw = data.get("attendees") or []
    if isinstance(attendees_raw, str):
        attendees = [a.strip() for a in re.split(r"[,;\n]+", attendees_raw) if a.strip()]
    else:
        attendees = [str(a).strip() for a in attendees_raw if str(a).strip()]

    try:
        from demo.calendar_reader import create_calendar_event

        event = create_calendar_event(
            title=title,
            start=str(data.get("start") or ""),
            end=(data.get("end") or None),
            all_day=bool(data.get("all_day")),
            location=(data.get("location") or None),
            description=(data.get("description") or todo.get("content") or None),
            attendees=attendees,
        )
        return jsonify(ok=True, event=event, todo=todo), 201
    except ValueError as exc:
        return jsonify(ok=False, error=str(exc)), 400
    except Exception as exc:
        return jsonify(ok=False, error=str(exc)), 502


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
