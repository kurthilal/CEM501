# CEM501: Communication Skills for Construction Engineering and Management

**Spring 2026 | Bogazici University**

| | |
|---|---|
| **Course Code** | CEM501 |
| **Credits** | 3 |
| **Semester** | Spring 2026 |
| **Meeting Time** | Saturdays, 14:00 – 16:30 |
| **Meeting Format** | Online (Zoom — link distributed via email and calendar invite) |
| **Instructor** | Dr. Eyuphan Koc |
| **Email** | eyuphan.koc@bogazici.edu.tr |
| **Office** | Department of Civil Engineering, Bogazici University |
| **Office Hours** | By appointment (email to schedule) |

---

## Course Description

This course develops the professional communication skills that graduate students in Construction Engineering and Management need to succeed in industry. Students learn to write effective project correspondence (emails, RFIs, submittals, reports), deliver technical presentations, lead and participate in meetings, negotiate with stakeholders, and communicate across cultures. Concurrently, students build a personal AI communication agent as a semester-long project, using AI coding assistants (Cursor, Claude Code) as their primary development tools. No prior programming experience is required — the course teaches students to direct AI-generated code, not to program from scratch.

---

## Learning Outcomes

Upon successful completion of this course, students will be able to:

1. **Write** clear, professional project correspondence — emails, RFIs, submittals, and reports — that meets industry standards and contractual expectations.
2. **Deliver** structured technical presentations and participate effectively in project meetings, including OAC meetings and negotiation sessions.
3. **Apply** prompt engineering techniques to direct large language models for communication tasks such as drafting, summarization, and triage.
4. **Build** a functional AI communication agent by directing AI coding tools through iterative prompting, code review, and testing.
5. **Evaluate** AI-generated content critically, identifying hallucinations, tone mismatches, and professional risks before sending or submitting.
6. **Adapt** communication style for different audiences, cultures, and channels, drawing on frameworks such as Hofstede's cultural dimensions and high-context vs. low-context communication.
7. **Document** software architecture decisions and reflect on the development process in writing.
8. **Give and receive** structured peer feedback on both written and verbal communication.

---

## Three Course Strands

The course is organized into three interwoven strands:

**Strand A — Verbal Communication** (Weeks 4, 7, 10, 13)
Presentations, meeting participation, negotiation, and cross-cultural communication. These weeks include graded in-class verbal activities and peer feedback.

**Strand B — Written Communication & AI Foundations** (Weeks 1, 2, 3, 5, 6, 8)
Professional writing genres (email, RFIs, submittals, reports) paired with the technical foundations of working with AI tools — LLM concepts, prompt engineering, and AI-assisted coding workflows.

**Strand C — Agentic AI Pipeline** (Weeks 9, 11, 12, 14)
System architecture, multi-channel integration, agent memory, and the final demo. Students bring together everything from Strands A and B into a working personal communication agent.

---

## Weekly Schedule

| Wk | Topic | Strand | Key Activity | Milestone / HW | Readings |
|----|-------|--------|-------------|-----------------|----------|
| 1 | Communication Landscape & Tool Setup | B | Tool setup workshop | HW0: Fork repo, first commit | Week 01 notes |
| 2 | Professional Email & Intro to LLMs | B | First LLM API call demo | M0: Successful LLM API call | Week 02 notes |
| 3 | RFIs, Submittals & Prompt Engineering | B | Prompt template workshop | M1: Prompt template library | Week 03 notes; Anthropic prompt guide |
| 4 | Presentation Skills for Engineers | A | 3-min presentation + peer feedback | Self-assessment HW | Week 04 notes |
| 5 | Reading & Triaging Email with AI Tools | B | Email triage drill + build session | M2: Email reader module | Week 05 notes |
| 6 | Reports & LLM Summarization | B | Report summarization exercise | M3: Daily digest generator | Week 06 notes |
| 7 | Meeting Communication | A | Mock OAC meeting | Meeting minutes HW | Week 07 notes |
| 8 | The Email Agent: Drafting & Sending | B | Agent build-along | M4: Email agent v1 | Week 08 notes |
| — | **Midterm** | A+B | 5-min presentation + take-home | Part A (10%) + Part B (10%) | — |
| 9 | Agentic Architecture & Design | C | Architecture sketch + peer review | M5: ARCHITECTURE.md | Week 09 notes; Anthropic "Building Effective Agents" |
| 10 | Negotiation & Conflict Resolution | A | Negotiation role-play | Negotiation memo HW | Week 10 notes; Fisher & Ury, *Getting to Yes* |
| 11 | Multi-Channel Integration | C | Telegram bot workshop | M6: Multi-channel agent | Week 11 notes |
| 12 | Agent Memory & Scheduling | C | Reliability workshop | M7: Persistent agent | Week 12 notes |
| 13 | Cross-Cultural Communication | A | International project simulation | M8: Final integration | Week 13 notes; Hofstede Insights |
| 14 | **Final Demos** | C | 7-min demo + 3-min Q&A | M9: Final submission | — |

---

## Semester Project

The semester project is the construction of a **personal AI communication agent** — a system that can read, triage, draft, and send professional emails, with extensions to other channels (e.g., Telegram). The agent is built incrementally through milestones M0–M9, each tied to a course week.

### Milestone Progression

| Milestone | Week | Deliverable |
|-----------|------|-------------|
| M0 | 2 | Screenshot or log of a successful LLM API call |
| M1 | 3 | `project/templates/` with at least 3 prompt templates |
| M2 | 5 | `project/reader.py` — reads and triages email |
| M3 | 6 | `project/digest.py` — generates a daily digest |
| M4 | 8 | `project/agent.py` — email agent v1 (read + draft + send) |
| M5 | 9 | `project/ARCHITECTURE.md` — system design document |
| M6 | 11 | `project/channels/` — at least one additional channel |
| M7 | 12 | `project/memory/` + `project/logs/` — persistence and logging |
| M8 | 13 | Full integration, all tests passing |
| M9 | 14 | Final demo + `project/REFLECTION.md` (500–800 words) |

### Project Grading Breakdown

| Component | Weight |
|-----------|--------|
| Architecture document (M5) | 5% |
| Code quality & milestone progression (M0–M8) | 10% |
| Final demo (M9, 7-min live demo + 3-min Q&A) | 10% |
| Reflection document (M9) | 5% |
| **Total** | **30%** |

---

## Grading Policy

### Grade Components

| Component | Weight | Notes |
|-----------|--------|-------|
| Weekly Homework | 25% | Lowest homework grade is dropped |
| Verbal Communication | 15% | 4 assessed sessions (Weeks 4, 7, 10, 13) |
| Midterm | 20% | Part A: presentation (10%) + Part B: take-home (10%) |
| Semester Project | 30% | Architecture 5% + Code 10% + Demo 10% + Reflection 5% |
| Participation & Peer Feedback | 10% | Attendance, in-class engagement, peer feedback quality |
| **Total** | **100%** | |

### Letter Grade Scale

Bogazici University uses the following grade point system. Final letter grades are assigned based on overall course performance and may be adjusted for class distribution:

| Grade | Points | Grade | Points |
|-------|--------|-------|--------|
| AA | 4.0 | DC | 1.5 |
| BA | 3.5 | DD | 1.0 |
| BB | 3.0 | FD | 0.5 |
| CB | 2.5 | FF | 0.0 |
| CC | 2.0 | | |

---

## Midterm & Final

### Midterm (20%)

The midterm has two parts:

- **Part A — Presentation (10%):** A 5-minute individual presentation on a CEM communication challenge. Graded using the same rubric as Week 4.
- **Part B — Take-Home (10%):** A coding/writing assignment — build a specified feature for your agent. Distributed after Part A; due 48 hours later.

### Final (Week 14)

There is **no written final exam**. The final assessment is the **live demo** during Week 14:

- 7 minutes: live demonstration of your communication agent
- 3 minutes: Q&A from instructor and peers
- Graded via the final demo rubric (see `Week14_Final_Demos/rubrics/`)

---

## Technology Requirements

This course assumes **near-zero programming background**. You will use AI coding assistants to write code, not write it yourself from scratch. You need:

- **Laptop** with internet access (Mac, Windows, or Linux)
- **GitHub account** — all submissions via GitHub
- **Cursor** — AI-native IDE (primary development environment)
- **At least one CLI agent:** Claude Code, Codex CLI, or Gemini CLI
- **Python 3.11+** — runtime for the semester project
- **API keys** for at least one LLM provider (Anthropic, OpenAI, or Google). Free tiers are sufficient for coursework; no paid subscriptions required.

Setup instructions are provided in Week 1. The runtime stack (managed by your AI tools) includes: `anthropic`/`openai` SDKs, `imap_tools`, `smtplib`, `python-telegram-bot`, SQLite, and `schedule`.

---

## AI Tool Usage Policy

This course **encourages** the use of AI tools. Learning to direct AI effectively is a core course objective.

### Required for Every Submission

1. State which tools you used (e.g., "Built with Cursor + Claude Code").
2. Briefly describe your prompting approach (1–2 sentences).
3. Note any significant manual edits you made after AI generation.

### Allowed Use

- Using AI coding assistants (Cursor, Claude Code, Codex CLI, Gemini CLI) to generate, debug, and refactor code
- Using LLMs to draft, revise, and polish written work — provided you review and take responsibility for the output
- Using AI tools to brainstorm ideas, outline documents, and summarize readings

### Prohibited Use

- Submitting AI-generated output without review or attribution
- Copying another student's prompts or code without citation
- Using AI to complete graded verbal assessments (presentations, role-plays)

The goal is not to catch cheating — it is to develop your skill as an AI *director*. The better you document your process, the more you learn.

---

## Attendance & Participation

Participation accounts for **10%** of your final grade and includes:

- **Attendance** at weekly sessions
- **In-class engagement** during activities, workshops, and discussions
- **Peer feedback quality** — providing thoughtful, constructive feedback to classmates

**Verbal Communication weeks (4, 7, 10, 13) require attendance** for graded in-class activities (presentations, mock meetings, role-plays, simulations). Missing a verbal assessment without prior approval or medical documentation results in a zero for that session.

Peer feedback is **mandatory** during all verbal communication weeks. Rubrics and feedback forms are distributed in class.

---

## Late Submission Policy

- **10% deduction per day**, up to a maximum of 3 days late.
- After 3 days: **zero credit**.
- **Medical exceptions** require official documentation submitted within one week of the deadline.
- Deadline for all weekly submissions: **Sunday, 23:59** unless stated otherwise.

---

## Academic Integrity

All students are expected to adhere to **Bogazici University's academic integrity policies**. In this course, academic integrity means:

- **Your work is your own.** You may use AI tools freely (see AI Tool Usage Policy above), but you must review, understand, and take responsibility for everything you submit.
- **Cite your sources.** This includes AI tools, classmates' ideas, online references, and any external code or text.
- **Do not copy.** Submitting another student's code, prompts, or written work — with or without minor modifications — without attribution is plagiarism.
- **Do not fabricate.** Misrepresenting AI-generated content as entirely your own, or fabricating citations, data, or results, is a violation.

Violations will be handled according to Bogazici University disciplinary procedures and may result in a failing grade for the assignment or the course.

---

## Accessibility & Accommodations

Students with documented disabilities or special needs are encouraged to contact the instructor during the first two weeks of the semester to discuss appropriate accommodations. Bogazici University is committed to providing equal access to educational opportunities for all students. Accommodations will be arranged in coordination with the relevant university offices.

---

## Communication

- **Email:** eyuphan.koc@bogazici.edu.tr — for personal matters, grade inquiries, and accommodation requests. Expect a response within 48 hours on weekdays.
- **Office Hours:** By appointment — email to schedule a Zoom or in-person meeting.
- **GitHub Issues:** For technical questions about the semester project, open an issue in your fork. This helps build a searchable knowledge base for the class.
- **Course Announcements:** Distributed via email and posted to the course repository.

---

*This syllabus is the official policy document for CEM501, Spring 2026. The instructor reserves the right to make adjustments to the schedule or policies as needed, with advance notice to students.*

---

**Dr. Eyuphan Koc**
Department of Civil Engineering, Bogazici University
eyuphan.koc@bogazici.edu.tr
