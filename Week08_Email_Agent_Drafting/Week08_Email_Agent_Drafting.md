# CEM501: Communication Skills for CEM
## Week 8: The Email Agent — Drafting & Sending (Strand B to C Transition)
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Understand how independent modules compose into a working agent pipeline
- Grasp SMTP at a conceptual level — how programs send email on your behalf
- Internalize why safety guardrails are non-negotiable, backed by real incident data
- Build a complete email agent (reader + templates + sender) in a guided Cursor session
- Position this milestone as the bridge from written communication (Strand B) to agentic AI (Strand C)

---

## Part I: From Modules to Agent — The Big Picture
**(~15 min lecture)**

Over the past several weeks, you have built individual pieces of a communication system. Each piece works on its own. Today, we wire them together into something greater than the sum of its parts.

### 1.1 What You Have Built So Far

| Week | Module | File | What It Does |
|------|--------|------|-------------|
| 5 | Reader | `reader.py` | Connects to your inbox via IMAP, fetches and triages emails |
| 6 | Digest | `digest.py` | Summarizes emails into a morning briefing document |
| 3-4 | Templates | `templates.py` | Generates professional email drafts from brief prompts |

Each module is a standalone script. You can run `reader.py` without `digest.py`. You can use `templates.py` without connecting to any inbox. They are independent.

Today we create `agent.py` — a single script that connects these modules into a pipeline that can:

1. **Read** your inbox and triage messages by urgency
2. **Summarize** what needs your attention
3. **Draft** replies using your templates and an LLM
4. **Send** approved drafts — but only after you confirm

### 1.2 The Pipeline Architecture

This is a **sequential pipeline** — one of the most common patterns in software agent design. Each stage takes input from the previous stage and passes output to the next. Think of it like a construction quality control process: inspect materials, log defects, write the report, distribute it. Each step depends on the one before.

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  READER  │───>│  TRIAGE  │───>│  DRAFT   │───>│  SENDER  │
│ (IMAP)   │    │ (rules)  │    │ (LLM)    │    │ (SMTP)   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
      │               │               │               │
      v               v               v               v
  Fetch 10        Classify:       Generate         Deliver
  unread          URGENT /        reply for        after
  emails          ACTION /        each URGENT      human
                  FYI             & ACTION         approval
                                      │               │
                                      v               v
                                ┌─────────────────────────┐
                                │    HUMAN-IN-THE-LOOP     │
                                │                          │
                                │  "Send this reply to     │
                                │   contractor@build.co?   │
                                │   [y] confirm  [n] skip  │
                                │   [e] edit in Cursor"    │
                                └─────────────────────────┘
```

The critical design choice is that **human confirmation gate** between drafting and sending. The agent drafts; you decide. This is not a limitation — it is the architecture that makes the system safe enough to trust.

> **Key Insight:** In software engineering, this is called the **sequential orchestration pattern** — agents are chained in a predefined linear order where each processes the output of the previous one. By keeping each module independent, you can test, debug, and improve any single piece without breaking the others. This is the same principle behind modular construction — prefabricate components off-site, assemble on-site.

*Reference: Microsoft Azure Architecture Center. ["AI Agent Orchestration Patterns."](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)*

---

## Part II: How Email Sending Works — SMTP for Non-Programmers
**(~15 min lecture)**

You already know how email *reading* works — your reader module connects via IMAP and downloads messages. Sending works through a different protocol: **SMTP** (Simple Mail Transfer Protocol).

### 2.1 The Postal Service Analogy

> **Analogy:** SMTP is the postal service of the internet. When you send a physical letter, you write the address, seal the envelope, and drop it in a mailbox. The postal service picks it up and delivers it — you do not need to know which trucks, sorting facilities, or carriers are involved. SMTP works the same way: your program writes the message (To, From, Subject, Body), hands it to an SMTP server (the post office), and the server handles delivery to the recipient's mail server.

Here is what happens when your agent sends an email:

```
Your Agent                SMTP Server              Recipient's Server
    │                    (smtp.gmail.com)           (mail.company.com)
    │                          │                          │
    │  1. Connect (port 587)   │                          │
    │─────────────────────────>│                          │
    │                          │                          │
    │  2. Upgrade to TLS       │                          │
    │  (encryption handshake)  │                          │
    │<=========================│                          │
    │                          │                          │
    │  3. Authenticate         │                          │
    │  (email + app password)  │                          │
    │─────────────────────────>│                          │
    │                          │                          │
    │  4. Hand over message    │                          │
    │  (To, From, Subject,     │                          │
    │   Body, Attachments)     │                          │
    │─────────────────────────>│                          │
    │                          │  5. Look up recipient    │
    │                          │  and deliver              │
    │                          │─────────────────────────>│
    │                          │                          │
    │  6. "250 OK — Delivered" │                          │
    │<─────────────────────────│                          │
```

### 2.2 Key Concepts (You Do Not Need to Memorize These)

**Port 587** — The standard port for authenticated email submission. Think of it as the specific window at the post office designated for outgoing mail. Port 587 is the recommended port by internet standards bodies (IETF) for email clients submitting messages.

**TLS (Transport Layer Security)** — Encryption that protects your credentials and message content in transit. Without TLS, your email and password would travel across the internet as readable text — like writing your credit card number on a postcard. Port 587 uses STARTTLS, which means the connection starts unencrypted and upgrades to encrypted before any sensitive data is sent.

**App Passwords** — Gmail (and most providers) no longer allow your regular password for programmatic access. Instead, you generate a special "app password" — a one-time code that gives your script permission to send on your behalf without exposing your main password.

**MIME (Multipurpose Internet Mail Extensions)** — The standard for packaging email content. When your email has both a plain-text body and an HTML version, or includes attachments, MIME bundles them into a single message. Python's `email` library handles this for you.

> **Key Insight:** You do not need to understand the internals of SMTP any more than you need to understand the internal combustion engine to drive a car. What matters is that you understand the *trust model*: your script authenticates with *your* credentials, sends from *your* address, and anything it sends is legally and professionally *yours*. There is no "the AI sent it" defense.

*Reference: Cloudflare. ["What SMTP Port Should Be Used?"](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)*

---

## Part III: Safety Guardrails — Why "Send" Is the Most Dangerous Button
**(~20 min lecture)**

This is the most important section of today's lecture. Before your agent sends a single email, you need to understand what can go wrong — not in theory, but in documented reality.

### 3.1 The Scale of Misdirected Email

Misdirected emails — messages sent to the wrong person, with the wrong attachment, or to an unintended group — are one of the most common and costly errors in professional communication.

- **58% of employees** report having sent an email to the wrong person at some point in their career.
- **33% of users** send an average of nearly two misdirected emails per year — not once in a career, but *every year*.
- **44% of employees** admit they have mistakenly exposed personally identifiable information (PII) or business-sensitive information via corporate email, with over 70% of those incidents occurring in the last five years.

*Sources: [Proofpoint — "Misdirected Emails: How to Detect & Prevent Them"](https://www.proofpoint.com/us/blog/email-and-cloud-threats/misdirected-emails-how-detect-and-prevent-them); [Egress — "Misdirected Emails and Files"](https://www.egress.com/solutions/misdirected-emails-and-files)*

### 3.2 Misdirected Email Is the #1 Reported Data Breach Type

This is not a minor issue. Regulators track it.

- In the UK, **"data emailed to the wrong recipient"** was the single most frequently reported data breach to the Information Commissioner's Office (ICO) in 2023, accounting for **16% of all reported incidents** — more than phishing, more than ransomware, more than any other category.
- The Verizon 2025 Data Breach Investigations Report, analyzing over 22,000 incidents and 12,195 confirmed breaches, found that approximately **60% of all confirmed breaches involved a human action** — including misdelivery of sensitive data.
- In **78% of email data loss incidents**, the organization took further action against the employee involved: 46% received formal warnings, and in 27% of cases, the employee lost their job.

*Sources: [Beyond Encryption — "Analysis of 2023 ICO Breach Reporting"](https://www.beyondencryption.com/blog/data-security-an-analysis-of-the-latest-ico-findings); [Verizon — "2025 Data Breach Investigations Report"](https://www.verizon.com/business/resources/reports/dbir/); [Egress — "Misdirected Emails and Files"](https://www.egress.com/solutions/misdirected-emails-and-files)*

### 3.3 Real Incidents — What Goes Wrong

**The Autocomplete Trap (Legal Industry).** In *Terraphrase Engineering v. Arcadis*, a plaintiff's attorney sent multiple privileged litigation emails to his client's *former* employer because the email autocomplete filled in the old company address instead of the client's personal email. The opposing counsel at Arcadis received the privileged strategy emails, shared them with their legal team, and used the information in their counterclaim. The court ultimately granted a protective order, but the damage to the litigation strategy was done.

**The Reply-All Cascade.** In 2013, a single misdirected reply at Cisco triggered a reply-all chain across a distribution list of 23,570 members. The result: over **4 million emails**, **375 GB of network traffic**, and an estimated **$600,000 in lost productivity**. In 2016, a test email at the UK National Health Service reached 840,000 of its 1.2 million employees and generated an estimated **186 million emails**.

**The Construction Scenario.** Consider a CEM-specific situation: a subcontractor's project manager accidentally forwards an internal cost breakdown — showing actual costs and markup — to the general contractor instead of their own estimating team. That single email can undermine an entire change order negotiation. Or a delay notice is auto-sent to the wrong project owner, triggering a contractual clock on liquidated damages for a project that is actually on schedule.

> **Key Insight:** These are not hypothetical scenarios. In a world where 361.6 billion emails are sent per day, even a tiny error rate produces millions of misdirected messages annually. Now imagine giving an automated agent the ability to send on your behalf, at machine speed, without confirmation. That is not efficiency — it is a liability.

*Sources: [Miller Canfield — "Misdirected Email Can Lead To Trouble"](https://www.millercanfield.com/resources-alerts-649.html); [Wikipedia — "Email Storm"](https://en.wikipedia.org/wiki/Email_storm); [CBS News — "Reply-All Email Catastrophe"](https://www.cbsnews.com/news/reply-all-email-catastrophe-hits-thomson-reuters/)*

### 3.4 Why Human-in-the-Loop Is a Design Requirement

The concept of **Human-in-the-Loop (HITL)** comes from AI safety research. Instead of building fully autonomous systems, HITL designs insert human review at critical decision points — especially where errors are costly and irreversible.

Why does this matter for your email agent?

- Sending an email is an **irreversible action**. You cannot un-send a delivered message. Unlike editing a draft or re-running a triage script, once the SMTP server accepts your message, it is gone.
- Research on HITL systems shows measurable safety gains: one study found that adding a human validation checkpoint within an AI workflow **reduced critical assignment errors from approximately 1-in-35 to less than 1-in-500** — a 14x improvement.
- Studies on AI-generated professional communication consistently find that **human-written texts are judged to be of higher quality** regardless of audience. AI drafts tend to be formulaic, and recipients can often detect AI-generated content. When supervisors rely heavily on AI for messages, employees perceive them as less sincere and question their leadership.

The lesson: let the AI draft. Let the human review, edit, and approve. The AI makes you faster; the confirmation step keeps you safe.

> **Key Insight:** Your email agent's confirmation prompt is not a "nice to have." It is the single most important feature in the system. A fast agent with no guardrails is worse than no agent at all — because it can cause damage at machine speed.

*Sources: [Stanford HAI — "Humans in the Loop: Design of Interactive AI Systems"](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems); [IBM — "What Is Human In The Loop?"](https://www.ibm.com/think/topics/human-in-the-loop); [ACM Web Science 2025 — "Emails by LLMs: A Comparison of Language in AI-Generated and Human-Written Emails"](https://dl.acm.org/doi/10.1145/3717867.3717872); [ScienceDaily — "Why AI Emails Can Quietly Destroy Trust at Work"](https://www.sciencedaily.com/releases/2025/08/250811104226.htm)*

### 3.5 The Four Guardrails

Your agent must implement these before it is allowed to send anything:

**Guardrail 1: Confirmation Prompt**
Display the full draft — recipient, subject, body — and require the user to type `y` to send. Any other input cancels or opens the draft in an editor. No silent sends. Ever.

**Guardrail 2: Recipient Validation**
Warn if the recipient is not in a known contacts list. Warn if sending to more than 5 recipients. Block sends to distribution lists unless explicitly overridden. Flag if the domain looks unusual (typos like `gmial.com`).

**Guardrail 3: Content Check**
Warn if the subject line is empty. Warn if the body contains placeholder text like `[INSERT]`, `[TODO]`, or `[PLACEHOLDER]`. Warn if the body is shorter than 20 characters.

**Guardrail 4: Rate Limiting**
Maximum 10 sends per 10-minute window. Log every sent email (timestamp, recipient, subject) to `sent_log.txt`. This prevents runaway loops — if a bug causes your agent to attempt 1,000 sends, the rate limiter stops it after 10.

---

## Part IV: The Build-Along — Wiring Your Agent in Cursor
**(~40 min guided session)**

Today's build session uses **Cursor** — the AI-powered code editor. The workflow is similar to Claude Code but with a visual interface: you see your files, your terminal, and the AI chat panel side by side.

### Phase 1 — The Skeleton (10 min)

Open your project folder in Cursor. Open the AI chat panel (Cmd+L / Ctrl+L) and give it this prompt:

```
Create agent.py that:
1. Imports fetch_emails from reader.py and generate_draft from templates.py
2. Fetches the 10 most recent unread emails
3. Triages each email into URGENT, ACTION, or FYI
4. For each URGENT and ACTION email, generates a draft reply
5. Prints each draft with a placeholder [SEND] at the end
6. Add a main() function with argparse for a --dry-run flag

Do not implement actual sending yet. Use print("[SEND]") as a placeholder.
Include type hints and docstrings.
```

**Checkpoint 1:** Run `python agent.py --dry-run`. You should see triaged emails with draft replies and `[SEND]` placeholders. If you see import errors, check your file names and folder structure.

### Phase 2 — Add the Sender Module (10 min)

Now ask Cursor to build the sending function:

```
Add a send_email(to, subject, body) function to agent.py that:
1. Uses smtplib with STARTTLS on port 587
2. Reads SMTP_HOST, EMAIL_ADDRESS, and APP_PASSWORD from .env
3. Before sending, prints the full draft (To, Subject, Body) and asks
   the user to type 'y' to confirm, 'n' to skip, or 'e' to edit
4. Validates the recipient: warn if not in KNOWN_CONTACTS list,
   warn if sending to >5 recipients
5. Checks content: warn if subject is empty or body contains [INSERT] or [TODO]
6. Implements rate limiting: max 10 sends per 10-minute window
7. Logs every sent email to sent_log.txt with timestamp
```

**Checkpoint 2:** Review the generated code. Does the confirmation prompt appear before every send? Do the guardrails trigger when you test with bad inputs?

### Phase 3 — Wire Everything Together (10 min)

Replace the `[SEND]` placeholders with actual `send_email()` calls:

```
In agent.py, replace every print("[SEND]") with a call to send_email().
Pass the recipient address from the original email, the generated subject,
and the draft body. Respect the --dry-run flag: if dry-run is active,
print the draft but skip the send_email() call entirely.
```

**Checkpoint 3:** Run `python agent.py --dry-run` again. You should see the full pipeline — fetch, triage, draft, display — without any actual sends. The output should clearly label each step.

### Phase 4 — Dry-Run Testing and Verification (10 min)

Test the complete pipeline:

```bash
# Dry run — shows everything but sends nothing
python agent.py --dry-run

# Test with a real send to yourself (optional, instructor-guided)
python agent.py
```

**Checkpoint 4:** If you opt for a live test, send a test email to your own address. Verify:
- The confirmation prompt appeared and you typed `y`
- The email arrived in your inbox
- `sent_log.txt` contains the logged entry with timestamp

**Common Issues and Fixes:**

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| `ModuleNotFoundError: reader` | File not in same directory | Move files or fix import path |
| `.env` values not loading | Missing `python-dotenv` | `pip install python-dotenv` |
| SMTP auth failure | Using regular password | Generate an App Password in Google Account settings |
| `ConnectionRefusedError` | Wrong port or host | Verify `smtp.gmail.com` and port `587` |
| Rate limit triggered immediately | Clock not resetting | Check that the 10-minute window uses `time.time()` |

---

## Part V: Course Arc — What Comes Next
**(~5 min)**

### 5.1 The Strand B to Strand C Bridge

Today's session is the capstone of **Strand B (Written Communication)**. Over Weeks 3-8, you have gone from writing better emails by hand to building a system that reads, triages, drafts, and sends emails with AI assistance and human oversight.

But notice what you have actually built: it is not just an email tool. It is a **software agent** — a program that perceives its environment (inbox), reasons about what to do (triage and draft), and takes action (send). That is the definition of Strand C.

```
Strand B (Written)                    Strand C (Agentic AI)
──────────────────                    ─────────────────────
Week 3: Email writing principles      Week 9: Agent architecture patterns
Week 4: Templates & prompt design     Week 10: MIDTERM
Week 5: Email reader (IMAP)           Week 11: PM tool integration
Week 6: Digest & summarization        Week 12: Memory & scheduling
Week 7: RFI & formal docs             Week 13: Multi-agent coordination
                                      Week 14: Final agent demo
           │
           v
     ┌─────────────┐
     │   WEEK 8    │  <── YOU ARE HERE
     │ Email Agent │
     │  (Bridge)   │
     └─────────────┘
```

### 5.2 What Changes After the Midterm

After the midterm (Week 10), the complexity increases:

- **Week 9 — Agent Architecture:** Formalizing what you built today. Perception-reasoning-action loops. Tool use. State management.
- **Week 11 — PM Tool Integration:** Connecting your agent to project management platforms — reading tasks, updating statuses, generating reports.
- **Week 12 — Memory & Scheduling:** Giving your agent persistent memory (who have I emailed? what was discussed?) and the ability to run on a schedule.
- **Week 13 — Multi-Agent Coordination:** Multiple agents working together — one reads emails, one manages documents, one tracks deadlines.
- **Week 14 — Final Demo:** Your complete communication agent, demonstrated live.

> **Key Insight:** The midterm will test your understanding of everything in Strands A and B — communication principles, email writing, the tools you have built. The post-midterm work assumes you have a working email agent (M4) as your foundation. Do not skip this milestone.

---

### Tool Demo: Cursor Build-Along Walkthrough

The instructor will project Cursor on screen and walk through all four phases live. Key things to observe:

1. **How to prompt Cursor effectively:** Be specific about function signatures, library choices, and error handling. Vague prompts produce vague code.
2. **How to review AI-generated code:** Read every line of the `send_email()` function. Does it actually check the confirmation before calling `server.sendmail()`? Or does it send first and ask later?
3. **How to iterate:** If the first generation is not right, do not start over. Tell Cursor what to fix: "Move the confirmation prompt to before the SMTP connection, not after."
4. **How to test incrementally:** Run after each phase. Do not wait until everything is wired together to discover that Phase 1 had a bug.

> **Key Insight:** The skill you are practicing today is not "writing Python." It is **directing an AI coding tool to build something correctly and safely**. That is a transferable skill — it works with Cursor, Claude Code, Codex, or any future tool.

---

### In-Class Activity: Guided Build-Along (50 min)

Follow the four-phase build session described in Part IV. The instructor will project each phase live and pause for checkpoints.

**Checkpoints:**
- [ ] **After Phase 1:** Run `agent.py --dry-run`. Do you see triaged emails with draft replies and `[SEND]` placeholders?
- [ ] **After Phase 2:** Test the confirmation prompt. Does typing `n` skip the send? Does an empty subject trigger a warning? Does sending to an unknown address produce a warning?
- [ ] **After Phase 3:** Run `agent.py --dry-run` with the sender wired in. Does the full pipeline display without sending?
- [ ] **After Phase 4:** (Optional) Send a test email to yourself. Did it arrive? Is it logged in `sent_log.txt`?

**If you get stuck:**

Raise your hand. The three most common issues are:
1. **Import errors** — File naming or folder structure. Make sure `reader.py`, `templates.py`, and `agent.py` are in the same directory.
2. **`.env` not loading** — Install `python-dotenv` with `pip install python-dotenv` and make sure your `.env` file is in the project root.
3. **SMTP authentication** — You need an App Password, not your regular Gmail password. Go to Google Account > Security > App Passwords.

**If you finish early:**

Try enhancing your agent:
- Add a `--summary-only` flag that runs the pipeline but stops after the digest (no drafting or sending).
- Add color-coded terminal output (green for FYI, yellow for ACTION, red for URGENT).
- Add an `--export` flag that saves all drafts to a `drafts/` folder as `.txt` files for later review.

---

### Milestone: M4 — Email Agent v1

**Due:** Before Week 9

**Deliverable:** `project/agent.py` pushed to your course repository

**Requirements:**

1. **Pipeline completeness:** Reads inbox, triages into URGENT/ACTION/FYI, and generates draft replies for URGENT and ACTION emails
2. **Human confirmation:** Displays each draft (To, Subject, Body) and requires explicit user input (`y`/`n`/`e`) before any send
3. **Safety guardrails:** Implements at least 3 of the 4 guardrails from Section 3.5 (confirmation prompt, recipient validation, content check, rate limiting)
4. **Dry-run mode:** Supports a `--dry-run` flag that runs the full pipeline without sending
5. **Logging:** Logs all sent emails to `sent_log.txt` with timestamp, recipient, and subject
6. **Single command:** Works end-to-end with `python agent.py` (or `python agent.py --dry-run`)

**Grading:** Pass / Needs Revision (you may resubmit once after instructor feedback)

**Submission:** Push to your GitHub fork. The commit message should be: `M4: email agent v1`

---

### Further Reading

**Safety and Human-in-the-Loop:**
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control.* Ch. 7 — on why AI systems should defer to humans.
- Stanford HAI. ["Humans in the Loop: The Design of Interactive AI Systems."](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems)
- IBM. ["What Is Human In The Loop (HITL)?"](https://www.ibm.com/think/topics/human-in-the-loop)

**Email Security:**
- Verizon (2025). [*Data Breach Investigations Report.*](https://www.verizon.com/business/resources/reports/dbir/) — 60% of breaches involve human action.
- Proofpoint. ["Misdirected Emails: How to Detect & Prevent Them."](https://www.proofpoint.com/us/blog/email-and-cloud-threats/misdirected-emails-how-detect-and-prevent-them)
- Beyond Encryption. ["Data Security: An Analysis of 2023 ICO Breach Reporting."](https://www.beyondencryption.com/blog/data-security-an-analysis-of-the-latest-ico-findings)
- McDonald Hopkins. ["Proper Email Protocols on Construction Projects."](https://www.mcdonaldhopkins.com/insights/news/Proper-email-protocols-on-construction-projects)

**AI-Generated Communication:**
- Wilson, W. & Rose, H. (2025). "A Genre, Scoring, and Authorship Analysis of AI-Generated and Human-Written Refusal Emails." *SAGE Journals.* [Link](https://journals.sagepub.com/doi/10.1177/23294906251322890)
- ACM Web Science (2025). "Emails by LLMs: A Comparison of Language in AI-Generated and Human-Written Emails." [Link](https://dl.acm.org/doi/10.1145/3717867.3717872)

**Technical References:**
- Python Docs. `smtplib` — SMTP protocol client.
- Cloudflare. ["What SMTP Port Should Be Used? Port 25, 587, or 465?"](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)
- Cursor Documentation. ["Getting Started."](https://docs.cursor.com)
- Microsoft Azure. ["AI Agent Orchestration Patterns."](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
