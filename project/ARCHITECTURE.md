# System Architecture

**CEM501 Communication Skills for CEM -- Spring 2026**
**Milestone M5 Deliverable**

---

## System Overview

[Write 2-3 sentences describing the overall purpose and design philosophy of your system. What problem does it solve? What are the key design principles (modularity, separation of concerns, etc.)?]

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                      Scheduler                          │
│               (runs pipeline on interval)               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       v
┌──────────┐    ┌──────────────┐    ┌──────────────┐
│  Reader  │───>│  Classifier  │───>│   Drafter    │
│  (IMAP)  │    │   (LLM)      │    │   (LLM)      │
└──────────┘    └──────────────┘    └──────┬───────┘
                                          │
                       ┌──────────────────┘
                       v
                ┌──────────────┐    ┌──────────────┐
                │    Sender    │    │   Messenger   │
                │   (SMTP)     │    │  (Telegram)   │
                └──────────────┘    └──────────────┘
                       │                    │
                       v                    v
                ┌──────────────────────────────────┐
                │            Memory                │
                │   (conversation history store)   │
                └──────────────────────────────────┘
```

[Update this diagram to reflect your actual architecture. Add or remove components as needed.]

---

## Components

### Reader
**File:** `reader.py`
**Responsibility:** [Describe what this component does -- connects to IMAP server, fetches unread emails, parses headers and body, returns structured email objects.]
**Key dependencies:** [e.g., imap_tools]

### Classifier
**File:** `classifier.py`
**Responsibility:** [Describe what this component does -- takes a parsed email and uses an LLM to classify it by type (RFI, submittal, schedule update, etc.) and urgency (high, medium, low).]
**Key dependencies:** [e.g., anthropic or openai]

### Drafter
**File:** `drafter.py`
**Responsibility:** [Describe what this component does -- takes a classified email and its conversation history, generates an appropriate draft response using an LLM with role-specific prompts.]
**Key dependencies:** [e.g., anthropic or openai]

### Sender
**File:** `sender.py`
**Responsibility:** [Describe what this component does -- takes a finalized draft and sends it via SMTP, handles reply threading, CC lists, and delivery confirmation.]
**Key dependencies:** [e.g., smtplib (standard library)]

### Memory
**File:** `memory.py`
**Responsibility:** [Describe what this component does -- stores conversation threads, tracks email history per contact, provides context to the Drafter for follow-up emails.]
**Key dependencies:** [e.g., json or sqlite3]

### Scheduler
**File:** `scheduler.py`
**Responsibility:** [Describe what this component does -- runs the read-classify-draft-send pipeline on a configurable interval, handles logging and error recovery.]
**Key dependencies:** [e.g., schedule]

---

## Data Flow

1. **Scheduler** triggers the pipeline at a configured interval (e.g., every 5 minutes).
2. **Reader** connects to the IMAP server, fetches new unread emails, and returns structured email data.
3. **Classifier** receives each email and calls the LLM API to determine email type and urgency.
4. **Memory** is queried for any prior conversation context related to the sender or thread.
5. **Drafter** receives the classified email plus conversation history and generates a draft response.
6. [Optional: draft is sent to **Messenger** (Telegram) for human review/approval.]
7. **Sender** dispatches the approved draft via SMTP.
8. **Memory** stores the sent response for future context.

---

## API Keys & Configuration

All secrets are stored in a `.env` file (never committed to version control). See `.env.example` for the required variables.

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | LLM API access for classification and drafting |
| `OPENAI_API_KEY` | Alternative/backup LLM API (if used) |
| `EMAIL_ADDRESS` | IMAP/SMTP email account |
| `EMAIL_PASSWORD` | App-specific password for email access |
| `IMAP_SERVER` | Incoming mail server address |
| `SMTP_SERVER` | Outgoing mail server address |
| `SMTP_PORT` | SMTP port (typically 587 for TLS) |
| `TELEGRAM_BOT_TOKEN` | Telegram bot for notifications/approval (if used) |

---

## Future Improvements

[List 2-4 improvements you would make if you had more time.]

- [ ] [e.g., Add support for email attachments (PDF parsing, image OCR)]
- [ ] [e.g., Implement a web dashboard for reviewing drafts]
- [ ] [e.g., Add multi-language support for cross-cultural communication]
- [ ] [e.g., Fine-tune classification with project-specific training data]

---

*CEM501 - Spring 2026 - Dr. Eyuphan Koc - Bogazici University*
