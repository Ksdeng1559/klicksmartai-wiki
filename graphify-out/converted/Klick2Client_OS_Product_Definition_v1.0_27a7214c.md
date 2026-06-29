<!-- converted from Klick2Client_OS_Product_Definition_v1.0.docx -->


KLICK TO CLIENT OS
Product Definition Document

B2B LinkedIn-First Client Acquisition Operating System
Vertical-Agnostic | Signal-Driven | Autonomous

Version 1.0  |  Klick2Client  |  www.klick2client.com  |  Confidential

# Table of Contents

# 1. Executive Summary
## 1.1 Product Vision
Klick2Client OS is a B2B client acquisition operating system that transforms LinkedIn authority and expertise into a continuous, autonomous pipeline of qualified prospects — converting content into conversations, and conversations into clients.

The system is industry-agnostic by design. Any B2B practitioner who can demonstrate expertise and authority in their domain can deploy Klick2Client OS as a full-stack client acquisition engine — from signal detection through to closed business.

## 1.2 Core Operating Principle
LinkedIn is the primary lead generation source. Authoritative content published on LinkedIn serves as the intelligence foundation for the entire system. Every piece of content generates multiple downstream assets: outreach messages, follow-up sequences, personalization hooks, and conversion triggers — all derived from the practitioner's genuine expertise.

The system operates through two independent LinkedIn entry paths:

Path 1 — Content-Driven:
- Practitioner publishes authoritative LinkedIn content addressing a specific B2B problem
- A person likes, comments, or shares the post — self-selecting as a warm prospect
- Unipile detects the engagement event and triggers the ICP filter
- ICP match confirmed — profile enriched, personalization brief built
- Claude drafts a DM referencing the specific post they engaged with
- Draft enters the human approval queue with PSQ score and reasoning
- Practitioner approves — Unipile sends — prospect enters the lifecycle engine

Path 2 — Enriched Lead List:
- Signal intelligence identifies an ICP prospect who has not yet engaged with content
- Python enrichment scripts build full profile from Lead Sniper HNW output
- LinkedIn profile, activity, and real-time signals form the personalization brief
- Claude drafts a personalized connection request and 3-touch DM sequence
- All drafts enter the human approval queue with full context and PSQ scores
- Practitioner approves each message — Unipile sends — prospect enters lifecycle engine

The non-negotiable governance principle across both paths: Claude drafts and scores every message. The practitioner approves every message. No outbound communication leaves the system without explicit human sign-off.

## 1.3 What This Is Not
- Not a mass-blast outreach tool — every message is signal-driven and personalized
- Not industry-specific — the framework adapts to any B2B vertical
- Not a replacement for human expertise — it amplifies and distributes it at scale
- Not a static automation — the system learns and self-adjusts based on conversion data

# 2. System Architecture
## 2.1 Architecture Overview
Klick2Client OS is composed of six integrated layers, each with a distinct responsibility. No layer performs functions outside its defined scope — this is the foundation of the system's maintainability and scalability.


## 2.2 Data Flow
The following represents the end-to-end data flow through the system:

CONTENT ENGINE
- Practitioner publishes authoritative LinkedIn content
- Content is parsed into reusable messaging components: hooks, value statements, proof points, calls to action
- Components are stored in Supabase as the personalization library

SIGNAL INTELLIGENCE LAYER
- Signal algorithm runs continuously (APScheduler — Python-native)
- Brave Search: recent news and press about the individual or company
- Tavily Search: deep web research, wealth and business signals
- Gemini Grounding: factual verification and contextual enrichment
- AI Now Algorithm: [placeholder — injected at integration phase]
- New signal detected → triggers re-personalization pipeline

ENRICHMENT LAYER — PRIMARY OUTPUT: SALES BATTLECARD
- Python scripts process raw signals into structured prospect profiles
- EnrichLayer + BetterContact verify contact details and professional history
- Claude scores prospect fit and wealth probability
- Profile written to Supabase contacts table
- Primary deliverable: a two-page Sales Battlecard generated on demand and delivered to the sales advisor before every meeting — on-screen in the FastAPI UI and downloadable as PDF
- Battlecard is refreshed on demand — advisor pulls a fresh version before each conversation so intelligence is always current

LINKEDIN CONVERSION MODULE — TWO ENTRY PATHS
- Path 1 (Content-Driven / Warm): Post published, Unipile detects engagement (like/comment/share), ICP filter applied, profile enriched, Claude drafts DM referencing specific post, human approval queue, practitioner approves, Unipile sends
- Path 2 (Enriched Lead List / Cold): Lead Sniper identifies ICP, Python enrichment builds full profile, signal intelligence runs, profile and activity scraped for personalization, Claude drafts connection request and DM sequence, human approval queue, practitioner approves, Unipile sends
- Connection status check (both paths): if already connected, DM direct; if not connected, connection request first, then DM on acceptance
- Both paths are independent — a prospect may enter via either route but is never duplicated in the system

HUMAN-IN-THE-LOOP GOVERNANCE (ALL PATHS)
- Every outbound message — regardless of path, channel, or PSQ score — requires practitioner approval before sending. No exceptions.
- Claude drafts and scores. The practitioner decides. This is the non-negotiable governance principle of Klick2Client OS.
- Approval queue surfaces drafts ranked by ICP fit score with full context: prospect profile, signal data, content match, PSQ score, and Claude reasoning
- Practitioner actions on each draft: Approve / Edit and Approve / Reject / Defer

LIFECYCLE ENGINE
- Parallel tracks: LinkedIn (Touch 1, 2, 3) and Email (Day 30/60/90/180/270/360)
- Unipile unified messaging API handles all channel delivery after practitioner approval
- APScheduler batch job runs nightly — processes all contacts due for action, queues drafts for approval
- Unipile webhooks fire in real-time on reply, open, click events

INTELLIGENCE FEEDBACK LOOP
- conversion_analyzer.py: Claude evaluates whether personalization strategy worked
- KPI data written to conversion_kpis table in Supabase
- Claude surfaces recommendations for strategy adjustment — practitioner confirms before any change takes effect
- Human review dashboard shows all Claude recommendations with full rationale


# 3. LinkedIn Entry Paths — How Prospects Enter the System
## 3.1 Two Independent Entry Points
Every prospect in Klick2Client OS enters through one of two LinkedIn-driven paths. The paths are independent — a prospect cannot exist in both simultaneously — but both feed the same lifecycle engine and Kanban pipeline once approved and sent.

The governing principle across both paths is identical: Claude drafts and scores every message. The practitioner approves every message before it is sent. No outbound communication leaves the system without explicit human sign-off. This is not a configurable option — it is the non-negotiable governance framework of Klick2Client OS.

## 3.2 Path 1 — Content-Driven (Warm Lead)
This path activates when a person engages with the practitioner's LinkedIn content. Engagement is pre-qualified intent — the prospect has already self-selected by interacting with authoritative content that addresses a specific problem. This makes Path 1 the highest-conversion entry point in the system.


## 3.3 Path 2 — Enriched Lead List (Cold Outreach)
This path activates when Lead Sniper HNW identifies a prospect who matches the ICP definition but has not yet engaged with the practitioner's content. The entire personalization foundation is built from enriched data — LinkedIn profile, recent activity, and real-time intelligence signals — rather than content engagement.


## 3.4 Path Comparison


## 3.5 Content Library — The Shared Personalization Foundation
Both paths draw from the same content library. Every piece of LinkedIn content the practitioner publishes is parsed and stored as a set of reusable personalization assets. This is what makes the system's outreach feel genuinely expert rather than templated.

One authoritative LinkedIn post generates the following assets, all stored in Supabase:


# 4. LinkedIn Conversion Module
## 4.1 Purpose
The LinkedIn Conversion Module is the highest-leverage component of Klick2Client OS. It transforms raw prospect data and content intelligence into genuinely personalized message sequences — and presents them to the practitioner for approval before any message is sent. The module does not send. It drafts, scores, and queues. The practitioner sends.

## 4.2 Human-in-the-Loop Governance
This is the foundational operating principle of Klick2Client OS and applies to every message generated by the system across both LinkedIn paths, all email lifecycle stages, and all channels:


No message exits the system without practitioner approval. This governance model protects the practitioner's brand, ensures compliance with platform terms of service, and maintains the quality of every client relationship initiated through the system.

## 4.3 Three-Touch Sequence Design
Both LinkedIn entry paths use the same three-touch sequence structure. The personalization source differs by path — but the sequence logic, approval gate, and send mechanism are identical.


## 4.4 Pre-Send Quality Score (PSQ)
Every message drafted by Claude is scored before it enters the approval queue. The PSQ is a quality signal for the practitioner — it does not control whether a message is sent. The practitioner makes that decision. The PSQ informs it.


The practitioner sees the PSQ, the flag colour, and the Claude reasoning note for every draft in the queue. A red-flagged draft can still be approved — the practitioner may have context the system does not. The PSQ is an input, not a veto.

## 4.5 Approval Queue Design
The approval queue is accessible from the Kanban board and as a dedicated view in the FastAPI UI. Drafts are ranked by ICP fit score (highest priority first). Each queued item displays:
- Prospect name, company, role, and ICP fit score
- Entry path (Content-Driven / Enriched Lead List) and trigger event
- Personalization brief summary: top 3 hooks used, signal sources, content match
- Drafted message in full with PSQ score and colour flag
- Claude reasoning: why this message, why these hooks, what outcome is anticipated
- Practitioner actions: Approve / Edit and Approve / Reject / Defer (with optional note)
- Estimated send time after approval (based on Unipile queue and LinkedIn rate limits)

# 5. Lifecycle Engine — 360-Day Revenue Intelligence
## 5.1 Six-Stage Contact Lifecycle
Every prospect that enters the system is tracked across a 360-day lifecycle. The system never abandons a qualified prospect prematurely — it adapts the approach based on engagement signals and available intelligence.


## 5.2 Parallel Track Logic
A prospect simultaneously runs on two independent tracks. Kanban card position reflects the most advanced track. Each card displays both track statuses for full visibility.

- LinkedIn Track: Connection Request → Touch 1 → Touch 2 → Touch 3 (relationship-first)
- Email Track: Day 0 → Day 30 → Day 60 → Day 90 → Day 180 → Day 270 (documented, direct)
- WhatsApp: Reserved for Day 180+ only, and only for prospects with composite score above defined threshold
- Channel selection is Claude-decided per contact, per touch, based on available data and engagement history

## 5.3 Reply Handling
When a prospect replies on any channel, the Unipile webhook fires immediately:
- Message logged to Supabase messages table with direction: inbound
- Lifecycle sequence paused on that channel
- Kanban card moves to Actual Contact stage automatically
- Engagement score updated — composite score recalculated
- Human notification triggered — practitioner takes over the conversation
- Conversion outcome recorded when conversation concludes (meeting / proposal / closed / lost)

# 6. Kanban Pipeline Board
## 6.1 Purpose
The Kanban board is the practitioner-facing command centre of Klick2Client OS. It provides real-time visibility into every active prospect across all pipeline stages, with both LinkedIn and Email track statuses visible on each card simultaneously.

## 6.2 Five Pipeline Stages


## 6.3 Card Design
Each Kanban card displays:
- Prospect name, company, and ICP fit score
- LinkedIn track status (Touch 1 sent / Connected / Replied / Exhausted)
- Email track status (Pending / Sent / Opened / Replied / Bounced)
- Pre-send quality score of last outbound message
- Days in current stage
- Last activity date and channel
- Human override button — practitioner can manually move card to any stage

## 6.4 KPI Summary Bar
A live KPI summary bar runs across the bottom of the Kanban board displaying aggregated conversion metrics for the current period. Full detail is accessible on the separate KPI Dashboard page.
- Connection Acceptance Rate
- Reply Rate per Touch
- Meeting Conversion Rate
- Proposal-to-Close Rate
- Average Pre-Send Quality Score
- Top Converting Signal Source (Brave / Tavily / Gemini / AI Now)

# 7. Intelligence Feedback Loop — KPI-Driven Auto-Adjustment
## 7.1 Operating Principle
The feedback loop is what separates Klick2Client OS from a standard outreach automation tool. Every message sent generates data. That data is analysed by Claude to determine whether the personalization strategy is working. Future messages are adjusted accordingly — without human intervention, unless the practitioner chooses to override.

## 7.2 Measurement Framework
Two measurement points per message:

Pre-Send (Quality Gate)
- Pre-Send Quality Score (PSQ): 1-100, Claude-generated before every send
- PSQ reflects specificity of personalization, relevance of content match, quality of hook, and signal grounding
- Messages below threshold are regenerated before sending

Post-Send (Conversion Tracking)
- Reply Rate: did this message generate a response?
- Meeting Rate: did this conversation result in a booked call?
- Time to Conversion: how many days from first contact to each stage?
- Channel Performance: which channel drove the conversion at each stage?
- Signal Source Attribution: which intelligence source (Brave / Tavily / Gemini / AI Now) contributed to the converting message?

## 7.3 Auto-Adjustment Logic
Claude analyses conversion data weekly and makes the following adjustments autonomously:
- Message strategy shift: if Touch 2 reply rate drops below threshold, Claude adjusts the angle and tone
- Channel rebalancing: if Email outperforms LinkedIn at a given stage, Claude shifts emphasis
- Content library prioritization: content assets with higher conversion rates are weighted more heavily in future personalization
- Signal source weighting: intelligence sources that consistently contribute to converting messages are prioritized
- PSQ threshold adjustment: if high-PSQ messages are not converting, Claude raises the quality bar

## 7.4 Human Override
All Claude auto-adjustments are logged and visible on the KPI Dashboard. The practitioner can:
- Review any auto-adjustment decision with full rationale
- Override any individual decision without affecting the broader strategy
- Lock specific settings to prevent Claude from adjusting them
- Manually define message strategy for specific prospect segments

# 8. Technical Architecture
## 8.1 Technology Stack


## 8.2 File Architecture
Every file in the system has a single, well-defined responsibility. No file exceeds 300 lines of logic code. This is a non-negotiable design constraint.

- scheduler/lifecycle_runner.py — nightly batch: queries contacts due for action, coordinates agents
- scheduler/signal_monitor.py — continuous signal watching, triggers re-personalization and battlecard refresh on new events
- webhooks/unipile_receiver.py — FastAPI inbound event handler for all Unipile callbacks
- agents/lifecycle_agent.py — Claude decides stage action and channel per contact
- agents/message_builder.py — Claude generates email content for each lifecycle stage
- agents/conversion_analyzer.py — Claude evaluates personalization effectiveness and surfaces recommendations
- battlecard/battlecard_generator.py — assembles all data sources, calls Claude for synthesis, renders two-page brief
- battlecard/pdf_exporter.py — converts battlecard to downloadable PDF on demand
- linkedin_module/profile_analyzer.py — fetches and parses LinkedIn profile via Unipile
- linkedin_module/activity_scraper.py — extracts posts and engagement as personalization hooks
- linkedin_module/linkedin_agent.py — Claude generates and scores LinkedIn sequence content
- linkedin_module/sequence_builder.py — Touch 1 / 2 / 3 logic, timing, and channel rules
- intelligence/signal_monitor.py — signal algorithm placeholder, ready for injection
- kanban/board_api.py — FastAPI routes serving Kanban and KPI dashboard
- kanban/board_logic.py — stage rules, parallel track resolution, card movement logic
- db/schema.sql — all Supabase table definitions, indexes, RLS policies
- db/supabase_client.py — all database read/write operations, no business logic
- integrations/unipile_client.py — Unipile API wrapper, all channel send/receive
- config/settings.py — environment variables, stage constants, scoring thresholds
- main.py — starts APScheduler, FastAPI server, and all background services

## 8.3 Database Schema Summary
Eight tables in Supabase, each with a single concern:


# 9. Build Roadmap
## 9.1 Phased Delivery


# 10. Sales Battlecard — Pre-Meeting Intelligence Brief
## 10.1 Purpose and Design Principle
The Sales Battlecard is the primary output of the enrichment layer. Its purpose is not to automate a conversation — it is to equip the sales advisor to have a more informed, more confident, and more relevant personal conversation with the prospect.

Every data point in the battlecard exists to serve one goal: give the advisor a reason to be talking to this person, at this moment, about this specific topic. The Why Now signal is the most important element on the card — it is the intelligence that makes the outreach timely rather than generic.

The battlecard is generated on demand. The advisor pulls a fresh version before every meeting so the intelligence reflects the most current signals, not the state of the prospect at the time they first entered the system. A prospect who entered six months ago may have had a funding event, a leadership change, or a press mention last week — the battlecard will surface it.

## 10.2 Delivery Format
- On-screen in the FastAPI UI — accessible from the Kanban card for the prospect at any pipeline stage
- Downloadable as a PDF one-pager — formatted for print or mobile reference during a call
- Both formats are generated from the same Supabase data on demand — no separate storage required
- Branded with the client account name and sales advisor name on every battlecard

## 10.3 Battlecard Structure — Page 1: Who They Are and Why Now
Page 1 is the intelligence foundation. It answers three questions the advisor must be able to answer before any conversation: Who is this person? What do I know about their world right now? Why is now the right moment to talk?


## 10.4 Battlecard Structure — Page 2: How to Have the Conversation
Page 2 is the conversation playbook. It is built entirely from the prospect's own words, public activity, and detected signals — giving the advisor a set of openers and talking points that feel genuinely researched rather than scripted.


## 10.5 Battlecard Generation Process
The battlecard is generated by a dedicated Python module — battlecard_generator.py — which assembles all data sources into a structured brief and passes it to Claude for synthesis. The output is a formatted two-page document rendered in the FastAPI UI and exported as PDF on demand.

- Advisor opens prospect's Kanban card and clicks Generate Battlecard
- battlecard_generator.py queries Supabase for the full contact record
- signal_monitor.py performs a fresh intelligence check across all sources
- linkedin_module fetches the latest LinkedIn profile and activity snapshot
- Claude synthesizes all data into the structured battlecard format
- Battlecard renders in the FastAPI UI — on-screen view available immediately
- Advisor can download PDF version for print or mobile use
- Generation timestamp displayed on card — advisor knows exactly how fresh the intelligence is

## 10.6 Battlecard in the Pipeline Context
The battlecard is accessible at every Kanban stage but is most critical at two points:


# 11. Vertical Agnosticism — Deploying Across B2B Industries
## 11.1 Design Principle
Klick2Client OS is architected to be completely independent of any specific industry, vertical, or service type. The only requirements for deployment are:
- A defined Ideal Client Profile (ICP) expressible as a set of search and signal parameters
- A practitioner with genuine domain expertise capable of producing authoritative LinkedIn content
- A clear value proposition that can be articulated in a LinkedIn connection note (300 characters)

## 11.2 Configuration Points for Vertical Adaptation
The following system parameters are configured per deployment — no code changes required:


## 11.3 Example Vertical Configurations
To illustrate the flexibility of the system without limiting its application:

Professional Services (Legal, Accounting, Consulting)
- ICP: C-suite, business owners, company size 10-500 employees
- Signals: regulatory changes, funding rounds, leadership transitions, M&A activity
- Content themes: risk management, growth strategy, compliance, operational efficiency
- PSQ threshold: 80 — high personalization required for trust-dependent services

Financial Services (Wealth Management, Insurance, Commercial Finance)
- ICP: HNW individuals, business owners, CFOs, family offices
- Signals: liquidity events, property transactions, business sale or exit, inheritance
- Content themes: wealth preservation, tax efficiency, risk transfer, capital structuring
- PSQ threshold: 85 — regulatory environment demands high-quality, relevant outreach

Technology and SaaS
- ICP: VPs of Engineering, CTOs, Heads of Product, Operations leaders
- Signals: hiring surges, tech stack changes, product launches, Series A/B funding
- Content themes: scalability, technical debt, team productivity, integration architecture
- PSQ threshold: 75 — tech buyers respond to specificity over relationship-warmth

Recruitment and Executive Search
- ICP: CHROs, CEOs, Heads of People, private equity portfolio company operators
- Signals: leadership gaps, rapid headcount growth, restructuring announcements
- Content themes: talent strategy, leadership capability, organisational design
- PSQ threshold: 80 — candidate and client relationships built on trust and discretion

# 12. Glossary


| Layer | Name | Responsibility |
| --- | --- | --- |
| 1 | Content Engine | LinkedIn authority content → multi-format downstream assets |
| 2 | Signal Intelligence | Continuous prospect monitoring via Brave, Tavily, Gemini Grounding + signal algorithm |
| 3 | Enrichment Layer | Python scripts build full prospect profile from raw signals → primary output is the Sales Battlecard delivered to the advisor before every meeting |
| 4 | LinkedIn Conversion Module | Profile analysis, activity scraping, personalized 3-touch sequence generation |
| 5 | Lifecycle Engine | 360-day parallel-track outreach (LinkedIn + Email) via Unipile unified messaging |
| 6 | Intelligence Feedback Loop | Pre-send quality scoring + post-send conversion tracking → Claude auto-adjusts strategy |
| Step | Action | System Behaviour |
| --- | --- | --- |
| 1 | Post Published | Practitioner publishes authoritative LinkedIn content addressing a specific B2B problem or expertise domain |
| 2 | Engagement Detected | Unipile webhook fires on like, comment, or share. Engager identity captured. |
| 3 | Duplicate Check | System queries Supabase: is this person already in an active sequence? If yes, engagement score updated and path exits. No duplicate outreach. |
| 4 | ICP Filter | Engager profile checked against ICP definition (title, company size, sector, geography). Non-ICP contacts are logged but not advanced. |
| 5 | Profile Enrichment | LinkedIn profile fetched via Unipile. Activity scraped. Signal intelligence checked. Full personalization brief built. |
| 6 | Connection Check | Already connected: Claude drafts a DM referencing the specific post engaged with. Not connected: Claude drafts a connection request note first. |
| 7 | Claude Drafts + Scores | Message drafted using the post content, engagement type (liked vs. commented vs. shared), and prospect profile as personalization inputs. PSQ assigned. |
| 8 | Human Approval Queue | Draft surfaces in the practitioner approval queue with full context. Practitioner actions: Approve / Edit and Approve / Reject / Defer. |
| 9 | Send via Unipile | Approved message sent. Contact enters Supabase lifecycle engine at Stage 1. Kanban card created at First Contact. |
| Step | Action | System Behaviour |
| --- | --- | --- |
| 1 | Prospect Identified | Lead Sniper HNW detects signal (funding, M&A, property, regulatory, press) and identifies the individual. ICP match confirmed. |
| 2 | Python Enrichment | Enrichment scripts build full profile: contact details verified via EnrichLayer and BetterContact. Wealth or fit score calculated. |
| 3 | Signal Intelligence | Brave, Tavily, Gemini Grounding, and AI Now algorithm queried. All detected signals appended to the personalization brief. |
| 4 | LinkedIn Profile Analysis | profile_analyzer.py fetches full LinkedIn profile via Unipile. activity_scraper.py extracts recent posts, comments, and shared content as personalization hooks. |
| 5 | Content Library Match | System identifies the practitioner content asset most relevant to this prospect's profile, role, and detected signals. |
| 6 | Connection Check | Already connected: Claude drafts Touch 1 DM. Not connected: Claude drafts a personalized connection request note (300 char limit) followed by the planned DM sequence. |
| 7 | Claude Drafts + Scores | Full 3-touch sequence drafted: connection request note, Touch 1 DM, Touch 2 follow-up. Each message individually PSQ-scored. Low-scoring drafts regenerated before queuing. |
| 8 | Human Approval Queue | All drafts surface in approval queue ranked by ICP fit score. Full context shown: profile summary, signals detected, content match rationale, PSQ score, Claude reasoning. Practitioner actions: Approve / Edit and Approve / Reject / Defer. |
| 9 | Send via Unipile | Approved messages sent in sequence. Connection request first if not connected. Contact enters lifecycle engine at Stage 1. Kanban card created. |
| Dimension | Path 1 — Content-Driven | Path 2 — Enriched Lead List |
| --- | --- | --- |
| Entry Trigger | Engagement with a LinkedIn post (like, comment, share) | Signal detection by Lead Sniper HNW matching ICP definition |
| Lead Temperature | Warm — self-selected by engaging with relevant content | Cold — no prior interaction with the practitioner |
| Personalization Source | The specific post engaged with + profile data | Enriched profile + signal intelligence + content library match |
| Connection Logic | Check status: DM if connected, connection request if not | Check status: DM if connected, connection request if not |
| Approval Gate | Human approval required. No exceptions. | Human approval required. No exceptions. |
| Expected Conversion | Higher — intent pre-signalled by content engagement | Lower baseline, elevated by personalization quality and signal relevance |
| Volume Profile | Dependent on content reach and engagement rate | Dependent on ICP market size and Lead Sniper signal frequency |
| Content Asset | How It Is Used in Outreach |
| --- | --- |
| Core problem statement | Connection request note — frames why the outreach is relevant to this person now |
| Key insight or contrarian take | Touch 1 DM opener — sparks curiosity, positions practitioner as a peer not a vendor |
| Proof point or case reference | Touch 2 DM — social proof grounded in a specific, verifiable result |
| Framework or methodology | Touch 3 or email follow-up — demonstrates structured thinking and repeatable approach |
| Specific outcome or number | Email subject line or opening line — specificity drives open and reply rates |
| Call to action variant | Stage 3+ messages — low-friction next step appropriate to the relationship stage |
| Claude's Role | Practitioner's Role |
| --- | --- |
| Research and build the personalization brief | Review the brief before approving any draft |
| Draft every outbound message | Read every draft before it is sent |
| Score every draft with a Pre-Send Quality Score | Use the PSQ as a decision input — not a substitute for judgment |
| Regenerate low-quality drafts automatically | Approve, edit, reject, or defer every queued message |
| Surface conversion recommendations with rationale | Confirm or override every Claude recommendation |
| Log all actions, decisions, and outcomes | Maintain full audit visibility via the KPI dashboard |
| Touch | Trigger | Message Strategy | Char Limit | Approval |
| --- | --- | --- | --- | --- |
| Request | Prospect identified (Path 1 or 2). Not yet connected. | Personalized connection note. Specific reference to shared context, post engaged with, or detected signal. No generic phrases. | 300 characters | Human required |
| Touch 1 | Connection accepted (Unipile webhook) OR already connected at entry | Value-first message. References post (Path 1) or personalization brief (Path 2). No pitch. Opens a conversation. | No limit | Human required |
| Touch 2 | Day 7 — no reply to Touch 1 | Different angle. New signal or hook if available. Shorter and more direct than Touch 1. Soft call to action. | No limit | Human required |
| Touch 3 | Day 14 — no reply to Touch 2 | Final LinkedIn attempt. Minimal pressure. Leaves door open. Email track escalates from Day 30 onward. | No limit | Human required |
| PSQ Range | Meaning | Claude Action Before Queuing |
| --- | --- | --- |
| 90 - 100 | Highly specific. Verifiable personal or company detail referenced. Strong content-to-prospect relevance. | Queue for approval immediately |
| 75 - 89 | Good personalization. Minor generic elements. Solid signal grounding. | Queue for approval |
| 60 - 74 | Moderate personalization. Missing specific hooks or proof points from the brief. | Claude regenerates once. If still below 75, queues with PSQ flagged amber. |
| Below 60 | Generic or template-like. Insufficient signal data or poor content match. | Claude regenerates twice. If still below 60, queues with PSQ flagged red and note explaining the gap. |
| Stage | Day Mark | Status | System Action |
| --- | --- | --- | --- |
| 1 | Day 0 | New Lead | LinkedIn Touch 1 sent. Email track queued. Intelligence brief generated. |
| 2 | Day 30 | Active Outreach | LinkedIn Touch 2 or 3 (if not yet sent). Email Touch 1 deployed. |
| 3 | Day 60 | Nurture | Value-add email. New signal check triggers re-personalization if available. |
| 4 | Day 90 | Re-engagement | Direct short-form email. Different angle from previous touches. Brief and specific. |
| 5 | Day 180 | Dormant | New intelligence angle if signal detected. WhatsApp reserved for HNW score above threshold. |
| 6 | Day 270 | Final Attempt | Last outreach. High-score prospects flagged for human escalation review. |
| — | Day 360 | Archived | Revenue decay confirmed. Contact archived. Closed lost recorded. |
| Kanban Stage | Entry Trigger | Exit Trigger |
| --- | --- | --- |
| First Contact | Prospect enters system. LinkedIn Touch 1 or Email Touch 1 sent. | Any reply received on any channel. |
| Actual Contact | Reply received — two-way conversation has begun. | Calendar link sent or meeting verbally agreed. |
| Calendar Booked | Meeting confirmed in calendar. Discovery or qualification call scheduled. | Proposal or scope of work sent to prospect. |
| Final Proposal | Formal proposal or engagement letter delivered. | Prospect confirms or declines. |
| Close | Prospect confirms engagement. Contract signed or verbal agreement reached. | Terminal stage. Won or Lost recorded. |
| Layer | Technology | Role |
| --- | --- | --- |
| Language | Python | All business logic, enrichment scripts, agent orchestration |
| Database | Supabase (PostgreSQL) | Cloud-hosted, multi-client, source of truth for all contact and lifecycle data |
| AI / Intelligence | Claude API (Anthropic) | Stage decisions, message generation, quality scoring, conversion analysis |
| Unified Messaging | Unipile | Single API for LinkedIn, Email, WhatsApp outbound and inbound |
| Scheduling | APScheduler | Python-native cron — nightly batch + continuous signal monitoring |
| Web UI / Webhooks | FastAPI + Jinja2 | Kanban board, KPI dashboard, Unipile webhook receiver |
| HTTP Client | httpx (async) | Concurrent API calls to Unipile and intelligence sources |
| Data Validation | Pydantic | Validates data shapes between all system layers |
| Signal Sources | Brave, Tavily, Gemini, AI Now | Real-time intelligence — news, web research, factual grounding, proprietary signals |
| Lead Generation | Lead Sniper HNW | Top-of-funnel prospect detection and initial enrichment |
| Table | Purpose |
| --- | --- |
| contacts | Enriched prospect profile from Lead Sniper HNW — the master record |
| content_library | Parsed LinkedIn content assets: hooks, proof points, value statements, CTAs |
| lifecycle_events | Stage tracking per contact per channel — the lifecycle state machine |
| messages | Every message sent and received across all channels via Unipile |
| linkedin_sequences | LinkedIn 3-touch sequence state, profile data, activity hooks, personalization |
| signal_events | Intelligence signals detected per contact, source-attributed, timestamped |
| kanban_cards | Pipeline stage per contact with parallel track statuses and override flags |
| conversion_kpis | Aggregated KPI data: funnel metrics, PSQ performance, signal attribution |
| Phase | Name | Deliverables | Business Value |
| --- | --- | --- | --- |
| 1 | Foundation | schema.sql, settings.py, supabase_client.py | Lead Sniper contacts flow into Klick2Client OS |
| 2 | Content Engine | content_library table, content parsing scripts | LinkedIn content becomes the personalization source |
| 3 | Enrichment + Battlecard | enrichment scripts, battlecard_generator.py, PDF export, FastAPI battlecard view | Advisor receives a fresh intelligence brief before every meeting |
| 4 | Messaging Infrastructure | unipile_client.py, message_builder.py, lifecycle_agent.py | Automated lifecycle emails running via Unipile |
| 5 | Signal Intelligence | signal_monitor.py (placeholder + algorithm injection) | Real-time intelligence triggers battlecard refresh and re-personalization |
| 6 | LinkedIn Module | profile_analyzer, activity_scraper, linkedin_agent, sequence_builder | Personalized 3-touch LinkedIn sequences with quality scoring and approval queue |
| 7 | Feedback Loop | conversion_analyzer.py, unipile_receiver.py, lifecycle_runner.py | System surfaces conversion recommendations for practitioner review |
| 8 | Kanban + KPI UI | board_logic, board_api, board.html, kpi_dashboard.html | Full pipeline visibility, battlecard access at every stage, conversion analytics |
| 9 | Integration | main.py — wires all services into single entry point | One command runs entire Klick2Client OS |
| Section | Content |
| --- | --- |
| Header | Client account name and logo (left). Sales advisor name and title (right). Battlecard generation date and time (bottom right — signals freshness). |
| Prospect Identity | LinkedIn profile photo, full name, current title, company name, location, and tenure in current role. Company sector, size range, and revenue range where available from enrichment. |
| Enrichment Summary | Key facts surfaced through the enrichment process: previous roles and companies, board positions or advisory roles, professional qualifications, known associations and memberships, education background. Presented as a scannable brief — not a biography. |
| WHY NOW SIGNAL | The specific trigger that makes this conversation timely. Displayed prominently — this is the most important element on the card. Includes: signal type (funding / M&A / property / regulatory / press / leadership change), the specific detail detected, the source and date, and a one-line statement of why this signal is relevant to the advisor's value proposition. |
| LinkedIn Activity Highlights | The three most recent and relevant LinkedIn signals from the prospect: posts they authored (topic and key position taken), content they engaged with (what it reveals about their current priorities), and any public comments that indicate their thinking on relevant topics. |
| Section | Content |
| --- | --- |
| Conversation Starters | Three opening lines grounded directly in the prospect's own LinkedIn content or detected signals. Each starter is specific, verifiable, and references something the prospect has said, shared, or done publicly. No generic openers. Each includes a source note so the advisor knows exactly where the intelligence came from. |
| Talking Points | Four to six talking points aligned to the ICP pain points most relevant to this prospect's role, sector, and signal context. Each talking point connects the prospect's detected situation to the advisor's value proposition. Presented as a bridge: here is what they are experiencing — here is how that connects to what you offer. |
| Relevant Content Reference | The specific practitioner LinkedIn post or article most relevant to this prospect's situation. Includes the post title or topic, why the system selected it for this prospect, and a suggested way to reference it naturally in conversation — not as a sales tool but as a shared point of view. |
| Next Step Suggestion | Claude-suggested logical next step based on the prospect's pipeline stage and engagement history. Presented as a suggestion only — the advisor decides. Examples: propose a discovery call, share a specific case study, introduce a relevant framework, request a referral introduction. |
| Pipeline Stage | How the Battlecard Is Used |
| --- | --- |
| First Contact | Advisor reviews battlecard before approving the Claude-drafted LinkedIn message. Ensures the personalization is accurate and the Why Now signal is correctly framed. |
| Calendar Booked | Advisor pulls a fresh battlecard immediately before the discovery or qualification call. This is the primary use case — intelligence briefing for a live conversation. |
| Final Proposal | Battlecard refreshed to surface any new signals since the initial meeting. Talking points updated to reflect what was discussed in the call. |
| Any Stage | Advisor can pull a fresh battlecard at any time if a new signal is detected or if they want to re-brief themselves before a follow-up touchpoint. |
| Configuration Point | Description |
| --- | --- |
| ICP Definition | Job titles, company sizes, sectors, geographies, and signals that define the target prospect |
| Wealth / Fit Score Threshold | Minimum composite score required to enter the active outreach pipeline |
| Signal Algorithm Parameters | Which signal types to monitor: funding, M&A, hiring, property, press, regulatory — configurable per vertical |
| Content Library Themes | The expertise domains the practitioner publishes on — used for content-to-prospect matching |
| PSQ Threshold | Minimum pre-send quality score before a message is sent — adjustable per deployment |
| Channel Priority Rules | Which channels to use at which lifecycle stages — configurable based on where the ICP is most responsive |
| Lifecycle Timing | Day marks for each stage can be compressed or extended depending on typical B2B sales cycle length |
| Human Escalation Rules | Score thresholds and stage triggers that flag a prospect for direct practitioner attention |
| Term | Definition |
| --- | --- |
| ICP | Ideal Client Profile — the defined set of attributes that characterise the highest-value target prospect for a given deployment |
| PSQ | Pre-Send Quality Score — Claude-generated 1-100 score assessing the personalisation specificity and relevance of a message before it is sent |
| Sales Battlecard | A two-page AI-generated intelligence brief delivered to the sales advisor before every prospect meeting. Contains the prospect profile, enrichment summary, Why Now signal, LinkedIn activity highlights, conversation starters, talking points, and relevant content reference. Generated on demand — always reflects the most current intelligence. |
| Why Now Signal | The specific trigger event (funding, M&A, property, regulatory, press, leadership change) that makes outreach to a prospect timely and relevant at this particular moment. The most important element of the Sales Battlecard. |
| Signal Event | A detected piece of intelligence about a prospect (news, funding, property, regulatory) that triggers re-personalisation, battlecard refresh, or escalation |
| Lifecycle Stage | One of six defined states in the 360-day contact lifecycle (Day 0 / 30 / 60 / 90 / 180 / 270 / 360) |
| Parallel Tracks | The simultaneous operation of a LinkedIn outreach track and an Email outreach track for the same prospect |
| Content Library | The structured Supabase store of parsed LinkedIn content assets used as the source of personalisation for all outreach and battlecard content references |
| Touch | A single outbound message within a LinkedIn sequence (Connection Request, Touch 1 = first DM, Touch 2 = follow-up, Touch 3 = final LinkedIn message) |
| Unipile | The unified messaging API that handles all outbound and inbound communication across LinkedIn, Email, and WhatsApp |
| Revenue Decay | The progressive reduction in conversion probability as a prospect ages without engagement — measured and countered by the 360-day lifecycle engine |