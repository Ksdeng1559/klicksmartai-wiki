<!-- converted from doc_dda1961ee32d_BOSS-RaaS-v3-Revenue-Conversion-Machine.docx -->

BOSS v3
Multi-Channel Revenue Conversion Machine
Results as a Service  ·  Financial Services Vertical  ·  v3.0  ·  March 2026



◆  SECTION 1 — ARCHITECTURE UPGRADE: V2 → V3  ◆

# 1. What Changed and Why
The v2 architecture was validated as top-5% thinking for a lead enrichment system. But the analysis identified five structural gaps that prevent it from becoming a true Revenue OS. Each gap is documented here with its fix.

## 1.1  The Five Gaps Fixed in v3




◆  SECTION 2 — BOSS V3 SEVEN-LAYER ARCHITECTURE  ◆

# 2. The Seven-Layer Revenue OS
BOSS v3 operates as seven interdependent layers. Each layer has a single responsibility. Data flows downward during execution. Learning flows upward from Layer 5 (Feedback) back to Layer 3 (Intelligence). This is what makes the system adaptive rather than static.










◆  SECTION 3 — UNIFIED CONTEXT ARCHITECTURE  ◆

# 3. Solving Context Fragmentation
The silent killer of multi-agent systems is context fragmentation — each agent knows only part of the picture. An enrichment agent and a scoring agent and an outreach agent running on different context windows will produce contradictory outputs. BOSS v3 solves this with a shared context layer that every agent reads from before executing.

## 3.1  The /context/ Directory
A structured JSON context store lives in Supabase and is mounted as a Project Knowledge file in the BOSS Claude Project. Every agent reads the relevant context file at the start of each task. Context is versioned — a change to scoring_weights.json triggers a version bump and a notification to all agents using it.


## 3.2  Context JSON Schema — ICP Example

{
"client_name": "Pinnacle Financial Partners",
"vertical": "Financial Advisor",
"geography": ["British Columbia", "Alberta", "Ontario"],
"company_size_range": {"min_advisors": 1, "max_advisors": 20},
"aum_range": {"min_M": 10, "max_M": 500},
"decision_maker_titles": ["Owner", "Managing Partner", "Principal Advisor", "Branch Manager"],
"buying_triggers": ["hiring_advisor", "aum_plateau", "compliance_change", "competitor_exit", "technology_upgrade"],
"pain_keywords": ["prospecting", "client acquisition", "lead flow", "referrals drying up", "junior advisor"],
"exclusions": ["wirehouses", "banks", "clients_of_client_list.csv"],
"suppression_list_path": "gs://boss-raas/pinnacle/suppression.csv",
"offer_priority": ["database_reactivation", "lead_enrichment_engine", "conversion_audit"]
}

## 3.3  Intelligence Layer Output Schema
This is the enrichment output that gets passed to the Execution Engine. It replaces the old 'contact info only' output format. Every field is required before a lead enters the outreach queue.

{
"lead_id": "uuid",
"lead_score": 82,
"company": "Summit Wealth Management",
"contact": {"name": "Sarah Chen", "title": "Managing Partner", "email": "s.chen@summit.ca", "linkedin": "linkedin.com/in/sarahchen"},
"signal": {"type": "hiring_advisor", "source": "LinkedIn Jobs", "date": "2026-03-18", "strength": 9},
"intent": "Scaling client acquisition — hiring suggests AUM growth target",
"pain": "Lead flow inconsistent — junior advisor hire is a Band-Aid, not a system",
"hook": "Saw you're hiring a junior advisor — most firms find that doubles workload before it helps",
"recommended_offer": "Database Reactivation Engine",
"channel_routing": {"primary": "email", "secondary": "linkedin_dm", "score_threshold_met": true},
"compliance_status": "cleared",
"created_at": "2026-03-19T07:34:00Z"
}


◆  SECTION 4 — SIGNAL-FIRST WATERFALL ENRICHMENT  ◆

# 4. Refactored Enrichment Waterfall
The v2 enrichment sequence went straight from signal to email hunting. This wastes 60–80% of enrichment budget on signals that would fail qualification. The v3 waterfall front-loads a signal qualification gate — only strong signals get enriched.


Before spending any API credits on enrichment, the signal must pass three checks:
- Signal strength score ≥ configured threshold (default: 6/10 for warm, 8/10 for hot)
- Signal recency: detected within the last 7 days (older signals deprioritized to nurture pool)
- Not in suppression list: company + contact not in client_history.json exclusions
- ICP match: company size, geography, and industry match ICP.json parameters
IF signal fails any check → discard to cold pool (not deleted — retained for nurture sequences). IF signal passes → proceed to Stage 2.


Before hunting for email, resolve the full identity of the company and target contact. This prevents wasting waterfall attempts on the wrong person.
- Company → Domain: website scrape + LinkedIn company page to confirm domain pattern
- LinkedIn Graph: Apify LinkedIn Search Scraper — find people with ICP titles at the company
- Role Match: Claude Haiku validates title against decision_maker_titles[] in ICP.json
- Champion identification: also flag champion_titles[] contacts for a parallel sequence
- Output: confirmed company domain + target contact LinkedIn profile URL + role confidence score



Low confidence emails from pattern inference are placed in a separate queue — they require a validation pass before entering the outreach sequence.




This is the stage most enrichment systems skip entirely. After contact is validated, Claude Sonnet (not Haiku — this is where the money is made) reads the full signal context and generates the four intelligence fields that make every outreach feel custom-written.



◆  SECTION 5 — MULTI-CHANNEL EXECUTION ENGINE  ◆

# 5. Execution Engine — From Lead to Conversation
The Execution Engine is the layer that transforms enriched intelligence payloads into booked meetings. It operates across three channels — email (Smartlead AI), LinkedIn DM, and Instagram DM — with channel selection determined by lead score and signal type, not by calendar schedule.


## 5.1  Channel Routing Logic


## 5.2  Smartlead AI Integration
Smartlead AI is the email execution layer. BOSS does NOT manually upload lead lists to Smartlead. The OpenClaw → Smartlead Sync Agent pushes qualified leads via Smartlead API with the full intelligence payload as custom variables. Every email is generated from those variables — making each one appear individually written.

### Smartlead Campaign Architecture
Build four signal-based campaign buckets in Smartlead — not one generic campaign. Each bucket has its own email sequence and custom variable mapping:


### Signal-Based Email Sequence Structure


## 5.3  LinkedIn DM Methodology
LinkedIn DM is the secondary channel for hot leads (score ≥ 80). It runs in parallel with the email sequence — not as a substitute. The DM methodology follows a four-step conversation framework that is conversation-first, not pitch-first.



## 5.4  Instagram DM Methodology
Instagram DM is relevant for financial services professionals who run a personal brand — common among younger independent advisors and insurance agents. It follows the same four-step conversation framework as LinkedIn but with shorter, more casual language. Only activate for contacts with an active Instagram presence (10+ posts in last 90 days).


Instagram DM sequence: Day 0 context entry (reference a specific post or content piece) → Day 3 insight drop → Day 7 soft CTA. Three touches maximum on Instagram before moving to email only.

## 5.5  Lead Lists — Correct Usage
Lead lists (Apollo exports, purchased lists, referral lists) are fuel for the pipeline, not the strategy. They enter the system at the Signal Qualification Gate (Stage 1 of the waterfall) and are treated as 'low signal strength' until enrichment confirms a buying signal.



◆  SECTION 6 — EVENT-DRIVEN ARCHITECTURE  ◆

# 6. From Batch Jobs to Real-Time Triggers
The v2 system ran on daily cron jobs. Signal detected at 6am, enriched at 7am, delivered at 8am. That's a 2-hour lag from signal to outreach initiation. In competitive financial services prospecting, the advisor who responds to a buying signal in 2 hours beats the one who responds in 24. BOSS v3 uses event-driven architecture to compress that lag.

## 6.1  Event Bus Architecture
The event bus routes real-time signals from detection sources to the agents that act on them. Supabase Realtime handles internal events (database changes). n8n webhooks handle external events (Apify actor completions, Smartlead reply webhooks, Gmail incoming messages).


## 6.2  n8n Workflow Orchestration
n8n is the glue layer that connects external webhooks (Apify, Smartlead, Gmail) to Supabase and OpenClaw. It runs on the same VPS as OpenClaw — zero additional infrastructure cost. Key workflows:

- Apify → Supabase: Actor completes → webhook fires → n8n parses result JSON → writes to signals or contacts table via agent-ingest Edge Function
- Smartlead → Supabase: Reply received → webhook fires → n8n extracts reply data → writes to replies table → triggers Reply Classifier
- Supabase → Smartlead: Qualified lead approved → n8n reads from contacts table → POST to Smartlead API → assigns to correct campaign bucket with custom variables
- Gmail → Supabase: Incoming email to monitored address → n8n parses → writes to email_threads table → triggers Reply Classifier if matches active outreach sequence


◆  SECTION 7 — FEEDBACK LOOP & ADAPTIVE SCORING  ◆

# 7. The Learning Engine
The difference between a static lead generation system and an adaptive revenue OS is the feedback loop. BOSS v3 recalibrates its scoring model every Sunday night based on the previous week's outcomes. The system learns what converts and auto-adjusts to produce more of it.

## 7.1  The Closed-Loop Cycle


## 7.2  DuckDB Analytics Queries — The Learning Set
These five DuckDB queries run every Sunday as part of the Conversion Auditor workflow. The results power both the weekly client report and the scoring recalibration.



◆  SECTION 8 — COMPLIANCE LAYER  ◆

# 8. The Compliance Agent
Adding cold outreach at scale in financial services is high-risk territory. CASL, CAN-SPAM, FINRA, OSC, and FCA rules create real legal exposure if the system sends non-compliant messages. The Compliance Agent is not optional — it is a hard gate that every outbound message passes through before execution.


## 8.1  Compliance Agent — Pre-Send Checklist
Every message generated by the Outreach Swarm passes through the Compliance Agent before entering the send queue. This is a Haiku-powered gate (fast, cheap) with a Sonnet escalation path for flagged messages.


## 8.2  Data Handling Architecture



◆  SECTION 9 — OPENCLAW → SMARTLEAD SYNC ARCHITECTURE  ◆

# 9. Automating the Lead → Campaign Pipeline
The most common mistake with Smartlead is treating it as a manual upload tool. BOSS v3 never touches the Smartlead dashboard for lead imports. All lead-to-campaign assignments happen via API, triggered by OpenClaw when a lead passes the Quality Gate and operator approval.

## 9.1  Sync Agent Workflow


## 9.2  Reply Classification → Action Routing



◆  SECTION 10 — UPDATED AGENT WORKFORCE  ◆

# 10. Full Agent Workforce Registry
Every agent in BOSS v3 is listed here with its model, schedule, inputs, outputs, and the layer it belongs to. This is the operating manual for the Agent Workforce.



◆  SECTION 11 — V3 BUILD SEQUENCE  ◆

# 11. Phased Build Roadmap — v3
The v3 architecture is built in four phases. Each phase is deployable and revenue-generating before the next phase starts. You do not need Phase 4 complete to bill clients — Phase 1 generates CPL revenue from Day 30.


- All 15 Supabase tables provisioned (8 core + 7 v2 additions)
- Unified context layer: /context/ directory with ICP.json, scoring_weights.json, signal_patterns.json, offer_map.json
- Signal Scanner + Signal Qualification Gate (pre-enrichment filter)
- Full Signal-First Waterfall (S1→S5) with multi-layer validation
- Intelligence Builder producing complete payload (intent/pain/hook/offer)
- Quality Gate → Google Sheets approval queue → manual email delivery via gws
- Compliance Agent: pre-send checklist active
- First client onboarded, first billable leads delivered
- Exit: 20+ qualified leads delivered, CPL billing active, 15-min daily rhythm achieved


- n8n installed on VPS — Apify → Supabase + Smartlead → Supabase webhooks configured
- OpenClaw → Smartlead Sync Agent built and tested
- Four Smartlead campaign buckets configured with custom variable mapping
- Signal-Based Email Sequence (4-email, 9-day) deployed per campaign
- LinkedIn DM Methodology: Apify automation with velocity limits configured
- Reply Classifier Agent: 6-classification routing logic active
- Meeting Booker Agent: INTERESTED reply → draft calendar response → operator approval queue
- Exit: First meeting booked via system. Output metric shifts from 'leads delivered' to 'meetings booked per week'


- DuckDB installed on VPS — 5 weekly analytics queries operational
- Lead Scoring Recalibrator: Sunday night weight update cycle active
- Conversion Auditor: weekly Doc delivered to client Drive every Wednesday
- Retention Agent: weekly risk scoring with operator alerts at ≥70 risk
- Instagram DM added for contacts with active Instagram presence + score ≥ 75
- score_weights.json versioning with operator approval gate
- Exit: scoring model has recalibrated at least twice. Measurable improvement in meeting rate vs. Week 1 baseline.


- OpenClaw fully autonomous: signal scan → enrich → score → approve → send — operator reviews in morning batch (5 min per client)
- Event bus fully real-time: hot signals trigger enrichment within 5 minutes of detection
- Next.js dashboard: operator view replacing Google Sheets for pipeline visibility
- Multi-client data model: client_id isolation across all tables, per-client scoring weights, per-client offer maps
- BOSS Agentic CRM fully operational: system is self-improving, self-monitoring, and self-correcting
- OpenClaw trigger: Client 4 is the activation point for full autonomous operation
- Exit: BOSS is the Revenue Conversion Machine. The operator's job is strategy and oversight — not execution.


BOSS v3 — Multi-Channel Revenue Conversion Machine
v3.0  ·  March 2026  ·  Supersedes BOSS RaaS v1.0 and v2.0  ·  Companion to BOSS MVP Control Document v3.0
CONFIDENTIAL — KlickSmart AI Internal Use Only
| WHAT THIS VERSION CHANGES
v1/v2 built a Lead Delivery Machine. v3 is a Revenue Conversion Machine. The architecture is refactored from a linear pipeline (Signal→Enrich→Qualify→Deliver) into a closed-loop autonomous system (Signal→Enrich→Score→Act→Observe→Learn→Adapt→Repeat). Five critical gaps are addressed: the feedback loop, the execution layer, the event bus, the unified context architecture, and the compliance layer.
New in v3: Event-Driven Architecture · Signal-First Waterfall Enrichment · Smartlead AI Integration · LinkedIn/Instagram DM Methodology · Multi-Channel Orchestration · Compliance Agent · Unified Context Layer |
| --- |
| Gap | v2 Behaviour | v3 Fix | Impact |
| --- | --- | --- | --- |
| Linear pipeline thinking | Signal→Enrich→Qualify→Deliver — stops at delivery, client acts manually | Closed-loop: Signal→Enrich→Score→Act→Observe→Learn→Adapt→Repeat | System compounds — gets smarter every week automatically |
| Weak execution layer | System delivers a lead list. Client does all outreach manually. | Full Execution Engine: Smartlead AI email + LinkedIn DM + Instagram DM + Reply Classifier + Meeting Booker | Revenue pipeline, not a data feed |
| No event bus | Daily batch jobs, manual Claude prompts — creates hours of latency | Supabase Realtime + n8n webhooks — event triggers fire within seconds of signal detection | Real-time sniper system vs. overnight batch |
| Context fragmentation | ICP, scoring, client history scattered across Claude Projects + OpenClaw + gws | Unified /context/ layer: ICP.json + scoring_weights.json + signal_patterns.json + client_history.json shared across ALL agents | Every agent has the same knowledge — no contradictions |
| Weak enrichment output | Output = contact info (email, name, title) | Intelligence output = lead_score + signal + intent + pain hypothesis + hook + recommended_offer | Every outreach feels custom-written — because it is |
| THE CORE DISTINCTION: LEAD SYSTEM vs REVENUE SYSTEM
A lead system outputs data. A revenue system outputs conversations, meetings, and pipeline.
BOSS v3 is a Revenue Conversion Machine. The output metric is not 'leads delivered per week'. It is 'meetings booked per week' and 'deals in pipeline per month'. Every architectural decision flows from that distinction. |
| --- |
| L1 | Signal Engine
Tavily · Apify · Brave · Supabase Realtime | Real-time trigger detection — job postings, rate changes, review spikes, competitor moves. Event bus fires within seconds of signal detection. |
| --- | --- | --- |
| L2 | Enrichment Engine
Apify · Hunter · Apollo · DeBounce · SMTP ping | Signal-First Waterfall — qualify signal before spending enrichment budget. Identity resolution → contact waterfall → multi-layer validation. |
| --- | --- | --- |
| L3 | Intelligence Layer
Claude Sonnet · Haiku · Kimi · DuckDB | Scoring + intent analysis + pain hypothesis + hook generation + offer mapping. Output is a ready-to-deploy outreach payload, not just contact info. |
| --- | --- | --- |
| L4 | Execution Engine
Smartlead AI · LinkedIn DM · Instagram DM · gws Gmail | Signal-triggered multi-channel outreach. Email + DM sequences launched automatically. Reply Classifier routes responses. Meeting Booker closes the loop. |
| --- | --- | --- |
| L5 | Feedback Loop
DuckDB · Supabase · Lead Scoring Agent | Outcomes → DuckDB analytics → weekly scoring recalibration. System learns which signals, hooks, and channels convert. Weights update every Sunday night. |
| --- | --- | --- |
| L6 | Compliance Layer
Compliance Agent · Suppression DB · CASL/CAN-SPAM rules | Every outbound message checked before send. Identity + unsubscribe inserted automatically. Risky claims flagged for operator review. Data retention enforced. |
| --- | --- | --- |
| L7 | Delivery Layer
Google Workspace CLI · Google Sheets · Google Docs · Gmail | Client-facing interface. Master Lead Sheet, Conversion Audit Docs, Weekly Reports, Billing Tracker. Everything the client touches lives here. |
| --- | --- | --- |
| HOW THE LAYERS INTERACT
L1 detects a signal → fires an event to L2. L2 qualifies the signal → enriches to full lead profile → passes to L3. L3 scores, builds intent payload, maps to offer → passes to L4. L4 executes multi-channel outreach, collects replies → passes outcomes to L5. L5 runs DuckDB analytics, recalibrates scoring weights → updates L3. L6 inspects every L4 output before it sends — nothing bypasses compliance. L7 is the client window into all of this.
The operator sits between L3 and L4 — approving the outreach batch each morning. This is the human-in-the-loop gate that protects compliance while capturing 90% of automation value. |
| --- |
| Context File | Contents | Updated By | Read By |
| --- | --- | --- | --- |
| ICP.json | client_name, vertical, company_size_range, geography, decision_maker_titles, champion_titles, buying_triggers[], pain_keywords[], exclusions[] | Manual (operator) on client setup + quarterly review | Signal Scanner · Lead Enricher · Quality Gate · Compliance Agent |
| scoring_weights.json | dimension weights (signal_match, title_authority, email_verified, company_size, signal_recency, engagement_history), version, last_updated | Lead Scoring Agent (every Sunday night via DuckDB recalibration) | Lead Enricher · Quality Gate · Intelligence Layer |
| signal_patterns.json | hot_signals[], warm_signals[], cold_signals[], discard_signals[], signal_to_offer_map{} | Conversion Auditor (weekly update based on conversion data) | Signal Scanner · Intelligence Layer · Execution Engine |
| client_history.json | all_sent_leads[], replied_contacts[], meetings_booked[], disqualified_reasons{}, suppression_list[], channel_performance{} | All agents (append-only) · Retention Agent (weekly summary) | Outreach Swarm · Reply Classifier · Compliance Agent · Retention Agent |
| offer_map.json | signal_type → recommended_offer mapping, offer descriptions, proof points, objection handles for each offer | Manual (operator) per vertical, updated quarterly | Intelligence Layer · Outreach Swarm · Meeting Booker |
| S1 | Signal Qualification Gate
Pre-enrichment filter — save 60–80% of enrichment cost |
| --- | --- |
| S2 | Identity Resolution Layer
Company → Domain → LinkedIn Graph → Role Match |
| --- | --- |
| S3 | Contact Waterfall
Apollo → Hunter → Website scrape → Pattern inference |
| --- | --- |
| Step | Tool | Method | Success Rate | Cost | On Fail |
| --- | --- | --- | --- | --- | --- |
| 1 | Apollo | Direct DB lookup by LinkedIn URL or name+company | ~65% find rate | ~$0.02/lookup | → Step 2 |
| 2 | Hunter.io | Domain search + pattern validation against Apollo result | ~55% find rate on unknowns | ~$0.03/search | → Step 3 |
| 3 | Apify Contact Scraper | Scrape company website contact pages, about pages, team pages | ~30% find rate | ~$0.15/run | → Step 4 |
| 4 | Pattern inference | Apply domain pattern from known contacts at same company | ~40% confidence | ~$0.001 (local) | → flag as LOW CONFIDENCE |
| S4 | Multi-Layer Email Validation
DeBounce + SMTP ping + MX record check |
| --- | --- |
| Validation Step | Tool | What It Checks | Result Action |
| --- | --- | --- | --- |
| MX Record Check | DNS lookup (built-in) | Does the domain have active mail servers? | No MX record → discard immediately |
| DeBounce API | DeBounce | Syntax, domain validity, disposable email, catch-all detection | Status 5 (Safe) → proceed. Status 1/2 → discard. Catch-all → flag for SMTP. |
| SMTP Ping | SMTP handshake (built-in) | Does the specific mailbox exist on the server? | 200 OK → high confidence. 550 → discard. Timeout → flag as uncertain. |
| Engagement history | Supabase client_history.json | Has this email previously hard-bounced or unsubscribed? | In history → block regardless of other validation results |
| S5 | Enrichment Intelligence Layer
Intent · Pain · Hook · Offer — the winning output |
| --- | --- |
| Intelligence Field | Input Used | Model | Output Standard |
| --- | --- | --- | --- |
| Intent | Signal type + company size + hiring/growth indicators + ICP buying triggers | Sonnet | One sentence: what is this company trying to achieve RIGHT NOW based on the signal |
| Pain hypothesis | Intent + ICP pain_keywords + signal context + offer_map.json | Sonnet | One sentence: the specific operational pain this intent is creating that they haven't solved yet |
| Hook | Signal + pain + contact title + client_history (to avoid repeat hooks) | Sonnet | One sentence opener: references something specific and real, creates pattern break, no pitch |
| Recommended offer | Pain hypothesis + offer_map.json signal_to_offer mapping | Haiku (lookup) | The single best-fit offer from offer_map.json for this specific pain + signal combination |
| THE STRATEGIC DISTINCTION — PRECISION vs VOLUME
The wrong way to use this system: load 1,000 leads into Smartlead, send a template blast, measure open rates.
The right way: every lead enters the execution engine with a fully loaded intelligence payload (intent, pain, hook, offer). The email and DM are generated from that specific payload. Volume is a byproduct of the system running correctly — not the objective.
The test: if you removed the prospect name and company from any outreach message and it still made sense, it is not signal-driven. That is a templated blast. Signal-driven outreach is impossible to send to the wrong person. |
| --- |
| Lead Score | Primary Channel | Secondary Channel | Sequence Timing | Rationale |
| --- | --- | --- | --- | --- |
| ≥ 80 (Hot) | Email (Smartlead) Day 1 | LinkedIn DM Day 3 | Aggressive — 4 touches over 9 days | Signal is strong, intent is clear, move fast before signal ages |
| 60–79 (Warm) | Email (Smartlead) Day 1 | LinkedIn view Day 4 | Standard — 3 touches over 7 days | Good signal, qualified ICP — standard sequence, don't over-invest |
| 40–59 (Cool) | Email only Day 1 | None | Minimal — 2 touches over 14 days | Signal present but weak. Single email, one follow-up, then nurture pool. |
| < 40 (Cold) | Nurture pool | None | Monthly newsletter cadence | No active signal. Do not cold outreach. Add to nurture, re-evaluate when signal emerges. |
| Campaign Bucket | Trigger Signal | Custom Variables Used | Sequence Type |
| --- | --- | --- | --- |
| Campaign A — Hiring Signal | LinkedIn job posting detected (advisor/sales/client services role) | {{signal}}, {{intent}}, {{pain}}, {{hook}}, {{offer}} | 4-email sequence, 9 days |
| Campaign B — Rate/Market Change | Rate drop announcement or market event affecting their vertical | {{signal}}, {{market_context}}, {{pain}}, {{hook}}, {{offer}} | 3-email sequence, 7 days |
| Campaign C — Database Reactivation | Client's own old lead list uploaded for reactivation | {{last_interaction}}, {{pain}}, {{hook}}, {{offer}} | 5-email sequence, 21 days |
| Campaign D — Competitor/Review Signal | Competitor office closure, negative review spike, or personnel departure | {{signal}}, {{opportunity_context}}, {{hook}}, {{offer}} | 3-email sequence, 7 days |
| Day | Email Purpose | Opening Line Pattern | CTA |
| --- | --- | --- | --- |
| Day 0 | Signal-Based Opener | '{{hook}}' — references the exact signal, no generic opener | One soft question about their current situation |
| Day 2 | Insight Drop | 'Most [vertical] firms at this stage...' — pattern interrupt with a non-obvious truth | Implicit — no explicit ask |
| Day 5 | Micro Proof | 'We mapped this for a firm like yours in [geography]...' — outcome reference without case study | 'Worth a 12-minute look?' |
| Day 9 | Loop Closer | 'Should I close this out or send the [offer] overview?' — binary close | 'Just reply Y or N' |
| Step | Name | Purpose | Message Pattern | Length |
| --- | --- | --- | --- | --- |
| 1 | Context Entry | Establish relevance with a specific reference — never a generic opener | 'Hey [Name], saw [specific signal] — quick question...' | 1 sentence |
| 2 | Pattern Break | Say something non-obvious that creates curiosity. Reference a counterintuitive truth about their situation. | 'Most firms I see at this stage aren't short on leads — they're losing warm ones.' | 2 sentences max |
| 3 | Micro Value | Offer one specific, tangible thing — a mapped insight, a framework, a question they haven't asked themselves | 'We built a system that reactivates old pipelines automatically — happy to show you what it found for a similar firm.' | 2–3 sentences |
| 4 | Soft CTA | One question, no pressure. Binary or open-ended. Never ask for 'a call' in the first DM. | 'Want me to map it for your current database?' | 1 sentence |
| LINKEDIN AUTOMATION VELOCITY LIMITS (COMPLIANCE)
LinkedIn aggressively restricts automated connection requests and message sends. Exceeding limits triggers account restriction.
Safe daily limits: 20 connection requests per day maximum · 50 messages to 1st-degree connections per day · 0 automated InMails (these are always manual)
Technical requirement: LinkedIn DM automation runs through Apify LinkedIn actors with human-like delays (2–8 minutes between actions). Never use instant-send tools. Rate-limit all sequences at the agent config level. |
| --- |
| Activation Criteria | Message Tone | Best Use Case | Daily Limit |
| --- | --- | --- | --- |
| Contact has active Instagram (10+ posts/90 days) + score ≥ 75 | Casual, direct, no corporate language | Independent advisors and agents under 45 who post financial content or personal brand content | 15–20 DMs per day per account |
| Lead List Type | Signal Strength Assigned | Enters At | Sequence Assigned |
| --- | --- | --- | --- |
| Seed lists (fresh ICP build from Apollo/Apify) | Warm (score starts at 50, enrichment adjusts) | Stage 2 of waterfall — skip Signal Qualification | Campaign A or B depending on first signal found |
| Gap fill (ICP match but no current signal) | Cool (score starts at 35) | Enters nurture pool — monitor for signal emergence | Monthly nurture email only until signal detected |
| Database Reactivation (client's old leads) | Variable — score based on last interaction date | Campaign C — Database Reactivation sequence | Dedicated reactivation sequence (21 days, 5 touches) |
| Referral lists | Hot (score starts at 65, boosted by referral trust) | Stage 3 of waterfall — email validation only | Priority queue — immediate enrichment and outreach |
| Event | Source | Trigger Method | Agent Activated | Target Latency |
| --- | --- | --- | --- | --- |
| New job posting detected | Apify LinkedIn Jobs Actor (scheduled 2x/day) | Apify webhook → n8n → Supabase INSERT → Realtime | Signal Qualification Gate → Identity Resolution | < 5 minutes from detection |
| Rate change announced | Tavily search monitor (hourly for rate keywords) | n8n scheduled check → Supabase INSERT → Realtime | Signal Scanner → Campaign B trigger | < 30 minutes from announcement |
| Review spike detected | Apify Google Maps monitor (daily) | Apify webhook → n8n → Supabase INSERT | Signal Scanner → Campaign D trigger | < 2 hours from detection |
| Smartlead reply received | Smartlead webhook | Smartlead → n8n → Supabase replies table | Reply Classifier Agent → routing logic | < 2 minutes from reply |
| Gmail reply received | Gmail webhook (gws Realtime) | Gmail push notification → n8n → Supabase | Reply Classifier Agent → routing logic | < 1 minute from reply |
| Lead score drops below threshold | Supabase score update | Supabase Realtime trigger | Retention Agent → risk assessment | Immediate — database trigger |
| Invoice overdue 7+ days | Supabase billing table | Supabase Realtime + scheduled check | Retention Agent → operator alert | Daily check at 9am |
| Cycle Stage | Day/Time | Action | Data Written |
| --- | --- | --- | --- |
| Execute | Mon–Fri | Outreach Swarm sends email + DM sequences based on current scoring weights | outreach_sequences table — all sends logged |
| Observe | Ongoing (real-time) | Reply Classifier captures responses, Meeting Booker logs outcomes | replies table + meetings table |
| Analyze | Sunday 6pm | DuckDB query: signal_type × outcome, hook_category × reply_rate, score_band × meeting_rate, channel × conversion_rate | duckdb_snapshots table |
| Learn | Sunday 8pm | Lead Scoring Agent reads DuckDB snapshot, identifies over/underperforming dimensions | Drafts new score_weights.json version |
| Adapt | Sunday 10pm | Operator reviews proposed weight changes (simple Y/N approval) | score_weights.json updated → version bumped → all agents notified |
| Repeat | Monday 6am | Signal Scanner runs with updated weights — higher-quality signals surface first | System is measurably smarter than last week |
| Query Name | What It Measures | Recalibration Action |
| --- | --- | --- |
| signal_conversion_matrix | For each signal type: leads delivered, emails sent, replies received, meetings booked, conversion rate | Signal types with meeting_rate < 5% → reduce signal_match weight contribution. Signal types with meeting_rate > 25% → increase weight. |
| hook_effectiveness | For each hook category: sent count, reply rate, positive sentiment rate | Hook categories with reply_rate < 3% → flagged for Sonnet rewrite. Top-performing hooks → added to signal_patterns.json as templates. |
| channel_roi | Email vs. LinkedIn DM vs. Instagram DM: sends, replies, meetings, cost per meeting | Channel with cost_per_meeting > 2× median → reduce routing priority for that score band. |
| score_band_validation | For each score band (80+, 60–79, 40–59, <40): actual meeting rate vs. predicted | If 60–79 band is outperforming 80+ band → scoring formula has a miscalibrated dimension. Trigger full weight review. |
| time_to_response | Hours from signal detection to outreach send, broken by campaign type | If avg > 4 hours for hot signals → flag event bus latency issue to operator. |
| REGULATORY EXPOSURE — FINANCIAL SERVICES SPECIFIC
CASL (Canada): Requires implied or express consent for commercial electronic messages. Implied consent exists if the prospect has an existing business relationship with the sender OR the contact information is publicly displayed with no opt-out indication. Violation penalties: up to $10M per violation for corporations.
CAN-SPAM (US): Requires clear sender identification, honest subject lines, physical mailing address, and a working opt-out mechanism. Penalties: up to $51,744 per email.
FINRA/OSC/FCA: Prohibit misleading claims about financial products and unlicensed financial advice in any communication. Automated outreach that implies financial recommendations without licensing is a regulatory violation. |
| --- |
| Check | Rule | Pass Condition | Fail Action |
| --- | --- | --- | --- |
| Sender identity | CASL + CAN-SPAM: sender must be clearly identifiable | Message contains operator's name, company, and contact information | AUTO-INSERT sender block if missing |
| Unsubscribe mechanism | CASL + CAN-SPAM: functional opt-out required in every commercial email | Email contains unsubscribe link OR plain-text opt-out instruction | BLOCK send — add unsubscribe before re-queue |
| Subject line honesty | CAN-SPAM: no deceptive subject lines | Subject line does not contain false urgency, fake personal references, or misleading claims | FLAG for operator review |
| Financial advice claims | FINRA/OSC/FCA: no unlicensed financial recommendations | Message does not contain specific investment/insurance/mortgage advice or rate guarantees | BLOCK send — escalate to Sonnet for rewrite |
| Suppression check | CASL + CAN-SPAM: opt-outs must be honoured permanently | Contact email not in suppression list (checked against client_history.json) | BLOCK send — add to permanent suppression |
| LinkedIn velocity | LinkedIn ToS: no automation spam | Connection request count < 20/day, message count < 50/day for that account | QUEUE for next available slot — do not skip |
| Consent classification | CASL: implied vs. express consent | Signal type checked against consent_map (public job posting = implied consent) — documented | LOG consent basis with every send |
| Requirement | Implementation | Location |
| --- | --- | --- |
| Data retention policy | Leads older than 24 months with no interaction automatically archived (not deleted) to cold storage | Supabase scheduled Edge Function — runs 1st of each month |
| Right-to-delete workflow | Delete request received → remove from contacts, activities, outreach_sequences, replies tables → add email to permanent suppression list | Manual trigger by operator — 48-hour SLA |
| Suppression list enforcement | Every outreach generation step cross-checks against suppression list before writing to queue | client_history.json suppression_list[] checked at Stage 1 (Signal Qualification) AND at Compliance Agent gate |
| Cross-channel suppression | Opt-out via email removes from ALL channels (LinkedIn DM, Instagram DM, future channels) | Single suppression list in client_history.json — channel-agnostic |
| Consent documentation | Each send logged with: consent_basis (implied/express), consent_source (public profile / prior relationship), signal_date | outreach_sequences table: consent_basis + consent_source columns |
| Step | Actor | Action | API / Tool |
| --- | --- | --- | --- |
| 1 | Quality Gate (Haiku) | Lead batch approved by operator in Google Sheets approval tab | gws Sheets API — operator writes 'Y' in approval column |
| 2 | OpenClaw Sync Trigger | Supabase Realtime detects approval column update → fires sync event | Supabase Realtime → n8n webhook |
| 3 | n8n Sync Workflow | Reads approved leads from Supabase contacts table with full intelligence payload | Supabase REST API |
| 4 | Campaign Assignment Logic | Maps signal_type to Smartlead campaign ID using signal_patterns.json offer map | Local lookup — no API call |
| 5 | Smartlead API Push | POST to Smartlead /leads endpoint with contact data + custom variables ({{hook}}, {{pain}}, {{offer}}, {{signal}}) | Smartlead REST API |
| 6 | Confirmation Write | Writes Smartlead lead_id back to Supabase contacts table for reply tracking | Supabase agent-ingest Edge Function |
| 7 | Reply Webhook Active | Smartlead reply webhook fires on any response → n8n → Reply Classifier Agent | Smartlead webhook → n8n |
| Reply Classification | Definition | Automated Action | Operator Required? |
| --- | --- | --- | --- |
| INTERESTED | Positive reply, requests info, asks for call, or expresses timing | Meeting Booker Agent drafts calendar availability reply — queued for operator approval | Yes — operator approves reply before send |
| NOT NOW | Acknowledges outreach, timing not right, 'check back in X months' | Tag contact in Supabase: nurture_until date set. Removed from active sequence. Re-queues at date. | No — fully automated |
| REFERRAL | Refers to someone else at company or network | New contact created in Supabase with referral_source tag. Enters waterfall at Stage 2. | No — automated entry, operator notified |
| WRONG PERSON | Not the right contact, redirects to someone else | Existing record updated. New contact name/info extracted and entered at Stage 2. | No — automated |
| UNSUBSCRIBE | Any variation of opt-out request | Immediately added to permanent suppression across all channels. Removed from all active sequences. | No — fully automated, logged |
| OBJECTION | Price, timing, competitor, or trust objection | Objection type classified and logged. Objection Handler Agent drafts response based on objection_handles in offer_map.json. Queued for operator review. | Yes — operator reviews objection response |
| Agent | Layer | Model | Schedule / Trigger | Input | Output → Destination |
| --- | --- | --- | --- | --- | --- |
| Signal Scanner | L1 | Haiku | 2x daily 6am/2pm + event triggers | ICP.json + Tavily/Brave/Apify sources | signals table — urgency-scored |
| Signal Qualifier | L2 | Haiku | Realtime on signal INSERT | Signal record + ICP.json + suppression list | PASS → Identity Resolution · FAIL → cold pool |
| Identity Resolver | L2 | Haiku | After Signal Qualifier PASS | Signal record + ICP.json | Confirmed company domain + LinkedIn profile URL |
| Contact Waterfall | L2 | Haiku (routing) + API calls | After Identity Resolver | Company domain + LinkedIn URL | Validated email + confidence score → contacts table |
| Intelligence Builder | L3 | Sonnet | After Contact Waterfall | Full lead record + signal + ICP.json + offer_map.json | Complete intelligence payload (intent/pain/hook/offer) |
| Lead Scorer | L3 | Haiku | After Intelligence Builder | Lead record + scoring_weights.json | lead_score 0–100 → contacts table |
| Quality Gate | L3 | Haiku | After Lead Scorer | Scored lead batch | Google Sheets approval queue — awaits operator |
| Compliance Agent | L6 | Haiku + Sonnet escalation | Before every outbound send | Outreach message draft + compliance rules | CLEARED → send queue · BLOCKED → operator queue |
| Outreach Swarm | L4 | Sonnet (email/DM writing) | After operator approval | Intelligence payload + channel routing | Smartlead campaign + LinkedIn DM + Instagram DM |
| Reply Classifier | L4 | Haiku | Realtime on reply received | Reply text + contact record | Classification → action routing |
| Meeting Booker | L4 | Sonnet | On INTERESTED classification | Reply context + calendar availability | Draft reply → operator approval queue |
| Objection Handler | L4 | Sonnet | On OBJECTION classification | Objection type + offer_map objection_handles | Draft response → operator approval queue |
| Retention Agent | L5 | Haiku + Sonnet | Weekly Monday 7am | client_history + activities + billing data | Retention risk scores → alerts → retention_signals table |
| Conversion Auditor | L5 | DuckDB + Sonnet | Weekly Wednesday 7am | 5 DuckDB queries + prior week outcomes | Conversion Audit Doc → client Drive + scoring recalibration draft |
| Lead Scoring Recalibrator | L5 | Sonnet | Weekly Sunday 10pm (after operator Y/N) | DuckDB snapshot + proposed weight changes | Updated score_weights.json → version bump |
| Daily Report Generator | L7 | Haiku | Daily 8am | All tables — previous day metrics | KPI Sheet row + Daily Summary email → client |
| P1 | Foundation + RaaS Launch (Weeks 1–6)
Supabase · gws · Signal Scanner · Waterfall Enrichment · Quality Gate · Native Claude delivery |
| --- | --- |
| P2 | Execution Engine (Weeks 7–10)
Smartlead AI · LinkedIn DM · Reply Classifier · Meeting Booker · n8n event bus |
| --- | --- |
| P3 | Feedback Loop + Intelligence Upgrade (Weeks 11–14)
DuckDB · Adaptive scoring · Conversion Auditor · Retention Agent · Instagram DM |
| --- | --- |
| P4 | Multi-Client Scale + Agentic CRM (Month 4+)
OpenClaw autonomous · Full event bus · Next.js dashboard · Multi-tenant data model |
| --- | --- |
| THE STRATEGIC DESTINATION
Phase 1 output: 'We deliver enriched leads to your pipeline at CPL.' (Lead Feed System)
Phase 2 output: 'We book meetings for your advisors.' (Outreach Execution Service)
Phase 3 output: 'We run your revenue pipeline — signal to meeting to audit — and the system gets smarter every week.' (Revenue OS)
Phase 4 output: 'We installed an autonomous Revenue Conversion Machine in your business. It runs without you. You review the results.' (Agentic CRM Product)
You are building from Phase 1 revenue to fund Phase 4 infrastructure. Every phase is a complete, billable, valuable product on its own. |
| --- |