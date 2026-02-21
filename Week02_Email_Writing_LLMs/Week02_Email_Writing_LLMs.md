# CEM501: Communication Skills for CEM
## Week 2: Professional Email & Intro to LLMs
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Apply a clear structure to every professional email: subject, greeting, body, CTA, sign-off
- Identify and fix the most common email mistakes in CEM correspondence
- Explain, at a conceptual level, what a large language model (LLM) is and how it generates text
- Use Claude Code (or Codex CLI / Gemini CLI) to make your first LLM API call from the command line

> **Session Timeline (150 min)**
>
> | Block | Duration | Topic |
> |-------|----------|-------|
> | Part I | 20 min | Email — The Legal Backbone of Construction |
> | Part II | 25 min | The Anatomy of a Professional CEM Email |
> | *Break* | *10 min* | |
> | Part III | 25 min | What Are Large Language Models? |
> | Part IV | 20 min | What Is an API? Your First LLM Call |
> | Part V | 45 min | In-Class Activity — Email Clinic |
> | Wrap-up | 5 min | Homework, preview of Week 3 |

---

## Part I: Email — The Legal Backbone of Construction
**(~20 min lecture)**

Last week we saw the big picture: $31.3 billion in annual rework from miscommunication, $60.1 million average construction dispute values, 56% of failed projects citing communication as a root cause. This week we zoom in on the single most common form of written communication in CEM — email — and then introduce the tool that will help you write better ones.

---

### 1.1 The Email Flood: How Much Are We Actually Writing?

Email is not dying. Despite Slack, Microsoft Teams, Procore, and a dozen collaboration platforms, email remains the dominant channel for professional communication. The numbers are staggering:

| Statistic | Value | Source |
|-----------|-------|--------|
| Global emails sent/received per day | 376 billion | Radicati Group (2024) |
| Global email users | ~4.6 billion | Radicati Group (2024) |
| Emails received by average office worker daily | 121 | Radicati Group (2024) |
| Percentage of workweek spent on email (knowledge workers) | 28% | McKinsey Global Institute (2012) |
| Professionals who check email primarily on mobile | 64% | cloudHQ (2025) |
| Professionals who check inbox first thing in the morning | 58% | cloudHQ (2025) |

That 28% figure from McKinsey deserves a moment: it means the average knowledge worker spends more than **one full workday each week** just reading and writing email — before opening a single spreadsheet or attending a single meeting.

> **Key Insight:** Over a 45-year career, 28% of your workweek on email adds up to approximately 3,000 working days — over **8 years of your professional life** spent in your inbox. Learning to write email efficiently is not a soft skill. It is a time-management strategy.

*Sources: [Radicati Group (2024). "Email Statistics Report, 2024–2028."](https://www.radicati.com/?p=18519) McKinsey Global Institute (2012). ["The Social Economy."](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy) [cloudHQ (2025). "Workplace Email Statistics 2025."](https://blog.cloudhq.net/workplace-email-statistics/)*

---

### 1.2 Email in Construction: Higher Volume, Higher Stakes

Construction project managers are not average knowledge workers. Their email loads have unique characteristics that make writing quality even more critical:

- **Volume:** Construction project managers receive an average of **72 emails per day** (with a median of 50) and spend roughly **3 hours per day** managing email — that is 37% of an 8-hour workday on email alone.
- **Legal weight:** Emails about RFIs, change orders, schedule impacts, and payment disputes can become **evidence in claims and litigation**. Courts regularly evaluate whether written notice was "timely" and "proper" — and a vague email does not count.
- **Searchability:** Construction firms must retain project correspondence for years, sometimes decades, due to contractual and regulatory obligations. A poorly organized email thread can make it impossible to find critical information during a dispute.
- **Multi-party complexity:** A single project involves owners, architects, engineers, general contractors, subcontractors, suppliers, and inspectors — each with different priorities, vocabularies, and expectations.

> **Key Insight:** When you send an email on a construction project, you are not just communicating — you are creating a legal record. Every email you write could be Exhibit A in a $60 million dispute. Write accordingly.

*Sources: [ProjectManagement.com Discussion: "Managing High Volume of Emails."](https://www.projectmanagement.com/discussion-topic/137135/managing-high-volume-of-emails) [For Construction Pros: "Understanding How to Effectively Communicate via Email."](https://www.forconstructionpros.com/business/article/21025295/understanding-how-to-effectively-communicate-via-email-for-construction-projects)*

---

### 1.3 The Cost of Bad Writing — Beyond Construction

The construction industry does not exist in isolation. Here is what the broader business world found when it tried to quantify the cost of poor writing:

- **$1.2 trillion per year** — the estimated cost of poor communication to U.S. businesses, according to a Grammarly and Harris Poll survey. That translates to **$12,506 per employee per year** lost to miscommunication.
- **100%** of knowledge workers surveyed experience miscommunication at least weekly. **One in four** report miscommunication multiple times per day.
- **One in five** business leaders report losing business due to poor communication, while **43%** say effective communication has helped them win new business.

Writing clearly is not a nicety — it is a competitive advantage with measurable financial returns.

*Sources: [Grammarly & Harris Poll (2022). "State of Business Communication Report."](https://www.businesswire.com/news/home/20220125005525/en/Grammarly-and-Harris-Poll-Research-Estimates-U.S.-Businesses-Lose-%241.2-Trillion-Annually-to-Poor-Communication) [Grammarly & Harris Poll (2023). "The State of Business Communication."](https://www.businesswire.com/news/home/20230222005390/en/Grammarly-Business-and-Harris-Poll-Find-Poor-Workplace-Communication-Is-Sinking-Productivity-and-Performance)*

---

## Part II: The Anatomy of a Professional CEM Email
**(~25 min lecture + examples)**

---

### 2.1 Five Elements of Every Project Email

Every email you send on a construction project should contain five elements. Think of this as a checklist — if any element is missing or weak, the email needs revision.

| Element | Purpose | CEM Example |
|---------|---------|-------------|
| **Subject line** | Searchable, specific, scannable | `[Project Riverside] RFI-042: Foundation Drain Detail at Grid B-3` |
| **Greeting** | Sets tone and relationship | `Dear Mr. Yilmaz,` or `Hi Ayse,` (match formality to the relationship) |
| **Body** | Context, facts, request | 2–3 short paragraphs max — frontload the key information |
| **Call to Action (CTA)** | What you need, by when | `Please confirm the revised detail by Friday, Feb 20.` |
| **Sign-off** | Professional close + full signature | `Best regards,` + name, title, company, phone |

---

### 2.2 The Subject Line — Your Email's First Impression

The subject line matters more than most people realize:

- **47%** of recipients decide whether to open an email based solely on the subject line.
- **69%** of people mark emails as spam based on the subject line alone.
- On construction projects, subject lines are also how people **search for emails months or years later** during claims, audits, and close-out.

**The CEM subject line formula:**

```
[Project Name] Document Type - Number: Brief Description
```

Examples:
- `[Kadikoy Mixed-Use] RFI-017: Rebar Spacing at Pile Cap PC-12`
- `[Metro Line 3] Submittal-045: Structural Steel Shop Drawings — Rev 2`
- `[Campus Dormitory] Schedule Impact Notice: 5-Day Delay — Excessive Rainfall`

**Bad subject lines vs. good ones:**

| Bad | Good |
|-----|------|
| `Question` | `[Riverside] RFI-042: Foundation Drain Detail at Grid B-3` |
| `FYI` | `[Metro Line 3] Concrete Test Results — Pours 14–17, All Pass` |
| `Urgent!!!` | `[Campus Dorm] ACTION REQUIRED: Crane Permit Expiry Feb 15` |
| `Change` | `[Kadikoy] CO-008: Added Retaining Wall at Grid Line J` |

*Sources: [Superhuman (2024). "Email Subject Line Statistics."](https://blog.superhuman.com/email-subject-line-statistics/) [FinancesOnline (2024). "52 Email Subject Line Statistics."](https://financesonline.com/email-subject-line-statistics/)*

---

### 2.3 The Body — Front-Load, Then Support

Construction professionals are busy. They receive 72+ emails a day. They will not read four paragraphs before discovering what you need. Rules:

1. **First sentence = the point.** State what you need or what happened.
2. **Second paragraph = supporting facts.** Dates, contract references, activity IDs, measurements.
3. **Third paragraph (if needed) = context or background.** Only include if the reader needs it.
4. **Bullet points** for any list of three or more items.
5. **One email, one topic.** If you have two unrelated requests, send two emails.

> **Key Insight:** The most common email mistake in CEM is burying the request. If your reader has to scroll past three paragraphs of background to find out what you need, you have failed. Front-load the ask.

**Before and after — the same request, two versions:**

❌ **Buried lead:**
```
Hi Ms. Arslan,

I wanted to follow up on our conversation from last week about the
foundation details. As you know, the soil report came back and there
were some discrepancies with the original design assumptions. Our
structural engineer reviewed everything and had a few questions.
Could you please clarify the drain detail at Grid B-3?
```

✅ **Front-loaded:**
```
Hi Ms. Arslan,

Could you please clarify the foundation drain detail at Grid B-3?
The soil report (attached) shows a discrepancy with the original
design assumptions, and our structural engineer needs your input
before we proceed with forming.
```

Both versions contain the same information. The front-loaded version puts the request in the first sentence, so the reader knows *exactly* what you need within five seconds.

---

### 2.4 Common CEM Email Mistakes

**Mistake 1 — Vague subject lines**
Bad: `Question` / Good: `[Metro Line 3] RFI-017: Rebar Spacing at Pile Cap PC-12`

**Mistake 2 — No clear CTA**
Bad: `Let me know what you think.` / Good: `Please respond with the approved shop drawing by COB Thursday, Feb 20.`

**Mistake 3 — Emotional language in contractual correspondence**
Bad: `Your team's incompetence caused this delay.`
Good: `The concrete pour scheduled for Jan 15 was delayed due to incomplete formwork inspection. We request a 3-day time extension per Section 8.3 of the General Conditions.`

**Mistake 4 — No contract reference**
Bad: `We need more time for the delay.`
Good: `Per Section 8.3.1 of the General Conditions, we hereby provide formal notice of a weather-related delay and request a 5-day non-compensable time extension.`

**Mistake 5 — Missing response deadline**
Bad: `Can you get back to me on this?`
Good: `Please provide your determination by February 20, 2026.`

---

### 2.5 Example: Bad vs. Good Email — Schedule Delay Notice

**Bad Email**
```
Subject: Delay

Hi,

There's been a delay on site because of the weather and some other stuff.
We need more time. Can you approve?

Thanks,
Mehmet
```

**What is wrong:** No project name. No contract reference. No specific dates. No measurable data. No deadline for response. "Some other stuff" is not a legal argument. "Can you approve?" is not a formal request.

**Good Email**
```
Subject: [Kadikoy Mixed-Use] Schedule Impact Notice: 5-Day Delay Due to
         Excessive Rainfall

Dear Ms. Arslan,

Per Section 8.3.1 of the General Conditions, this email serves as formal
notice of a weather-related delay on the Kadikoy Mixed-Use Project
(Contract No. KMU-2025-003).

Continuous rainfall from Feb 3–7, 2026 (5 consecutive days exceeding
25 mm/day) prevented the following critical-path activities:
- Excavation at Zone C (Activity ID: EXC-C-010)
- Foundation formwork at Zone B (Activity ID: FRM-B-008)

We request a 5-day non-compensable time extension. Supporting weather
data from the Istanbul Meteorological Station is attached.

Please confirm receipt and provide your determination by February 20, 2026.

Best regards,
Mehmet Demir, PE
Project Manager | Demir Construction
+90 532 XXX XXXX
mehmet.demir@demirconstruction.com
```

> **Key Insight:** The good email is specific, references the contract, includes measurable data (25 mm/day), identifies affected activities by ID, and states a clear response deadline. It protects the contractor's rights while remaining professional. This is the difference between a time extension granted and a time extension denied.

---

### 2.6 CC, BCC, and Reply All — Who Sees What?

Getting the recipient fields right is part of writing a professional email. On a construction project, a misplaced CC can escalate a routine issue, and a careless Reply All can share sensitive information with the wrong parties.

**When to use each field:**

| Field | Use When… | Example |
|-------|-----------|---------|
| **To** | The person must act — they own the response | The architect who needs to answer your RFI |
| **CC** | The person needs to stay informed but does not need to act | Your project manager, who should know the RFI was sent |
| **BCC** | You need a record sent to someone without other recipients knowing | Copying your firm's legal counsel on a dispute-related email |
| **Reply All** | Everyone on the thread genuinely needs to see your response | Confirming a schedule change that affects all parties |

**CEM-specific CC guidance:**

- **CC the owner's representative** when: issuing formal notices (delays, claims, change orders), transmitting submittals, requesting time extensions — any action that creates a contractual record.
- **Do NOT CC the owner** on: internal coordination with subcontractors, pricing discussions, or draft documents. Premature owner visibility can complicate negotiations.
- **Archiving:** On most projects, a project controls or document control team is CC'd on formal correspondence to maintain a central record. If your project uses Procore, Aconex, or similar software, emails sent through the system are archived automatically.

**The Reply-All disaster:**

> A mechanical subcontractor on a hospital project hit "Reply All" on a pricing thread — accidentally sharing their internal cost breakdown (including profit margins) with the owner, the architect, and three competing subcontractors. The GC's relationship with the owner was strained for weeks as the owner demanded to know why the subcontractor's markup was "so high." The subcontractor lost their negotiating position entirely.
>
> **Lesson:** Before you press Reply All, ask: "Does *every* person on this thread need to see my response?" If not, reply only to the sender.

**A note on BCC ethics:** BCC is appropriate for protecting privacy (e.g., mass-distributing meeting minutes without exposing everyone's email) and for keeping legal counsel informed. It is *not* appropriate for secretly monitoring someone or building a case behind their back while pretending to have a private conversation. If your use of BCC would embarrass you if discovered, do not use it.

---

## Part III: What Are Large Language Models?
**(~25 min lecture)**

You now have a framework: five elements, front-loaded structure, contract references, clear CTAs. Following these rules manually takes discipline and time — especially when you are writing your 30th email of the day. This raises a natural question: *can a machine help?*

The answer is yes — but only if you understand what the machine is actually doing. An LLM that drafts a delay notice for you is not a colleague who "knows" construction law. It is a statistical pattern-matcher that has seen millions of professional emails. It can produce remarkably polished text, but it can also invent contract clauses that do not exist and cite specification sections that were never written. To use it safely, you need to know how it works.

---

### 3.1 The Core Idea: A Very Sophisticated Autocomplete

You already know autocomplete. When you type "See you tom" on your phone, it suggests "tomorrow." Your phone is predicting the next word based on patterns it has seen before.

A Large Language Model (LLM) — like Claude, ChatGPT, or Gemini — does the same thing, but at a vastly larger scale. Instead of learning from your text messages, it learned from a significant fraction of all text on the internet: books, articles, websites, code, emails, research papers — hundreds of billions of words.

> **Analogy:** Imagine you read every email, every report, every contract, and every textbook ever written in your field. Then someone gives you the beginning of a sentence and asks you to finish it. You would be very good at predicting what comes next — not because you "understand" the content the way a human does, but because you have seen so many examples that you recognize the patterns. That is what an LLM does.

The key technical insight: **an LLM generates text one word (or "token") at a time, always predicting what the most likely next word should be, given everything that came before it.**

---

### 3.2 Key Concepts (No Math Required)

Here are the terms you will encounter this semester, explained in plain language:

| Term | What It Means | Analogy |
|------|--------------|---------|
| **Token** | The basic unit the model reads and writes. Usually a word or part of a word. "Construction" = 1 token. "Subcontractor" might be 2 tokens ("sub" + "contractor"). In English, 1 word is roughly 1.3 tokens. | Letters in Scrabble — the model builds sentences tile by tile. |
| **Training** | The process of showing the model billions of text examples so it learns patterns. Training GPT-3 cost an estimated $4.6 million in compute alone. | Studying for an exam by reading every textbook in the library — except the library contains 500 billion words. |
| **Prompt** | The text you give the model as input. The quality of your prompt determines the quality of the output. | Your order at a restaurant. "Give me food" gets you something random. "Grilled salmon, medium, with lemon butter sauce, no asparagus" gets you exactly what you want. |
| **Context window** | How much text the model can "see" at once. Modern models can handle 100,000–1,000,000+ tokens. | The size of the model's desk. A bigger desk means it can spread out more documents and reference them while writing. |
| **Hallucination** | When the model generates plausible-sounding but incorrect information. It does not "know" facts — it predicts likely text. | A confident colleague who sounds authoritative but sometimes makes things up. Always verify. |

> **Key Insight:** The single most important concept for this course: **the quality of your output depends on the quality of your prompt.** A vague prompt yields a vague response. A precise, context-rich prompt yields a precise, useful response. This is the skill we will build all semester.

**Tokens in action — a CEM subject line:**

Let us see how tokenization works with a real example. The subject line:

```
[Kadikoy Mixed-Use] RFI-017: Rebar Spacing at Pile Cap PC-12
```

breaks into approximately **22 tokens**: `[`, `Kad`, `ikoy`, ` Mixed`, `-`, `Use`, `]`, ` RFI`, `-`, `017`, `:`, ` Re`, `bar`, ` Spacing`, ` at`, ` Pile`, ` Cap`, ` PC`, `-`, `12`, and the surrounding punctuation. Notice that common English words like "at" and "Spacing" are single tokens, but the Turkish project name "Kadikoy" gets split into parts the model has seen less frequently.

Why does this matter? Because context windows are measured in tokens, not words. A model with a 100,000-token context window can hold roughly **1,500 professional emails** at once — enough to analyze an entire project's RFI correspondence in a single prompt. We will use this capability later in the semester when we build document analysis agents.

---

### 3.3 A Brief Timeline of LLMs

You do not need to memorize this. But knowing where these tools came from helps you understand how fast the field is moving — and why these tools exist now but did not exist five years ago.

**What is a Transformer?**

The Transformer is the architecture that makes modern LLMs possible. Before 2017, language models processed text sequentially — word by word, left to right — which was slow and made it hard to capture relationships between distant words. The Transformer introduced a mechanism called **attention**, which allows the model to look at *all* the words in a passage simultaneously and figure out which ones are most relevant to each other.

Think of it this way: if you are reading a long contract clause and you encounter the word "it," your brain instantly jumps back to figure out what "it" refers to — maybe a noun from three sentences ago. A Transformer does the same thing, but mathematically, across thousands of words at once. This is why modern LLMs can handle 100-page documents: they can "attend to" any part of the input when generating each word of the output.

Every major LLM today — Claude, ChatGPT, Gemini — is built on this Transformer architecture. The "T" in "GPT" literally stands for "Transformer."

| Year | Milestone | Significance |
|------|-----------|-------------|
| **2017** | Google publishes "Attention Is All You Need" | Introduces the **Transformer** architecture — the foundation of every modern LLM. Before this, language models were slow and limited. |
| **2018** | OpenAI releases GPT-1 (117M parameters) | First "Generative Pre-trained Transformer." Showed that pre-training on lots of text, then fine-tuning, works remarkably well. |
| **2020** | OpenAI releases GPT-3 (175B parameters) | A massive leap: 1,000x larger than GPT-1. Could write essays, code, and poetry. Trained on ~500 billion words. For comparison, a child hears ~100 million words by age 10. |
| **2022** | OpenAI launches ChatGPT (Nov 30) | GPT-3.5 wrapped in a chat interface. Reached 100 million users in 2 months — the fastest-growing consumer app in history at that time. |
| **2023** | GPT-4, Claude, Gemini all launch | The "Big Three" — OpenAI, Anthropic, and Google — each release frontier models. Multimodal capabilities (text + images) arrive. |
| **2024** | Reasoning models (OpenAI o1), context window expansion | Models learn to "think step by step" before answering. Context windows grow from 8K to 200K–1M tokens, enabling analysis of entire document sets in one prompt. |
| **2025–26** | Claude 4.5/4.6, AI coding agents | Models become faster, cheaper, and deployable on phones. AI coding agents (Claude Code, Codex CLI, Gemini CLI) let you interact with LLMs from the terminal — which is exactly what we will do in Part IV today. |

> **Key Insight:** The entire LLM revolution is built on a single 2017 paper by eight Google researchers. From that paper to the tools you are using today: less than 8 years. The rate of change is unprecedented, which is why learning to work with these tools now — early in your career — gives you a significant professional advantage.

*Sources: Vaswani et al. (2017). ["Attention Is All You Need."](https://arxiv.org/abs/1706.03762) [Life Architect: "Timeline of AI and Language Models."](https://lifearchitect.ai/timeline/) [Simon Willison (2025). "2025: The Year in LLMs."](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)*

---

### 3.4 Does AI Actually Make Writing Better? The Evidence

This is not a hypothetical question. Researchers have tested it:

**The MIT Study (2023):** Shakked Noy and Whitney Zhang (MIT) recruited 453 college-educated professionals — marketers, consultants, HR managers, data analysts — and gave them realistic writing tasks: drafting cover letters, composing restructuring emails, writing analysis plans. Half had access to ChatGPT; half did not. The results:

| Metric | Without AI | With AI | Change |
|--------|-----------|---------|--------|
| Task completion time | ~27 min | ~17 min | **40% faster** |
| Output quality (rated by blind evaluators) | Baseline | +18% | **18% higher quality** |
| Performance gap between low- and high-ability writers | Large | Reduced | **More equal outcomes** |

The most striking finding: **AI helped weaker writers more than stronger ones**, reducing inequality in output quality. However, 68% of participants simply copied and pasted the AI output without editing — a practice that, in CEM, would be dangerous (hallucinated contract clauses, wrong activity IDs, incorrect dates).

**What a hallucinated contract clause looks like:**

Imagine an LLM generates this sentence in a delay notice: *"Per Section 8.3.2(b)(iii) of the General Conditions, the Contractor is entitled to a compensable time extension for force majeure events exceeding 72 continuous hours."* It sounds authoritative. It follows the right pattern. But if your contract's force majeure clause is actually in Section 12.1 and requires 5 business days' written notice — you have just sent a formal claim citing a provision that does not exist. That is not a formatting error. It is a false legal assertion on a document that may become Exhibit A in arbitration.

> **Key Insight:** AI makes you faster and can raise your floor. But it does not replace your judgment. On a construction project, an AI-generated delay notice with a hallucinated contract section number is worse than no notice at all. The human reviews, verifies, and takes responsibility. That is your role.

*Source: Noy, S. & Zhang, W. (2023). "Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence." [Science](https://www.science.org/doi/10.1126/science.adh2586). See also: [MIT News coverage](https://news.mit.edu/2023/study-finds-chatgpt-boosts-worker-productivity-writing-0714).*

---

### 3.5 Privacy and Confidentiality — What NOT to Paste into an LLM

Before you start using LLMs for project work, there is a critical boundary you must understand: **not everything belongs in a prompt.**

When you type text into Claude, ChatGPT, or any cloud-based LLM, that text travels over the internet to the provider's servers. Depending on the provider and your subscription tier, your input may be used to train future models, stored in logs, or accessible to the provider's employees for safety review. This has real implications for construction professionals.

**Sensitive information you should NEVER paste into a general-purpose LLM:**

| Category | Examples | Why It Matters |
|----------|----------|---------------|
| **Proprietary project data** | Detailed cost estimates, bid breakdowns, profit margins | Competitors could gain advantage; violates NDA terms |
| **Client correspondence** | Owner emails, architect comments, meeting minutes with names | May contain privileged or confidential business information |
| **Dispute / claim communications** | Delay notices, legal counsel emails, mediation documents | Attorney-client privilege can be waived by disclosure to third parties |
| **Personally identifiable information (PII)** | Employee SSNs, home addresses, health records, salary data | Violates data protection laws (KVKK in Turkey, GDPR in the EU) |
| **Pre-bid / procurement information** | Subcontractor quotes, supplier pricing, bid strategy documents | Sharing before award can constitute bid-rigging exposure |

**Practical guidance for this course:**

- In class exercises and homework, **use fictionalized scenarios** — made-up project names, placeholder names, synthetic data. This is what we will do all semester.
- In professional practice, **establish a firm-wide AI usage policy** before anyone starts using LLMs on project data. Many large contractors (Skanska, Turner, Vinci) already have these policies in place.
- Be aware of **enterprise AI tiers**: providers like Anthropic and OpenAI offer business plans that contractually guarantee your data will not be used for training. If your firm uses AI on real project data, this tier is the minimum acceptable option.

> **Key Insight (KVKK / Data Protection):** Turkey's Personal Data Protection Law (KVKK, No. 6698) imposes obligations on data controllers — including construction firms — regarding the processing, storage, and transfer of personal data. Pasting employee or client personal data into a foreign-hosted LLM without a lawful basis constitutes a cross-border data transfer that may violate KVKK. When in doubt, anonymize first.

---

## Part IV: What Is an API? Your First LLM Call
**(~20 min demo + hands-on)**

---

### 4.1 What Is an API? The Restaurant Analogy

You will hear the term "API" a lot in this course. Here is what it means, with no jargon:

**API** stands for **Application Programming Interface**. It is a way for two software systems to talk to each other.

> **Analogy:** Think of a restaurant. You (the customer) sit at a table. The kitchen (the AI model) prepares food. But you do not walk into the kitchen yourself. Instead, you tell the **waiter** what you want, the waiter carries your order to the kitchen, the kitchen prepares it, and the waiter brings it back to your table.
>
> The waiter is the API. The menu is the API documentation. Your order is the "request." The food you receive is the "response."
>
> When you type a prompt into Claude Code, here is what happens behind the scenes:
> 1. You type your prompt (your order).
> 2. Claude Code packages it and sends it over the internet to Anthropic's servers (the waiter walks to the kitchen).
> 3. The Claude model processes your prompt and generates a response (the kitchen prepares your food).
> 4. The response streams back to your terminal (the waiter brings your plate).

That is it. An API call is just: **send a request, get a response.** You do not need to know how the kitchen works. You just need to know how to place a good order — which is why prompt engineering matters.

---

### 4.2 Tool Demo: Your First LLM API Call

Let us make this concrete. Open your terminal, navigate to your project folder, and try these prompts in sequence. Watch how the output changes as you add more context.

**Step 1 — A bare-minimum prompt:**
```bash
claude "Write a delay notice email."
```
Observe: The model will produce *something* — but it will be generic. No project name, no contract reference, no specific dates. It is like ordering "food" at a restaurant.

**Step 2 — Adding context:**
```bash
claude "Write a professional email from the project manager to the owner's representative, providing formal notice of a 5-day weather delay on the Kadikoy Mixed-Use Project. Reference contract section 8.3.1. Include specific dates (Feb 3-7, 2026) and affected activities. Tone: formal and contractually precise."
```
Observe: The output should now include a proper subject line, contract references, specific dates, and a professional structure. Same model, dramatically better output — because you gave it a better prompt.

**Step 3 — Asking the model to critique its own output:**
```bash
claude "Review the email you just wrote. Does it include: (1) a searchable subject line with project name, (2) a contract reference, (3) specific dates and durations, (4) affected activity IDs, (5) a clear CTA with a response deadline? If anything is missing, rewrite the email with all five elements."
```
Observe: The model can self-correct when given a checklist. This is a preview of how your communication agent will work — you will build checklists and templates that the AI applies automatically.

---

### 4.3 What to Notice During the Demo

As you run these prompts, pay attention to:

1. **Speed.** The response appears token by token (streaming). The model is generating text one piece at a time — just like the word prediction we discussed.
2. **Context sensitivity.** The second prompt produces dramatically better output than the first. The model did not get "smarter" — you gave it better input.
3. **Limitations.** The model may invent an activity ID (e.g., "EXC-C-010") that sounds plausible but does not exist on your project. This is hallucination in action. Always verify facts.
4. **No memory between sessions.** If you close your terminal and open a new one, the model does not remember your previous conversation (unless you are in an ongoing session). Context is not persistent by default.

---

## Part V: In-Class Activity — Email Clinic
**(45 min)**

---

### Activity Instructions

1. **Read (5 min)** — Each student receives a printed "bad email" from a realistic CEM scenario. Scenarios include:
   - An RFI response that is vague and non-committal
   - A submittal rejection with no explanation of deficiencies
   - A payment dispute email written in angry, emotional language
   - A meeting minutes distribution with no action items or deadlines

---

**Scenario 1 — The Vague RFI Response (full text, annotated):**

```
Subject: RE: Question                                       ← [No project name, no RFI number, unsearchable]

Hi,                                                         ← [No name — who is this addressed to?]

Thanks for your question. We looked at it and think it
should be fine the way it is. Let us know if you have       ← [No reference to what was asked]
any other questions.                                        ← [No specification reference, no drawing reference]

                                                            ← [No CTA, no deadline, no next steps]
Best,
Ahmet                                                       ← [No title, no company, no phone, no email]
```

**What should the good version include?**
- Subject: `RE: [Kadikoy Mixed-Use] RFI-017: Rebar Spacing at Pile Cap PC-12`
- Address the requester by name
- Restate the question briefly: "Regarding your inquiry about rebar spacing at Pile Cap PC-12 (Drawing S-201, Detail 4)..."
- Provide the answer with a specification or drawing reference: "The design intent is #5 bars at 200 mm o.c. each way, per Specification Section 03 20 00, Paragraph 3.4.B."
- State any conditions: "If field conditions differ from Drawing S-201, submit a field sketch for review before proceeding."
- Deadline / next step: "Please confirm receipt. If you require further clarification, respond by February 20, 2026."
- Full signature block with name, title, firm, phone, and email

> **Note:** Three additional scenarios (submittal rejection, payment dispute, meeting minutes) are provided as printable PDFs in the `scenarios/` subfolder. Distribute one scenario per table group.

---

2. **Rewrite (15 min)** — Rewrite the email applying today's five-element structure and rules. Work individually, on paper or in Cursor.

3. **LLM comparison (10 min)** — Paste the same bad email into Claude Code with this prompt:
   ```
   Rewrite this email professionally for a construction project context.
   Apply these rules: (1) specific subject line with project name,
   (2) proper greeting, (3) frontloaded body with facts, (4) clear CTA
   with deadline, (5) professional sign-off with full signature block.
   ```
   Compare the LLM output with your own rewrite.

4. **Pair review (10 min)** — Swap your rewrite with a partner. Use this checklist:
   - [ ] Subject line includes project name and document reference?
   - [ ] CTA is specific with a deadline?
   - [ ] Tone is professional and factual (no emotional language)?
   - [ ] Contract or specification references included where relevant?
   - [ ] Body is 3 paragraphs or fewer?

5. **Debrief (5 min)** — Class discussion:
   - Where did the LLM do better than your manual rewrite?
   - Where did your human judgment add value the LLM missed?
   - Did the LLM hallucinate any facts (contract sections, dates, names)?

---

## Homework / Milestone

### M0 — First LLM Calls from CLI

**Objective:** Demonstrate that your toolchain works and you can interact with an LLM from the command line.

**Instructions:**
1. Run at least **3 different CEM-related prompts** using Claude Code (or Codex CLI / Gemini CLI) from your terminal. Example prompt ideas:
   - "Draft an RFI for an unclear foundation drain detail on Drawing S-201"
   - "Write a professional email requesting an updated CPM schedule from the GC"
   - "Summarize the key elements of a proper delay notice under a standard AIA contract"

2. Save the prompts and outputs in a file: `project/logs/m0_first_calls.md`

3. At the end of the file, write **3–5 sentences** reflecting on what you observed. What surprised you? Where was the output good? Where was it wrong or incomplete?

4. Commit and push:
   ```bash
   git add project/logs/m0_first_calls.md
   git commit -m "M0: first LLM calls from CLI"
   git push origin main
   ```

**Due:** Before Week 3 session.

**Grading:** Pass/Fail. The file must contain at least 3 prompt-response pairs and your reflection paragraph.

---

### What's Next — Week 3 Preview

Next week we move from *general* email writing to the two most critical document types in construction communication: **RFIs** (Requests for Information) and **Submittals**. You will learn:

- Why the average project generates **~800 RFIs** and what makes a good one vs. a bad one
- How to write a submittal transmittal letter that does not get rejected on the first round
- The **system / user / assistant** roles in LLM prompting — the framework that turns a generic chatbot into a CEM specialist
- How to build **reusable prompt templates** in Cursor that enforce the five-element email checklist automatically

The trajectory: this week you learned the rules manually. Next week, you start teaching the machine to apply them for you.

> **Reminder:** Complete **M0 (First LLM Calls from CLI)** before next session. You will need a working toolchain for the Week 3 hands-on exercises.

---

### Further Reading

**Email in CEM:**
- [For Construction Pros: "Understanding How to Effectively Communicate via Email for Construction Projects"](https://www.forconstructionpros.com/business/article/21025295/understanding-how-to-effectively-communicate-via-email-for-construction-projects)
- [Newforma: "Modernizing Email Management in Construction"](https://www.newforma.com/modernizing-email-management-in-construction-improve-project-efficiency/)
- [Plain Language Guide Series (Digital.gov)](https://digital.gov/guides/plain-language)

**Understanding LLMs (non-technical):**
- Timothy B. Lee, Understanding AI (2023). ["Large Language Models, Explained with a Minimum of Math and Jargon"](https://www.understandingai.org/p/large-language-models-explained-with)
- Miguel Grinberg (2024). ["How LLMs Work, Explained Without Math"](https://blog.miguelgrinberg.com/post/how-llms-work-explained-without-math)
- [AWS: "What Is an LLM?"](https://aws.amazon.com/what-is/large-language-model/)

**AI and Writing:**
- Noy, S. & Zhang, W. (2023). ["Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence."](https://www.science.org/doi/10.1126/science.adh2586) *Science.*
- [Anthropic: Prompting Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices)

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
