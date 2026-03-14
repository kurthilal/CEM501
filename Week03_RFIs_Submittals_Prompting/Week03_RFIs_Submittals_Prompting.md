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

*Source: Navigant Construction Forum (2013), "Impact & Control of RFIs on Construction Projects." Data widely cited by [CMAA](https://www.cmaanet.org/sites/default/files/resource/Impact%20&%20Control%20of%20RFIs%20on%20Construction%20Projects.pdf) and [eSUB](https://esub.com/blog/rfi-cost-construction-firm).*

---

### 1.2 The Cost: $1,080 per RFI -- and That Is Just the Beginning

The Navigant study estimated the average cost to review and respond to a single RFI at approximately **$1,080**. More recent industry estimates place the figure between **$1,000 and $3,000 per RFI** when indirect costs (coordination meetings, re-sequencing work, waiting time) are included.

But here is the part that should alarm you: **more than 13% of RFIs** were classified as "unjustifiable" -- meaning the answer was already available in the contract documents. On a large project, these unnecessary RFIs cost an estimated **$113,400** in wasted review time alone.

| Cost Category | Estimated Value |
|---------------|-----------------|
| Cost per RFI (review + response) | $1,080 (Navigant avg.) |
| Cost of unjustifiable RFIs per project | ~$113,400 |
| Total RFI management cost per project | ~$859,680 |

> **Key Insight:** One in eight RFIs should never have been written. Before you submit an RFI, ask yourself: "Did I actually check the drawings and specs?" You will save your team roughly $1,000 every time the answer is yes.

*Sources: Navigant Construction Forum (2013); [eSUB: The RFI and its Cost to Your Construction Firm](https://esub.com/blog/rfi-cost-construction-firm); [Construction Junkie: The Cost of RFIs](https://www.constructionjunkie.com/blog/2015/9/7/the-cost-of-rfis-and-best-practices-for-construction-professionals).*

---

### 1.3 The Time: 9.7 Days of Schedule Exposure

According to the Navigant study, the average time to first reply on an RFI is **6.4 days**, while the median time from RFI creation to closure is **9.7 days**. On complex or multi-discipline questions, response times stretch well beyond two weeks.

Worse still, **nearly 22% of all RFIs receive no response at all**. An unanswered RFI is not just an administrative failure -- it is a ticking schedule bomb. When an RFI involves a critical-path activity, every day of delay translates directly to project-level delay, with general conditions costs running **$3,000 to $8,000 per day** on typical commercial projects (site trailers, supervision, temporary utilities, equipment rentals).

Some industry analyses suggest that RFI-related delays can add up to **10% of a project's total duration**, though this figure varies widely by project type and management quality.

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
| **Suggested Solution** | Your proposed interpretation | Speeds response significantly (the reviewer can simply agree or modify rather than drafting from scratch) |
| **Impact if Unanswered** | Schedule/cost consequence + response deadline | Creates urgency and documents potential claims |
| **Attachments** | Marked-up drawing, photo, or sketch | Visual evidence eliminates ambiguity |

> **Key Insight:** The number-one reason RFIs get rejected or delayed is that they ask multiple unrelated questions in a single submission. One RFI = one question. Always.

**Example of a weak RFI:**

```
Subject: Question about rebar

Hi,

We have some questions about the rebar on the project.

1. What is the spacing for the pile cap rebar at Grid B-3?
2. Do we need to increase the concrete cover on the north wall?
3. Should we use epoxy-coated rebar for the exterior footings?

Can you clarify? Thanks.
```

**What is wrong:**

- **Vague subject line** -- "Question about rebar" references no drawing, spec section, or location. The reviewer cannot prioritize or route it (violates the Subject Line field in section 1.4).
- **Multiple unrelated questions** -- Three different issues (spacing, cover, coating) bundled into one RFI. This guarantees partial answers and delays (violates the one-question rule).
- **No suggested resolution** -- The contractor offers no interpretation, forcing the engineer to start from scratch.
- **No deadline or impact statement** -- No schedule consequence, no urgency. This RFI will sit at the bottom of the pile.
- **No attachments** -- No marked-up drawing or photo to show the conflict.
- **Casual tone** -- "Hi," "Can you clarify?", and "Thanks." are fine for email, not for a contractual document that may become a claim exhibit.

**Now compare with the strong version:**

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

A recent industry survey by BuildSync (6,000+ construction professionals) reported the following figures on first-submission rejection rates:

| Metric | Value |
|--------|-------|
| First-submission rejection rate | **~35%** (survey estimate) |
| Cost per rejection | **~$805** (labor, coordination, schedule impact) |
| Time added per rejection cycle | **2-4 weeks** |
| Rejection cost on a 500-submittal project | **~$140,000+** (derived) |

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

**Example: Completed Submittal Transmittal**

```
SUBMITTAL TRANSMITTAL

Project:    Kadikoy Mixed-Use Development (KMU-2026)
Contract:   C-2026-0341
Submittal:  SUB-S-008, Rev 0
Date:       February 10, 2026
Spec Ref:   05 12 00 -- Structural Steel Framing

To:         Architect of Record -- Mimarlar Tasarim A.S.
From:       Koc Insaat Ltd. (General Contractor)

ENCLOSED ITEMS:
  1. Shop drawings (structural steel connections, Zones A-C)   6 sheets
  2. Mill certificates (W14x30 wide-flange beams)              2 certificates
  3. Connection calculations (moment connections at Grid D)     1 set (14 pages)

Manufacturer:   Kardemir A.S.
Fabricator:     Celik Montaj Ltd.

CONTRACTOR'S CERTIFICATION:
We have reviewed the enclosed submittal and confirm that it complies with
the contract documents, applicable codes, and project specifications,
except as noted.

ACTION REQUESTED:
  [X] Approved
  [ ] Approved as Noted
  [ ] Revise and Resubmit
  [ ] Rejected

DISTRIBUTION:
  - Architect of Record (2 copies)
  - Structural Engineer of Record (1 copy)
  - Project File (1 copy)
  - Fabricator (1 copy, returned after review)

Prepared by: A. Yilmaz, PE — Project Engineer, Koc Insaat Ltd.
```

Notice the structure: the transmittal identifies the **project and contract** (traceability), references the **exact spec section** (so the reviewer knows what to check against), **itemizes every enclosure** with quantities (nothing is ambiguous), includes the **contractor's certification** (confirming someone actually reviewed the content before submission), and specifies the **action requested** and **distribution list** (so the routing is clear). This is the submittal equivalent of the strong RFI: every field serves a purpose, and nothing is left for the reviewer to guess.

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
| **Use examples** (multishot prompting) | Show the model what good output looks like | Providing a sample submittal for reference |
| **Let Claude think** (chain of thought) | Ask it to reason step-by-step before answering | Requiring a contractor to show calculations, not just the answer |
| **Use XML tags** | Organize your prompt into labeled sections | Using CSI MasterFormat divisions to organize specs |
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

### 3.4 Bad Prompt vs. Good Prompt: The Difference in Action

Rules are abstract until you see them applied. Let us take the same rebar issue from section 1.4 and watch what happens with two very different prompts.

**Vague prompt:**

```
Write an RFI about a rebar issue.
```

**What the model produces:**

```
Dear Sir/Madam,

We would like to request information regarding a rebar issue on the
project. There appears to be a discrepancy in the rebar specifications.
Please clarify the correct rebar size, spacing, and placement.

Thank you for your attention to this matter.

Sincerely,
[Your Name]
```

This output is useless. No project name, no drawing reference, no spec section, no specific question, no suggested resolution, no deadline. You could not send this. The model is not at fault -- it produced exactly what was asked for: a generic RFI about a generic rebar issue.

**Structured prompt (applying all 5 rules):**

```
You are a project engineer on the Kadikoy Mixed-Use Development
($45M, Contract C-2026-0341). [Rule 1: Role]

Reference documents:
- Drawing S-201, Detail 4: shows #5 rebar at 12" o.c. for pile cap
  at Grid B-3
- Spec Section 03 30 00, Para 3.2.A: requires #5 at 8" o.c. for pile
  caps exceeding 1.2 m depth
- The pile cap at Grid B-3 is 1.5 m deep [Rule 2: Reference documents]

Draft a single RFI asking which rebar spacing governs -- the drawing
or the spec. [Rule 3: One task]

Use the same structure as this example:
[Context → Conflict → Question → Suggested Resolution → Impact]
[Rule 4: Show an example]

Format: formal RFI, under 200 words, with fields for RFI Number,
Date, Subject, Question, Suggested Resolution, and Impact.
[Rule 5: Output format]

The suggested resolution is to install per the spec (more stringent).
Rebar fabrication for Zone B starts Feb 24; response needed by Feb 19
to avoid a 3-day critical-path delay.
```

**What the model produces:**

```
RFI Number: RFI-[TBD]
Date:       February 12, 2026
To:         Structural Engineer of Record
Subject:    Drawing S-201 Detail 4 vs. Spec 03 30 00 Para 3.2.A --
            Rebar Spacing at Grid B-3 Pile Cap

Drawing S-201, Detail 4 indicates #5 rebar at 12" o.c. for the pile
cap at Grid B-3. Specification Section 03 30 00, Paragraph 3.2.A
requires #5 at 8" o.c. for pile caps exceeding 1.2 m in depth. The
pile cap at Grid B-3 is 1.5 m deep.

Question: Which rebar spacing governs -- the drawing (12" o.c.) or
the specification (8" o.c.)?

Suggested Resolution: Install #5 rebar at 8" o.c. per the
specification, as it is the more stringent requirement.

Impact: Rebar fabrication for Zone B is scheduled to begin February 24.
A response is requested by February 19 to avoid a 3-day delay to the
critical path.
```

This output is near-send-ready. It matches the anatomy from section 1.4: context, conflict, single question, suggested resolution, and schedule impact with dates. A project engineer would review it, assign the RFI number, and submit.

> **Key Insight:** Same model, same capability -- the only difference is the quality of the input. A vague prompt produces vague output. A structured prompt produces a structured document. This is exactly the same principle as writing a strong RFI: garbage in, garbage out.

---

## Part IV: Building Your Prompt Template Library
**(~15 min lecture + demo)**

### 4.1 Why Templates Matter

Using standardized templates for common documents reduces errors and ensures consistency. Research by the UK's Get It Right Initiative (GIRI) found that errors in construction cost the UK industry **GBP 10-25 billion per year**, with their Error Reduction Framework -- a structured approach combining root cause analysis, standardized processes, and organizational culture change -- identified as a key mitigation strategy.

The same principle applies to AI prompts: a well-designed template with clear structure, defined fields, and consistent formatting will produce reliable output every time -- just like a standard RFI form produces better RFIs than free-form emails.

*Source: [GIRI: Get It Right Initiative](https://getitright.uk.com/); [zipBoard: 9 Common Construction Document Errors and How to Avoid Them](https://zipboard.co/blog/aec/common-errors-to-look-out-for-during-construction-document-reviews/).*

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

### What's Next -- Week 4 Preview

This week we focused on **written** communication (Strand B): RFIs, submittals, and prompt templates. Next week we shift to **verbal** communication (Strand A): presentations and public speaking.

- **The challenge:** Estimates of public speaking anxiety range from ~25-40% for significant fear (Gallup, Chapman University surveys) to 75% when including any degree of nervousness. For engineers -- who often default to data-heavy, text-dense slides -- the gap between technical competence and presentation skill is a competitive differentiator.
- **What we will cover:** The **Hook-Problem-Solution-Ask** framework for structuring a persuasive presentation, evidence-based principles for slide design (signal-to-noise ratio, assertion-evidence format), and practical techniques for managing presentation anxiety.
- **Lightning talk assignment:** You will deliver a **3-minute lightning talk** on a construction scenario -- a schedule delay, a change order dispute, a safety incident, or a constructability concern. Start thinking about your topic now.

> **Reminder:** Your **M1 -- Prompt Template Library** (3 templates + test outputs) is due before the Week 4 session. Make sure your `project/templates/` directory is committed and pushed.

---

### Further Reading

- Navigant Construction Forum (2013). "Impact & Control of RFIs on Construction Projects." [CMAA hosted PDF](https://www.cmaanet.org/sites/default/files/resource/Impact%20&%20Control%20of%20RFIs%20on%20Construction%20Projects.pdf)
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
