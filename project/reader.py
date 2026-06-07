"""Compatibility entrypoint: implementation lives in ``demo.reader``."""

from demo.reader import *  # noqa: F403

if __name__ == "__main__":
    fetch_recent_emails()
