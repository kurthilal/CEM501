from __future__ import annotations

import os
import smtplib
from dataclasses import dataclass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv


@dataclass(frozen=True)
class SmtpConfig:
    smtp_server: str
    smtp_port: int
    email_address: str
    email_password: str


def load_smtp_config() -> SmtpConfig:
    load_dotenv()
    return SmtpConfig(
        smtp_server=os.getenv("SMTP_SERVER", "smtp.gmail.com"),
        smtp_port=int(os.getenv("SMTP_PORT", "587")),
        email_address=os.environ["EMAIL_ADDRESS"],
        email_password=os.environ["EMAIL_PASSWORD"],
    )


def send_email(*, to_email: str, subject: str, body_text: str) -> None:
    cfg = load_smtp_config()

    msg = MIMEMultipart()
    msg["From"] = cfg.email_address
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_text, "plain", "utf-8"))

    with smtplib.SMTP(cfg.smtp_server, cfg.smtp_port) as server:
        server.starttls()
        server.login(cfg.email_address, cfg.email_password)
        server.send_message(msg)

