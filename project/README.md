# Poder — Internal AI Communication Agent

**CEM501 Communication Skills for CEM — Spring 2026**  
**Boğaziçi University | Dr. Eyuphan Koc**

---

## Student Information

- **Name:** Hilal Kurt
- **Email:** hilal.kurt@std.bogazici.edu.tr
- **Repository:** [github.com/kurthilal/CEM501](https://github.com/kurthilal/CEM501)

---

## Description

Poder is a **localhost-first AI communication agent** built for a construction-tech startup workflow: email triage and reply drafting, Gmail calendar integration, customer CRM with a sales pipeline, daily todos, LinkedIn/Instagram post drafting, and Telegram field messaging — all from a single web dashboard backed by SQLite.

The agent addresses the founder problem of managing investor email, pilot-site client messages, Telegram threads, and outbound content **manually and in parallel**. Every outbound message stays **human-in-the-loop**: the system classifies, drafts, and logs; the user reviews before send.

---

## Architecture Overview

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full system design (updated through M8/M9).

**High-level summary:** A modular pipeline reads email via IMAP, classifies with Claude (or rule fallback), drafts replies, persists to SQLite, and optionally sends via SMTP — plus a Flask web UI for inbox, calendar, CRM, todos, social media drafting, and Telegram.

---

## Setup Instructions

All commands run from the **`project/`** directory.

### 1. Clone the repository

```bash
git clone https://github.com/kurthilal/CEM501.git
cd CEM501/project
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Edit .env — at minimum for email: EMAIL_ADDRESS, EMAIL_PASSWORD
# Optional: ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, WEB_ALLOW_SEND=1
```

### 5. Verify setup

```bash
python3 -c "import anthropic, flask; print('Setup OK')"
```

---

## How to Run

### Web dashboard (recommended)

```bash
python3 -m demo.web.app
# → http://127.0.0.1:5000
```

Modules in the sidebar: Dashboard, Daily TodoList, Calendar, Customer Relations, Social Media Drafter, Inbox preview, Telegram chat, Memory (SQLite).

Set `WEB_ALLOW_SEND=1` in `.env` to enable SMTP replies, calendar event creation, and Telegram send from the browser.

### Email pipeline (scheduler, dry-run)

Processes recent mail: read → classify → draft → log to SQLite (no SMTP send):

```bash
python3 -m demo.scheduler --once --dry-run --max-emails 5
```

See [agent.log](agent.log) for a recorded end-to-end run with 5 email scenarios.

### Telegram bot

```bash
python3 -m demo.test_bot
```

Requires `TELEGRAM_BOT_TOKEN` in `.env`. Incoming messages are classified, drafted, and logged.

### CLI inbox table

```bash
python3 reader.py
```

### Turkish run guides

- [CALISTIRMA_KILAVUZU.txt](CALISTIRMA_KILAVUZU.txt) — installation and all commands
- [WEB_KULLANIM_KITAPCIGI.txt](WEB_KULLANIM_KITAPCIGI.txt) — web UI usage manual

---

## Milestones Completed

- [x] **M0:** Environment setup and API key configuration
- [x] **M1:** Email reading via IMAP
- [x] **M2:** Email classification with LLM
- [x] **M3:** Draft generation with prompt engineering
- [x] **M4:** Email sending via SMTP
- [x] **M5:** Architecture documentation and code review
- [x] **M6:** Conversation memory and context tracking
- [x] **M7:** Scheduling and automation
- [x] **M8:** Messaging platform integration (Telegram + web dashboard)
- [x] **M9:** Final polish, testing, and demo preparation

---

## AI Tools Used

| Tool / Model | How It Was Used |
|--------------|-----------------|
| Claude (Anthropic API) | Email classification, reply drafting, social media posts, photo descriptions |
| Cursor + Claude Code | Primary IDE pair-programming for Python, Flask UI, and documentation |
| ChatGPT / Claude (planning) | Prompt template brainstorming and architecture discussions |

---

## Reflection

See [REFLECTION.md](REFLECTION.md) for the full project reflection (500–800 words).

---

## Submission Artifacts

| File | Purpose |
|------|---------|
| `README.md` | Clone-and-run instructions (this file) |
| `ARCHITECTURE.md` | System design (M8/M9 final) |
| `REFLECTION.md` | Semester reflection |
| `agent.log` | End-to-end email pipeline log (3+ scenarios) |

---

*CEM501 — Spring 2026 — Dr. Eyuphan Koc — Boğaziçi University*
