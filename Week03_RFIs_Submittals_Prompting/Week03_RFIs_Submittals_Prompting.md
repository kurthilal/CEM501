# CEM501: Communication Skills for CEM
## Week 3: RFIs, Submittals & Prompt Engineering
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Quantify the cost, schedule, and quality impact of poorly written RFIs using industry data
- Write a clear, actionable RFI that minimizes back-and-forth with the design team
- Prepare a submittal transmittal letter with all required metadata and avoid common rejection triggers
- Explain the system / user / assistant roles in LLM prompting using CEM analogies
- Build reusable prompt templates for CEM documents using Cursor

---

## Part I: RFIs -- The Most Critical Written Communication in CEM
**(~30 min lecture)**

A Request for Information (RFI) is how the contractor formally asks the architect or engineer to clarify design intent. It sounds simple, but the data tells a different story: RFIs are one of the most expensive, time-consuming, and schedule-critical communication acts on any construction project.

### 1.1 The Scale: How Many RFIs Does a Project Generate?

In 2013, the Navigant Construction Forum published the most comprehensive RFI study to date, analyzing data from **1,362 projects worldwide** containing over **1 million RFI responses**. The headline findings:

| Metric | Value |
|--------|-------|
| Average RFIs per project | **~796** |
| RFIs per $1M of construction | **9.9** |
| Average hours spent on RFIs per project | **6,368 hours** |
| Average cost of RFI management per project | **$859,680** |

Think about what that means: on a $100 million project, expect roughly **990 RFIs**, consuming thousands of person-hours across the project team.

> **Key Insight:** RFIs are not occasional clarifications -- they are a continuous, high-volume communication stream. Managing them well is not optional; it is a core project management competency.

*Source: Navigant Construction Forum (2013), "Construction Dispute Digest: The RFI." Data widely cited by [CMAA](https://www.cmaanet.org/sites/default/files/resource/Impact%20&%20Control%20of%20RFIs%20on%20Construction%20Projects.pdf) and [eSUB](https://esub.com/blog/rfi-cost-construction-firm).*

---

### 1.2 The Cost: $1,080 per RFI -- and That Is Just the Beginning

The Navigant study estimated the average cost to review and respond to a single RFI at approximately **$1,080**. More recent industry estimates place the figure between **$1,000 and $3,000 per RFI** when indirect costs (coordination meetings, re-sequencing work, waiting time) are included.

But here is the part that should alarm you: **more than 13% of RFIs** were classified as "unjustifiable" -- meaning the answer was already available in the contract documents. Collectively, these unnecessary RFIs cost an average of **$113,400 per project** in wasted review time alone.

| Cost Category | Estimated Value |
|---------------|-----------------|
| Cost per RFI (review + response) | $1,080 (Navigant avg.) |
| Cost of unjustifiable RFIs per project | ~$113,400 |
| Total RFI management cost per project | ~$859,680 |

> **Key Insight:** One in eight RFIs should never have been written. Before you submit an RFI, ask yourself: "Did I actually check the drawings and specs?" You will save your team roughly $1,000 every time the answer is yes.

*Sources: Navigant Construction Forum (2013); [eSUB: The RFI and its Cost to Your Construction Firm](https://esub.com/blog/rfi-cost-construction-firm); [Construction Junkie: The Cost of RFIs](https://www.constructionjunkie.com/blog/2015/9/7/the-cost-of-rfis-and-best-practices-for-construction-professionals).*

---

### 1.3 The Time: 9.7 Days of Schedule Exposure

According to the Navigant study, the average first reply time for an RFI is **6.4 days**, with a median of **9.7 days**. On complex or multi-discipline questions, response times stretch well beyond two weeks.

Worse still, **nearly 22% of all RFIs receive no response at all**. An unanswered RFI is not just an administrative failure -- it is a ticking schedule bomb. When an RFI involves a critical-path activity, every day of delay translates directly to project-level delay, with general conditions costs running **$3,000 to $8,000 per day** on typical commercial projects (site trailers, supervision, temporary utilities, equipment rentals).

Industry sources estimate that RFI-related delays can add up to **10% of a project's total duration**.

> **Key Insight:** A single unanswered RFI on the critical path can cost more than the entire RFI management budget for a small project. This is why your RFI must clearly state the response deadline and the schedule consequence if that deadline is missed.

*Sources: Navigant Construction Forum (2013); [Foundamental: RFI in Construction](https://www.foundamental.com/perspectives/rfi-request-for-information-in-construction); [SubmittalLink: Hidden Costs of Manual RFIs](https://www.submittallink.com/post/hidden-costs-of-construction-admin).*

---

### 1.4 Anatomy of a Strong RFI

Given the cost and schedule exposure, every RFI you write should be engineered for speed and clarity. Here are the essential fields:

| Field | What to Include | Why It Matters |
|-------|----------------|----------------|
| **RFI Number** | Sequential project ID (e.g., RFI-047) | Tracking and audit trail |
| **Date Submitted** | Date of formal issuance | Establishes the delay clock |
| **Subject Line** | Specific reference: drawing number, spec section, grid line | Lets reviewer find the issue in seconds |
| **Question** | One clear question per RFI | Multi-question RFIs get delayed or partially answered |
| **Suggested Solution** | Your proposed interpretation | Speeds response by 30-50% (the reviewer can simply agree or modify) |
| **Impact if Unanswered** | Schedule/cost consequence + response deadline | Creates urgency and documents potential claims |
| **Attachments** | Marked-up drawing, photo, or sketch | Visual evidence eliminates ambiguity |

> **Key Insight:** The number-one reason RFIs get rejected or delayed is that they ask multiple unrelated questions in a single submission. One RFI = one question. Always.

**Example of a strong RFI question:**

```
Drawing S-201, Detail 4 shows #5 rebar at 12" o.c. for the pile cap at
Grid B-3, while Specification Section 03 30 00, Para 3.2.A calls for
#5 at 8" o.c. for pile caps exceeding 1.2 m depth. The pile cap at
Grid B-3 is 1.5 m deep.

Question: Which rebar spacing governs -- the drawing or the spec?

Suggested resolution: Install #5 at 8" o.c. per the specification,
as it is the more stringent requirement.

Impact: Rebar fabrication for Zone B is scheduled to begin Feb 24.
A response is requested by Feb 19 to avoid a 3-day delay to the
critical path.
```

Notice the structure: **context** (what the documents say), **conflict** (the discrepancy), **question** (single, specific), **suggestion** (saves the engineer time), and **consequence** (schedule impact with a date).

---

## Part II: Submittals & Transmittals
**(~20 min lecture)**

If an RFI is a question, a submittal is a declaration: "We intend to use this product / fabricate this component in this way. Do you agree it complies with the contract?"

### 2.1 Submittal Volume and the Rejection Problem

Submittals -- shop drawings, product data, samples, calculations -- are one of the highest-volume document types on commercial construction projects. A mid-sized commercial building can generate **300 to 800+ submittals**. Each one must be reviewed by the contractor's project team before being forwarded to the architect or engineer for formal review.

The industry-wide data on first-submission rejection rates is sobering:

| Metric | Value |
|--------|-------|
| First-submission rejection rate | **~35%** (industry average) |
| Cost per rejection | **~$805** |
| Time added per rejection cycle | **2-4 weeks** |
| Rejection cost on a 500-submittal project | **~$140,000+** |

After three rejection-resubmission cycles, a single mechanical equipment submittal can consume **10-12 weeks of schedule time** -- and if that equipment has a manufacturing lead time of 16-20 weeks, you may have just pushed procurement into the next production slot, adding months of delay.

> **Key Insight:** A submittal is not just paperwork. It is the contractor's declaration that the proposed material or method complies with the contract documents. Submitting carelessly creates liability and triggers costly rejection cycles.

*Sources: [Amazing Architecture: The Resubmittal Spiral](https://amazingarchitecture.com/articles/the-resubmittal-spiral-breaking-the-cycle-of-construction-delays); [AZ Big Media: The Three-Week Submittal Review Trap](https://azbigmedia.com/real-estate/commercial-real-estate/construction/the-three-week-submittal-review-trap-why-timing-matters-more-than-you-think/).*

---

### 2.2 The Transmittal Letter: Your Submittal's Cover Page

Every submittal package requires a transmittal letter that serves as the routing and tracking document. Key fields:

| Field | Example |
|-------|---------|
| **Submittal number and revision** | SUB-M-012 Rev 1 |
| **Spec section reference** | 05 12 00 -- Structural Steel |
| **Description of items** | 6 sheets of shop drawings, 2 product data sheets |
| **Manufacturer/Supplier** | Vulcraft, a division of Nucor |
| **Action requested** | Approved / Approved as Noted / Revise & Resubmit |
| **Contractor's review stamp** | Confirms the contractor has verified compliance |

### 2.3 Why Submittals Get Rejected: The Top Causes

Based on industry data, the most common reasons for submittal rejection include:

1. **Specification non-compliance** -- The submitted product does not match the specified product or approved equal criteria. This is the leading cause.
2. **Incomplete information** -- Missing calculations, certifications, or data sheets that the spec section requires.
3. **Wrong spec section reference** -- The submittal cites the wrong CSI division or paragraph, sending reviewers on a search.
4. **No contractor review stamp** -- Submitting without the contractor's compliance check stamp signals to the reviewer that nobody has actually verified the content.
5. **Poor drawing quality** -- Shop drawings that are illegible, lack dimensions, or do not show connections to adjacent work.

> **Key Insight:** The single most effective thing you can do to reduce rejections is to read the specification section before submitting. Check what product is specified, what data is required, and what certifications must be included. This 15-minute check saves 2-4 weeks of resubmission time.

---

## Part III: Prompt Engineering -- Talking to AI Effectively
**(~25 min lecture)**

You have now seen that construction communication follows patterns: an RFI has a structure, a submittal has required fields, a transmittal has a standard format. Prompt engineering is the same idea applied to AI: **structuring your input so the output matches your intent**.

Think of it this way: writing a prompt is like writing an RFI -- but to an AI instead of an architect.

### 3.1 What Is Prompt Engineering?

Prompt engineering is the practice of crafting inputs to a large language model (LLM) so that the output is accurate, relevant, and formatted the way you need. Both Anthropic (the maker of Claude) and OpenAI have published extensive research on what makes prompts effective.

Anthropic's documentation organizes prompt engineering into a hierarchy of techniques, ordered from most broadly effective to most specialized:

| Technique | Description | CEM Analogy |
|-----------|-------------|-------------|
| **Be clear and direct** | Strip out fluff, use plain language, avoid ambiguity | Writing a spec section, not a novel |
| **Use examples** (few-shot) | Show the model what good output looks like | Providing a sample submittal for reference |
| **Let the model think** (chain of thought) | Ask it to reason step-by-step before answering | Requiring a contractor to show calculations, not just the answer |
| **Use XML/Markdown tags** | Organize your prompt into labeled sections | Using CSI MasterFormat divisions to organize specs |
| **Give a role** (system prompt) | Tell the model who it is and how to behave | The project specifications that govern all work |
| **Chain complex prompts** | Break a big task into sequential smaller tasks | Phased construction: foundation before structure |

*Source: [Anthropic: Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).*

OpenAI's prompt engineering guide identifies six parallel strategies:

1. **Write clear instructions** -- Be specific about format, length, and style
2. **Provide reference text** -- Give the model source material to draw from
3. **Split complex tasks into subtasks** -- Do not ask for a full project plan in one prompt
4. **Give the model time to think** -- Ask for reasoning before the final answer
5. **Use external tools** -- Offload tasks that tools do better (e.g., calculations)
6. **Test changes systematically** -- Evaluate outputs against criteria

*Source: [OpenAI: Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering).*

> **Key Insight:** Notice the overlap between good RFI writing and good prompt writing: be specific, provide context, ask one clear question, and state what format you want the answer in. The skills transfer directly.

---

### 3.2 The Three Roles: System, User, and Assistant

Modern LLMs like Claude operate with three message roles. Understanding these is essential for building effective templates.

| Role | Purpose | CEM Analogy |
|------|---------|-------------|
| **System** | Sets the model's identity, behavior rules, tone, and constraints. Runs "behind the scenes." | **Project specifications** -- they govern all work but are not repeated in every conversation. |
| **User** | Provides the specific request, question, or data for this interaction. | **The RFI question** -- the specific issue you need resolved right now. |
| **Assistant** | The model's response. You can also pre-fill this to guide format. | **The architect's reply** -- the response that resolves your question. |

**Why this matters for templates:** When you create a prompt template, the system prompt is the part that stays constant across many uses (your "spec"), while the user prompt changes each time (each new "RFI"). This separation is what makes templates reusable.

### 3.3 Five Rules for CEM Prompt Engineering

Drawing from both the Anthropic and OpenAI research, here are five rules tailored for construction professionals:

**Rule 1: State the role and domain explicitly.**
Do not just say "write an RFI." Say: "You are a project engineer on a $45M commercial building project. Write a formal RFI following CSI format conventions."

**Rule 2: Provide the reference documents.**
If you want the AI to check a spec section, paste the relevant paragraph into the prompt. LLMs cannot read your project files unless you give them the text. As OpenAI notes: providing reference text reduces fabrication and grounds the output in facts.

**Rule 3: One task per prompt.**
Just as one RFI should contain one question, one prompt should request one deliverable. "Write an RFI and also summarize the meeting minutes" will produce mediocre results for both.

**Rule 4: Show an example of good output.**
Anthropic's research emphasizes that models pay close attention to examples. If you include one well-written RFI as a reference, the model will mirror its structure and tone.

**Rule 5: Specify the output format.**
Do you want a table? Bullet points? A formal letter? A JSON object? Say so explicitly. This is equivalent to specifying deliverable format in a contract.

---

## Part IV: Building Your Prompt Template Library
**(~15 min lecture + demo)**

### 4.1 Why Templates Matter

Using standardized templates for common documents reduces errors and ensures consistency. Research by the UK's Get It Right Initiative (GIRI) found that errors in construction cost the UK industry **GBP 10-25 billion per year**, with standardized processes and checklists identified as a key mitigation strategy.

The same principle applies to AI prompts: a well-designed template with clear structure, defined fields, and consistent formatting will produce reliable output every time -- just like a standard RFI form produces better RFIs than free-form emails.

*Source: [GIRI: Get It Right Initiative](https://getitright.uk.com/); [zipBoard: How to Reduce Construction Document Errors](https://zipboard.co/blog/aec/common-errors-to-look-out-for-during-construction-document-reviews/).*

---

### 4.2 Template 1: RFI Drafter

```markdown
# rfi_drafter.md

## System Prompt
You are a senior project engineer on a commercial construction project.
Your task is to draft formal Requests for Information (RFIs) that follow
industry best practices. Each RFI must contain exactly ONE question.

Writing rules:
- Use formal, concise, technical language
- Always reference specific drawing numbers, detail numbers, spec
  sections, and grid lines
- Include a suggested resolution (this speeds up the architect's response)
- State the schedule impact with a specific date
- Keep the total RFI body under 200 words

Output format:
- RFI Number: [to be assigned]
- Date: [current date]
- To: [Architect/Engineer of Record]
- Subject: [Drawing/Spec reference + brief description]
- Question: [single, specific question]
- Suggested Resolution: [contractor's proposed interpretation]
- Impact if Unanswered: [schedule consequence + deadline for response]
- Attachments: [list of attached files]

## User Prompt Template
Draft an RFI for the following issue:
- Project: {{project_name}}
- Drawing/Spec Reference: {{reference}}
- Issue Description: {{issue}}
- Suggested Resolution: {{suggestion}}
- Affected Trade: {{trade}}
- Activity Start Date: {{activity_date}}
- Response Needed By: {{deadline}}
```

---

### 4.3 Template 2: Submittal Transmittal Letter

```markdown
# submittal_transmittal.md

## System Prompt
You are a project engineer preparing a formal submittal transmittal
letter for a commercial construction project. The transmittal must
be professional, complete, and reference the correct specification
section.

Writing rules:
- Use standard construction industry terminology
- Reference the CSI spec section number and title
- Include the contractor's compliance statement
- Keep the transmittal to one page
- List all enclosed items with quantities

Output format: A formal transmittal letter with these sections:
1. Header (project name, submittal number, date, spec section)
2. Item list (description, quantity, manufacturer)
3. Contractor's certification statement
4. Action requested
5. Distribution list

## User Prompt Template
Prepare a submittal transmittal for:
- Project: {{project_name}}
- Submittal No.: {{submittal_no}} (Rev {{revision}})
- Spec Section: {{spec_section}}
- Description: {{description}}
- Manufacturer/Supplier: {{supplier}}
- Number of Copies/Sheets: {{copies}}
- Certifications Included: {{certs}}
- Action Requested: {{action}}
- Notes: {{notes}}
```

---

### 4.4 Template 3: Daily Report Summarizer

```markdown
# daily_report_summary.md

## System Prompt
You are a field engineer summarizing daily construction activities for
the project manager. Summaries must be factual, concise, and organized
by trade. Flag items needing follow-up as "ACTION REQUIRED:".
Use past tense for completed work. Keep under 300 words.

Output format: Date/weather, manpower table (trade, headcount, hours),
work completed by zone, delays/issues, safety observations, action items.

## User Prompt Template
Summarize today's field activities:
- Date: {{date}} | Weather: {{weather}}
- Trades on site: {{trades_and_headcount}}
- Work performed: {{activities}}
- Issues or delays: {{issues}}
- Safety notes: {{safety}}
```

---

### Tool Demo: Building and Testing Templates in Cursor
**(~15 min live demo)**

1. **Setup:** Create `project/templates/` and paste the RFI template into `rfi_drafter.md`.

2. **Iterate with Cursor AI chat (Cmd+L):**
   `"Review this system prompt. Is it specific enough to produce consistent, professional RFIs? What fields am I missing?"`
   Accept the suggestions that make sense, reject the rest. This is the prompt engineering cycle: draft, test, refine.

3. **Test with Claude Code:**
   ```bash
   claude "Using the template in project/templates/rfi_drafter.md,
   draft an RFI for a discrepancy between Drawing M-401 and
   Spec Section 23 05 13 regarding pipe hanger spacing. The spec
   calls for 8-foot max spacing but the drawing shows 10-foot.
   Trade: mechanical. Activity starts March 10. Need response by
   March 3. Impact: 2-day delay to overhead rough-in."
   ```

4. **Evaluate:** Does the output follow template structure? Is it professional? Would you send it without editing? If not, adjust the system prompt and run again.

> **Key Insight:** A good prompt template is like a good contract form -- it standardizes quality and saves drafting time. The Navigant data shows ~800 RFIs per project. Saving 10 minutes per RFI through better templates saves **133 hours per project**.

---

### In-Class Activity: Build and Test Your Template Library
**(45 minutes)**

1. **Template Creation (20 min)** -- Using Cursor, create at least two prompt templates in `project/templates/`: one for an RFI, one for a CEM document of your choice (daily report, meeting minutes, delay notice, submittal cover, or change order). Each needs a system prompt (role, tone, format, constraints) and a user prompt with `{{placeholder}}` fields.

2. **Test Drive (10 min)** -- Use Claude Code to generate a document from each template with realistic project data. Ask: Does the output match the format? Is the language professional? Would you send it without editing?

3. **Peer Review (10 min)** -- Share your screen with a partner. Is the system prompt specific enough? Are placeholder fields complete? Does the output read like a real project document?

4. **Commit (5 min):**
   ```bash
   git add project/templates/
   git commit -m "M1: add prompt templates for RFI and submittal"
   git push origin main
   ```

---

### Homework / Milestone

**M1 -- Prompt Template Library**

Your `project/templates/` directory must contain at least **3 prompt templates** covering different CEM document types. Requirements:

| Criterion | Details |
|-----------|---------|
| **Quantity** | Minimum 3 templates (e.g., RFI, submittal, daily report, meeting minutes, delay notice) |
| **System prompt quality** | Each must define role, tone, format, constraints, and output structure |
| **User prompt completeness** | Each must have placeholder fields with clear labels |
| **Test outputs** | Generate one sample output per template using Claude Code; save all in `project/logs/m1_template_outputs.md` |
| **Version control** | All files committed and pushed to your repository |

**Due:** Before the Week 4 session.

**Grading rubric:** Completeness (3 templates present), specificity of system prompts, realism of placeholder fields, and quality of sample outputs.

---

### Summary: The RFI-to-Prompt Pipeline

| Construction Communication | Prompt Engineering Equivalent |
|---------------------------|-------------------------------|
| Specification = governs all work | System prompt = governs all outputs |
| RFI question = specific, single issue | User prompt = specific, single request |
| Suggested resolution = speeds response | Example output = guides the model |
| Marked-up drawing = visual evidence | Reference text = grounding data |
| One question per RFI = clarity | One task per prompt = focus |
| Response deadline = urgency | Output format specification = structure |

The skills you build writing good RFIs transfer directly to writing good prompts. Both are about **clarity, structure, specificity, and context**.

---

### Further Reading

- Navigant Construction Forum (2013). "Construction Dispute Digest: The RFI." [Summary via CMAA](https://www.cmaanet.org/sites/default/files/resource/Impact%20&%20Control%20of%20RFIs%20on%20Construction%20Projects.pdf)
- [eSUB: The RFI and its Cost to Your Construction Firm](https://esub.com/blog/rfi-cost-construction-firm)
- [Procore: RFIs -- A Contractor's Guide](https://www.procore.com/library/rfi-construction)
- [Amazing Architecture: The Resubmittal Spiral](https://amazingarchitecture.com/articles/the-resubmittal-spiral-breaking-the-cycle-of-construction-delays)
- [Anthropic: Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI: Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Interactive Prompt Engineering Tutorial (GitHub)](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- Levin, P. (2016). *Construction Contract Claims, Changes & Dispute Resolution,* Ch. 7.
- [Get It Right Initiative (GIRI)](https://getitright.uk.com/) -- UK research on reducing construction errors.

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
