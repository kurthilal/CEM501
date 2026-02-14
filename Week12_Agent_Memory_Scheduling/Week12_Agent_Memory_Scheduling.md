# CEM501: Communication Skills for CEM
## Week 12: Agent Memory & Scheduling
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Understand why persistent memory is essential for a communication agent that operates across sessions
- Design a simple SQLite-based schema for contacts, messages, and conversation history
- Implement scheduled tasks (reminders, follow-ups) using Python's `schedule` library
- Apply logging and error-handling patterns to make your agent reliable in daily use
- Quantify the cost of downtime and the value of resilient software design

---

## Part I: Why Agents Need Memory
**(~20 min lecture)**

Imagine hiring a project assistant who, every single morning, has no memory of yesterday. They do not remember which subcontractor you emailed, what the architect said about the curtain wall detail, or that you have a submittal deadline on Thursday. You would fire that assistant immediately. Yet this is exactly how most scripts and chatbots work by default: they start from a blank slate every time you run them.

In construction, continuity is everything. A single project generates hundreds of RFIs, submittals, and stakeholder conversations that span months or years. Your communication agent must remember what happened last week to be useful this week.

---

### 1.1 Session vs. Persistent Memory

| Memory Type | How It Works | Lifespan | CEM Example |
|------------|-------------|----------|-------------|
| **Session memory** (Python variables) | Data lives in RAM while the script runs | Dies when the process stops | Drafting one email in a single sitting |
| **Persistent memory** (database on disk) | Data written to a file that survives restarts | Indefinite | Tracking all emails to a subcontractor over 6 months |

Session memory is fine for a one-off task. But the moment your agent needs to recall context from a previous run — "What did I last send to the structural engineer?" — you need persistence.

### 1.2 The Industry Shift: Memory as a First-Class Feature

The AI industry recognized this gap in 2024-2025 and moved aggressively to solve it. By mid-2025, every major AI vendor — OpenAI, Google, Anthropic — had shipped persistent memory features for their assistants.

Research from the Mem0 platform (2025) quantified the impact of well-designed memory systems:

- **26% improvement** in response quality (measured by LLM-as-a-Judge) compared to OpenAI's built-in memory
- **91% lower p95 latency** — the agent retrieves relevant context faster
- **90% reduction in token cost** — instead of stuffing entire conversation histories into every prompt, the system retrieves only what is relevant

Memory systems today operate at various granularities: individual turns, utterances, entire sessions, topic clusters, and graph-structured facts that capture relationships between entities.

> **Key Insight:** A project manager who loses context between meetings loses trust. The same applies to your agent. Memory is what turns a disposable script into a tool you actually rely on — and recent research shows it makes agents both cheaper and faster, not just smarter.

*Source: Chhikara et al. (2025). "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory." arXiv:2504.19413*

---

## Part II: SQLite — A Database in a Single File
**(~20 min lecture)**

### 2.1 What Is a Database?

Think of a database as a structured spreadsheet. Like Excel, it stores data in rows and columns. Unlike Excel, it enforces rules (this column must be a number, that column cannot be empty), handles concurrent queries without corruption, and lets you search instantly across millions of records. For your agent, you need something small, fast, and embedded directly in your Python program.

### 2.2 Why SQLite?

SQLite is the most widely deployed database engine in the world — and it is not close.

- There are over **1 trillion SQLite databases** in active use today. Every smartphone, every web browser (Chrome, Firefox, Safari), every copy of iTunes, and even aircraft flight systems contain SQLite databases.
- The entire library is **350 KiB** in size — smaller than a single high-resolution photo.
- No server needed. The entire database is a **single ordinary disk file** that you can copy, email, or back up like any other file.
- Python includes SQLite by default: `import sqlite3` — no installation required.
- For many read-heavy workloads, SQLite is **35% faster than reading directly from the filesystem** — the database's indexing and caching outperform raw file I/O.

> **Key Insight:** You do not need to install, configure, or maintain anything. `import sqlite3` gives you a production-grade database engine that powers more applications worldwide than Oracle, MySQL, PostgreSQL, and SQL Server combined. For a personal communication agent, it is the perfect choice.

*Sources: sqlite.org/mostdeployed.html; sqlite.org/fasterthanfs.html*

### 2.3 Three Operations You Need

You do not need to become a database expert. Your agent needs exactly three operations:

| Operation | What It Does | CEM Example |
|-----------|-------------|-------------|
| **INSERT** | Save new data | Store a contact, log a sent message |
| **SELECT** | Retrieve data | Look up a contact's email, find past messages with a subcontractor |
| **UPDATE** | Modify existing data | Mark a follow-up as completed, update a contact's phone number |

### 2.4 Memory Schema for Your Agent

```sql
-- Contacts you communicate with on the project
CREATE TABLE contacts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    email       TEXT,
    phone       TEXT,
    role        TEXT,       -- e.g., 'Structural Engineer', 'Owner Rep'
    company     TEXT,
    notes       TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Every message your agent sends or receives
CREATE TABLE message_history (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id  INTEGER REFERENCES contacts(id),
    direction   TEXT CHECK(direction IN ('sent', 'received')),
    subject     TEXT,
    body        TEXT,
    channel     TEXT,       -- 'email', 'sms', 'slack'
    sent_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scheduled follow-ups and reminders
CREATE TABLE scheduled_tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    due_at      TIMESTAMP NOT NULL,
    contact_id  INTEGER REFERENCES contacts(id),
    status      TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'done', 'skipped')),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

> **Key Insight:** This schema mirrors what a PM already tracks mentally — who am I talking to, what did we say, and what do I need to follow up on? The database just makes it persistent, searchable, and immune to human forgetting.

---

## Part III: Conversation & Contact History
**(~15 min lecture)**

### 3.1 What to Store and Why

Every time your agent sends or receives a message, it should log the event. This creates an audit trail that is invaluable for:

- **Context before drafting** — Query `message_history` to see what you last sent a contact and when. Your agent can reference the previous conversation naturally: "Following up on my email from March 3rd regarding RFI-042..."
- **Meeting preparation** — Pull all recent messages for meeting attendees to build a briefing summary in seconds.
- **Follow-up tracking** — After sending, always INSERT the message into history so future runs know it happened.
- **Dispute protection** — In CEM, a timestamped log of every communication can be worth millions during claims and litigation.

### 3.2 The Send-and-Log Pattern

```python
# Pseudocode -- your agent's send function
def send_and_log(contact_id, subject, body):
    send_email(contact_id, subject, body)      # actual sending
    db.execute(
        "INSERT INTO message_history (contact_id, direction, subject, body, channel) "
        "VALUES (?, 'sent', ?, ?, 'email')",
        (contact_id, subject, body)
    )
    logging.info(f"Sent and logged: contact_id={contact_id}, subject='{subject}'")
```

This pattern ensures that no communication is ever lost. Think of it as the digital equivalent of a construction project log — but one that never has a missing entry, never has illegible handwriting, and is instantly searchable.

---

### 3.3 Privacy Considerations

- **Never store passwords or API keys** in your database — these belong in environment variables or secure vaults.
- **Data minimization** — store only what your agent needs. If a subject line and timestamp suffice, do not log the full body.
- **Access control** — `memory.db` contains professional correspondence. Treat it like a project's confidential files.

---

## Part IV: Scheduling — Making Your Agent Autonomous
**(~15 min lecture)**

### 4.1 What Is Scheduling?

Scheduling is the alarm clock for your agent. Instead of you remembering to run a script every Monday morning, you tell the agent: "Do this task at this time, on this schedule, without me having to think about it."

In construction management, this maps directly to the discipline of scheduling itself — except instead of scheduling concrete pours and steel erections, you are scheduling communications: reminders, digests, follow-ups, and status checks.

### 4.2 Cron and the `schedule` Library

The oldest universal scheduling system is **cron** (Unix, 1975), which uses a five-field syntax: `0 8 * * 1` means "every Monday at 8:00 AM." You do not need cron directly, but the concept — "run this thing at this time on this pattern" — is the foundation.

The Python `schedule` library offers a human-readable version of the same idea:

```python
import schedule
import time

schedule.every().monday.at("08:00").do(send_weekly_rfi_summary)
schedule.every(3).days.do(check_pending_followups)
schedule.every().friday.at("16:00").do(send_weekly_status_digest)

while True:
    schedule.run_pending()
    time.sleep(60)
```

**Limitation:** The `schedule` library runs inside your Python process. When the process exits, the scheduler stops. For production use, consider **APScheduler** (persistent job store), **Celery with celery-beat** (distributed task queue), or **python-crontab** (writes directly to the system cron).

### 4.3 CEM Use Cases

| Scheduled Task | Frequency | Business Value |
|---------------|-----------|---------------|
| Monday-morning status digest to owner | Weekly | Proactive communication, builds trust |
| Submittal deadline reminders (48h before) | Event-driven | Prevents missed deadlines |
| Unanswered RFI follow-ups (after 5 business days) | Daily check | Reduces response delays |
| Weekly subcontractor communication summary | Weekly | Tracks accountability |
| Monthly project communication metrics report | Monthly | Data for lessons learned |

### 4.4 The Construction Scheduling Software Market

Your agent is part of a larger industry trend. The construction scheduling software market was valued at **$1.31 billion in 2024** and is projected to reach **$2.09 billion by 2029**, growing at a compound annual growth rate of **10.1%**. Today, **87% of contractors** are using or planning to use cloud-based construction management software.

PMI research consistently shows that **more than half of all project budget risk** is attributable to ineffective communications. Poor communication is the **primary reason construction projects fail** roughly one-third of the time. Automated scheduling of communications is not a luxury — it is risk mitigation.

> **Key Insight:** A $50 million project with automated communication scheduling does not just save time — it reduces the probability of the disputes, delays, and rework that poor communication causes. At $60 million per average U.S. construction dispute (Arcadis 2025), even a small reduction in dispute risk dwarfs the cost of building these tools.

---

## Part V: Logging & Error Handling
**(~20 min lecture)**

### 5.1 "If You Can't See It, You Can't Fix It"

On a construction site, you would never accept a superintendent who says, "Something went wrong last Tuesday, but I didn't write it down." That is what a program without logging does — it fails silently, and you have no way to reconstruct what happened.

Logging is your agent's daily report. It records what happened, when, and whether it succeeded or failed.

### 5.2 Log Levels

```python
import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
```

| Level | When to Use | CEM Parallel |
|-------|------------|-------------|
| **DEBUG** | Detailed diagnostic info (variable values, query results) | Field engineer's personal notes |
| **INFO** | Normal operations (sent email, ran scheduled task) | Daily report entry |
| **WARNING** | Recoverable issues (API rate limit, retry succeeded) | Near-miss safety report |
| **ERROR** | Failures that need attention (send failed, database locked) | Incident report |

**Resource cost:** In well-configured systems, logging consumes **1-5% of application resources** — a trivial cost for the visibility it provides. High-traffic applications typically log **1-10% of routine operations** but **100% of errors**. The key is structured logging: using JSON key-value pairs makes logs machine-parsable, searchable, and aggregatable across systems.

```
2026-04-14 08:01:23 | INFO  | Email sent to contact_id=7, subject='RFI-042 Response'
2026-04-14 08:01:24 | INFO  | Message logged to database, id=1042
2026-04-14 08:15:00 | WARNING | SMTP rate limit hit, backing off 30s
2026-04-14 08:15:31 | INFO  | Retry succeeded for contact_id=12
2026-04-14 09:00:00 | ERROR | Database file locked, cannot write -- another process?
```

> **Key Insight:** Construction daily logs are legal documents. Your agent's log file serves the same purpose digitally — it is the authoritative record of what your system did and when. In a dispute over whether an email was sent, your log is your evidence.

---

### 5.3 The Cost of Downtime

Why does reliability matter so much? Because failure is expensive:

- **ITIC (2024):** 91% of mid-size and large enterprises report that one hour of downtime costs more than **$300,000**. Among those, **44% say it exceeds $1 million per hour**.
- **Error handling bugs** — the kind where a program crashes instead of recovering gracefully — take an average of **44.1 days to fully address** from discovery to final fix.
- **88% of users** form negative opinions about brands with poorly performing apps, and **34% switch to a competitor immediately** after a bad experience.

For your communication agent, "downtime" means missed follow-ups, unsent reminders, and broken workflows — exactly the communication failures that PMI says cause 56% of project failures.

### 5.4 Retry with Exponential Backoff

Network failures are inevitable. The professional response is not to crash — it is to retry intelligently. **Exponential backoff** is the industry-standard pattern: the delay between retries doubles after each failed attempt (1s, 2s, 4s, 8s...), preventing your agent from hammering a struggling server.

```python
import time
import random

def send_with_retry(contact_id, subject, body, max_retries=3):
    for attempt in range(max_retries):
        try:
            send_email(contact_id, subject, body)
            logging.info(f"Sent to {contact_id} on attempt {attempt + 1}")
            return True
        except ConnectionError:
            wait = (2 ** attempt) + random.uniform(0, 1)  # backoff + jitter
            logging.warning(f"Attempt {attempt + 1} failed, retrying in {wait:.1f}s...")
            time.sleep(wait)
    logging.error(f"All {max_retries} attempts failed for contact_id={contact_id}")
    return False
```

Best practices from AWS Prescriptive Guidance and Microsoft .NET documentation:

1. **Limit retries** — do not retry forever; set a maximum (3-5 attempts is typical)
2. **Classify errors** — retry on transient failures (network timeout), do not retry on permanent failures (invalid email address)
3. **Add jitter** — randomize the delay slightly so multiple agents do not all retry at the same instant
4. **Cap maximum delay** — even with exponential growth, set an upper bound (e.g., 60 seconds)
5. **Log every attempt** — you need to see the retry pattern in your logs to diagnose recurring issues

> **Key Insight:** On a construction site, a missed follow-up email can delay a concrete pour. In software, a crash at 2 AM before a Monday site meeting means your weekly digest never goes out. Retry logic and clear error logs are not optional — they are professional practice, just like safety protocols on a job site.

---

## Part VI: Tool Demo — Building Memory & Scheduling with AI Assistance
**(~15 min live demo)**

Open Claude Code (or Codex/Gemini CLI) in your project directory and try these prompts in sequence:

1. **"Create a SQLite database called memory.db with tables for contacts, message_history, and scheduled_tasks using the schema from our Week 12 lecture notes."**
2. **"Write a Python function send_and_log that sends an email and records it in message_history."**
3. **"Add a scheduler that checks for pending follow-ups every morning at 8 AM and sends reminders for overdue items."**
4. **"Add logging to all database operations and email sends. Use INFO and ERROR levels. Log to agent.log."**
5. **"Add retry logic with exponential backoff to the email sending function. Maximum 3 retries."**

After each prompt, review: Does `send_and_log` log *after* a successful send, not before? Does the retry function log each attempt? Are there any hardcoded passwords or API keys? Is the logging format consistent?

---

## In-Class Activity: Reliability Workshop
**(~35 min hands-on)**

### Phase 1: Break Something on Purpose (15 min)

1. Open your agent's email-sending function.
2. Add a line that simulates a network failure: `raise ConnectionError("Simulated network failure")`
3. Run your agent. What happens?
4. Now add the `send_with_retry` function from Part V. Run again.
5. Open `agent.log`. You should see WARNING entries for failed attempts and either an INFO (success) or ERROR (all attempts exhausted).

**Checkpoint:** Raise your hand when your log shows at least one retry cycle.

### Phase 2: Add Memory (15 min)

1. Create the SQLite tables from Part II (use the schema above or ask your AI agent to generate it).
2. Insert at least 3 sample contacts with realistic CEM roles (e.g., "Structural Engineer at ACME Consulting").
3. Insert at least 5 sample messages with different directions, channels, and timestamps.
4. Write a SELECT query that retrieves all messages sent to a specific contact, ordered by date.
5. Verify persistence: close Python, reopen it, and run the query again. The data should still be there.

**Checkpoint:** Show your partner the query results.

### Phase 3: Peer Review (10 min)

Swap laptops with a partner. Open their `agent.log` file and answer these questions:

- Can you tell what the agent did and when, just by reading the log?
- Are error messages specific enough to diagnose the problem?
- Is there any sensitive information (passwords, API keys) in the log? (There should not be.)

If you cannot answer "yes, yes, no" — their logging needs work. Give them specific, constructive feedback.

---

## Milestone M7: Persistent Agent with Memory + Logs

**Due:** End of Week 12

### Deliverables

| File | Description |
|------|-------------|
| `memory.db` | SQLite database with `contacts`, `message_history`, and `scheduled_tasks` tables, populated with at least 5 contacts and 10 messages |
| `scheduler.py` | A working scheduled task (any interval) that queries the database and produces output |
| `agent.log` | Log file demonstrating at least 10 logged events across INFO, WARNING, and ERROR levels |
| Updated `ARCHITECTURE.md` | New section explaining your memory schema design, scheduling approach, and error-handling strategy |

### Evaluation Criteria

| Criterion | Weight | What We Look For |
|-----------|--------|-----------------|
| **Schema design** | 25% | Tables are normalized, constraints are sensible, data is realistic CEM content |
| **Scheduler reliability** | 25% | Runs without crashing, handles edge cases (no pending tasks, database locked) |
| **Logging quality** | 25% | Logs are readable, timestamped, use appropriate levels, contain no secrets |
| **Error handling** | 25% | At least one error case handled gracefully with retry logic; failure states logged |

> **Key Insight:** This milestone tests whether your agent can survive the real world — restarts, failures, and the passage of time. A script that only works under perfect conditions is a demo. A script that recovers from failures and remembers its history is a tool.

---

### Further Reading

**AI Memory Systems:**
- Chhikara, P. et al. (2025). "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory." [arXiv:2504.19413](https://arxiv.org/abs/2504.19413)

**SQLite:**
- SQLite Documentation: [sqlite.org/lang.html](https://www.sqlite.org/lang.html) (focus on SELECT and INSERT pages)
- "Most Widely Deployed Database Engine": [sqlite.org/mostdeployed.html](https://www.sqlite.org/mostdeployed.html)
- "Faster Than the Filesystem": [sqlite.org/fasterthanfs.html](https://www.sqlite.org/fasterthanfs.html)

**Scheduling:**
- `schedule` library: [schedule.readthedocs.io](https://schedule.readthedocs.io/)
- APScheduler documentation: [apscheduler.readthedocs.io](https://apscheduler.readthedocs.io/)

**Logging & Reliability:**
- Python Logging HOWTO: [docs.python.org/3/howto/logging.html](https://docs.python.org/3/howto/logging.html)
- AWS Prescriptive Guidance: [Retry with Backoff Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)
- Microsoft .NET Documentation: [Transient Fault Handling](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/)
- ITIC (2024). Hourly Cost of Downtime Survey.

**Construction Scheduling Software:**
- Construction Scheduling Software Market Report (2024-2029). Mordor Intelligence / The Business Research Company.

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
