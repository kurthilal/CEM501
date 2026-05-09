from __future__ import annotations

import imaplib
import email
from email.header import decode_header
from email.utils import parseaddr, parsedate_to_datetime
from html.parser import HTMLParser
import os
import re
import sys
from dotenv import load_dotenv

from .contracts import EmailMessage

def decode_mime_str(value):
    parts = decode_header(value)
    decoded = []
    for part, charset in parts:
        if isinstance(part, bytes):
            decoded.append(part.decode(charset or "utf-8", errors="replace"))
        else:
            decoded.append(part)
    return "".join(decoded)


class _HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self._chunks = []

    def handle_data(self, data):
        self._chunks.append(data)

    def get_text(self):
        return " ".join(self._chunks)


def _strip_html(html: str) -> str:
    stripper = _HTMLStripper()
    stripper.feed(html)
    text = stripper.get_text()
    return re.sub(r"\s+", " ", text).strip()


def get_body_preview(msg, max_chars: int = 200) -> str:
    plain, html = None, None
    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            cd = part.get("Content-Disposition", "")
            if "attachment" in cd:
                continue
            charset = part.get_content_charset() or "utf-8"
            if ct == "text/plain" and plain is None:
                plain = part.get_payload(decode=True).decode(charset, errors="replace")
            elif ct == "text/html" and html is None:
                html = part.get_payload(decode=True).decode(charset, errors="replace")
    else:
        charset = msg.get_content_charset() or "utf-8"
        payload = msg.get_payload(decode=True).decode(charset, errors="replace")
        if msg.get_content_type() == "text/html":
            html = payload
        else:
            plain = payload

    text = plain if plain is not None else (_strip_html(html) if html else "")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_chars:
        return text[:max_chars].rstrip() + "…"
    return text


CATEGORY_ORDER = {"URGENT": 0, "ACTION": 1, "FYI": 2, "ARCHIVE": 3}

_USE_COLOR = hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

COLORS = {
    "URGENT":  "\033[31m",  # red
    "ACTION":  "\033[33m",  # yellow
    "FYI":     "\033[34m",  # blue
    "ARCHIVE": "\033[90m",  # gray
    "RESET":   "\033[0m",
}

def _colorize(text: str, category: str) -> str:
    if not _USE_COLOR:
        return text
    return f"{COLORS[category]}{text}{COLORS['RESET']}"

def _load_email_config() -> tuple[str, str, str]:
    load_dotenv()
    email_address = os.environ["EMAIL_ADDRESS"]
    email_password = os.environ["EMAIL_PASSWORD"]
    imap_server = os.getenv("IMAP_SERVER", "imap.gmail.com")
    return email_address, email_password, imap_server


def _parse_from(sender_raw: str) -> tuple[str | None, str | None]:
    name, addr = parseaddr(sender_raw)
    name = decode_mime_str(name) if name else None
    addr = addr or None
    return name, addr


def _parse_date(date_raw: str) -> "datetime | None":
    if not date_raw:
        return None
    try:
        dt = parsedate_to_datetime(date_raw)
        # Normalize to naive UTC-ish for storage simplicity.
        if getattr(dt, "tzinfo", None) is not None:
            dt = dt.astimezone(None).replace(tzinfo=None)
        return dt
    except Exception:
        return None


def read_recent_emails(n: int = 20) -> list[EmailMessage]:
    email_address, email_password, imap_server = _load_email_config()
    messages: list[EmailMessage] = []

    with imaplib.IMAP4_SSL(imap_server) as mail:
        mail.login(email_address, email_password)
        mail.select("INBOX")

        _, data = mail.search(None, "ALL")
        all_ids = data[0].split()
        recent_ids = all_ids[-n:]

        for uid in reversed(recent_ids):
            _, msg_data = mail.fetch(uid, "(RFC822)")
            raw = msg_data[0][1]
            msg = email.message_from_bytes(raw)

            sender_raw = decode_mime_str(msg.get("From", ""))
            subject = decode_mime_str(msg.get("Subject", "")) or ""
            date_raw = msg.get("Date", "")
            body_text = get_body_preview(msg, max_chars=10_000)
            snippet = re.sub(r"\s+", " ", body_text).strip()[:200]

            from_name, from_email = _parse_from(sender_raw)
            message_id = msg.get("Message-ID")
            raw_headers = {k: decode_mime_str(v) for k, v in msg.items()}
            thread_key = (from_email or sender_raw) + "|" + subject

            messages.append(
                EmailMessage(
                    message_id=message_id,
                    from_email=from_email,
                    from_name=from_name,
                    subject=subject,
                    date=_parse_date(date_raw),
                    body_text=body_text,
                    snippet=snippet,
                    raw_headers=raw_headers,
                    thread_key=thread_key,
                )
            )

    return messages


def fetch_recent_emails(n=20):
    rows = []
    for m in read_recent_emails(n=n):
        sender = m.from_email or (m.from_name or "Unknown")
        date = m.date.isoformat(sep=" ", timespec="seconds") if m.date else ""
        category = triage_email(m.subject, sender)
        preview = m.snippet
        rows.append((category, sender, m.subject, date, preview))

    rows.sort(key=lambda r: CATEGORY_ORDER[r[0]])

    # Compute column widths from data (no truncation for category/date)
    cat_w     = max(len(r[0]) for r in rows) if rows else 7
    date_w    = max(len(r[3]) for r in rows) if rows else 4
    sender_w  = min(30, max((len(r[1]) for r in rows), default=6))
    subject_w = min(45, max((len(r[2]) for r in rows), default=7))

    header = (
        f"{'CATEGORY':<{cat_w}}  "
        f"{'SENDER':<{sender_w}}  "
        f"{'SUBJECT':<{subject_w}}  "
        f"{'DATE':<{date_w}}"
    )
    divider = "-" * len(header)
    print(header)
    print(divider)

    for category, sender, subject, date, preview in rows:
        sender_col  = sender[:sender_w].ljust(sender_w)
        subject_col = subject[:subject_w].ljust(subject_w)
        line = (
            f"{category:<{cat_w}}  "
            f"{sender_col}  "
            f"{subject_col}  "
            f"{date}"
        )
        print(_colorize(line, category))
        if preview:
            indent = " " * (cat_w + 2)
            print(f"{indent}{preview}")


TRIAGE_RULES = [
    ("URGENT",  ["stop work", "safety", "incident", "notice of delay"]),
    ("ACTION",  ["rfi", "submittal", "review", "approval"]),
    ("FYI",     ["update", "recap", "photos", "minutes"]),
]

def triage_email(subject: str, sender: str) -> str:
    text = (subject + " " + sender).lower()
    for category, keywords in TRIAGE_RULES:
        if any(kw in text for kw in keywords):
            return category
    return "ARCHIVE"


if __name__ == "__main__":
    fetch_recent_emails()
