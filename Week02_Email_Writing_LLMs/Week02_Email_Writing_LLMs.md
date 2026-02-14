# CEM501: Communication Skills for CEM
## Week 2: Professional Email & Intro to LLMs
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Apply a clear structure to every professional email: subject, greeting, body, CTA, sign-off
- Identify and fix the most common email mistakes in CEM correspondence
- Explain, at a conceptual level, what a large language model (LLM) is and how it generates text
- Use Claude Code (or Codex CLI / Gemini CLI) to make your first LLM API call from the command line

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

If the construction-specific evidence from Week 1 was not convincing enough, consider the broader business data:

- **$1.2 trillion per year** — the estimated cost of poor communication to U.S. businesses, according to a Grammarly and Harris Poll survey. That translates to **$12,506 per employee per year** lost to miscommunication.
- **100%** of knowledge workers surveyed experience miscommunication at least weekly. **One in four** report miscommunication multiple times per day.
- **One in five** business leaders report losing business due to poor communication, while **43%** say effective communication has helped them win new business.

Writing clearly is not a nicety — it is a competitive advantage with measurable financial returns.

*Sources: [Grammarly & Harris Poll (2022). "State of Business Communication Report."](https://www.businesswire.com/news/home/20220125005525/en/Grammarly-and-Harris-Poll-Research-Estimates-U.S.-Businesses-Lose-%241.2-Trillion-Annually-to-Poor-Communication) [Grammarly (2023). "The State of Business Communication: New Threats and Opportunities."](https://www.grammarly.com/business/learn/state-of-business-communications-2023/)*

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

## Part III: What Are Large Language Models?
**(~25 min lecture)**

Now that we understand *what* good email looks like, let us introduce the tool that will help you write them faster and better. But first, you need a conceptual understanding of how that tool actually works.

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

---

### 3.3 A Brief Timeline of LLMs

You do not need to memorize this. But knowing where these tools came from helps you understand how fast the field is moving — and why these tools exist now but did not exist five years ago.

| Year | Milestone | Significance |
|------|-----------|-------------|
| **2017** | Google publishes "Attention Is All You Need" | Introduces the **Transformer** architecture — the foundation of every modern LLM. Before this, language models were slow and limited. |
| **2018** | OpenAI releases GPT-1 (117M parameters) | First "Generative Pre-trained Transformer." Showed that pre-training on lots of text, then fine-tuning, works remarkably well. |
| **2020** | OpenAI releases GPT-3 (175B parameters) | A massive leap: 1,000x larger than GPT-1. Could write essays, code, and poetry. Trained on ~500 billion words. For comparison, a child hears ~100 million words by age 10. |
| **2022** | OpenAI launches ChatGPT (Nov 30) | GPT-3.5 wrapped in a chat interface. Reached 100 million users in 2 months — the fastest-growing consumer app in history at that time. |
| **2023** | GPT-4, Claude, Gemini all launch | The "Big Three" — OpenAI, Anthropic, and Google — each release frontier models. Multimodal capabilities (text + images) arrive. |
| **2024–25** | Rapid iteration: GPT-5, Claude Opus 4, Gemini 3 | Models become faster, cheaper, more capable. Context windows expand to 1M+ tokens. AI coding agents (Claude Code, Codex CLI, Gemini CLI) emerge. |

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

> **Key Insight:** AI makes you faster and can raise your floor. But it does not replace your judgment. On a construction project, an AI-generated delay notice with a hallucinated contract section number is worse than no notice at all. The human reviews, verifies, and takes responsibility. That is your role.

*Source: Noy, S. & Zhang, W. (2023). "Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence." [Science](https://www.science.org/doi/10.1126/science.adh2586). See also: [MIT News coverage](https://news.mit.edu/2023/study-finds-chatgpt-boosts-worker-productivity-writing-0714).*

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

### Further Reading

**Email in CEM:**
- [For Construction Pros: "Understanding How to Effectively Communicate via Email for Construction Projects"](https://www.forconstructionpros.com/business/article/21025295/understanding-how-to-effectively-communicate-via-email-for-construction-projects)
- [Newforma: "Modernizing Email Management in Construction"](https://www.newforma.com/modernizing-email-management-in-construction-improve-project-efficiency/)
- [Plain Language Guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/guidelines/)

**Understanding LLMs (non-technical):**
- Ars Technica / Timothy B. Lee (2023). ["Large Language Models, Explained with a Minimum of Math and Jargon"](https://www.understandingai.org/p/large-language-models-explained-with)
- Miguel Grinberg (2024). ["How LLMs Work, Explained Without Math"](https://blog.miguelgrinberg.com/post/how-llms-work-explained-without-math)
- [AWS: "What Is an LLM?"](https://aws.amazon.com/what-is/large-language-model/)

**AI and Writing:**
- Noy, S. & Zhang, W. (2023). ["Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence."](https://www.science.org/doi/10.1126/science.adh2586) *Science.*
- [Anthropic: Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
