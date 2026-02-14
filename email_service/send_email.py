#!/usr/bin/env python3
"""
CEM501 Email Service - Send emails to class via Gmail SMTP.

Setup:
  1. Copy .env.example to .env and fill in your Gmail credentials.
  2. Enable 2FA on your Google account.
  3. Create an App Password: https://myaccount.google.com/apppasswords
  4. Run: python send_email.py
"""

import json
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTACTS_FILE = SCRIPT_DIR / "contacts.json"
ENV_FILE = SCRIPT_DIR / ".env"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
CC_ADDRESS = "eyuphan.koc@bogazici.edu.tr"


def load_env():
    """Load credentials from .env file."""
    if not ENV_FILE.exists():
        print("ERROR: .env file not found. Copy .env.example to .env and fill in your credentials.")
        sys.exit(1)
    env = {}
    for line in ENV_FILE.read_text().strip().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            env[key.strip()] = val.strip()
    return env


def load_contacts():
    """Load contacts from contacts.json."""
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_recipients(contacts):
    """Build recipient list from contacts."""
    return [s["email"] for s in contacts["students"]]


def send_email(subject, body, recipients, attachments=None, sender_name="CEM501 - Spring 2026", html=False):
    """
    Send an email to a list of recipients.

    Args:
        subject: Email subject line.
        body: Email body (plain text or HTML).
        recipients: List of email addresses, or a single email string.
        attachments: Optional list of file paths to attach.
        sender_name: Display name for the sender.
        html: If True, body is treated as HTML.
    """
    env = load_env()
    gmail_addr = env["GMAIL_ADDRESS"]
    gmail_pass = env["GMAIL_APP_PASSWORD"]

    if isinstance(recipients, str):
        recipients = [recipients]

    msg = MIMEMultipart()
    msg["From"] = f"{sender_name} <{gmail_addr}>"
    msg["To"] = gmail_addr
    msg["Cc"] = CC_ADDRESS
    msg["Bcc"] = ", ".join(recipients)
    msg["Subject"] = subject

    content_type = "html" if html else "plain"
    msg.attach(MIMEText(body, content_type, "utf-8"))

    if attachments:
        for filepath in attachments:
            filepath = Path(filepath)
            if not filepath.exists():
                print(f"  WARNING: Attachment not found: {filepath}")
                continue
            part = MIMEBase("application", "octet-stream")
            part.set_payload(filepath.read_bytes())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filepath.name}")
            msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(gmail_addr, gmail_pass)
        server.send_message(msg)

    print(f"Email sent to {len(recipients)} recipients.")


def send_to_class(subject, body, attachments=None, html=False):
    """Send an email to all students."""
    contacts = load_contacts()
    recipients = get_recipients(contacts)
    send_email(subject, body, recipients, attachments=attachments, html=html)


# --- CLI usage ---
if __name__ == "__main__":
    contacts = load_contacts()
    print(f"Course: {contacts['course']}")
    print(f"Students: {len(contacts['students'])}")
    print()

    if len(sys.argv) < 3:
        print("Usage: python send_email.py <subject> <body>")
        print('  e.g. python send_email.py "Week 1 Materials" "Hi class, materials are posted."')
        sys.exit(0)

    subject = sys.argv[1]
    body = sys.argv[2]
    attachments = sys.argv[3:] if len(sys.argv) > 3 else None

    print(f"Subject: {subject}")
    print(f"Body: {body[:100]}...")
    recipients = get_recipients(contacts)
    print(f"Recipients ({len(recipients)}):")
    for r in recipients:
        print(f"  - {r}")
    print()

    confirm = input("Send? [y/N] ")
    if confirm.lower() == "y":
        send_to_class(subject, body, attachments=attachments)
    else:
        print("Cancelled.")
