# CEM501: Communication Skills for Construction Engineering and Management

**Spring 2026 | Bogazici University | Dr. Eyuphan Koc**

---

## Course Overview

Professional communication is the single skill that determines whether technical expertise actually gets applied. This course teaches graduate CEM students to communicate effectively — in writing, in meetings, in presentations, and across cultures — while building a personal AI communication agent as the semester project.

In 2026, AI-augmented communication is the norm. You will learn to **direct AI coding tools** (Cursor, Claude Code, Gemini CLI) to build real software, without needing prior programming experience. The goal: become an effective *director* of AI-generated code, not a programmer.

## Three Strands

| Strand | Focus | Weeks |
|--------|-------|-------|
| **A — Verbal Communication** | Presentations, meetings, negotiation, cross-cultural | 4, 7, 10, 13 |
| **B — Written Communication & AI Foundations** | Professional writing + LLM concepts + AI coding tools | 1, 2, 3, 5, 6, 8 |
| **C — Agentic AI Pipeline** | Build your personal communication agent | 9, 11, 12, 14 |

## Weekly Schedule

| Wk | Topic | Milestone |
|----|-------|-----------|
| 1 | Communication Landscape & Tool Setup | HW0: Fork repo, first commit |
| 2 | Professional Email & Intro to LLMs | M0: Can call LLM from CLI |
| 3 | RFIs, Submittals & Prompt Engineering | M1: Prompt template library |
| 4 | Presentation Skills for Engineers | Self-assessment HW |
| 5 | Reading & Triaging Email with AI Tools | M2: Email reader module |
| 6 | Reports & LLM Summarization | M3: Daily digest generator |
| 7 | Meeting Communication | Meeting minutes HW |
| 8 | The Email Agent: Drafting & Sending | M4: Email agent v1 |
| — | **Midterm** | Presentation (10%) + Take-home (10%) |
| 9 | Agentic Architecture & Design | M5: ARCHITECTURE.md |
| 10 | Negotiation & Conflict Resolution | Negotiation memo HW |
| 11 | Multi-Channel Integration | M6: Multi-channel agent |
| 12 | Agent Memory & Scheduling | M7: Persistent agent |
| 13 | Cross-Cultural Communication | M8: Final integration |
| 14 | Final Demos | M9: Final submission |

## Grading

| Component | Weight |
|-----------|--------|
| Weekly Homework (drop lowest) | 25% |
| Verbal Communication (4 assessed sessions) | 15% |
| Midterm (verbal 10% + written/code 10%) | 20% |
| Semester Project (arch 5% + code 10% + demo 10% + reflection 5%) | 30% |
| Participation & Peer Feedback | 10% |

## Tech Stack

You will use **AI coding assistants** as your primary development tool:

- **Cursor** — AI-native IDE (primary environment)
- **Claude Code** — CLI agent for terminal-based development
- **Gemini CLI / Codex CLI** — alternative CLI agents

The runtime stack (managed by AI tools, understood conceptually):
- Python 3.11+, `anthropic`/`openai` for LLM APIs
- `imap_tools` for email reading, `smtplib` for sending
- `python-telegram-bot` for messaging integration
- SQLite for persistence, `schedule` for automation

## Getting Started

```bash
# 1. Fork this repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/CEM501.git
cd CEM501

# 3. Create a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up your environment
cp project/.env.example project/.env
# Edit project/.env with your API keys
```

## Repository Structure

```
CEM501_Spring2026/
├── Week01–14/          # Weekly lecture notes
├── project/            # Your semester project lives here
│   ├── templates/      # M1: Prompt templates
│   ├── channels/       # M6: Messaging integrations
│   ├── memory/         # M7: Persistent storage
│   └── logs/           # M7: Agent logs
├── email_service/      # Reference email utilities
└── resources/          # Reading list & references
```

See [SUBMISSION_GUIDELINES.md](SUBMISSION_GUIDELINES.md) for homework and project submission details.

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
Department of Civil Engineering, Bogazici University
