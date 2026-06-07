"""Run the read → classify → draft → log pipeline on an interval."""

from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime, timedelta

import schedule
from dotenv import load_dotenv
from pathlib import Path

from .classifier import classify_email
from .drafter import draft_email_reply
from .memory import Memory
from .reader import read_recent_emails
from .sender import send_email

_PROJECT_ROOT = Path(__file__).resolve().parent.parent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
log = logging.getLogger("scheduler")


def run_cycle(*, dry_run: bool, max_emails: int, mem: Memory) -> None:
    load_dotenv(_PROJECT_ROOT / ".env")
    emails = read_recent_emails(n=max_emails)
    if not emails:
        log.info("No emails fetched.")
        return

    for item in emails:
        subject = item.get("subject") or ""
        body = item.get("body") or ""
        sender = item.get("from_addr") or ""
        category = classify_email(subject=subject, body=body, sender=sender)
        draft_body = draft_email_reply(
            subject=subject, body=body, category=category, sender=sender
        )

        contact_id = None
        if sender:
            contact_id = mem.upsert_contact(name=sender.split("@")[0], email=sender)

        mem.log_message(
            contact_id=contact_id,
            direction="received",
            subject=subject,
            body=body[:4000],
            channel="email",
        )
        mem.log_message(
            contact_id=contact_id,
            direction="sent",
            subject=f"DRAFT [{category}]: Re: {subject}"[:500],
            body=draft_body[:4000],
            channel="email",
        )

        if category == "URGENT":
            mem.schedule_task(
                description=f"Urgent follow-up: {subject}",
                due_at=datetime.utcnow() + timedelta(hours=2),
                contact_id=contact_id,
            )
        elif category == "ACTION":
            mem.schedule_task(
                description=f"Action follow-up: {subject}",
                due_at=datetime.utcnow() + timedelta(hours=48),
                contact_id=contact_id,
            )

        log.info(
            "processed subject=%r category=%s dry_run=%s",
            subject[:80],
            category,
            dry_run,
        )

        if not dry_run and sender:
            try:
                send_email(to_email=sender, subject=f"Re: {subject}", body=draft_body)
                log.info("sent to=%s", sender)
            except Exception as exc:
                log.error("send_failed: %s", exc)


def main() -> None:
    ap = argparse.ArgumentParser(description="CEM501 demo agent scheduler")
    ap.add_argument("--interval-mins", type=int, default=5)
    ap.add_argument("--max-emails", type=int, default=5)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--once", action="store_true")
    args = ap.parse_args()

    mem = Memory()
    if args.once:
        run_cycle(dry_run=args.dry_run, max_emails=args.max_emails, mem=mem)
        return

    schedule.every(args.interval_mins).minutes.do(
        run_cycle,
        dry_run=args.dry_run,
        max_emails=args.max_emails,
        mem=mem,
    )
    log.info(
        "scheduler started interval_mins=%s dry_run=%s",
        args.interval_mins,
        args.dry_run,
    )
    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()
