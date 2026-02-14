# CEM501: Communication Skills for CEM
## Week 6: Reports & LLM Summarization (Strand B)
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Explain the legal and contractual significance of construction reports — especially daily reports
- Write a structured daily construction report from raw field notes
- Understand how LLMs tokenize, read, and summarize text (context windows, chunking, hallucination risks)
- Design and build a digest pipeline using Claude Code that summarizes project communications

---

## Part I: Construction Reports — More Than Paperwork

There is a saying in construction law: **"If it was not documented, it did not happen."** This is not a figure of speech — it is a legal reality. Daily reports, inspection logs, and progress records are the primary evidence in construction claims and disputes. Writing a good report is not administrative busywork. It is risk management.

### 1.1 The Report Ecosystem on a Construction Project

A large-scale project can accumulate over 6,000 files across shared workspaces, with over 3,000 unique email threads exchanged in just a two-year span. Construction professionals spend an average of **3 to 3.5 hours per day** on emails alone, and roughly **40% of their time** searching for updates, compiling reports, and attending meetings.

| Report Type | Frequency | Primary Audience | Purpose |
|-------------|-----------|-----------------|---------|
| **Daily Report** | Every workday | PM, Owner, Legal record | Weather, labor, equipment, work performed, issues |
| **Weekly Progress** | Weekly | Owner, Lender | % complete, schedule status, cost status |
| **Monthly Pay Application** | Monthly | Owner, Accounting | Earned value, invoicing |
| **Incident / Safety** | As needed | Safety officer, OSHA | Accidents, near-misses, corrective actions |
| **Inspection Report** | As needed | QA/QC, Architect | Compliance with specs and drawings |
| **Punch List** | Near completion | Subcontractors, Owner | Outstanding deficiencies to close out |
| **Change Order Log** | Ongoing | PM, Owner, Contractor | Scope changes, cost and time impacts |

*Sources: [CooperLink: Construction Email Management](https://www.cooperlink.io/post/construction-project-partners-how-to-efficiently-manage-emails-and-collaborate-finally); [RICS: Information Overload for Project Managers](https://ww3.rics.org/uk/en/journals/construction-journal/information-overload-creating-clarity-as-a-project-manager.html)*

---

### 1.2 Daily Reports as Legal Evidence

A daily report written at 5 PM today can become the decisive piece of evidence in a $60 million dispute three years from now. The **Arcadis 2025 Global Construction Disputes Report** (15th edition) found that the average U.S. construction dispute jumped ~40% in 2024 — from $43 million to over **$60 million** — with an average resolution time of **12.5 months**. The leading cause, for the third consecutive year: **errors and omissions in contract documents**.

Daily reports are admissible in court as **business records** — an exception to the hearsay rule — but only if they meet these conditions:

1. **Created by someone present** at the events described
2. **Prepared contemporaneously** — at or shortly after the events, not days later
3. **Part of regular business practice** — not created specifically for litigation
4. **Factual and objective** — not editorialized opinions

> **Key Insight:** In a tunnel project dispute in Baltimore, a contractor's superintendent dictated daily observations into a voice recorder during his commute each evening. These shift-by-shift records proved "invaluable" during a three-week hearing, helping secure additional compensation and time. The discipline of same-day documentation — not brilliance, not eloquence — won the case.

*Sources: [Miller Nash LLP: Rules of Evidence in Construction Claims](https://www.millernash.com/industry-news/what-do-the-rules-of-evidence-have-to-do-with-documenting-a-construction-claim-everything); [Virginia Tech: Documentation and Records](https://pressbooks.lib.vt.edu/constructioncontracting/chapter/documentation-and-records/); [Arcadis 2025 Disputes Report (PDF)](https://media.arcadis.com/-/media/project/arcadiscom/com/expertise/global/contract-solutions/2025/2025-15th-annual-construction-disputes-report-final-19jun25.pdf)*

### 1.3 Real Consequences: When Reports Win or Lose Disputes

**Scenario A — Good documentation saves $2.4M:** A GC encounters unexpected rock during hospital foundation excavation. The superintendent's daily reports record the exact date, hours on rock removal, equipment mobilized, and crews affected. The contractor presents 47 consecutive daily reports with consistent entries. The arbitrator awards $2.4 million.

**Scenario B — Poor documentation loses $1.8M:** A subcontractor claims 62 days of owner-caused delay, but daily reports were filed only 3-4 days per week with vague entries like "waited for materials" — no dates, quantities, or responsible parties. The claim is denied.

> **Key Insight:** The party with better documentation almost always prevails. A daily report is not just a record of work — it is insurance. You cannot retroactively create good documentation.

*Source: [ConsensusDocs: Proactively Addressing Construction Claims](https://www.consensusdocs.org/news/proactively-addressing-potential-construction-claims/)*

---

## Part II: What Makes a Good Daily Report

### 2.1 The Seven Required Elements

A complete daily report covers seven categories. Omitting any one creates a gap that opposing counsel will exploit.

| # | Element | Why It Matters |
|---|---------|---------------|
| 1 | **Date, project name, report number** | Establishes the chain of documentation |
| 2 | **Weather** (morning + afternoon) | Supports or refutes weather delay claims |
| 3 | **Manpower** (by trade, sub, count) | Proves staffing levels and contractor performance |
| 4 | **Equipment** (status: active, idle, standby) | Documents idle equipment costs for claims |
| 5 | **Work performed** (locations, quantities, %) | The factual core of the report |
| 6 | **Delays, issues, RFI status** | Real-time record of impediments |
| 7 | **Safety and visitors** | OSHA compliance and witness documentation |

> **Key Insight:** Weather logs recorded at multiple times throughout the day strengthen delay claims significantly. An afternoon thunderstorm that halted concrete pouring will not appear in a morning-only weather entry.

---

### 2.2 Example: A Well-Written Daily Report

```
==================================================
DAILY CONSTRUCTION REPORT
Project: Bogazici Research Center — Phase 2
Date: March 12, 2026       Report #: DCR-047
Prepared by: A. Yilmaz, Assistant PM
Weather:  Morning 8°C overcast, light wind
          Afternoon 12°C partly cloudy
          Impact: None
==================================================

MANPOWER (Total on site: 30)
  Ironworkers    (Sub: Demir AS)     — 12
  Concrete       (Sub: Beton Ltd)    —  8
  Electricians   (Sub: Elektrik Co)  —  4
  General labor                      —  6

EQUIPMENT ON SITE
  Tower crane (TC-01)   — operational, full day
  Concrete pump         — active 09:00–14:00
  Backhoe               — IDLE (awaiting excavation permit)

WORK PERFORMED
  - Completed rebar placement, Level 3 slab,
    Grid A1–A5 (100%)
  - Poured concrete, Level 2 columns, Grid B3–B7
    (12 m3, mix C30/37)
  - Continued electrical rough-in, Level 1 east wing
    (~60% complete)
  - Formwork stripping, Level 2 slab, Grid A1–A3

DELAYS / ISSUES
  - Curtain wall anchor submittal: pending architect
    review (RFI-032, submitted Feb 28 — 12 days
    outstanding)
  - Backhoe idle: excavation permit for utility trench
    delayed by municipality — 3rd day idle
  - Concrete delivery was 45 min late (arrived 09:45
    vs. scheduled 09:00); no schedule impact

SAFETY
  - Toolbox talk: working at heights (28 attendees)
  - No incidents or near-misses

VISITORS
  - S. Ozkan (Owner's rep) — site walk 10:00–11:30
  - Structural inspector — L2 column rebar check,
    APPROVED

PHOTOS ATTACHED: 4 (rebar placement L3, concrete
pour L2, idle backhoe, formwork stripping)
==================================================
```

### 2.3 What Makes This Report Effective

Notice the qualities that give this report evidentiary value:

- **Specific locations**: Grid lines and levels, not "worked on the building"
- **Quantities**: 12 m3 of C30/37, not "poured concrete"
- **Named subcontractors**: Demir AS, Beton Ltd — accountability is clear
- **Status flags**: 100%, ~60%, IDLE, APPROVED, pending
- **Time references**: "09:45 vs. scheduled 09:00" — precision matters for delay analysis
- **Days outstanding**: "12 days outstanding" on RFI-032 — builds the delay narrative day by day
- **Photo references**: Visual evidence tied to written description

### 2.4 Common Mistakes in Daily Reports

| Mistake | Example | Why It Hurts |
|---------|---------|-------------|
| Vague work descriptions | "Worked on concrete" | Cannot prove what was actually done |
| Missing quantities | "Poured columns" | Cannot verify progress or payment |
| No location references | "Installed rebar" | Where? Which level? Which grid? |
| Skipping "no incident" entries | Leaving safety blank | Opposing counsel argues safety was not monitored |
| Editorializing | "Owner is being unreasonable about the RFI" | Undermines credibility as objective business record |
| Inconsistent filing | Reports only 3-4 days/week | Gaps suggest incomplete monitoring |

> **Key Insight:** Write "No incidents or near-misses" rather than leaving the safety section empty. An empty field looks like negligence. A "none" entry proves you checked.

---

## Part III: LLM Summarization — How AI Reads and Condenses

Your project generates daily reports, emails, RFIs, meeting minutes, and inspection logs — potentially hundreds of pages per week. No human can read all of it carefully. This is where LLM summarization becomes a practical tool. But first, you need to understand what happens under the hood.

### 3.1 Tokens — How the AI Reads

An LLM does not read words the way you do. It reads **tokens** — fragments of text that are typically smaller than words.

> **Analogy:** Think of tokens like syllables. When you read the word "unbelievable," you process it as one word. The AI breaks it into three pieces: "un," "believ," and "able." Each piece is a token. Common short words like "the" or "is" are single tokens. Longer or rarer words get split into multiple tokens.

The technical process is called **tokenization** — the AI uses an algorithm (typically Byte-Pair Encoding) to split text into these fragments and assign each one a numerical ID. The model does not see letters or words — it sees a sequence of numbers.

**Practical rule of thumb:**
- **1,000 words is roughly 1,300–1,500 tokens**
- A typical daily report (300–400 words) is about 400–600 tokens
- A one-page email is roughly 200–400 tokens

This matters because LLMs have a hard limit on how many tokens they can process at once.

---

### 3.2 Context Windows — The AI's Working Memory

The **context window** is the total tokens an LLM can hold at once — your instruction, the input text, and the generated output must all fit. Current sizes (early 2026):

| Model | Context Window | Practical Equivalent |
|-------|---------------|---------------------|
| **Claude Sonnet 4** | 200,000 tokens (1M in extended beta) | ~130,000 words / a 500-page book |
| **GPT-5** | 400,000 tokens | ~260,000 words / two 500-page books |
| **Gemini 2.5 Pro** | 1,000,000 tokens | ~650,000 words / five 500-page books |

These numbers sound huge, but there is a caveat: **models degrade before hitting their limit.** A model claiming 200K tokens typically becomes unreliable around 130K, with sudden drops. It may "forget" information in the middle of a long input — a phenomenon called **lost in the middle**.

> **Key Insight:** A context window is like your desk. A bigger desk lets you spread out more documents, but you still focus on what is right in front of you. If you stack 500 pages on a large desk, you will still lose track of what is on page 247. The same happens to LLMs.

*Sources: [AIMultiple: LLMs for Extended Context Windows (2026)](https://aimultiple.com/ai-context-window); [Elvex: Context Length Comparison (2026)](https://www.elvex.com/blog/context-length-comparison-ai-models-2026)*

---

### 3.3 What Happens When You Say "Summarize This"

Summarization is **lossy compression** — the model reads your instruction + document as tokens, decides what matters, and generates a shorter version. What gets kept depends on how you frame the instruction:

| Prompt | Result Quality |
|--------|---------------|
| "Summarize this" | Generic, unfocused — the model guesses what matters |
| "Summarize this for a project manager in 3 bullets" | Better — audience and format are specified |
| "Extract all safety incidents, delays, and outstanding RFIs" | Best — targeted extraction, not open-ended summary |

> **Key Insight:** "Summarize this" is the weakest possible summarization prompt. It is like telling an intern "read this and tell me what's important" without explaining your role or priorities. Always specify **who** the summary is for and **what categories** of information to extract.

---

### 3.4 Chunking — When the Input Is Too Large

To summarize 200 daily reports (~100K tokens), you use **chunking**: split into groups of 20, summarize each group, then combine those summaries into a final one. This **map-reduce summarization** trades one long, unreliable pass for multiple short, reliable passes. For our digest pipeline, a morning's emails (10–30 messages) fit in one pass — but you should know the concept for scaling up.

---

### 3.5 Hallucination Risks in Summarization

LLMs can **hallucinate** — generate information that is plausible-sounding but factually wrong or absent from the source text. This is the single most important risk when using AI for construction documentation.

The **Vectara Hallucination Leaderboard** (updated February 2026) evaluates how often LLMs introduce fabricated facts when summarizing documents across 7,700+ articles. Selected results:

| Model | Hallucination Rate | Factual Consistency |
|-------|-------------------|-------------------|
| Gemini 2.5 Flash Lite | 3.3% | 96.7% |
| GPT-4.1 | 5.6% | 94.4% |
| Gemini 2.5 Pro | 7.0% | 93.0% |
| GPT-4o | 9.6% | 90.4% |
| Claude Haiku 4.5 | 9.8% | 90.2% |
| Claude Opus 4.5 | 10.9% | 89.1% |
| Claude Sonnet 4.5 | 12.0% | 88.0% |

Even the best models hallucinate **3–5% of the time** on summarization tasks. In medical text summarization, a 2025 study in *npj Digital Medicine* found a 1.47% hallucination rate and a 3.45% omission rate in LLM-generated clinical notes.

What does this mean for construction? If you summarize 30 emails and the model fabricates a detail in one of them — say, it states an RFI was "approved" when the original email said "under review" — that error could cause a crew to proceed with unapproved work.

> **Key Insight:** LLM summaries are drafts, not records. Always treat AI-generated summaries as a first pass that requires human verification. Never file an AI summary as an official project document without review.

*Sources: [Vectara Hallucination Leaderboard (GitHub)](https://github.com/vectara/hallucination-leaderboard); [npj Digital Medicine: Clinical Safety of LLM Summarization (2025)](https://www.nature.com/articles/s41746-025-01670-7)*

---

## Part IV: Building a Digest Pipeline

### 4.1 What the Digest Generator Does

Your `digest.py` takes emails from `reader.py` (Week 5) and produces a **one-page morning digest** a PM can read in 2 minutes.

**Architecture:** `reader.py (fetch emails)` → `group by triage category` → `summarize URGENT/ACTION via LLM` → `list FYI subjects` → `count ARCHIVE` → `format and print digest`

### 4.2 Building It Step by Step with Claude Code

Open your terminal, navigate to your project folder, and launch Claude Code (`cd ~/cem501-agent/project && claude`).

**Step 1 — Describe the pipeline:**

```
"Create digest.py that takes a list of email dictionaries
with keys: subject, sender, body, and triage_category.
Group emails by category. For URGENT and ACTION emails,
include a one-line summary of each. For FYI, list subject
lines only. Skip ARCHIVE emails (just show count).
Output a formatted text digest with a header showing
the date and time."
```

**Step 2 — Review:** Read through it. Ask: `"Explain the group_by_category function line by line"`

**Step 3 — Test with hardcoded data:**
```
"Add a test function with 6 sample construction emails
(2 URGENT, 2 ACTION, 1 FYI, 1 ARCHIVE) and run the
digest on them"
```

**Step 4 — Add LLM summarization:** `"Add a summarize_email(body) function that uses the Anthropic API to generate a one-sentence summary. Use it for URGENT and ACTION emails only."`

**Step 5 — Connect to your reader:** `"Import fetch_recent and triage_email from reader.py so the digest pulls from my actual inbox"`

### 4.3 Example Digest Output

```
=== PROJECT MORNING DIGEST ===
Generated: March 13, 2026 at 07:15
Covering: 10 emails from last 12 hours
============================================

--- URGENT (1) ---
[1] From: OSHA Inspector
    Subject: Fall protection deficiency — immediate
             correction required
    Summary: Inspector found missing guardrails on
             Level 4 east. Correction required before
             work resumes above Level 3.

--- ACTION (3) ---
[2] From: Project Architect
    Subject: RFI-047 Response: Rebar spacing at Pier 3
    Summary: Architect approved Option B (150mm
             spacing). Proceed with installation.

[3] From: Concrete Supplier
    Subject: Updated delivery schedule for Week 12
    Summary: Thursday pour moved to Friday due to
             plant maintenance. Adjust formwork crew.

[4] From: Owner's Rep
    Subject: Schedule review meeting — agenda needed
    Summary: Requesting agenda items by EOD Wednesday
             for Friday OAC meeting.

--- FYI (4) ---
  - Weekly safety stats — February summary
  - Subcontractor insurance cert renewal (Demir AS)
  - Project photo album updated
  - Industry newsletter: New OSHA silica dust rules

--- ARCHIVE (2 emails skipped) ---
============================================
=== END DIGEST ===
```

> **Key Insight:** The digest is not a replacement for reading critical emails. It is a triage tool — it tells you which 2-3 emails need your attention right now, so you do not waste 30 minutes scanning your entire inbox. The URGENT and ACTION summaries are AI-generated drafts; always click through to the original email before taking action.

---

## Tool Demo: Claude Code Session (Live, ~10 min)

The instructor will build the digest generator live, demonstrating: (1) describing what you want in plain language, (2) reviewing generated code before accepting, (3) testing incrementally, and (4) iterating with follow-up instructions like "add error handling" or "make the output cleaner."

**Watch for:** The instructor reviews AI output before accepting — the same principle as reviewing an AI summary before filing it as a project record.

---

## In-Class Activity (60 min total)

### Activity 1: Write a Daily Report from Raw Field Notes (25 min)

You will receive raw field notes from a fictional day on a bridge rehabilitation project — messy, incomplete, unordered. Transform them into a professional daily report following Part II. Use the template format.

**Peer review (5 min):** Swap with a partner and check:
- [ ] Specific locations (grid lines, spans, levels)?
- [ ] Quantities included (m3, linear meters, count)?
- [ ] Subcontractors named?
- [ ] Could it support a delay claim?
- [ ] Safety section complete (even if "no incidents")?
- [ ] Tone objective and factual?

### Activity 2: Build Session — Digest Generator (35 min)

Follow along to build `digest.py` using Claude Code (or Codex CLI / Gemini CLI).

**Checkpoints:**
1. (10 min) Basic digest with hardcoded sample emails — runs and prints
2. (10 min) Add LLM summarization for URGENT and ACTION items
3. (10 min) Connect to `reader.py` and run with live inbox data
4. (5 min) Customize formatting, categories, summary length

**Stretch goal:** Add a `--format html` flag for an emailable digest.

---

## Milestone: M3 — Daily Digest Generator

**Due:** Before Week 7

**Deliverable:** `project/digest.py` pushed to your course repository

**Requirements:**

1. Accepts a list of email dictionaries (or reads from `reader.py`)
2. Groups emails by triage category (URGENT, ACTION, FYI, ARCHIVE)
3. Generates a one-sentence LLM summary for URGENT and ACTION items
4. Outputs a formatted text digest with date/time header
5. Works end-to-end: `python digest.py` prints a digest from your inbox
6. Includes at least 3 hardcoded test emails so the grader can verify without inbox access

**Grading:** Pass / Needs Revision

**Pass criteria:** Code runs without errors, produces a readable digest, and summaries are coherent. You do not need to handle edge cases perfectly — the goal is a working prototype.

---

### Further Reading

**Construction Documentation:**
- Hinze, J. (2006). *Construction Planning and Scheduling.* Ch. 17: Project Documentation
- [Virginia Tech: Documentation and Records in Construction Contracting](https://pressbooks.lib.vt.edu/constructioncontracting/chapter/documentation-and-records/)
- [Arcadis (2025). Global Construction Disputes Report (PDF)](https://media.arcadis.com/-/media/project/arcadiscom/com/expertise/global/contract-solutions/2025/2025-15th-annual-construction-disputes-report-final-19jun25.pdf)
- [Miller Nash LLP: Rules of Evidence in Construction Claims](https://www.millernash.com/industry-news/what-do-the-rules-of-evidence-have-to-do-with-documenting-a-construction-claim-everything)

**LLM Summarization and Hallucination:**
- [Vectara Hallucination Leaderboard (GitHub)](https://github.com/vectara/hallucination-leaderboard)
- [npj Digital Medicine: Clinical Safety of LLM Summarization (2025)](https://www.nature.com/articles/s41746-025-01670-7)
- Anthropic. "Prompt Engineering Guide" — summarization best practices
- [Seantrott: Tokenization in LLMs, Explained](https://seantrott.substack.com/p/tokenization-in-large-language-models)

**Information Overload in Construction:**
- [RICS: Information Overload — Creating Clarity as a PM](https://ww3.rics.org/uk/en/journals/construction-journal/information-overload-creating-clarity-as-a-project-manager.html)
- [ResearchGate: Project Information Overload & PMIS in Construction (2023)](https://www.researchgate.net/publication/372546196_Project_Information_Overload_Role_of_PMIS_in_Managerial_Decision-Making_A_Study_in_Construction_Companies_of_Oman)

---
**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
