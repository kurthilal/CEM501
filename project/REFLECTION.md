# REFLECTION.md

**CEM501 — Semester Project**  
**Poder — Internal AI Communication Agent**

---

When I first proposed building an internal AI agent for Poder as our CEM501 project, I was not approaching it as an academic exercise. I was approaching it as a founder who was genuinely drowning. At the time, I was managing investor follow-up emails, client messages from our Dursunköy pilot, Telegram threads from the field, LinkedIn drafts for Podercast, and an accelerator application pipeline — all simultaneously, all manually. The project gave me a structured reason to do something I had been putting off: actually build the tool I needed.

The first technical decision that shaped everything else was the choice to run the agent locally. I made this call early, and I would make it again. Our clients are construction companies; they ask hard questions about where their data goes. A localhost-only deployment is not a limitation in a B2B construction context, it is a trust signal. Designing around this constraint forced us to think carefully about what the agent actually needed to do versus what would have been technically impressive but operationally irrelevant.

The modular architecture was not planned from the start — it emerged from necessity. We built the Inbox Preview module first because email triage was the most immediate pain point. Once that worked independently, it became the template for everything else: Calendar, CRM, Social Media Drafter, Telegram. Each module could be tested and demonstrated in isolation, which turned out to matter enormously during development. When something broke — and things broke regularly — the failure was contained. I learned that modularity is not just a software engineering principle; it is a project management strategy.

The hardest problem was not technical. It was the human-in-the-loop design. My initial instinct was to automate as much as possible: classify the email, draft the reply, send it. That instinct was wrong. The moment I imagined the agent sending an email to Emlak Konut without my review, I understood the real constraint: the agent's output quality is not the issue. The issue is that I need to own every communication that leaves my name. The system had to make it frictionless for me to review and approve, not frictionless for the agent to act without me. That reframing changed how we designed every module.

Working with Claude API directly, rather than using a pre-built wrapper, also taught me something about how language models fail. The classification system (URGENT / ACTION / FYI / ARCHIVE) works well on most emails, but it fails gracefully on ambiguous ones. I stopped trying to make it perfect and started designing the interface so that misclassification was easy to catch and correct. Reliable enough plus easy to override turned out to be more useful than accurate but opaque.

What surprised me most was how quickly the agent became part of my actual workflow rather than remaining a demo artifact. Within two weeks of completing the Inbox module, I was using it daily. That feedback loop — building something, using it, noticing what was wrong, fixing it — accelerated my understanding of what AI agents are genuinely useful for far more than any paper or lecture could have.

The lesson I carry forward: an AI agent earns its place not by doing impressive things, but by reliably removing the smallest, most repetitive frictions from a workflow. Start there, and everything else follows.
