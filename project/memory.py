from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Literal, Sequence


Direction = Literal["sent", "received"]
TaskStatus = Literal["pending", "done", "skipped"]


@dataclass(frozen=True)
class Contact:
    id: int
    name: str
    email: str | None
    role: str | None
    company: str | None
    culture_region: str | None
    preferred_tone: str | None


class Memory:
    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
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

            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS contacts (
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    name            TEXT NOT NULL,
                    email           TEXT,
                    phone           TEXT,
                    role            TEXT,
                    company         TEXT,
                    notes           TEXT,
                    culture_region  TEXT,
                    preferred_tone  TEXT,
                    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(email)
                );
                """
            )

            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS message_history (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    contact_id  INTEGER REFERENCES contacts(id),
                    direction   TEXT CHECK(direction IN ('sent', 'received')) NOT NULL,
                    subject     TEXT,
                    body        TEXT,
                    channel     TEXT,
                    sent_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS scheduled_tasks (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    due_at      TIMESTAMP NOT NULL,
                    contact_id  INTEGER REFERENCES contacts(id),
                    status      TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'done', 'skipped')),
                    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

            conn.execute("CREATE INDEX IF NOT EXISTS idx_message_contact ON message_history(contact_id, sent_at);")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_tasks_due ON scheduled_tasks(status, due_at);")

    # ----------------------------
    # Contacts
    # ----------------------------
    def upsert_contact(
        self,
        *,
        name: str,
        email: str | None,
        role: str | None = None,
        company: str | None = None,
        culture_region: str | None = None,
        preferred_tone: str | None = None,
        notes: str | None = None,
    ) -> int:
        with self._connect() as conn:
            if email:
                row = conn.execute("SELECT id FROM contacts WHERE email = ?", (email,)).fetchone()
                if row:
                    conn.execute(
                        """
                        UPDATE contacts
                        SET name = COALESCE(?, name),
                            role = COALESCE(?, role),
                            company = COALESCE(?, company),
                            culture_region = COALESCE(?, culture_region),
                            preferred_tone = COALESCE(?, preferred_tone),
                            notes = COALESCE(?, notes)
                        WHERE id = ?
                        """,
                        (name, role, company, culture_region, preferred_tone, notes, row["id"]),
                    )
                    return int(row["id"])

            cur = conn.execute(
                """
                INSERT INTO contacts (name, email, role, company, notes, culture_region, preferred_tone)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name, email, role, company, notes, culture_region, preferred_tone),
            )
            return int(cur.lastrowid)

    def get_contact_by_email(self, email: str) -> Contact | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT id, name, email, role, company, culture_region, preferred_tone
                FROM contacts
                WHERE email = ?
                """,
                (email,),
            ).fetchone()
            if not row:
                return None
            return Contact(
                id=int(row["id"]),
                name=str(row["name"]),
                email=str(row["email"]) if row["email"] else None,
                role=str(row["role"]) if row["role"] else None,
                company=str(row["company"]) if row["company"] else None,
                culture_region=str(row["culture_region"]) if row["culture_region"] else None,
                preferred_tone=str(row["preferred_tone"]) if row["preferred_tone"] else None,
            )

    # ----------------------------
    # Message history
    # ----------------------------
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
                    (sent_at or datetime.utcnow()).isoformat(timespec="seconds"),
                ),
            )
            return int(cur.lastrowid)

    def get_recent_messages(self, *, contact_id: int, limit: int = 10) -> list[sqlite3.Row]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, direction, subject, body, channel, sent_at
                FROM message_history
                WHERE contact_id = ?
                ORDER BY sent_at DESC
                LIMIT ?
                """,
                (contact_id, limit),
            ).fetchall()
            return list(rows)

    # ----------------------------
    # Scheduling / follow-ups
    # ----------------------------
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
                (description, due_at.isoformat(timespec="seconds"), contact_id),
            )
            return int(cur.lastrowid)

    def get_due_tasks(self, *, now: datetime | None = None) -> list[sqlite3.Row]:
        t = now or datetime.utcnow()
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, description, due_at, contact_id, status
                FROM scheduled_tasks
                WHERE status = 'pending' AND due_at <= ?
                ORDER BY due_at ASC
                """,
                (t.isoformat(timespec="seconds"),),
            ).fetchall()
            return list(rows)

    def set_task_status(self, *, task_id: int, status: TaskStatus) -> None:
        with self._connect() as conn:
            conn.execute(
                "UPDATE scheduled_tasks SET status = ? WHERE id = ?",
                (status, task_id),
            )


def default_memory() -> Memory:
    base = Path(__file__).parent
    return Memory(base / "memory" / "memory.db")
