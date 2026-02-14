# CEM501: Communication Skills for CEM
## Week 1: Communication Landscape & Tool Setup
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Understand why communication is a core competency in construction engineering and management
- Quantify the cost of poor communication using industry data
- Map the three course strands: verbal, written, and AI-augmented communication
- Set up the development toolchain: Git, GitHub, Cursor, and Claude Code
- Make your first commit to the course repository

---

## Part I: Why Communication Matters in CEM
**(~20-25 min lecture)**

Construction projects fail more often from communication breakdowns than from technical errors. This is not a platitude — it is one of the most rigorously documented facts in our industry. Let's walk through the evidence.

---

### 1.1 The Scale of the Problem: $31.3 Billion in Rework

In 2018, FMI and PlanGrid (now Autodesk Build) published *Construction Disconnected*, a landmark survey of over 600 U.S. construction professionals. The headline findings:

- Poor communication and inaccurate project data account for **48% of all rework** on U.S. construction sites.
- Breaking that down: **26% of rework** is caused by miscommunication between team members, and **22%** by poor or inaccessible project information.
- The annual cost: **$31.3 billion** in rework alone — $17 billion from miscommunication and $14.3 billion from bad data.

> **Key Insight:** $31.3 billion per year is not an abstract number. That is roughly the GDP of a small country, lost every year to preventable communication failures in one national construction market.

*Source: FMI & PlanGrid (2018). "Construction Disconnected." [Press release](https://www.prnewswire.com/news-releases/new-research-from-plangrid-and-fmi-identifies-factors-costing-the-construction-industry-more-than-177-billion-annually-300689826.html)*

---

### 1.2 Where the Time Goes: 14 Hours per Week Wasted

The same FMI/PlanGrid study tracked how construction professionals spend their working hours. The results are striking:

| Non-Productive Activity | Hours/Week |
|------------------------|------------|
| Searching for project data | 5.5 |
| Conflict resolution among stakeholders | ~5.0 |
| Managing rework and fixing mistakes | ~4.0 |
| **Total non-productive time** | **~14+ hours** |

That is **35% of a 40-hour work week** spent on avoidable problems — nearly two full working days. Across the entire U.S. construction workforce, this non-productive time costs an estimated **$177.5 billion in labor costs annually**.

> **Key Insight:** When your superintendent spends Monday and Tuesday looking for information, resolving misunderstandings, and fixing rework — that is not "part of the job." That is a system failure, and better communication is the fix.

*Source: FMI & PlanGrid (2018). [For Construction Pros summary](https://www.forconstructionpros.com/business/business-services/financing-insurance-leasing/press-release/21015974/plangrid-poor-communication-rework-bad-data-management-cost-construction-industry-177b-annually)*

---

### 1.3 Rework: The Hidden Tax on Every Project

Rework is the most direct financial consequence of poor communication. Decades of research have tried to pin down its cost as a percentage of total project value:

| Study | Rework as % of Contract Value |
|-------|-------------------------------|
| Cnudde (1991) | 10–20% |
| Nylén (1996) | ~10% |
| Love & Li (2000) | 2.4–3.2% |
| Hwang et al. (2009) | ~5.0% |
| McDonald (2013) | ~6.4% |
| Dougherty & Hughes (2014) | ~4.9% |

Most studies cluster between **4–10% of total project cost**. On a $50 million project, even 5% rework means $2.5 million burned — enough to fund an entire project management team for a year. And 48% of that rework traces back to communication.

Projects with consistent QA/QC processes (which are fundamentally communication systems — checklists, inspections, sign-offs) keep rework costs under 5% of budget 56% of the time, compared to only 37% for projects without such standards.

*Sources: Love, P.E.D. & Li, H. (2000). "Quantifying the causes and costs of rework in construction." Construction Management and Economics. Hwang, B.G. et al. (2009). "Measuring the Impact of Rework on Construction Cost Performance." Journal of Construction Engineering and Management, ASCE. See also [PlanRadar: Cost of Rework in Construction](https://www.planradar.com/us/cost-of-rework-construction/)*

---

### 1.4 Project Failure and the PMI Data

The Project Management Institute (PMI) has consistently identified communication as the top risk to project success:

- According to the **PMI Pulse of the Profession** report, ineffective communication is a contributing factor in **56% of failed projects**.
- PMI estimates that **one in five projects fails** as a direct result of poor communication.
- The PMBOK Guide states that project managers spend approximately **90% of their time communicating** — formally and informally.

> **Key Insight:** If you are a project manager and communication is 90% of your job, then communication skill is not supplementary to your technical skill — it *is* the core technical skill of your role.

*Sources: PMI (2013). "The High Cost of Low Performance: The Essential Role of Communications." [Pulse of the Profession](https://www.pmi.org/learning/library/en-2013-pulse-high-cost-low-performance-13512). See also: PMI (2006). ["Art of Communication in Project Management."](https://www.pmi.org/learning/library/effective-communication-better-project-management-6480)*

---

### 1.5 When Communication Fails Become Disputes: $60 Million Average

When communication problems are not caught early, they escalate into formal disputes. The Arcadis Global Construction Disputes Report (2025) — the 15th annual edition — provides the current state:

- The **average value of a construction dispute** in the U.S. is **$60.1 million**.
- The **average duration** of a dispute in North America is approximately **12.5 months**.
- The **leading cause of disputes**, for the third consecutive year: **errors and omissions in contract documents** — which are, at their root, communication failures (unclear specs, ambiguous scope, missing information).
- Other top causes: failure to understand or comply with contractual obligations, and owner-directed changes without adequate documentation.

> **Key Insight:** A $60 million dispute that takes over a year to resolve often started as an ambiguous paragraph in a specification, an RFI that was never answered, or a verbal agreement that was never documented. The cost of writing clearly is zero. The cost of writing poorly can be $60 million.

*Source: Arcadis (2025). "Global Construction Disputes Report: Construction Disputes in Motion." [Report PDF](https://media.arcadis.com/-/media/project/arcadiscom/com/expertise/global/contract-solutions/2025/2025-15th-annual-construction-disputes-report-final-19jun25.pdf)*

---

### 1.6 Productivity: Construction's Stubborn Underperformance

McKinsey Global Institute's 2017 report *Reinventing Construction* placed communication and coordination at the heart of the industry's productivity crisis:

- Global labor productivity growth in construction has averaged only **1% per year** over the past two decades, compared to **2.8% for the total world economy** and **3.6% for manufacturing**.
- Construction is among the **least digitized sectors in the world** — second to last in the U.S. on MGI's digitization index.
- Large projects typically take **20% longer than scheduled** and can run **up to 80% over budget**.
- McKinsey estimated that digital transformation could yield **14–15% productivity gains** and **4–6% cost reductions** — gains that depend heavily on better information flow and communication.

> **Key Insight:** Construction's productivity problem is not about bricklaying speed or crane capacity. It is about information — getting the right document to the right person at the right time. That is a communication problem.

*Source: McKinsey Global Institute (2017). ["Reinventing Construction: A Route to Higher Productivity."](https://www.mckinsey.com/capabilities/operations/our-insights/reinventing-construction-through-a-productivity-revolution)*

---

### 1.7 The KPMG Evidence: Budget and Schedule Failures

KPMG's Global Construction Survey (2015) surveyed senior executives across the construction industry worldwide:

- **69% of projects** failed to come within 10% of their expected budget over a three-year period.
- **75% of projects** failed to meet their scheduled deadline within a 10% margin.
- The report identified **poor scope management and inadequate communication** as the biggest contributors to project failure.
- Only 50% of respondents used a Project Management Information System (PMIS) — meaning half the industry was managing complex communication with spreadsheets, email threads, and phone calls.

*Source: KPMG International (2015). ["Climbing the Curve: Global Construction Survey 2015."](https://assets.kpmg.com/content/dam/kpmg/pdf/2015/04/global-construction-survey-2015.pdf)*

---

### 1.8 The Document Flood: What CEM Professionals Actually Manage

Consider the sheer volume of written communication on a single project:

- **RFIs:** Industry research estimates approximately **10 RFIs per $1 million** of project value. A $50 million project may generate ~500 RFIs, each requiring an average of **8 hours** to receive, log, review, and respond to. Average first response time: **6–10 days**.
- **Submittals:** A large commercial project can involve hundreds of submittals, each with multiple review cycles.
- **Daily reports:** One per day, per active work area — potentially dozens across a large site.
- **Emails:** The average professional receives **121 emails per day**. Construction PMs dealing with multiple subcontractors, owners, and consultants often exceed this significantly.
- **Meeting minutes, change orders, schedule narratives, safety briefings, claims correspondence...**

Each of these documents is a communication act with contractual, financial, and safety implications. A poorly written RFI doesn't just waste time — it can delay critical-path work and generate claims.

> **Key Insight:** You will write more in your CEM career than most novelists. The difference: your words have contractual force, and your audience includes lawyers.

*Sources: CMAA (n.d.). ["Impact & Control of RFIs on Construction Projects."](https://www.cmaanet.org/sites/default/files/resource/Impact%20&%20Control%20of%20RFIs%20on%20Construction%20Projects.pdf) Procore (n.d.). ["Contractor's Guide to RFIs."](https://www.procore.com/library/rfi-construction)*

---

### 1.9 Safety: When Miscommunication Becomes Life-Threatening

Communication failures in construction don't just cost money — they cost lives.

- Construction workers account for approximately **20% of all workplace fatalities** in the United States (2023 data).
- OSHA investigated 96 structural collapses during construction (1990–2008) and found that **construction errors contributed to 80%** of these incidents — errors often rooted in miscommunication about plans, specifications, and field conditions.
- Inadequate communication between teams, subcontractors, and workers leads to confusion about safety requirements and unsafe conditions. Improvement in communication — whether an overarching safety plan or specialized protocols like hand signals — has a **measurable effect on reducing incidents**.

> **Key Insight:** When a superintendent says "pour the slab" and the electrician hasn't finished the rough-in because nobody communicated the schedule change — that is an annoyance. When a rigger signals a crane operator and the signal is misunderstood — that is a fatality. Communication is life safety.

*Sources: [OSHA Construction Incident Investigation Reports](https://www.osha.gov/construction/engineering). [OSHA Commonly Used Statistics](https://www.osha.gov/data/commonstats)*

---

### 1.10 Why This Course Exists: The Communication Skill Stack

Let's synthesize the evidence:

| Finding | Source |
|---------|--------|
| 48% of rework from communication + data issues | FMI/PlanGrid (2018) |
| $31.3B annual rework cost from miscommunication | FMI/PlanGrid (2018) |
| 14+ hours/week wasted on non-productive activities | FMI/PlanGrid (2018) |
| 56% of failed projects cite communication | PMI Pulse of the Profession (2013) |
| 90% of a PM's time is communication | PMBOK Guide |
| $60.1M average U.S. construction dispute | Arcadis (2025) |
| 69% of projects fail budget targets | KPMG (2015) |
| 1% annual productivity growth (vs. 2.8% economy-wide) | McKinsey (2017) |

The pattern is clear: **communication is the single largest controllable risk factor in construction project delivery.** And yet, most CEM programs teach technical skills — scheduling, estimating, structural analysis — and treat communication as an afterthought.

This course is the corrective. You will learn to:
1. **Write** — emails, RFIs, reports, meeting minutes that are clear, complete, and contractually sound.
2. **Speak** — presentations, meetings, negotiations where you are persuasive and precise.
3. **Build** — an AI-powered communication agent that amplifies your writing and organizational skills.

---

## Part II: Three Strands of This Course

| Strand | Focus | Example Deliverables |
|--------|-------|---------------------|
| **A -- Verbal** | Presentations, meetings, negotiation | Lightning talks, OAC meeting simulations |
| **B -- Written** | Emails, RFIs, reports, proposals | Email rewrites, RFI templates, project reports |
| **C -- AI Agent** | Building a personal communication agent | Prompt libraries, email drafting agent, final demo |

All three strands converge toward one capstone: a working AI communication agent that can draft, review, and organize your CEM correspondence.

---

## Part III: What Is an AI Communication Agent?

Think of it as a personal assistant that lives in your terminal. By the end of the semester you will have built a system that can:

- Draft professional emails given a brief prompt
- Apply CEM-specific templates (RFI, submittal cover letter, delay notice)
- Summarize meeting notes and flag action items
- Learn your tone and preferences over time

You do **not** need prior programming experience. Cursor and Claude Code will write most of the code for you — your job is to direct them with clear instructions, which is itself a communication skill.

---

## Part IV: The Toolchain (Demystified)

If you have never used any of these tools before — that is completely fine. Let's start with plain-language explanations.

---

### 4.1 What Is a "Terminal" / "Command Line" / "CLI"?

Your computer has two ways to talk to it. The one you know: clicking icons, dragging files, tapping buttons — that is the **graphical interface (GUI)**. The other way: typing short text commands into a black window — that is the **terminal** (also called the command line, shell, or CLI).

Think of it like this:

> **Analogy:** The GUI is like walking into a restaurant and pointing at the menu. The terminal is like calling the kitchen directly and saying exactly what you want. Both get you food — the terminal is just faster and more precise once you learn the language.

On **macOS**, the terminal app is called *Terminal* (or *iTerm2*). On **Windows**, you will use *PowerShell* or *Windows Terminal*. You type a command, press Enter, and the computer responds with text.

That's it. No magic. You will only need a handful of commands this semester, and the AI tools will help you with the rest.

---

### 4.2 Git — Your Project's "Save History"

You already use "Save" in Word or Google Docs. But what if you want to go back to the version from last Tuesday? Or see exactly what changed between two versions? That is what **Git** does.

> **Analogy:** Git is like a detailed logbook for your project. Every time you make a meaningful change, you write a short note ("added email reader module") and Git takes a snapshot of every file at that moment. You can flip back to any page in the logbook at any time.

Key terms (in plain language):

| Git Term | What It Means |
|----------|--------------|
| **Repository (repo)** | A project folder that Git is tracking. Just a folder with a hidden `.git` directory inside. |
| **Commit** | A saved snapshot — one entry in your logbook. Has a short message describing what changed. |
| **Branch** | A parallel copy of your project. Like drafting two versions of a report — you can pick the better one later. |
| **Push** | Upload your local commits to the internet (GitHub) so others can see them. |
| **Pull** | Download the latest changes from GitHub to your computer. |
| **Clone** | Copy an entire repository from GitHub to your computer for the first time. |
| **Fork** | Make your own copy of someone else's repository on GitHub — like photocopying a textbook so you can write in the margins. |

You do **not** need to memorize these. You will use them so often this semester that they will become second nature.

---

### 4.3 GitHub — Your Project's "Cloud Backup + Sharing Platform"

**Git** lives on your computer. **GitHub** is a website (github.com) that stores your Git repositories online.

> **Analogy:** If Git is the logbook on your desk, GitHub is the shared Google Drive folder where everyone can see the logbook. It is also where you submit homework — instead of emailing files, you "push" your commits to GitHub, and the instructor can see exactly what you changed and when.

GitHub also gives you a **profile** (like a portfolio) where future employers can see your projects.

---

### 4.4 Cursor — Your AI-Powered Text Editor

A **text editor** (or IDE — Integrated Development Environment) is where you write and edit files. You can think of it as "Word, but for code and configuration files."

**Cursor** is a text editor with a built-in AI assistant. You can highlight any text and ask the AI to rewrite it, explain it, or generate something new. You can also chat with it in a side panel.

> **Analogy:** Cursor is like working with a very fast, very knowledgeable colleague sitting next to you. You describe what you want ("write an email template for RFI responses"), and they draft it for you. You review, adjust, and approve.

Download: [cursor.com](https://cursor.com)

---

### 4.5 AI Coding Agents — Your Terminal Assistants

In addition to Cursor (the visual editor), you will use **AI coding agents that run in your terminal**. These are tools you talk to by typing, and they can read your files, write code, run commands, and build things for you — all from the command line.

> **Analogy:** If Cursor is the colleague sitting next to you at a desk, a terminal AI agent is a colleague you can call on the phone. You tell them what you need ("build me an email reader that connects to Gmail"), and they do it — creating files, writing code, testing things — while you watch and give feedback.

We will primarily use **Claude Code** in class. You are free to use **Codex CLI** (OpenAI) or **Gemini CLI** (Google) instead or in addition — they all serve the same purpose. Pick whichever feels most natural to you.

| Tool | Made By | Install Command | Launch Command |
|------|---------|----------------|----------------|
| **Claude Code** | Anthropic | `npm install -g @anthropic-ai/claude-code` | `claude` |
| **Codex CLI** | OpenAI | `npm install -g @openai/codex` | `codex` |
| **Gemini CLI** | Google | `npm install -g @google/gemini-cli` | `gemini` |

**Claude Code** — Made by Anthropic (the company behind Claude). Runs in your terminal, can read/edit your project files, run commands, and build entire features from natural-language descriptions. Sign in with your Anthropic API key or Claude account. *This is the default tool for in-class demos.*

**Codex CLI** — Made by OpenAI (the company behind ChatGPT). Same idea — a coding agent in your terminal. Sign in with your ChatGPT account (Plus/Pro) or an OpenAI API key. Supports multiple models including GPT-5 series. Good alternative if you already have a ChatGPT subscription.

**Gemini CLI** — Made by Google. Open-source terminal agent powered by Gemini models. Sign in with your Google account (free tier available). Lightweight and well-integrated with Google Cloud services.

> **Key Insight:** All three tools do the same fundamental thing: you describe what you want in plain English, the AI writes code, you review and approve. The skill you are learning — *directing an AI coding agent* — transfers across all of them. Do not stress about picking the "right" one.

**A note on `npm`:** All three agents install via `npm` (Node Package Manager). This requires **Node.js** on your computer — we will install it together in the workshop below.

---

### 4.6 Summary: The Full Toolchain

| Tool | What It Does | Analogy |
|------|-------------|---------|
| **Terminal** | Text-based interface to your computer | Calling the kitchen directly |
| **Git** | Tracks every change in your project | A logbook with snapshots |
| **GitHub** | Stores your project online, enables sharing | Google Drive for your logbook |
| **Cursor** | AI-powered editor for writing/editing files | A colleague at your desk |
| **Claude Code / Codex / Gemini** | AI agent in your terminal that builds things for you | A colleague on the phone |

---

### Step-by-Step Tool Setup

Follow these steps **in order**. Raise your hand if you get stuck at any step.

**Step 1 — Install Git**
```
# macOS (Homebrew — if you don't have brew, see Step 1b)
brew install git

# Windows
# Download from https://git-scm.com/downloads
```
Verify: open your terminal and type `git --version`. You should see `git version 2.x.x` or higher.

**Step 1b — Install Homebrew (macOS only, if you don't have it)**
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Step 2 — Install Node.js**

Node.js is required to install the AI terminal agents. Download from [nodejs.org](https://nodejs.org) (use the LTS version).

Verify: `node --version` should return `v20.x.x` or higher.

**Step 3 — Create a GitHub Account**
- Go to https://github.com and sign up (use your Bogazici email for the student pack).
- Enable two-factor authentication.

**Step 4 — Fork the Course Repository**
- Navigate to the course repo link (provided on Moodle).
- Click **Fork** in the top-right corner.
- Clone your fork to your local machine:
```
git clone https://github.com/<your-username>/cem501-agent.git
cd cem501-agent
```

**Step 5 — Install Cursor**
- Download from [cursor.com](https://cursor.com).
- Open the cloned repo folder in Cursor: `File > Open Folder`.
- Familiarize yourself with the AI chat panel (Cmd+L / Ctrl+L).

**Step 6 — Install an AI Terminal Agent (pick at least one)**
```
# Option A: Claude Code (recommended for class demos)
npm install -g @anthropic-ai/claude-code

# Option B: Codex CLI
npm install -g @openai/codex

# Option C: Gemini CLI
npm install -g @google/gemini-cli
```

Verify your installation:
```
claude --version    # if you installed Claude Code
codex --version     # if you installed Codex CLI
gemini --version    # if you installed Gemini CLI
```

Launch the agent, sign in when prompted, and confirm it works by asking it something simple:
```
claude               # starts Claude Code
# Then type: "What files are in this directory?"
```

**Step 7 — First Commit**
- Open `README.md` in Cursor and add your name and a one-sentence bio.
- Stage, commit, and push:
```
git add README.md
git commit -m "HW0: add student bio"
git push origin main
```

> **Key Insight:** Every homework and milestone in this course is submitted as a Git commit (or set of commits) pushed to your fork. There are no file uploads — learning version control is part of the curriculum.

---

### In-Class Activity: First Commit Workshop

**Duration:** 40 minutes

1. **Solo (15 min)** — Follow the Step-by-Step Tool Setup above. Complete Steps 1-6.
2. **Pair check (10 min)** — Swap screens with a neighbor. Verify each other's commit appears on GitHub.
3. **Group debrief (15 min)** — Common errors, Q&A, troubleshooting.

If you finish early, explore Cursor's AI features: highlight a sentence in README.md and ask Cursor to "rewrite this more professionally."

---

### Homework / Milestone

**HW0 — Fork, Clone & First Commit**

- Fork the course repository and clone it locally.
- Edit `README.md` with your name, program, and one sentence about your CEM interest.
- Commit with the message `HW0: add student bio` and push to your fork.
- **Due:** Before Week 2 session.

Grading: Pass/Fail. The commit must appear in your GitHub fork.

---

### Further Reading

**Communication in CEM:**
- FMI & PlanGrid (2018). [*Construction Disconnected: The Cost of Miscommunication and Rework*](https://www.autodesk.com/blogs/construction/construction-disconnected-fmi-report/)
- McKinsey Global Institute (2017). [*Reinventing Construction: A Route to Higher Productivity*](https://www.mckinsey.com/capabilities/operations/our-insights/reinventing-construction-through-a-productivity-revolution)
- Arcadis (2025). [*Global Construction Disputes Report*](https://media.arcadis.com/-/media/project/arcadiscom/com/expertise/global/contract-solutions/2025/2025-15th-annual-construction-disputes-report-final-19jun25.pdf)
- PMI (2013). [*Pulse of the Profession: The High Cost of Low Performance*](https://www.pmi.org/learning/library/en-2013-pulse-high-cost-low-performance-13512)
- KPMG (2015). [*Climbing the Curve: Global Construction Survey*](https://assets.kpmg.com/content/dam/kpmg/pdf/2015/04/global-construction-survey-2015.pdf)
- Dainty, A., Moore, D. & Murray, M. (2006). *Communication in Construction: Theory and Practice.* Taylor & Francis.

**Tools:**
- [Git Handbook (GitHub Docs)](https://docs.github.com/en/get-started/using-git/about-git)
- [Cursor Documentation](https://docs.cursor.com)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Codex CLI Quickstart (OpenAI)](https://developers.openai.com/codex/quickstart/)
- [Gemini CLI Documentation](https://geminicli.com/docs/)

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
