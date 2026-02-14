# CEM501: Communication Skills for CEM
## Week 14: Final Demos -- All Strands Converge
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Understand why the technical demo is a career skill, not just a course requirement
- Structure a compelling 7-minute demonstration with a clear narrative arc
- Prepare a live demo survival plan with backups, test data, and rehearsal protocols
- Handle Q&A sessions with professionalism, including techniques for difficult questions
- Produce a reflective document (REFLECTION.md) grounded in honest self-evaluation
- Deliver all final submission artifacts: code, ARCHITECTURE.md, REFLECTION.md, agent.log

---

## Part I: The Art of the Technical Demo

This is the last week. Three strands -- verbal communication, written communication, and AI-augmented development -- converge into a single 7-minute window. Everything you have built, everything you have learned about professional writing in CEM, everything you have discovered about working with AI coding tools: it all comes together on demo day.

But this is not just about a grade. This is about a skill you will use for the rest of your career.

---

### 1.1 Why Demos Matter Beyond the Classroom

In the B2B software world, a Bain & Company survey found that nearly **75% of buyers base their final purchasing decision on the product demo** -- not on the sales pitch, not on the brochure, but on watching the product actually work. The demo is where decisions are made.

This translates directly to construction engineering and management. In your career, you will:

- **Demo project status** to owners and investors at monthly progress meetings
- **Present claims and disputes** to arbitrators (where the average U.S. construction dispute is worth $60.1 million, per Arcadis 2025)
- **Pitch proposals** to clients, competing against other firms for contracts worth millions
- **Show software tools** to your team to justify technology adoption

In every one of these situations, the ability to show something working -- to make the abstract concrete, the complex simple -- is what separates the professional who gets the contract from the one who does not.

> **Key Insight:** The MIT CEE Communication Lab puts it this way: the goal of a technical demonstration is to "leave your audience excited about your technology and show them something memorable that will stick with them after they've left the demo site." Not impressed by your code. Not confused by your architecture. *Excited* and *remembering*.

*Source: [MIT CEE Communication Lab -- Technical Demonstrations](https://mitcommlab.mit.edu/cee/commkit/technical-demonstrations/)*

---

### 1.2 What Makes Demos Fail

Research on software demo effectiveness identifies a consistent pattern of mistakes. Problem-solution demos that focus on specific pain points convert **37% better** than feature tours, according to industry analysis. Yet most first-time presenters default to a feature tour.

Here are the most common failures:

**Showing configuration instead of value.** You open your terminal and start explaining your folder structure, your `.env` file, your database schema. The audience loses interest by the third file. Nobody cares about your configuration -- they care about what your agent *does*.

**No story arc.** You jump straight into "and then I click this button" without explaining *why* anyone should care. Y Combinator's guide to demo day pitches emphasizes: "work on the narrative first and leverage your data to tell a story about what you have achieved." Even the most technical demo needs a beginning (the problem), a middle (the solution), and an end (the impact).

**No backup plan.** Live demos fail. They fail in front of investors, they fail in front of CEOs, they fail at Apple keynotes. The question is not whether something will go wrong -- it is whether you have prepared for it. More on this in Part III.

**Reading code on screen.** Your audience is not a compiler. If you are reading lines of Python to a room of CEM graduate students, you have already lost them. Show what the code *does*, not what the code *says*.

*Sources: [Y Combinator -- Guide to Demo Day Pitches](https://www.ycombinator.com/blog/guide-to-demo-day-pitches/); [Supademo -- Software Demo Presentation Guide](https://supademo.com/blog/software-demo-presentation)*

---

## Part II: Structuring Your 7-Minute Demo

Y Combinator coaches hundreds of founders on demo day presentations every year. Their core advice is deceptively simple: "Practice. Make sure you know your story so well that it comes out as smoothly as a Steve Jobs pitch." But structure is what makes practice productive.

Follow this minute-by-minute guide:

---

### Minute 0-1: The Problem Statement

Open with the *problem*, not the solution. Be specific.

| Weak Opening | Strong Opening |
|---|---|
| "I built an AI email agent." | "On a 15-subcontractor hospital project, the PM spends 3 hours per day managing RFI follow-ups across email, WhatsApp, and phone. My agent cuts that to 15 minutes." |
| "This tool helps with communication." | "Last month, a delay notice was sent to the wrong subcontractor because the PM copied the wrong email address from a spreadsheet. My agent prevents that." |

One slide maximum. State the problem, quantify it if you can, and make the audience nod in recognition.

---

### Minute 1-2: The Solution Overview

Show your architecture diagram -- one slide. Name your components in plain language. Explain the flow in one or two sentences.

Example: "My agent has three parts. An email reader that connects to Gmail, a classifier that sorts incoming messages into RFIs, submittals, and general correspondence, and a drafter that generates context-aware replies using the project's RFI log as reference."

Do not explain every technology choice here. The Q&A is for that. This is the 30-second flyover that orients your audience before the live demo.

---

### Minutes 2-5: The Live Demo

This is the core. Show **2-3 scenarios** running live. Narrate what the agent is doing and why at each step.

**Scenario design matters.** Choose scenarios that showcase different capabilities:
- Scenario 1: An incoming RFI email gets classified, logged, and a draft response is generated
- Scenario 2: A delay notice is drafted with the correct contractual language and sent to the right recipient
- Scenario 3: The agent handles an edge case -- a message in a different language, a missing contact, a conflicting instruction

Narrate as you go: "Watch what happens when this email arrives -- the agent recognizes it as an RFI because of the subject line pattern and the sender's role in the contact database. Now it pulls the relevant specification section and drafts a response."

> **Key Insight:** Including realistic scenarios rather than abstract test data increases audience understanding by **65%** over generic examples, according to software demo research. Use real project names, real subcontractor roles, real document types. "Bogazici Library Renovation" is better than "Test Project 1."

*Source: [Storylane -- How to Prepare a Great Software Demo Presentation](https://www.storylane.io/blog/how-to-prepare-a-great-software-demo-presentation)*

---

### Minute 5-6: Lessons Learned

This is where you show depth. Share one technical lesson and one communication lesson.

- **Technical:** "I learned that LLM-generated emails need guardrails. Without them, my agent once drafted a delay notice that was technically accurate but so blunt it would have damaged the client relationship. I added a tone-check step."
- **Communication:** "Building this agent made me realize how much implicit knowledge goes into a professional email. Things I never thought about -- greeting conventions, when to CC someone, how to phrase a request vs. a demand -- became explicit rules I had to encode."

Be honest about what did not work. Honesty signals mastery, not weakness.

---

### Minute 6-7: What's Next

If you had four more weeks, what would you add? This demonstrates that you understand the system's limitations and see a path forward.

Examples: "I would add Slack integration so the agent can monitor both email and messaging channels." "I would build a dashboard that tracks RFI response times across the project." "I would add multi-language support for projects with international teams."

End with a clear closing statement, not a trailing "so yeah, that's it." Try: "This agent saves a PM two hours per day on email management. That is ten hours per week returned to actual project management. Thank you."

---

## Part III: Live Demo Survival Guide

Live demos fail. This is not pessimism -- it is engineering reality. The question is whether you have prepared for failure.

---

### 3.1 What Can Go Wrong

| Failure Mode | Likelihood | Impact |
|---|---|---|
| Wi-Fi drops or is slow | High (classroom networks are unreliable) | Agent cannot reach API |
| API rate limit or timeout | Medium | LLM call hangs for 30+ seconds |
| Database is empty or corrupted | Medium (if you reset it during testing) | No data to demo |
| Typo in live command | High (nerves cause mistakes) | Command fails, audience sees error |
| Projector resolution mismatch | Medium | Text is unreadable |
| Laptop runs out of battery | Low but catastrophic | Demo ends abruptly |

---

### 3.2 The Preparation Protocol

**1. Pre-record a backup video.** Run your complete demo flow on your own machine and record it with screen capture. If the live demo fails entirely, you play the video and narrate over it. You will lose some points for not running live, but you will lose far more points for standing in silence while your terminal throws errors.

**2. Have test data ready and verified.** Populate your database the night before. Do not use placeholder data like "test123" or "John Doe" -- use realistic CEM data: actual project names, realistic email content, proper subcontractor roles. Verify it works by running the full demo flow once with this data.

**3. Practice the exact flow a minimum of 5 times.** Presentation research consistently recommends a minimum of 3-5 full rehearsals, with experts suggesting even more for high-stakes presentations. Carmine Gallo, writing in *Inc.*, recommends practicing important presentations at least 10 times. For a 7-minute demo, even 5 full run-throughs is only 35 minutes of your time -- there is no excuse not to do this.

**4. Practice on the same hardware you will use.** As the MIT CEE Communication Lab advises: "Invest significant effort in achieving consistent performance before the demonstration date." Run on the same laptop, same operating system, same terminal. Do not switch machines on demo day.

**5. Increase font size and clean your screen.** Minimum 16pt in terminal, 24pt on slides. Close every application except what you need. The back row matters.

**6. Bring your charger and an adapter.** HDMI and USB-C adapters are available in the classroom, but do not rely on this. Bring your own.

> **Key Insight:** The best way to handle a technical failure during a demo is to maintain composure. Acknowledge the issue briefly ("It looks like the API is taking longer than expected -- let me switch to my backup recording"), pivot to your backup, and continue narrating. Composure under pressure is itself part of the evaluation. A graceful recovery demonstrates more professionalism than a flawless demo.

*Sources: [MIT CEE Communication Lab -- Technical Demonstrations](https://mitcommlab.mit.edu/cee/commkit/technical-demonstrations/); [Inc. -- Why You Should Practice Your Presentation 10 Times](https://www.inc.com/carmine-gallo/why-you-should-practice-your-presentation-10-times-before-taking-stage.html)*

---

## Part IV: Handling Q&A Like a Professional

After your 7-minute demo, you will face 3 minutes of questions from the instructor and your classmates. This is not an interrogation -- it is a conversation about your work. But it requires preparation.

---

### 4.1 Three Types of Questions to Expect

**Technical Questions**
"Why did you use SQLite instead of PostgreSQL?" "How does your agent handle API rate limits?" "What happens if the email has an attachment?"

These test whether you understand your own design decisions. Know *why* you made each choice, not just *what* you chose.

**Conceptual Questions**
"How would this scale to a 200-person project?" "What happens if the LLM gives bad advice and the PM sends it without reviewing?" "Could this replace a project coordinator?"

These test whether you can think beyond your implementation. They are about vision, limitations, and professional judgment.

**Communication Questions**
"How did building this agent change how you think about professional email?" "What cross-cultural communication scenario was hardest to handle?" "What did you learn about tone that surprised you?"

These connect your technical work back to the course's core mission. This is a communication skills course -- the agent is the vehicle, not the destination.

---

### 4.2 How to Handle "I Don't Know"

Saying "I don't know" is not a failure. Saying "I don't know" *well* is a professional skill.

**Strong responses to difficult questions:**
- "I haven't tested that scenario, but my hypothesis is that the classifier would struggle because it relies on subject-line patterns. I would need to add content analysis to handle it."
- "That is a great question. I am not sure about the specific technical answer, but here is how I would investigate it."
- "Honestly, that was a limitation I identified but did not have time to address. It is first on my list of improvements."

**Weak responses:**
- "I don't know." (and silence)
- "That's not really relevant to what I built."
- Guessing confidently and getting it wrong

---

### 4.3 The Bridge Technique

Sometimes you will receive a question that is tangential or that you are not prepared for. The **ABC bridge technique**, widely used in professional communications, helps you handle this gracefully:

1. **Acknowledge** the question: "That is an interesting point about multi-language support..."
2. **Bridge** to your prepared territory: "...and while I did not implement that feature, it connects to something I did work on..."
3. **Communicate** your key message: "...which is the tone-adaptation module that adjusts formality based on the recipient's role."

Use this sparingly. If you bridge every question, you will sound evasive. Reserve it for genuinely off-topic questions.

> **Key Insight:** Repeat or paraphrase every question before answering. This ensures the entire audience hears it, gives you a few seconds to think, and confirms you understood the question correctly. This is standard practice in professional presentations and conference Q&A sessions.

*Source: [The Vocate -- The Bridging Technique for Public Speaking (ABC Method)](https://www.vocate.work/articles/bridging-technique-for-public-speaking/)*

---

## Part V: The Reflection Document

After your demo, you will write a REFLECTION.md document. This is not a formality. It is, according to decades of educational research, one of the most effective tools for consolidating learning.

---

### 5.1 Why Reflective Writing Matters

A meta-analysis of reflective interventions in higher education found a **positive and significant medium-sized effect (g = 0.56)** on learning outcomes, based on 23 studies with over 2,000 participants. That is a meaningful effect -- comparable to the difference between a B and a B+ in many grading systems.

Research published in *Frontiers in Psychology* found that reflective journal writing improves students' **flexibility, adaptability, planning ability, and self-regulation of learning** -- precisely the skills that matter in professional practice. Reflective writing does not just document what happened; it transforms experience into transferable knowledge.

A separate meta-analysis found a **significant positive relationship between reflective thinking and academic achievement** with a medium effect size (r = 0.527), confirming that students who reflect systematically perform better across subjects and disciplines.

In professional contexts, reflective practice is how engineers, doctors, and project managers learn from experience without having to repeat mistakes. The REFLECTION.md you write this week is practice for a habit that will serve you for decades.

> **Key Insight:** The three-fold benefit of reflective writing, as identified by education researchers: it improves program-level assessment, deepens individual student learning, and engages faculty in professional development. When you write honestly about what worked and what failed, everyone benefits -- including future students who will read anonymized examples of your reflections.

*Sources: [Frontiers in Psychology -- Higher Education Students' Reflective Journal Writing and Lifelong Learning Skills (2021)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.707168/full); [ScienceDirect -- Can Reflective Interventions Improve Students' Academic Achievement? A Meta-Analysis (2023)](https://www.sciencedirect.com/science/article/abs/pii/S1871187123001414); [ERIES Journal -- Meta-Analysis Study: The Relationship Between Reflective Thinking and Learning Achievement](https://www.eriesjournal.com/index.php/eries/article/view/735)*

---

### 5.2 REFLECTION.md Structure

**Length:** 500-800 words. Quality over quantity. Every sentence should carry weight.

```markdown
# REFLECTION.md

## What I Built
One paragraph. What does your agent do? Who is it for?
Be specific: "An email agent for CEM project managers that reads
incoming correspondence, classifies it by document type, and drafts
context-aware responses using project-specific data."

## What I Learned About Communication
How did building an automated communication tool change your
understanding of professional communication in CEM? Be specific.
What rules did you have to make explicit that you previously
followed without thinking? What surprised you about tone, formality,
or cross-cultural conventions?

## What I Learned About AI-Assisted Development
This is specific to working with Claude Code, Cursor, or whichever
AI coding tools you used. What was the experience of directing an
AI agent to write code? Where did it excel? Where did it fail?
What did you learn about giving clear instructions to an AI --
and how does that parallel giving clear instructions to a team member?

## What I Would Do Differently
If you started over, what would you change in your approach,
your architecture, or your time management? Be honest and specific.
"I would start the database design earlier" is better than
"I would manage my time better."

## Connection to Professional Practice
How will you use what you learned -- communication skills,
not just code -- in your career? Be concrete.
```

**What makes a strong reflection:**
- Specific examples, not generalizations
- Honest acknowledgment of failures and struggles
- Connection between the technical work and communication insights
- Evidence of growth -- how your thinking changed from Week 1 to Week 14

**What makes a weak reflection:**
- Vague praise ("this was a great course")
- Pure technical description without personal insight
- Blaming tools or time constraints without self-reflection
- Fewer than 500 words (suggests surface-level engagement)

---

## Part VI: Demo Day Logistics

---

### 6.1 Schedule Format

**Date:** Week 14 class sessions (both slots if needed)

| Time | Activity | Duration |
|---|---|---|
| 0:00 - 0:07 | Student A: Demo | 7 min |
| 0:07 - 0:10 | Student A: Q&A | 3 min |
| 0:10 - 0:12 | Transition / Setup | 2 min |
| 0:12 - 0:19 | Student B: Demo | 7 min |
| 0:19 - 0:22 | Student B: Q&A | 3 min |
| 0:22 - 0:24 | Transition / Setup | 2 min |
| ... | ... | ... |

- **Demo order** will be posted by end of Week 13 (randomized)
- Arrive **10 minutes before your slot** to set up and test the projector connection
- Bring your own laptop with your agent ready to run
- HDMI and USB-C adapters are available in the classroom, but bring your own if possible

---

### 6.2 Setup Checklist

Complete this checklist **the evening before** your demo:

- [ ] Agent runs end-to-end without manual intervention for at least one complete scenario
- [ ] Database is populated with realistic CEM data (project names, subcontractor contacts, email content)
- [ ] Terminal font size set to 16pt minimum; unnecessary windows and notifications closed
- [ ] Architecture diagram printed or loaded on first slide
- [ ] Backup video recorded and saved locally (not just in cloud)
- [ ] Backup screenshots saved in a separate folder in case video also fails
- [ ] REFLECTION.md drafted (finalize after demo based on Q&A insights)
- [ ] Timed rehearsal completed at least 5 times (all under 7 minutes)
- [ ] Laptop charger packed
- [ ] Adapter cable packed (HDMI/USB-C)
- [ ] Phone set to Do Not Disturb

---

### 6.3 Peer Feedback Requirements

Research consistently shows that peer assessment improves learning. A meta-analysis by Double et al. (2020), published in *Educational Psychology Review*, examined 54 studies and found that peer assessment has a **positive effect on academic performance (g = 0.31)** compared to no-assessment controls. Importantly, the act of *giving* feedback benefits learning as much as *receiving* it -- the reviewer develops critical evaluation skills that transfer to self-assessment.

**Your peer feedback responsibilities:**

- All students **attend all demos** (attendance taken)
- Each student submits **brief peer feedback** (3-5 sentences) for **at least 5 classmates**
- Submit via the course portal by **end of the last demo session**
- Peer feedback is **ungraded but required** for course completion

**What to include in peer feedback:**
1. One thing the demo did well (be specific: "the scenario with the misdirected RFI was compelling because...")
2. One suggestion for improvement (constructive, not critical: "the architecture slide could have benefited from...")
3. One question you would have asked if time allowed

> **Key Insight:** Research on peer assessment design shows that formative peer feedback -- where students can apply the feedback to future work -- is most effective when combined with clear criteria and multiple iterations. The rubric (see `rubrics/final_demo_rubric.md`) gives you the criteria. Your feedback gives your classmates one final opportunity to learn from an outside perspective.

*Source: [Double, K.S. et al. (2020). "The Impact of Peer Assessment on Academic Performance: A Meta-analysis of Control Group Studies." Educational Psychology Review.](https://link.springer.com/article/10.1007/s10648-019-09510-3)*

---

### 6.4 Evaluation Rubric

Your demo will be assessed using the rubric in `rubrics/final_demo_rubric.md`. The five categories and their weights:

| Category | Weight | What It Measures |
|---|---|---|
| System Functionality | 25% | Does the agent work? Does it handle edge cases? |
| Architecture & Design | 20% | Is the code modular, maintainable, well-documented? |
| Live Demo Quality | 20% | Is the demo rehearsed, logical, and professionally presented? |
| Communication & Explanation | 20% | Can you explain *what* and *why* clearly? |
| Q&A Handling | 15% | Can you think on your feet and demonstrate deep understanding? |

Research on rubric-based assessment in higher education confirms that rubrics improve both **consistency and fairness** -- they reduce variation in grades across evaluators and make expectations transparent. As one review noted, rubrics are most effective when students see the criteria *before* the assessment, which is why this rubric has been available since the start of the semester.

*Source: [Brookhart, S.M. & Chen, F. (2020). "Beyond Fairness and Consistency in Grading: The Role of Rubrics in Higher Education." Springer.](https://link.springer.com/chapter/10.1007/978-981-15-1628-3_3)*

**Bonus points (up to +0.2):** Integration of additional channels (Telegram, Slack), particularly creative features, exceptional error handling or logging.

---

## Milestone M9: Final Submission

**Due:** 48 hours after your demo slot

### Deliverables

| Artifact | Requirements |
|---|---|
| **Complete code repository** | Clean, with a working `README.md` that includes setup instructions. A new person should be able to clone your repo and run the agent. |
| **ARCHITECTURE.md** | System diagram, component descriptions, design decisions. Updated from M8 to reflect final state. |
| **REFLECTION.md** | 500-800 words following the structure in Section 5.2 above. |
| **agent.log** | Final log file showing a realistic multi-step workflow. This should demonstrate your agent handling at least 3 different email scenarios. |

### Submission Method

Push all deliverables to your GitHub repository and submit the repository link via the course portal. Ensure your last commit is timestamped before the deadline.

### A Note on Academic Integrity

Your REFLECTION.md should be written by you, not by an AI. The entire point of this document is your authentic voice reflecting on your experience. I will read these carefully. AI-generated reflections are obvious -- they lack the specificity, the struggle, and the honest self-assessment that characterize genuine learning. This is the one document in the course where the human voice is the whole point.

---

### Closing: What You Have Built

Fourteen weeks ago, many of you had never opened a terminal. You did not know what Git was. You had never written a line of Python -- or any code at all. And yet here you are, about to demo a working AI-powered communication agent that you designed, directed, and refined over an entire semester.

But the agent is not the point. The point is what you learned *through* the agent:

- That professional communication has rules, and those rules can be articulated
- That giving clear instructions -- to an AI, to a subcontractor, to a team member -- is the same fundamental skill
- That technology amplifies communication but does not replace the judgment behind it
- That the difference between a good email and a bad one can be worth millions of dollars in construction

Go out there and demo well. Not perfectly -- well. Show us the problem, show us the solution, and tell us what you learned.

---

### Further Reading

- Reynolds, G. -- *Presentation Zen* (Chapters 4-6 on story structure)
- Alley, M. -- *The Craft of Scientific Presentations* -- the assertion-evidence approach
- Duarte, N. -- *slide:ology* -- visual design principles for technical presentations
- MIT CEE Communication Lab -- [Technical Demonstrations CommKit](https://mitcommlab.mit.edu/cee/commkit/technical-demonstrations/)
- Y Combinator -- [A Guide to Demo Day Presentations](https://www.ycombinator.com/blog/guide-to-demo-day-pitches/)

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
