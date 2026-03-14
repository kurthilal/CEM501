## M0 — First LLM Calls from CLI

### Call 1
**Prompt**

```bash
claude "Draft an RFI for an unclear foundation drain detail on Drawing S-201 for the Riverside Residential Project. Make it professional and concise."
```

**Output**

```text
Subject: [Riverside Residential] RFI-001: Clarification on Foundation Drain Detail on Drawing S-201

Dear Ms. Kaya,

We are reviewing Drawing S-201 for the Riverside Residential Project and would like to request clarification on the foundation drain detail at Grid B-3.

The current detail does not clearly indicate:
- The exact elevation of the perforated drain pipe relative to the footing
- The specified pipe diameter and material
- The required filter fabric type and extent around the drain

Please confirm the intended pipe elevation, size, and material, as well as the required filter fabric specification, so that we can proceed with installation in accordance with the design intent.

We appreciate your timely response so we can avoid any impact to the foundation schedule.

Best regards,
Hilal Kurt Irfanoglu
Site Engineer | Poder
Phone: +90 539 207 54 45
Email: info@yalıtım.com
```

---

### Call 2
**Prompt**

```bash
claude "Write a professional email from the project manager to the general contractor requesting an updated CPM schedule for the Kadikoy Mixed-Use Project. Tone: firm but collaborative."
```

**Output**

```text
Subject: [Kadikoy Mixed-Use] Request for Updated CPM Schedule

Dear Mr. Demir,

I hope you are well. As we approach the end of the current reporting period for the Kadikoy Mixed-Use Project, we require an updated CPM schedule to accurately assess progress and forecast upcoming critical activities.

Please submit a revised, statused CPM schedule in native and PDF formats, reflecting all approved change orders and current activity progress, including:
- Actual start and finish dates for activities completed this period
- Updated remaining durations for ongoing activities
- Any changes to critical path activities and total float values

Kindly provide the updated schedule no later than Friday, March 21, 2026, so that we can incorporate it into the monthly progress report and coordinate upcoming work with key stakeholders.

Thank you in advance for your cooperation.

Best regards,
Hilal Kurt Irfanoglu
Project Manager | Poder
Phone: +90 539 207 54 45
Email: info@yalıtım.com
```

---

### Call 3
**Prompt**

```bash
claude "Summarize the key elements of a proper delay notice under a standard AIA construction contract. Output as a short, clear bullet list for a civil engineering student."
```

**Output**

```text
Key elements of a proper delay notice under a typical AIA construction contract include:

- Project identification: State the project name, contract number, and parties involved.
- Clear description of the delaying event: Explain what happened (e.g., extreme weather, late design decision, unforeseen site condition).
- Dates and duration: Specify when the delay started, how long it has lasted, and the estimated total impact in days.
- Contract references: Cite the relevant contract clauses (for example, the article that covers excusable delays or time extensions).
- Impact on critical path: Describe which activities on the CPM schedule are affected and how the overall completion date may be impacted.
- Mitigation efforts: Briefly note any reasonable steps the contractor has taken to reduce or avoid the delay.
- Formal request: Clearly state the time extension or other relief being requested.
- Deadline and documentation: Indicate any attached supporting documents (weather reports, correspondence, photos) and request a written determination by a specific date.
```

---

### Reflection (3–5 sentences)

Working with the LLM from the CLI, I noticed that the quality of the output depended heavily on how specific my prompts were. When I included project names, drawing numbers, and tone instructions, the model produced emails that looked close to real CEM correspondence. However, I also saw that it sometimes invented details, like generic names or assumptions about schedule data, so I would need to verify all factual information before sending anything on an actual project. Overall, the tool was fast and helpful for drafting, but it still requires human judgment to check accuracy, add project-specific details, and make sure the message aligns with the contract.

