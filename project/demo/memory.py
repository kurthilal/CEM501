"""SQLite-backed memory under ``demo/memory/memory.db``."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

TelegramDirection = Literal["received", "sent"]
TelegramMsgType = Literal["text", "photo"]

Direction = Literal["sent", "received"]
TaskStatus = Literal["pending", "done", "skipped"]

CRM_PIPELINE_STAGES: tuple[str, ...] = (
    "cold_call",
    "meeting",
    "demo",
    "offer",
    "accepted",
)
DEFAULT_CRM_PIPELINE_STAGE = "cold_call"
CrmPipelineStage = Literal[
    "cold_call", "meeting", "demo", "offer", "accepted"
]


def normalize_crm_pipeline_stage(stage: str | None) -> str:
    raw = (stage or "").strip().lower().replace("-", "_").replace(" ", "_")
    if raw in CRM_PIPELINE_STAGES:
        return raw
    aliases = {
        "coldcall": "cold_call",
        "cold": "cold_call",
    }
    return aliases.get(raw, DEFAULT_CRM_PIPELINE_STAGE)


class Memory:
    def __init__(self, db_path: str | Path | None = None) -> None:
        base = Path(__file__).resolve().parent
        self.db_path = Path(db_path) if db_path else base / "memory" / "memory.db"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA foreign_keys=ON;")
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS contacts (
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    name            TEXT NOT NULL,
                    email           TEXT,
                    phone           TEXT,
                    role            TEXT,
                    company         TEXT,
                    notes           TEXT,
                    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(email)
                );
                CREATE TABLE IF NOT EXISTS message_history (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    contact_id  INTEGER REFERENCES contacts(id),
                    direction   TEXT CHECK(direction IN ('sent', 'received')) NOT NULL,
                    subject     TEXT,
                    body        TEXT,
                    channel     TEXT,
                    sent_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS scheduled_tasks (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    due_at      TIMESTAMP NOT NULL,
                    contact_id  INTEGER REFERENCES contacts(id),
                    status      TEXT DEFAULT 'pending'
                        CHECK(status IN ('pending', 'done', 'skipped')),
                    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE INDEX IF NOT EXISTS idx_msg_contact ON message_history(contact_id, sent_at);
                CREATE INDEX IF NOT EXISTS idx_task_due ON scheduled_tasks(status, due_at);

                CREATE TABLE IF NOT EXISTS telegram_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chat_id INTEGER NOT NULL,
                    user_id INTEGER,
                    username TEXT,
                    direction TEXT NOT NULL
                        CHECK(direction IN ('received', 'sent')),
                    message_type TEXT NOT NULL
                        CHECK(message_type IN ('text', 'photo')),
                    text_content TEXT,
                    photo_file_ids TEXT,
                    telegram_message_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE INDEX IF NOT EXISTS idx_tg_chat_created
                    ON telegram_messages(chat_id, created_at);

                CREATE TABLE IF NOT EXISTS telegram_chats (
                    chat_id         INTEGER PRIMARY KEY,
                    chat_type       TEXT NOT NULL DEFAULT 'private',
                    title           TEXT,
                    username        TEXT,
                    is_active       INTEGER NOT NULL DEFAULT 1,
                    last_activity   TIMESTAMP,
                    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE INDEX IF NOT EXISTS idx_tg_chats_active
                    ON telegram_chats(is_active, last_activity DESC);
                """
            )
            self._migrate_telegram_columns(conn)
            self._migrate_telegram_chats(conn)
            self._migrate_contacts_pipeline(conn)
            self._migrate_daily_todos(conn)

    def _migrate_daily_todos(self, conn: sqlite3.Connection) -> None:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_todos (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                content     TEXT NOT NULL,
                item_type   TEXT NOT NULL DEFAULT 'task'
                    CHECK(item_type IN ('task', 'note')),
                is_done     INTEGER NOT NULL DEFAULT 0,
                list_date   DATE NOT NULL DEFAULT (date('now')),
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_daily_todos_date
                ON daily_todos(list_date, is_done, item_type)
            """
        )

    def _migrate_contacts_pipeline(self, conn: sqlite3.Connection) -> None:
        cols = {
            row[1] for row in conn.execute("PRAGMA table_info(contacts)").fetchall()
        }
        if "pipeline_stage" not in cols:
            conn.execute(
                """
                ALTER TABLE contacts
                ADD COLUMN pipeline_stage TEXT NOT NULL DEFAULT 'cold_call'
                """
            )

    def _migrate_telegram_chats(self, conn: sqlite3.Connection) -> None:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='telegram_chats'"
        ).fetchone()
        if not rows:
            return
        conn.execute(
            """
            INSERT OR IGNORE INTO telegram_chats (chat_id, chat_type, title, is_active, last_activity)
            SELECT chat_id,
                   CASE
                       WHEN chat_id > 0 THEN 'private'
                       WHEN CAST(chat_id AS TEXT) LIKE '-100%' THEN 'supergroup'
                       ELSE 'group'
                   END,
                   'Chat ' || chat_id,
                   1,
                   MAX(created_at)
            FROM telegram_messages
            GROUP BY chat_id
            """
        )

    @staticmethod
    def infer_chat_type(chat_id: int) -> str:
        if chat_id > 0:
            return "private"
        if str(chat_id).startswith("-100"):
            return "supergroup"
        return "group"

    @staticmethod
    def is_group_chat_type(chat_type: str | None) -> bool:
        return (chat_type or "") in ("group", "supergroup")

    def upsert_telegram_chat(
        self,
        *,
        chat_id: int,
        chat_type: str | None = None,
        title: str | None = None,
        username: str | None = None,
        is_active: bool = True,
        last_activity: datetime | None = None,
    ) -> None:
        ctype = chat_type or self.infer_chat_type(chat_id)
        title = (title or "").strip() or None
        username = (username or "").strip() or None
        ts = (last_activity or datetime.utcnow()).strftime("%Y-%m-%d %H:%M:%S")
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO telegram_chats (
                    chat_id, chat_type, title, username, is_active, last_activity, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(chat_id) DO UPDATE SET
                    chat_type = excluded.chat_type,
                    title = COALESCE(excluded.title, telegram_chats.title),
                    username = COALESCE(excluded.username, telegram_chats.username),
                    is_active = excluded.is_active,
                    last_activity = COALESCE(excluded.last_activity, telegram_chats.last_activity),
                    updated_at = excluded.updated_at
                """,
                (chat_id, ctype, title, username, 1 if is_active else 0, ts, ts),
            )

    def list_telegram_chat_ids(self, *, active_only: bool = False) -> list[int]:
        query = "SELECT chat_id FROM telegram_chats"
        if active_only:
            query += " WHERE is_active = 1"
        query += " ORDER BY COALESCE(last_activity, updated_at) DESC"
        with self._connect() as conn:
            rows = conn.execute(query).fetchall()
        return [int(r["chat_id"]) for r in rows]

    def _migrate_telegram_columns(self, conn: sqlite3.Connection) -> None:
        rows = conn.execute("PRAGMA table_info(telegram_messages)").fetchall()
        cols = {r[1] for r in rows}
        if "photo_llm_description" not in cols:
            conn.execute(
                "ALTER TABLE telegram_messages ADD COLUMN photo_llm_description TEXT"
            )
        if "photo_tags" not in cols:
            conn.execute("ALTER TABLE telegram_messages ADD COLUMN photo_tags TEXT")

    def upsert_contact(
        self,
        *,
        name: str,
        email: str | None,
        role: str | None = None,
        company: str | None = None,
        notes: str | None = None,
    ) -> int:
        with self._connect() as conn:
            if email:
                row = conn.execute(
                    "SELECT id FROM contacts WHERE email = ?", (email,)
                ).fetchone()
                if row:
                    conn.execute(
                        """
                        UPDATE contacts SET name = ?, role = ?, company = ?, notes = ?
                        WHERE id = ?
                        """,
                        (name, role, company, notes, row["id"]),
                    )
                    return int(row["id"])
            cur = conn.execute(
                """
                INSERT INTO contacts (name, email, role, company, notes)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, email, role, company, notes),
            )
            return int(cur.lastrowid)

    def list_contacts(
        self,
        *,
        limit: int = 100,
        search: str | None = None,
    ) -> list[dict[str, Any]]:
        limit = max(1, min(limit, 500))
        query = """
            SELECT id, name, email, phone, role, company, notes,
                   pipeline_stage, created_at
            FROM contacts
        """
        params: list[Any] = []
        if search:
            like = f"%{search.strip()}%"
            query += """
                WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?
                   OR company LIKE ? OR role LIKE ? OR notes LIKE ?
            """
            params.extend([like, like, like, like, like, like])
        query += " ORDER BY name COLLATE NOCASE ASC, id DESC LIMIT ?"
        params.append(limit)
        with self._connect() as conn:
            rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def get_contact(self, contact_id: int) -> dict[str, Any] | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT id, name, email, phone, role, company, notes,
                       pipeline_stage, created_at
                FROM contacts
                WHERE id = ?
                """,
                (contact_id,),
            ).fetchone()
        return dict(row) if row else None

    def create_contact(
        self,
        *,
        name: str,
        email: str | None = None,
        phone: str | None = None,
        role: str | None = None,
        company: str | None = None,
        notes: str | None = None,
        pipeline_stage: str | None = None,
    ) -> int:
        stage = normalize_crm_pipeline_stage(pipeline_stage)
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO contacts (
                    name, email, phone, role, company, notes, pipeline_stage
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name, email, phone, role, company, notes, stage),
            )
            return int(cur.lastrowid)

    def update_contact(
        self,
        contact_id: int,
        *,
        name: str,
        email: str | None = None,
        phone: str | None = None,
        role: str | None = None,
        company: str | None = None,
        notes: str | None = None,
        pipeline_stage: str | None = None,
    ) -> bool:
        stage = normalize_crm_pipeline_stage(pipeline_stage)
        with self._connect() as conn:
            cur = conn.execute(
                """
                UPDATE contacts
                SET name = ?, email = ?, phone = ?, role = ?, company = ?,
                    notes = ?, pipeline_stage = ?
                WHERE id = ?
                """,
                (name, email, phone, role, company, notes, stage, contact_id),
            )
            return cur.rowcount > 0

    def update_contact_pipeline_stage(
        self,
        contact_id: int,
        pipeline_stage: str,
    ) -> bool:
        stage = normalize_crm_pipeline_stage(pipeline_stage)
        with self._connect() as conn:
            cur = conn.execute(
                """
                UPDATE contacts SET pipeline_stage = ? WHERE id = ?
                """,
                (stage, contact_id),
            )
            return cur.rowcount > 0

    def delete_contact(self, contact_id: int) -> bool:
        with self._connect() as conn:
            conn.execute(
                "UPDATE message_history SET contact_id = NULL WHERE contact_id = ?",
                (contact_id,),
            )
            conn.execute(
                "UPDATE scheduled_tasks SET contact_id = NULL WHERE contact_id = ?",
                (contact_id,),
            )
            cur = conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
            return cur.rowcount > 0

    def log_message(
        self,
        *,
        contact_id: int | None,
        direction: Direction,
        subject: str | None,
        body: str | None,
        channel: str,
        sent_at: datetime | None = None,
    ) -> int:
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO message_history (contact_id, direction, subject, body, channel, sent_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    contact_id,
                    direction,
                    subject,
                    body,
                    channel,
                    (sent_at or datetime.utcnow()).strftime("%Y-%m-%d %H:%M:%S"),
                ),
            )
            return int(cur.lastrowid)

    def insert_telegram_message(
        self,
        *,
        chat_id: int,
        user_id: int | None,
        username: str | None,
        direction: TelegramDirection,
        message_type: TelegramMsgType,
        text_content: str | None = None,
        photo_file_ids: list[str] | None = None,
        photo_llm_description: str | None = None,
        photo_tags: list[str] | None = None,
        telegram_message_id: int | None = None,
        created_at: datetime | None = None,
    ) -> int:
        photo_json: str | None
        if photo_file_ids:
            photo_json = json.dumps(photo_file_ids)
        else:
            photo_json = None
        tags_json: str | None
        if photo_tags:
            tags_json = json.dumps([t.strip() for t in photo_tags if t and str(t).strip()])
        else:
            tags_json = None
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO telegram_messages (
                    chat_id, user_id, username, direction, message_type,
                    text_content, photo_file_ids, photo_llm_description,
                    photo_tags, telegram_message_id, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    chat_id,
                    user_id,
                    username,
                    direction,
                    message_type,
                    text_content,
                    photo_json,
                    photo_llm_description,
                    tags_json,
                    telegram_message_id,
                    (created_at or datetime.utcnow()).strftime("%Y-%m-%d %H:%M:%S"),
                ),
            )
            return int(cur.lastrowid)

    def list_telegram_messages(
        self,
        *,
        chat_id: int | None = None,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        limit = max(1, min(limit, 500))
        with self._connect() as conn:
            if chat_id is not None:
                rows = conn.execute(
                    """
                    SELECT id, chat_id, user_id, username, direction, message_type,
                           text_content, photo_file_ids, photo_llm_description,
                           photo_tags, telegram_message_id, created_at
                    FROM telegram_messages
                    WHERE chat_id = ?
                    ORDER BY created_at DESC, id DESC
                    LIMIT ?
                    """,
                    (chat_id, limit),
                ).fetchall()
                rows = list(reversed(rows))
            else:
                rows = conn.execute(
                    """
                    SELECT id, chat_id, user_id, username, direction, message_type,
                           text_content, photo_file_ids, photo_llm_description,
                           photo_tags, telegram_message_id, created_at
                    FROM telegram_messages
                    ORDER BY created_at DESC, id DESC
                    LIMIT ?
                    """,
                    (limit,),
                ).fetchall()
        out: list[dict[str, Any]] = []
        for r in rows:
            d = dict(r)
            raw = d.get("photo_file_ids")
            if raw:
                try:
                    d["photo_file_ids"] = json.loads(raw)
                except json.JSONDecodeError:
                    d["photo_file_ids"] = []
            else:
                d["photo_file_ids"] = []
            traw = d.get("photo_tags")
            if traw:
                try:
                    parsed = json.loads(traw)
                    d["photo_tags"] = parsed if isinstance(parsed, list) else []
                except json.JSONDecodeError:
                    d["photo_tags"] = []
            else:
                d["photo_tags"] = []
            out.append(d)
        if chat_id is None:
            out.reverse()
        return out

    def telegram_file_id_is_known(self, file_id: str) -> bool:
        """Return True if file_id was stored from an incoming Telegram photo."""
        if not file_id:
            return False
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT photo_file_ids FROM telegram_messages
                WHERE direction = 'received'
                  AND message_type = 'photo'
                  AND photo_file_ids IS NOT NULL
                  AND photo_file_ids != ''
                """
            ).fetchall()
        for r in rows:
            raw = r["photo_file_ids"]
            try:
                ids = json.loads(raw)
                if file_id in ids:
                    return True
            except (json.JSONDecodeError, TypeError):
                continue
        return False

    def telegram_chat_exists(self, chat_id: int) -> bool:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT 1 FROM telegram_chats
                WHERE chat_id = ? AND is_active = 1
                """,
                (chat_id,),
            ).fetchone()
            if row:
                return True
            row = conn.execute(
                "SELECT 1 FROM telegram_messages WHERE chat_id = ? LIMIT 1",
                (chat_id,),
            ).fetchone()
        return row is not None

    def list_telegram_chats(self) -> list[dict[str, Any]]:
        """Chats/groups the bot knows about, merged with message activity."""
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT
                    c.chat_id,
                    c.chat_type,
                    c.title,
                    c.username,
                    c.is_active,
                    COALESCE(msg.last_activity, c.last_activity, c.updated_at) AS last_activity,
                    COALESCE(msg.message_count, 0) AS message_count,
                    COALESCE(msg.photo_count, 0) AS photo_count,
                    msg.preview AS last_preview
                FROM telegram_chats c
                LEFT JOIN (
                    SELECT
                        chat_id,
                        MAX(created_at) AS last_activity,
                        COUNT(*) AS message_count,
                        SUM(CASE WHEN message_type = 'photo' THEN 1 ELSE 0 END) AS photo_count,
                        (
                            SELECT
                                CASE
                                    WHEN message_type = 'photo' THEN COALESCE(text_content, 'Photo')
                                    ELSE COALESCE(text_content, photo_llm_description, '')
                                END
                            FROM telegram_messages tm2
                            WHERE tm2.chat_id = telegram_messages.chat_id
                            ORDER BY tm2.id DESC
                            LIMIT 1
                        ) AS preview
                    FROM telegram_messages
                    GROUP BY chat_id
                ) msg ON msg.chat_id = c.chat_id
                WHERE c.is_active = 1
                ORDER BY COALESCE(msg.last_activity, c.last_activity, c.updated_at) DESC
                """
            ).fetchall()

            out: list[dict[str, Any]] = []
            for row in rows:
                cid = int(row["chat_id"])
                chat_type = row["chat_type"] or self.infer_chat_type(cid)
                title = (row["title"] or "").strip()
                username = (row["username"] or "").strip()
                if not title:
                    if self.is_group_chat_type(chat_type):
                        title = f"Group {cid}"
                    elif username:
                        title = f"@{username}"
                    else:
                        title = f"Chat {cid}"

                preview = (row["last_preview"] or "").strip()
                if not preview:
                    preview = "—"

                out.append(
                    {
                        "chat_id": cid,
                        "chat_type": chat_type,
                        "title": title[:180],
                        "username": username,
                        "is_group": self.is_group_chat_type(chat_type),
                        "last_activity": row["last_activity"],
                        "message_count": int(row["message_count"] or 0),
                        "photo_count": int(row["photo_count"] or 0),
                        "preview": preview[:180],
                    }
                )
            return out

    def list_pending_tasks(self, limit: int = 20) -> list[dict[str, Any]]:
        """Scheduled tasks still awaiting action (notifications)."""
        limit = max(1, min(limit, 100))
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, description, due_at, contact_id, status, created_at
                FROM scheduled_tasks
                WHERE status = 'pending'
                ORDER BY due_at ASC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return [dict(r) for r in rows]

    def list_waiting_telegram_chats(self, limit: int = 20) -> list[dict[str, Any]]:
        """
        Chats whose latest message is incoming (``received``) — awaiting a bot reply.
        """
        limit = max(1, min(limit, 100))
        with self._connect() as conn:
            agg = conn.execute(
                """
                SELECT chat_id, MAX(id) AS last_id
                FROM telegram_messages
                GROUP BY chat_id
                """
            ).fetchall()

            waiting: list[dict[str, Any]] = []
            for row in agg:
                last = conn.execute(
                    """
                    SELECT id, chat_id, user_id, username, direction, message_type,
                           text_content, photo_llm_description, created_at
                    FROM telegram_messages
                    WHERE id = ?
                    """,
                    (row["last_id"],),
                ).fetchone()
                if not last or last["direction"] != "received":
                    continue

                cid = int(last["chat_id"])
                meta = conn.execute(
                    """
                    SELECT chat_type, title, username
                    FROM telegram_chats
                    WHERE chat_id = ? AND is_active = 1
                    """,
                    (cid,),
                ).fetchone()
                if meta and (meta["title"] or "").strip():
                    title = str(meta["title"]).strip()
                    uname = meta["username"] or ""
                else:
                    label_row = conn.execute(
                        """
                        SELECT username FROM telegram_messages
                        WHERE chat_id = ?
                          AND direction = 'received'
                          AND username IS NOT NULL
                          AND username != ''
                        ORDER BY id DESC LIMIT 1
                        """,
                        (cid,),
                    ).fetchone()
                    uname = label_row["username"] if label_row else None
                    title = f"@{uname}" if uname else f"Chat {cid}"

                preview_parts: list[str] = []
                if last["message_type"] == "photo":
                    preview_parts.append("Photo")
                if last["text_content"]:
                    preview_parts.append(str(last["text_content"])[:120])
                elif last["photo_llm_description"]:
                    preview_parts.append(str(last["photo_llm_description"])[:120])
                preview = " · ".join(preview_parts) if preview_parts else "—"

                waiting.append(
                    {
                        "chat_id": cid,
                        "title": title,
                        "username": uname or "",
                        "message_type": last["message_type"],
                        "preview": preview[:180],
                        "created_at": last["created_at"],
                        "message_id": int(last["id"]),
                    }
                )

            waiting.sort(key=lambda x: str(x["created_at"]), reverse=True)
            return waiting[:limit]

    def list_memory_feed(self, limit: int = 80) -> list[dict[str, Any]]:
        """Merge ``message_history`` and ``telegram_messages`` for the Memory UI."""
        limit = max(1, min(limit, 200))
        with self._connect() as conn:
            email_rows = conn.execute(
                """
                SELECT id, direction, subject, channel, sent_at AS ts,
                       substr(body, 1, 320) AS body_preview
                FROM message_history
                ORDER BY sent_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            tg_rows = conn.execute(
                """
                SELECT id, chat_id, username, direction, message_type, text_content,
                       photo_llm_description, photo_tags, created_at AS ts
                FROM telegram_messages
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        feed: list[dict[str, Any]] = []
        for r in email_rows:
            feed.append(
                {
                    "source": "email",
                    "id": r["id"],
                    "ts": r["ts"],
                    "direction": r["direction"],
                    "channel": r["channel"] or "",
                    "subject": r["subject"] or "",
                    "tags": "",
                    "preview": (r["body_preview"] or "")[:300],
                }
            )
        for r in tg_rows:
            tags: list[str] = []
            raw_tags = r["photo_tags"]
            if raw_tags:
                try:
                    parsed = json.loads(raw_tags)
                    if isinstance(parsed, list):
                        tags = [str(t) for t in parsed if str(t).strip()]
                except json.JSONDecodeError:
                    tags = []
            parts: list[str] = []
            if r["message_type"] == "photo":
                parts.append("[photo]")
            if r["text_content"]:
                parts.append(str(r["text_content"])[:220])
            if r["photo_llm_description"]:
                parts.append(str(r["photo_llm_description"])[:220])
            preview = " ".join(parts) if parts else "(telegram)"
            feed.append(
                {
                    "source": "telegram",
                    "id": r["id"],
                    "ts": r["ts"],
                    "direction": r["direction"],
                    "channel": f"telegram:{r['chat_id']}",
                    "subject": r["username"] or "",
                    "tags": ", ".join(tags),
                    "preview": preview[:320],
                }
            )

        feed.sort(key=lambda x: str(x["ts"]), reverse=True)
        return feed[:limit]

    def schedule_task(
        self,
        *,
        description: str,
        due_at: datetime,
        contact_id: int | None,
    ) -> int:
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO scheduled_tasks (description, due_at, contact_id, status)
                VALUES (?, ?, ?, 'pending')
                """,
                (
                    description,
                    due_at.strftime("%Y-%m-%d %H:%M:%S"),
                    contact_id,
                ),
            )
            return int(cur.lastrowid)

    @staticmethod
    def _normalize_list_date(list_date: str | None) -> str:
        if list_date:
            raw = list_date.strip()[:10]
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        return datetime.now().strftime("%Y-%m-%d")

    def list_daily_todos(
        self,
        *,
        list_date: str | None = None,
        include_done: bool = False,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        day = self._normalize_list_date(list_date)
        limit = max(1, min(limit, 200))
        query = """
            SELECT id, content, item_type, is_done, list_date, created_at, updated_at
            FROM daily_todos
            WHERE list_date = ?
        """
        params: list[Any] = [day]
        if not include_done:
            query += " AND (item_type = 'note' OR is_done = 0)"
        query += """
            ORDER BY
                CASE item_type WHEN 'note' THEN 1 ELSE 0 END,
                is_done ASC,
                id DESC
            LIMIT ?
        """
        params.append(limit)
        with self._connect() as conn:
            rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def count_open_daily_tasks(self, *, list_date: str | None = None) -> int:
        day = self._normalize_list_date(list_date)
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT COUNT(*) AS n
                FROM daily_todos
                WHERE list_date = ? AND item_type = 'task' AND is_done = 0
                """,
                (day,),
            ).fetchone()
        return int(row["n"]) if row else 0

    def get_daily_todo(self, todo_id: int) -> dict[str, Any] | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT id, content, item_type, is_done, list_date, created_at, updated_at
                FROM daily_todos
                WHERE id = ?
                """,
                (todo_id,),
            ).fetchone()
        return dict(row) if row else None

    def create_daily_todo(
        self,
        *,
        content: str,
        item_type: str = "task",
        list_date: str | None = None,
    ) -> int:
        text = (content or "").strip()
        if not text:
            raise ValueError("Content is required")
        kind = (item_type or "task").strip().lower()
        if kind not in ("task", "note"):
            raise ValueError("item_type must be task or note")
        day = self._normalize_list_date(list_date)
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO daily_todos (content, item_type, is_done, list_date)
                VALUES (?, ?, 0, ?)
                """,
                (text, kind, day),
            )
            return int(cur.lastrowid)

    def update_daily_todo(
        self,
        todo_id: int,
        *,
        content: str | None = None,
        is_done: bool | None = None,
    ) -> bool:
        fields: list[str] = []
        params: list[Any] = []
        if content is not None:
            text = content.strip()
            if not text:
                raise ValueError("Content cannot be empty")
            fields.append("content = ?")
            params.append(text)
        if is_done is not None:
            fields.append("is_done = ?")
            params.append(1 if is_done else 0)
        if not fields:
            return False
        fields.append("updated_at = CURRENT_TIMESTAMP")
        params.append(todo_id)
        with self._connect() as conn:
            cur = conn.execute(
                f"UPDATE daily_todos SET {', '.join(fields)} WHERE id = ?",
                params,
            )
            return cur.rowcount > 0

    def delete_daily_todo(self, todo_id: int) -> bool:
        with self._connect() as conn:
            cur = conn.execute("DELETE FROM daily_todos WHERE id = ?", (todo_id,))
            return cur.rowcount > 0
