# CEM501: Communication Skills for CEM
## Week 11: Multi-Channel Integration (Strand C)
**Spring 2026 | Dr. Eyuphan Koc | Bogazici University**

---

### Learning Objectives

- Explain why construction teams need multi-channel communication and quantify the cost of channel fragmentation
- Map the messaging landscape in a typical CEM project (who uses what, and why)
- Apply the channel abstraction pattern so your agent can support new channels without rewriting core logic
- Set up a Telegram bot using BotFather and connect it to your agent pipeline
- Use Cursor / Claude Code to scaffold a new channel integration from scratch

---

## Part I: Why Multi-Channel Matters in CEM
**(~20 min lecture)**

### 1.1 The Fragmentation Reality

Here is a fact that will not surprise anyone who has worked on a construction site: no two stakeholders use the same communication tool. The superintendent texts photos on WhatsApp. The project manager logs RFIs in Procore. The owner's rep insists on email. The design consultant marks up drawings in Bluebeam. The safety officer files reports in a dedicated app.

This is not a technology problem — it is a people problem. Each stakeholder gravitates toward the tool that fits their workflow, their device, and their comfort level. The result is **channel fragmentation**: critical project information is scattered across five, six, or more platforms, and no single person has a complete picture.

Research from the Harvard Business Review quantifies this at the individual level: workers toggle between different applications and websites roughly **1,200 times per day**, spending nearly **four hours per week** just reorienting themselves after each switch — about 9% of their total work time.

*Source: Rogelberg, S. et al. (2022). ["How Much Time and Energy Do We Waste Toggling Between Applications?"](https://hbr.org/2022/08/how-much-time-and-energy-do-we-waste-toggling-between-applications) Harvard Business Review.*

At the organizational level, Haiilo's research on digital workplace fatigue found that the average employee uses **35+ different digital tools** daily. And 91% of enterprises now use **two or more chat platforms** simultaneously — not because they planned to, but because different teams adopted different tools organically.

*Sources: [Haiilo (2024). "Digital Fatigue: How Fragmented Tools Are Hurting Your Team."](https://blog.haiilo.com/blog/digital-fatigue-how-fragmented-tools-are-hurting-your-team/) [Mio (2024). "The State of Workplace Messaging."](https://www.m.io/blog/state-of-workplace-messaging)*

> **Key Insight:** Channel fragmentation is not a failure of discipline — it is a natural consequence of diverse teams with different needs. The solution is not to force everyone onto one platform (that never works). The solution is to build a bridge between platforms. That is what your agent will become this week.

---

### 1.2 The Construction-Specific Problem

Construction makes fragmentation worse than most industries for three reasons:

1. **The field-office divide.** Field crews work on mobile devices in dusty, noisy environments with unreliable connectivity. They need fast, lightweight tools — which is why WhatsApp dominates. According to a BauInfoConsult industry survey, **72% of construction professionals** use WhatsApp for brief business exchanges with colleagues and subcontractors. A JBKnowledge ConTech Report found that **92% of construction workers** use their smartphone every day at work — and most of these are personal devices, not company-issued.

2. **Subcontractor diversity.** A typical commercial project involves 20-50 subcontractors, each with their own communication preferences and systems. You cannot dictate what tools a steel erector or an electrical sub uses internally.

3. **Contractual formality requirements.** While field communication happens informally on messaging apps, contract-relevant communication (RFIs, change orders, delay notices) must be documented in formal systems. The gap between where conversations happen and where they need to be recorded is where information gets lost.

*Sources: [BauInfoConsult / 123onsite (2024). "WhatsApp on the Construction Site."](https://123onsite.com/?bau-blog=whatsapp-on-the-construction-site-better-to-chat-in-compliance-with-the-law-and-documentation) [MindForge (2024). "Smartphone App Usage Among Construction Workers."](https://www.mindforgeapp.com/blog-posts/smartphone-app-usage-among-construction-workers-adoption-preferences-and-barriers)*

---

### 1.3 The Cost of Information Silos

When information is trapped in the wrong channel, projects pay the price:

- **Rework:** Recall from Week 1 — the FMI/PlanGrid study found that **48% of all rework** traces back to miscommunication and poor data access, costing **$31.3 billion annually** in the U.S. alone. Much of this starts with a message that never reached the right person because it was sent on the wrong platform.

- **Decision delays:** A ClickUp survey of 5,000 professionals found that **1 in 5 workers** spends more than **3 hours daily** just searching for files, messages, or context scattered across tools.

- **Productivity loss:** Research indicates that poor communication caused by fragmented tools reduces productivity by up to **40%**, and employees overwhelmed by fragmented digital tools are **twice as likely** to leave their jobs.

- **Per-team cost:** Industry analysis estimates that information silos cost construction firms up to **$450,000 annually per team** in lost efficiency and rework.

*Sources: [FMI & PlanGrid (2018). "Construction Disconnected."](https://www.prnewswire.com/news-releases/new-research-from-plangrid-and-fmi-identifies-factors-costing-the-construction-industry-more-than-177-billion-annually-300689826.html) [ClickUp Insights (2025). "The State of Workplace Communication."](https://clickup.com/blog/team-communication-survey/) [Haiilo (2024).](https://blog.haiilo.com/blog/digital-fatigue-how-fragmented-tools-are-hurting-your-team/) [CrewView (2024). "Breaking Down Silos."](https://www.crewview.com/blog/breaking-down-silos-how-centralized-construction-management-technology-reduces-costs-and-boosts)*

> **Key Insight:** A foreman texts a photo of a cracked beam to the superintendent on WhatsApp. That photo never reaches the structural engineer's email thread. Three days later, concrete is poured over the problem. Your agent, sitting at the center of multiple channels, can prevent exactly this scenario — routing field reports to the right people regardless of which app originated the message.

---

## Part II: The Channel Landscape
**(~15 min lecture)**

### 2.1 Who Uses What (and Why)

Here is a realistic map of communication tools on a large commercial construction project:

| Stakeholder | Primary Tool(s) | Why This Tool | Formality Level |
|-------------|-----------------|---------------|-----------------|
| Field crew / foremen | WhatsApp, phone calls | Mobile-first, works on spotty WiFi, already on their personal phone | Low (informal) |
| Superintendent | WhatsApp + Procore | Bridges field and office; needs both speed and documentation | Medium |
| Project manager | Email, MS Teams, Procore | Formal records, document control, owner-facing communication | High |
| Owner's representative | Email, formal letters | Contractual communication, audit trail | Very high |
| Design consultants | Email, Bluebeam, BIM 360 | Drawing markups, RFI responses, model coordination | High |
| Safety officer | Dedicated safety app, email | Incident reporting, compliance documentation | High |
| Subcontractor PMs | Email, WhatsApp, their own PM software | Varies widely — each sub has their own ecosystem | Mixed |

Notice the pattern: **formality increases as you move from field to office to contractual communication.** Your agent needs to understand this gradient — a WhatsApp message from a foreman requires a different response style than an email from the owner's counsel.

---

### 2.2 The Major Messaging Platforms at a Glance

**WhatsApp** — 3 billion monthly active users worldwide (as of late 2025). Over 130 billion messages sent daily. In construction, it is the de facto field communication tool in most markets outside the U.S., and increasingly within the U.S. as well. Its strength is ubiquity — every worker already has it. Its weakness: no project structure, no audit trail, messages buried in endless scrolling. WhatsApp Business (400+ million businesses) adds some structure but remains limited for construction workflows.

*Source: [Infobip (2025). "WhatsApp Statistics."](https://www.infobip.com/blog/whatsapp-statistics)*

**Microsoft Teams** — approximately 320 million monthly active users (2024), with around 220 million daily active users by mid-2025. Dominant in office environments, especially organizations already using Microsoft 365. Strong for video meetings, file sharing, and integration with SharePoint/OneDrive. Less adopted by field crews who find it heavy on mobile data and overly complex for quick messages.

*Source: [DemandSage (2026). "Microsoft Teams Statistics."](https://www.demandsage.com/microsoft-teams-statistics/)*

**Slack** — 42 million daily active users globally (early 2025), with users spending an average of 1 hour 42 minutes per day on the platform. Popular in tech-forward construction firms and design offices. Excellent channel organization and integrations. Less common among traditional field crews.

*Source: [SQ Magazine (2025). "Slack Statistics."](https://sqmagazine.co.uk/slack-statistics/)*

**Telegram** — surpassed 1 billion monthly active users in March 2025, with approximately 500 million daily active users. Open bot API makes it the easiest platform for building integrations (which is why we use it in this class). Strong in international markets and increasingly popular for automated notifications and bot-driven workflows.

*Source: [Backlinko (2026). "How Many People Use Telegram."](https://backlinko.com/telegram-users)*

> **Key Insight:** No single platform "wins" in construction. The question is not which tool to adopt — it is how to connect the tools your team already uses. That is the engineering problem we solve this week.

---

## Part III: The Channel Abstraction Pattern
**(~20 min lecture + live coding)**

### 3.1 The Travel Adapter Analogy

You are traveling from Istanbul to London to Tokyo. Each country has different electrical outlets. You have three options:

1. **Buy a new charger in every country.** (Rewrite your entire agent for each channel — terrible.)
2. **Only visit countries with your outlet type.** (Force everyone onto one platform — impossible in CEM.)
3. **Carry a universal travel adapter.** (Build one interface that adapts to any outlet — this is what we do.)

The channel abstraction pattern is your universal adapter. Your agent's core logic — classify the message, draft a response, send it — stays identical. Only the "plug shape" changes: how you receive messages and how you send them back.

In software design, this is a well-known concept called the **Adapter Pattern** (sometimes called the Strategy Pattern, depending on how you look at it). The adapter creates an intermediary layer that translates between your code and the external system. Your core logic never needs to know whether the message came from email, Telegram, or WhatsApp.

*Reference: [Adapter Pattern — Wikipedia.](https://en.wikipedia.org/wiki/Adapter_pattern) [Sourcemaking: Adapter Design Pattern.](https://sourcemaking.com/design_patterns/adapter)*

> **Key Insight:** This is the same principle as using a standard contract form (AIA A201, FIDIC Red Book). The interface is fixed — the clauses, the structure, the definitions. The project-specific details fill in the blanks. Abstraction is not just a software idea; it is how CEM already works.

---

### 3.2 The Pattern in Code

Here is the base class (the "universal adapter shape"):

```python
class Channel:
    """Base class — every communication channel must implement these methods."""

    def fetch_messages(self) -> list[dict]:
        """Pull new incoming messages from this channel."""
        raise NotImplementedError

    def send_message(self, recipient: str, text: str) -> bool:
        """Send a message through this channel. Returns True if successful."""
        raise NotImplementedError

    @property
    def channel_name(self) -> str:
        """Human-readable name of this channel (e.g., 'email', 'telegram')."""
        raise NotImplementedError
```

Now each channel fills in the details — but the "shape" stays the same:

```python
class EmailChannel(Channel):
    channel_name = "email"

    def fetch_messages(self):
        # Uses IMAP to connect to inbox and pull new emails
        ...

    def send_message(self, recipient, text):
        # Uses SMTP to send an email
        ...


class TelegramChannel(Channel):
    channel_name = "telegram"

    def fetch_messages(self):
        # Uses Telegram Bot API to get new messages
        ...

    def send_message(self, recipient, text):
        # Uses Telegram Bot API to send a reply
        ...
```

Your main agent loop stays unchanged regardless of how many channels you add:

```python
# This code works with 1 channel or 10 channels — no changes needed
active_channels = [EmailChannel(), TelegramChannel()]

for channel in active_channels:
    new_messages = channel.fetch_messages()
    for msg in new_messages:
        category = classifier.classify(msg["text"])
        draft = drafter.draft(msg["text"], category)
        channel.send_message(msg["sender"], draft)
        print(f"[{channel.channel_name}] Replied to {msg['sender']}: {category}")
```

Want to add Slack next month? Write a `SlackChannel` class with the same two methods, add it to `active_channels`, and you are done. No changes to the classifier, the drafter, or the main loop.

> **Key Insight:** The power of this pattern is that adding a new channel is a *local* change — you add one file, not modify ten files. In construction terms: if you design your rebar connections properly, you can swap in a different beam without redesigning the entire frame.

---

## Part IV: Setting Up a Telegram Bot
**(~15 min lecture + live demo)**

### 4.1 Why Telegram as Our Class Default

We use Telegram for the in-class demo because:

1. **Easiest bot setup** — five minutes with BotFather, no server required, no company approval needed.
2. **Free and open API** — no usage limits for basic bots, no credit card required.
3. **Polling mode** — your bot can pull messages without setting up a public server (unlike WhatsApp/Twilio, which requires webhooks and a public URL).
4. **1 billion users** — it is a real platform your stakeholders might actually use, not a toy.

You are free to use a different channel for your milestone (Slack, WhatsApp via Twilio, Discord) — but Telegram will get you up and running fastest.

---

### 4.2 How Telegram Bots Work

The architecture is simple:

```
User sends message in Telegram app
        │
        ▼
Telegram's servers receive and store the message
        │
        ▼
Your Python script asks Telegram: "Any new messages?" (polling)
        │
        ▼
Telegram returns the message to your script
        │
        ▼
Your script processes it (classify → draft) and sends a reply
        │
        ▼
Telegram delivers the reply to the user's app
```

Two key concepts:

- **Bot Token:** A long string (like `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`) that identifies your bot and authenticates your API calls. Think of it as a combined username + password. Anyone with this token can control your bot — so treat it like a secret.

- **Polling vs. Webhooks:** Polling means your code periodically asks Telegram "anything new?" (simple, great for development). Webhooks mean Telegram pushes new messages to your server instantly (efficient, better for production). We use polling in class.

*Reference: [Telegram Bot API — Introduction for Developers.](https://core.telegram.org/bots) [Telegram Bot Tutorial: From BotFather to Hello World.](https://core.telegram.org/bots/tutorial)*

---

### 4.3 Step-by-Step: Create Your Bot with BotFather

Follow these steps during class. You need a Telegram account (free, takes 30 seconds to create).

**Step 1 — Open BotFather**
1. Open Telegram on your phone or desktop.
2. Search for `@BotFather` (look for the verified blue checkmark).
3. Start a conversation — tap "Start" or send `/start`.

**Step 2 — Create a new bot**
1. Send the command: `/newbot`
2. BotFather asks for a **display name**. Type something descriptive:
   `CEM501 Agent - [YourName]`
3. BotFather asks for a **username**. This must end in `bot`:
   `cem501_yourname_bot`
4. BotFather replies with your **API token**. It looks like this:
   `7204583109:AAH3gqPSFaFKGBuiQ_example_token`

**Step 3 — Save the token securely**

```bash
# Add to your .env file (NEVER commit this file to Git)
echo "TELEGRAM_BOT_TOKEN=your_token_here" >> .env
```

Verify that `.env` is listed in your `.gitignore` file. If it is not, add it now:

```bash
echo ".env" >> .gitignore
```

> **Key Insight:** The bot token is like a master key to your bot. If you accidentally commit it to a public GitHub repository, anyone can hijack your bot. This is the same principle as never hardcoding passwords in source code — credentials belong in environment variables, not in your codebase.

---

### 4.4 Step-by-Step: Your First Working Bot

**Step 4 — Install the library**

```bash
pip install python-telegram-bot python-dotenv
```

**Step 5 — Minimal echo bot (test the connection)**

Create a file called `test_bot.py`:

```python
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

load_dotenv()  # loads TELEGRAM_BOT_TOKEN from .env

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Simply echoes back whatever the user sends."""
    await update.message.reply_text(f"You said: {update.message.text}")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot is running... press Ctrl+C to stop.")
app.run_polling()
```

Run it:

```bash
python test_bot.py
```

Now open Telegram, search for your bot's username, tap "Start," and send any message. If it echoes back — you are connected. Congratulations: you just built a working messaging integration in under five minutes.

---

## Part V: Wiring the Bot to Your Agent
**(~15 min lecture + live coding)**

### 5.1 From Echo to Intelligence

Right now your bot echoes messages. That is like having a phone that only repeats what you say. Let's connect it to the pipeline you have been building all semester: **receive → classify → draft → respond.**

Replace the echo handler with your agent logic:

```python
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Import your existing agent components
from agent.classifier import classify_message
from agent.drafter import draft_response

load_dotenv()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Route incoming Telegram messages through the agent pipeline."""
    incoming_text = update.message.text
    sender = update.message.from_user.first_name

    # Step 1: Classify
    category = classify_message(incoming_text)

    # Step 2: Draft a response
    draft = draft_response(incoming_text, category)

    # Step 3: Send the response back through Telegram
    await update.message.reply_text(draft)

    # Optional: log for debugging
    print(f"[Telegram] {sender} -> {category} -> replied")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Agent bot is running...")
app.run_polling()
```

That is it. The same classifier and drafter you built in Weeks 8-10 now work on a completely new channel. No AI code changed — only the input/output wiring.

### 5.2 The Full Picture

Here is how your agent architecture looks now with two channels:

```
    ┌─────────┐     ┌─────────────┐     ┌──────────┐     ┌─────────┐
    │  Email  │────▶│             │────▶│          │────▶│  Email  │
    │  Input  │     │  Classifier │     │  Drafter │     │  Output │
    └─────────┘     │             │     │          │     └─────────┘
                    │  (same for  │     │  (same   │
    ┌─────────┐     │   all       │     │   for    │     ┌─────────┐
    │Telegram │────▶│   channels) │────▶│   all)   │────▶│Telegram │
    │  Input  │     │             │     │          │     │  Output │
    └─────────┘     └─────────────┘     └──────────┘     └─────────┘
```

The classifier and drafter are the "brain." The channels are the "ears and mouth." You can add as many ears and mouths as you want without performing brain surgery.

> **Key Insight:** This is exactly how large construction PM platforms like Procore work internally. When Procore sends you a notification, it does not have separate logic for email notifications vs. mobile push notifications vs. in-app alerts. It has one notification engine and multiple delivery channels. You are building the same architecture at a smaller scale.

---

### Tool Demo: Using Cursor to Add the Telegram Integration
**(Live demo, ~10 min)**

Here is the exact prompt you can give Cursor or Claude Code to scaffold the integration:

**Prompt:**
> "Create a file `project/channels/telegram_channel.py` that implements the `Channel` base class from `project/channels/base.py`. Use the `python-telegram-bot` library. The class should:
> 1. Load the bot token from an environment variable `TELEGRAM_BOT_TOKEN`
> 2. Implement `fetch_messages()` using polling
> 3. Implement `send_message()` to reply to a given chat ID
> 4. Include docstrings explaining each method
> 5. Handle errors gracefully (e.g., network timeouts, invalid tokens)"

**What to look for in the generated code:**
- Does it inherit from the `Channel` base class?
- Does it load the token from `.env`, not hardcode it?
- Does it handle the case where the token is missing or invalid?
- Are the method signatures consistent with the base class?

If something looks wrong, tell Cursor: "The `send_message` method signature doesn't match the base class — fix it." That is the workflow: generate, review, correct. You are the project manager; the AI is the drafter.

---

### In-Class Workshop: Set Up Your Telegram Bot (35 min)

| Phase | Time | Task |
|-------|------|------|
| **1. Setup** | 10 min | Create your bot with BotFather (Steps 1-3). Store the token. Install the library. |
| **2. Test** | 5 min | Run the echo bot (Step 5). Confirm it responds in Telegram. |
| **3. Integrate** | 15 min | Connect the bot to your classifier and drafter (Part V). Use Cursor to help scaffold the `TelegramChannel` class. |
| **4. Demo** | 5 min | Send a simulated RFI message via Telegram. Verify your agent classifies it and drafts a response. Demo to a neighbor. |

**If you finish early:**
- Add a `/status` command that returns how many messages the agent has processed in this session.
- Add a `/help` command that lists what types of messages the agent can handle.
- Try sending a photo with a caption and see how your classifier handles it (hint: it will need a text fallback).

> **Key Insight:** The first channel integration is the hardest because you are building the abstraction layer. The second channel (Slack, WhatsApp, Discord) should take half the time if your abstraction is clean. This is the payoff of good software design — and it mirrors the payoff of good contract templates in CEM.

---

### Handling Other Channels (Reference)

You are not required to implement these, but here is what it takes if you want to go further:

**WhatsApp (via Twilio)**
- Requires a Twilio account (free trial available, provides a sandbox number).
- Uses **webhooks** — Twilio forwards incoming WhatsApp messages to your server via HTTP POST.
- More complex than Telegram because you need a **publicly accessible URL** (use `ngrok` to expose your local machine during development).
- Good choice if your project scenario involves field crews who primarily use WhatsApp.

**Slack**
- Create a Slack App at [api.slack.com](https://api.slack.com).
- Use **Socket Mode** for development (no public URL needed — similar to Telegram's polling).
- Required Bot Token scopes: `chat:write`, `channels:read`, `app_mentions:read`.
- Good choice if your project scenario involves an office-based team.

**Microsoft Teams**
- Requires registering a bot through the Azure Bot Framework.
- More setup overhead than Telegram or Slack, but worth it if your organization is on Microsoft 365.
- Uses webhooks with Azure hosting (or the Bot Framework Emulator for local testing).

The abstraction pattern means switching to any of these is a matter of writing **one new class** that implements `fetch_messages()` and `send_message()`. Your classifier, drafter, and main loop remain untouched.

---

### Milestone M6 — Due Before Week 12

**Deliverable:** `project/channels/` directory with at least one channel beyond email.

**Requirements:**

| Requirement | Points |
|-------------|--------|
| A new channel class (e.g., `telegram_channel.py`) that inherits from the `Channel` base class | 20 |
| The channel can receive a message and return an agent-generated response (live demo or screenshot) | 30 |
| Token / credentials stored in `.env`, not hardcoded anywhere in source code | 10 |
| A brief `project/channels/README.md` explaining which channels are implemented and how to configure them | 15 |
| Code clarity: docstrings, consistent naming, clean structure | 15 |
| Error handling: bot responds gracefully to unexpected inputs or missing credentials | 10 |
| **Total** | **100** |

**Submission:** Push to your GitHub fork before the Week 12 session. The grader will clone your repo, add their own `.env` with a test bot token, and verify the integration works.

---

### Further Reading

**Messaging & Channel Integration:**
- Telegram Bot API documentation: [core.telegram.org/bots/api](https://core.telegram.org/bots/api)
- Telegram Bot Tutorial — From BotFather to Hello World: [core.telegram.org/bots/tutorial](https://core.telegram.org/bots/tutorial)
- `python-telegram-bot` library docs: [docs.python-telegram-bot.org](https://docs.python-telegram-bot.org)
- Twilio WhatsApp Quickstart: [twilio.com/docs/whatsapp](https://twilio.com/docs/whatsapp)
- Slack API — Getting Started: [api.slack.com/start](https://api.slack.com/start)

**Industry Data Cited in This Lecture:**
- HBR (2022). ["How Much Time and Energy Do We Waste Toggling Between Applications?"](https://hbr.org/2022/08/how-much-time-and-energy-do-we-waste-toggling-between-applications)
- Haiilo (2024). ["Digital Fatigue: How Fragmented Tools Are Hurting Your Team."](https://blog.haiilo.com/blog/digital-fatigue-how-fragmented-tools-are-hurting-your-team/)
- Mio (2024). ["The State of Workplace Messaging."](https://www.m.io/blog/state-of-workplace-messaging)
- ClickUp Insights (2025). ["The State of Workplace Communication."](https://clickup.com/blog/team-communication-survey/)
- MindForge (2024). ["Smartphone App Usage Among Construction Workers."](https://www.mindforgeapp.com/blog-posts/smartphone-app-usage-among-construction-workers-adoption-preferences-and-barriers)
- FMI & PlanGrid (2018). ["Construction Disconnected."](https://www.prnewswire.com/news-releases/new-research-from-plangrid-and-fmi-identifies-factors-costing-the-construction-industry-more-than-177-billion-annually-300689826.html)

**Software Design Patterns:**
- [Adapter Pattern — Wikipedia](https://en.wikipedia.org/wiki/Adapter_pattern)
- [Sourcemaking: Adapter Design Pattern](https://sourcemaking.com/design_patterns/adapter)

---

**Dr. Eyuphan Koc** | eyuphan.koc@bogazici.edu.tr
