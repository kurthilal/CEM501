from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime

import schedule

from .agent import process_once
from .logging_setup import setup_logging
from .memory import default_memory


log = logging.getLogger("scheduler")


def run_due_followups() -> None:
    mem = default_memory()
    due = mem.get_due_tasks(now=datetime.utcnow())
    if not due:
        log.info("followups_due count=0")
        return

    log.info("followups_due count=%d", len(due))
    for row in due:
        log.info("followup task_id=%s due_at=%s contact_id=%s desc=%r", row["id"], row["due_at"], row["contact_id"], row["description"])
        mem.set_task_status(task_id=int(row["id"]), status="done")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--interval-mins", type=int, default=10)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    setup_logging(log_path=(__file__.replace("scheduler.py", "logs/agent.log")), verbose=args.verbose)

    schedule.every(args.interval_mins).minutes.do(process_once, dry_run=args.dry_run, max_emails=5)
    schedule.every().day.at("08:00").do(run_due_followups)

    log.info("scheduler_started interval_mins=%d dry_run=%s", args.interval_mins, args.dry_run)

    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()

