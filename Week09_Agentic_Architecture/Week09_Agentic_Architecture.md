# CEM501: Communication Skills for CEM
## Week 9: Agentic Architecture & Design (Strand C)
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Explain what makes software "agentic" and identify the sense-decide-act loop in your own email agent
- Name the core components of a communication agent and describe each one's role
- Write a clear ARCHITECTURE.md document that a teammate (or future you) can follow
- Draw a system diagram (even text-based) showing data flow between components
- Apply modular design principles so your agent can be extended in later weeks

---

## Part I: What Makes Software "Agentic"?
**(~25 min lecture)**

### 1.1 From Scripts to Agents

So far in Strand C you have built pieces — a prompt library, an email reader, a classifier. Each piece runs when you tell it to and stops when it finishes. That is a **script**: you press a button, it does one thing, done.

An **agent** is different. An agent operates in a loop. It watches for new information, decides what to do about it, carries out that decision, and then goes back to watching. It can run while you sleep. It can handle situations you did not explicitly program, because the LLM at its core can reason about novel inputs.

Anthropic's December 2024 guide *Building Effective Agents* draws a useful distinction between two kinds of agentic systems:

- **Workflows** — systems where LLMs and tools are orchestrated through predefined code paths. You decide the sequence in advance. The LLM fills in the blanks but does not choose what happens next.
- **Agents** — systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Your email agent this semester sits between these two poles. The overall pipeline (read, classify, draft, send) is a workflow. But within each step — particularly classification and drafting — the LLM exercises judgment. That is the agentic part.

> **Key Insight:** Anthropic's core recommendation is to "find the simplest solution possible, and only increase complexity when needed." Start with a workflow. Add autonomy only where it creates clear value. You do not need a fully autonomous agent to be useful — Klarna's AI assistant, built on a structured workflow pattern, handled 2.3 million customer service conversations in its first month and reduced average resolution time from 11 minutes to under 2 minutes.

*Sources: Anthropic (2024). ["Building Effective Agents."](https://www.anthropic.com/research/building-effective-agents) Klarna (2024). ["Klarna AI assistant handles two-thirds of customer service chats in its first month."](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)*

---

### 1.2 The Sense-Decide-Act Loop

The foundational model for intelligent agents comes from Russell and Norvig's textbook *Artificial Intelligence: A Modern Approach*, which defines an agent as "anything that perceives its environment through sensors and acts upon that environment through actuators." The agent function maps the agent's entire history of percepts to an action.

In practical terms, every agent — from a thermostat to a self-driving car to your email assistant — follows a three-phase loop:

| Phase | What It Does | Your Agent Example |
|-------|-------------|-------------------|
| **Sense** | Perceive new information from the environment | Fetch unread emails via IMAP; extract sender, subject, body |
| **Decide** | Analyze the information and choose a response | LLM classifies intent (RFI, submittal, schedule update); rules select a template |
| **Act** | Execute the chosen response | Draft a reply, send it (or queue for human review), log the interaction |

The loop runs continuously (or on a schedule). Each cycle is one "tick" of the agent.

> **CEM Analogy:** Think of a site superintendent doing a morning walk-through. She **senses** the site conditions — weather, crew readiness, material deliveries, safety hazards. She **decides** — reassign the concrete crew because of rain, expedite the missing rebar delivery, close off an unsafe area. She **acts** — makes phone calls, updates the schedule, posts signage. Then she does it again the next morning. Your email agent is doing the same thing, but for your inbox.

The key insight from Chip Huyen's analysis of agent systems is that non-agentic systems typically perform a single operation, while agentic systems require "multiple steps to accomplish a task" — and accuracy compounds at each step. If each step is 95% accurate, a 10-step pipeline drops to about 60% overall accuracy. This is why keeping your architecture simple matters.

*Sources: Russell, S. & Norvig, P. (2020). Artificial Intelligence: A Modern Approach, 4th ed. Pearson. Chapter 2: Intelligent Agents. Huyen, C. (2025). ["Agents."](https://huyenchip.com/2025/01/07/agents.html)*

---

### 1.3 Why This Matters for CEM

Construction is one of the industries most poised for — and most behind on — AI adoption. The Royal Institution of Chartered Surveyors (RICS) published its *AI in Construction 2025* report based on a global survey of over 2,200 professionals. The findings reveal a stark gap between perception and practice:

- **45% of respondents** reported no AI implementation at all in their organizations.
- **34%** were in early pilot phases.
- Only **1.5%** reported AI use across multiple processes.
- Fully embedded, organization-wide AI use was reported by **less than 1%**.

And yet, **nearly 70% of project managers and quantity surveyors** believe AI will help them deliver greater value. The interest is there. The capability is not.

> **Key Insight:** You are learning to build agentic systems at exactly the right time. The construction industry knows it needs AI but does not yet know how to adopt it. CEM professionals who can design, document, and deploy even simple AI agents will have a significant competitive advantage.

*Source: RICS (2025). ["Artificial Intelligence in Construction Report."](https://www.rics.org/news-insights/artificial-intelligence-in-construction-report)*

---

## Part II: Your Agent's Architecture
**(~20 min lecture)**

### 2.1 The Six Components

Your communication agent has six core components. You do not need to build all six at once — in fact, you should not. But you need to understand what each one does and how they connect.

**1. Reader** — Connects to the inbox (IMAP), pulls new messages, extracts metadata (sender, subject, date, attachments). This is the agent's *sensor*. Without it, the agent is blind.

**2. Classifier** — Sends the email body to an LLM with a system prompt and returns a category (RFI, submittal, schedule update, informal, urgent, etc.). This is the first half of the *decision* phase. It answers: "What kind of message is this?"

**3. Drafter** — Uses the classification label, email text, templates from your prompt library, and project context from Memory to generate a draft reply. This is the second half of the *decision* phase. It answers: "What should we say back?"

**4. Sender** — Pushes the approved draft back through SMTP, or holds it in a review queue for human approval. This is the agent's *actuator*. It turns decisions into actions.

**5. Memory** — Stores past interactions, sender profiles, project context, and user corrections so the agent improves over time. Memory turns a stateless script into a learning system.

**6. Scheduler** — Triggers the sense-decide-act loop on a defined interval (every 5 minutes, every hour, every morning at 6 AM). Without a scheduler, you still have to press the button yourself.

> **Key Insight:** You do not need all six components working perfectly to have a useful agent. Start with Reader + Classifier. Add Drafter next. Sender and Memory come later. The Scheduler is the last piece — it is what makes the agent truly autonomous. Incremental delivery is how real software gets built.

---

### 2.2 Architecture Diagram

Below is a text-based diagram showing how data flows between the six components. You can use this exact format in your ARCHITECTURE.md — no special tools required.

```
                        +-----------+
                        | Scheduler |  (triggers every N minutes)
                        +-----+-----+
                              |
                              v
    +-------+           +----------+         +-----------+
    | IMAP  |---------->|  Reader  |-------->| Classifier|
    | Inbox |  (fetch)  +----------+  (raw   +-----------+
    +-------+                          email)      |
                                          (category + email)
                                                   |
                                                   v
    +----------+        +-----------+        +---------+
    |  Memory  |<------>|  Drafter  |------->| Sender  |
    +----------+ (context+-----------+ (draft)+----+----+
                 + logs)                          |
                                                  v
                                            +----------+
                                            | SMTP     |
                                            | Outbox   |
                                            +----------+
```

**What travels along each arrow:** raw email headers/body from IMAP to Reader; cleaned email object from Reader to Classifier; category label + confidence + original email from Classifier to Drafter; project context and sender history from Memory to Drafter (bidirectional — Drafter also logs interactions back); draft text + recipient from Drafter to Sender; final email from Sender to SMTP; and a "wake up" trigger from Scheduler to Reader.

---

### 2.3 Anthropic's Composable Patterns (Reference)

The *Building Effective Agents* guide identifies five composable workflow patterns. Your email agent primarily uses the first two:

| Pattern | Description | Your Agent Uses It? |
|---------|------------|-------------------|
| **Prompt Chaining** | Sequential steps where each LLM call processes the previous output | Yes — Reader feeds Classifier feeds Drafter |
| **Routing** | Classify input and direct to specialized handlers | Yes — different email types get different templates |
| **Parallelization** | Run the same task multiple times or split into parallel subtasks | Not yet — but could classify and summarize simultaneously |
| **Orchestrator-Workers** | Central LLM decomposes work and delegates to specialized sub-agents | Future — multi-channel coordination |
| **Evaluator-Optimizer** | One LLM generates, another evaluates, loop until quality threshold met | Future — draft quality checking |

The takeaway: you are already using established agent design patterns. You just did not have names for them until now.

*Source: Anthropic (2024). ["Building Effective Agents."](https://www.anthropic.com/research/building-effective-agents)*

---

## Part III: How to Write an Architecture Document
**(~20 min lecture)**

### 3.1 Why Documentation Matters — Even When AI Writes the Code

You might think: "If Claude Code writes my code and I can just ask it to explain things, why do I need a separate architecture document?"

Three reasons:

**1. Maintenance is most of the cost.** Research consistently shows that **60% or more of a software system's total lifecycle cost** goes to maintenance, not initial development. Within that maintenance budget, roughly 60% is spent on enhancements driven by changing requirements — not bug fixes. Documentation is what makes maintenance possible without the original developer (or the original AI conversation) present.

**2. AI tools work better with documentation.** When you give Claude Code or Cursor an ARCHITECTURE.md file, the AI can understand your system's intent, not just its syntax. A well-documented project produces better AI-generated code because the AI has more context to work with.

**3. Communication is the point.** This is a communication course. An architecture document is a form of technical writing. It communicates the *why* behind your design decisions to a future reader — who might be your teammate, your instructor, or yourself six months from now.

> **Key Insight:** The most common complaint in software teams is not "we don't have enough code." It is "we don't know why the code is the way it is." Architecture documentation answers that question. Google, AWS, and Microsoft all maintain formal Architecture Decision Record (ADR) processes for exactly this reason.

*Sources: O'Reilly (2009). ["The 60/60 Rule."](https://www.oreilly.com/library/view/97-things-every/9780596805425/ch34.html) AWS (2024). ["Master architecture decision records (ADRs)."](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)*

---

### 3.2 What Goes in ARCHITECTURE.md

Your architecture document should answer five questions:

1. **What does this system do?** (Overview — one paragraph)
2. **What are its parts?** (Components — one section per component)
3. **How do the parts connect?** (Data flow diagram)
4. **Why did you make these choices?** (Design decisions with justifications)
5. **What could be added later?** (Future extensions)

This maps closely to the simplified version of the **C4 model** created by Simon Brown, which structures software architecture documentation into four hierarchical levels:

| C4 Level | What It Shows | Your Equivalent |
|----------|--------------|----------------|
| **Context** | The system as a whole and its external users/systems | Overview section — who uses your agent, what it connects to |
| **Container** | The major deployable units (apps, databases, APIs) | Your six components (Reader, Classifier, etc.) |
| **Component** | The internal building blocks of each container | Individual functions within each component |
| **Code** | Classes, functions, implementation details | Your actual Python files |

For this course, you only need the first two levels: Context and Container. That is enough to communicate your architecture clearly.

*Source: Brown, S. (2024). [The C4 Model for Visualising Software Architecture.](https://c4model.com/)*

---

### 3.3 Architecture Decision Records (ADRs) — Simplified

An Architecture Decision Record captures a single design choice and its rationale. Major tech companies use formal ADR processes, but for your project, a simplified version in your ARCHITECTURE.md is sufficient.

Each design decision entry should have three parts:

```
**Decision:** We chose polling (check every 5 minutes) instead of push notifications.

**Context:** Push requires a webhook server, which adds deployment complexity.
Our use case (overnight RFI triage) does not need real-time response.

**Consequences:** Slight delay (up to 5 min) before new emails are processed.
Simpler deployment — no public server needed. Easy to change interval later.
```

> **Key Insight:** The value of an ADR is not the decision itself — it is the *context* and *consequences*. Six months from now, you will not remember why you chose polling over push. The ADR remembers for you. As the ADR community puts it: "Keep records pithy, assertive, on-topic, and factual."

*Sources: Nygard, M. (2011). ["Documenting Architecture Decisions."](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) Google Cloud (2024). ["Architecture decision records overview."](https://docs.google.com/architecture/architecture-decision-records)*

---

## Part IV: System Diagrams — Thinking Visually
**(~15 min lecture)**

### 4.1 Why Diagrams Matter

You have already seen the text-based diagram in Section 2.2. Let's talk about why even a simple diagram is worth creating.

Research on software documentation consistently finds that visual representations help developers understand systems faster than prose alone. The C4 model exists precisely because Simon Brown observed that "many development teams don't have any software architecture diagrams at all" — and the teams that do often create diagrams that are confusing, inconsistent, or at the wrong level of abstraction.

A text-based ASCII diagram in a Markdown file has one enormous advantage: it lives in version control alongside your code. It does not require Visio, Figma, or any special tool. It can be updated in the same commit that changes the code.

---

### 4.2 Diagram Checklist

When you draw your architecture diagram, verify that it passes these checks:

- [ ] Every component is labeled with a clear name
- [ ] Arrows show the direction of data flow (not just "connected to")
- [ ] Each arrow is labeled with what travels along it (e.g., "raw email text", "category label")
- [ ] External systems (IMAP, SMTP, LLM API) are visually distinguished from your components
- [ ] The diagram fits on one page — if it does not, your architecture may be too tightly coupled
- [ ] A classmate unfamiliar with your code can understand the diagram in under two minutes

---

### 4.3 Diagram Tips

- Use `+---+` boxes for components and `|` or `v` for directional arrows
- Place external systems (IMAP, SMTP, LLM API) at the edges of the diagram
- Use bidirectional arrows (`<--->`) for Memory connections
- Label every arrow with the data that travels along it
- Refer to the diagram in Section 2.2 as your starting template

---

## Part V: Designing for Extensibility
**(~10 min lecture)**

### 5.1 Why Modular Design Matters

Your agent is not done after this week. In the coming weeks, you will:

- **Week 11:** Add a new messaging channel (Telegram or Slack) alongside email
- **Week 12:** Add persistent memory so the agent learns from corrections

If your code is a single monolithic script where the email reader, classifier, and drafter are all tangled together, adding a new channel means rewriting everything. If your code is modular — each component in its own file with clear inputs and outputs — adding a new channel means writing one new component and plugging it in.

---

### 5.2 Two Principles for Extensible Design

**1. Separation of Concerns** — Each component does one job. The Classifier does not also send emails. The Reader does not also classify. If you find a component doing two things, split it.

**2. Channel Abstraction** — Define a common interface for message sources and sinks. Today you read from IMAP and send via SMTP. Next week you might read from Telegram and send via Telegram API. If your Reader and Sender are defined by their interface (input: message source credentials, output: message objects) rather than by their implementation (IMAP-specific code), adding a new channel is straightforward.

> **CEM Analogy:** In construction, project requirements change constantly. A building designed with rigid, load-bearing walls everywhere is expensive to renovate. A building designed with a structural frame and non-load-bearing partitions can be reconfigured without demolition. Software that is easy to modify mirrors the reality of construction — scope changes are inevitable, so design for them.

---

### 5.3 Practical Example: Adding Telegram

With a modular design, adding Telegram looks like this:

```
Current:
  [IMAP Reader] --> [Classifier] --> [Drafter] --> [SMTP Sender]

After Week 11:
  [IMAP Reader]     ---+
                       +--> [Classifier] --> [Drafter] --+--> [SMTP Sender]
  [Telegram Reader] ---+                                 +--> [Telegram Sender]
```

The Classifier and Drafter do not change at all. Only the Reader and Sender gain a sibling. That is the power of modular design.

---

## Tool Demo: Generating ARCHITECTURE.md with Cursor / Claude Code
**(15 min live walkthrough)**

### Step-by-Step

1. **Open your project in Cursor** (or launch `claude` in your terminal).
2. **Prompt:** *"Look at my project structure and generate an ARCHITECTURE.md describing each component, its responsibility, inputs, outputs, and how data flows between them. Include a text-based diagram and design decisions."*
3. **Review critically.** The AI may misname components, describe intended rather than actual behavior, miss error paths, or use generic language. Correct all of these.
4. **Commit:** `git add ARCHITECTURE.md && git commit -m "Add architecture doc (M5)"`

> **Key Insight:** The AI gives you a starting draft in minutes. Without AI, writing an architecture document from scratch takes hours. But the AI is not the architect — **you** are. The AI drafts; you verify, correct, and improve. This mirrors how AI will work in CEM practice: AI generates the first draft of an RFI response, but the engineer reviews and signs it.

---

## ARCHITECTURE.md Template

Below is the structure your M5 submission should follow. Adapt it to your project. For each component, use this format:

```markdown
# Architecture — [Your Agent Name]

## Overview
One-paragraph summary: what the agent does, who it serves, what it connects to.

## Components
For each component (Reader, Classifier, Drafter, Sender, Memory, Scheduler):
- **Responsibility:** One sentence
- **Input:** What data it receives
- **Output:** What data it produces
- **File:** Which source file implements it

## Data Flow Diagram
(Paste your text-based diagram here — see Section 2.2 for format)

## Design Decisions (ADR-style, at least two)
For each decision: **Decision**, **Context**, **Consequences**
Example decisions: polling vs. push, model selection, human-in-the-loop

## Error Handling
What happens when the LLM API times out? When classification confidence
is low? When the IMAP connection fails?

## Future Extensions
What you plan to add (channels, memory, attachment summarization, etc.)
```

---

## In-Class Activity: Whiteboard Architecture Session
**(35 min)**

### Instructions

**1. Solo sketch (10 min)** — On paper or a whiteboard, draw your agent's architecture from memory. Do not look at the template above. Label every component, every arrow, and what data flows along each arrow.

**2. Pair review (10 min)** — Swap with a neighbor. Your job is to find confusion. For every part of their diagram you do not immediately understand, mark it with a "?" sticky note. Be specific: "What format is this data in?" or "What happens if this step fails?"

**3. Revise (5 min)** — Address the "?" notes on your own diagram. Add labels, clarify names, note error paths.

**4. Group share (10 min)** — Two volunteers present their diagram to the class. We critique together using these focus questions:

**Focus questions for group critique:**
- Can someone unfamiliar with your code understand this diagram in under two minutes?
- Where is the single point of failure? What happens if the LLM API goes down?
- Is there any component doing more than one job? Should it be split?
- Could a new team member use this diagram to start contributing code without asking you questions?

---

## Milestone M5 — Due Before Week 10

**Deliverable:** `project/ARCHITECTURE.md` committed to your repository.

### Requirements

| Criterion | Weight | What We Look For |
|-----------|--------|-----------------|
| **Completeness** | 40% | All template sections filled in (Overview, Components, Diagram, Decisions, Future Extensions) |
| **Clarity** | 30% | Professional English. A reader unfamiliar with your code can understand the document. No jargon without definition. |
| **Accuracy** | 30% | The document matches your actual code. Component names match file names. The diagram reflects real data flow, not aspirational design. |

**Specific requirements:**
- Follows the template structure above (all sections present)
- Includes a data flow diagram (text-based is fine; image is also acceptable)
- Lists at least **two** design decisions with context and consequences (ADR-style)
- Is written in clear, professional English — remember, this is a communication course
- Is committed to your repository with a meaningful commit message

> **Key Insight:** Your ARCHITECTURE.md will be graded partly on *accuracy to your actual code*. Do not describe a six-component system if you have only built three components. Describe what exists, note what is planned, and be honest about the current state. In construction, as-built drawings are more valuable than design drawings because they reflect reality.

---

## Further Reading

**Agentic AI Architecture:**
- Anthropic (2024). ["Building Effective Agents."](https://www.anthropic.com/research/building-effective-agents) — The most practical guide to agent design patterns available. Read at least the sections on prompt chaining and routing.
- Huyen, C. (2025). ["Agents."](https://huyenchip.com/2025/01/07/agents.html) — Excellent overview of what makes systems agentic, with accuracy analysis.
- OpenAI (2025). [*A Practical Guide to Building Agents.*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — OpenAI's perspective on agent architecture, covering the Agents SDK and multi-agent patterns.
- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*, 4th ed. — Chapter 2 (Intelligent Agents) for the foundational sense-decide-act framework.

**Software Architecture Documentation:**
- Brown, S. (2024). [The C4 Model for Visualising Software Architecture.](https://c4model.com/) — The standard for simple, developer-friendly architecture diagrams.
- Nygard, M. (2011). ["Documenting Architecture Decisions."](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — The original blog post that launched the ADR movement.
- AWS (2024). ["Master Architecture Decision Records."](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/) — Best practices from AWS on writing effective ADRs.

**Construction & AI:**
- RICS (2025). ["Artificial Intelligence in Construction Report."](https://www.rics.org/news-insights/artificial-intelligence-in-construction-report) — Global survey of 2,200+ professionals on AI adoption in construction.

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
