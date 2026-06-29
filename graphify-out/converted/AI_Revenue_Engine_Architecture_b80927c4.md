<!-- converted from AI_Revenue_Engine_Architecture.docx -->


AI REVENUE ENGINE™
for Local Businesses
Agent Orchestration Architecture  ·  v2.0


OpenClaw  ·  InsForge  ·  Supabase  ·  Twilio  ·  Cal.com  ·  Smartlead
KlickSmart AI  ·  Vancouver, BC  ·  March 2026

# 1. Executive Summary

The AI Revenue Engine™ is a fully automated lead-to-booked-appointment system built for local home service businesses. It is sold as a done-for-you (DFY) service initially, with a white-label path as KlickSmart AI scales.
A single sentence captures what the client experiences:


Behind that sentence is a 6-layer technology stack with OpenClaw as the orchestrating brain, a two-database architecture (InsForge for agency-level operations, Supabase per client for full data isolation), Twilio for 2-way SMS, Cal.com for booking, and Smartlead for cold email.

Phase 1 targets two Metro Vancouver verticals: plumbers and HVAC contractors. The system is architected to scale horizontally — adding a new vertical or a new client requires cloning a client template, not rebuilding the system.



# 2. System Stack Overview

Six layers. Each layer has one owner, one responsibility, and communicates with adjacent layers through defined interfaces. OpenClaw sits at the centre — it is the only layer with read/write access across all others.

↕  REST API (InsForge CRM) + Supabase Realtime (client data)  ↕
↕  MCP read/write · Supabase SDK per client · REST API calls  ↕
↕  MCP · Twilio API · Cal.com API · Smartlead API · gws MCP  ↕
↕  Lead data flows up · Booking confirmations flow up · Reply triggers flow up  ↕
↕  Scraped from Google Maps via Lead Sniper · Enriched via Hunter.io  ↕

## 2.1 Stack Responsibilities at a Glance



# 3. Database Architecture

Two databases serve two different purposes. They are never merged. OpenClaw is the only system that reads from both.

## 3.1 InsForge — Agency Operations Database


## 3.2 Supabase — Per-Client Database

Schema is identical across all client projects — provisioned from a Supabase template on client onboarding.


## 3.3 How OpenClaw Connects to Each Client's Supabase
Each client record in InsForge stores that client's Supabase project URL and anon key. When OpenClaw spawns an agent for a specific client, it passes those credentials as context. The agent uses the Supabase SDK to connect to that client's isolated project.

// Pattern: OpenClaw fetches client credentials from InsForge

// then passes to spawned agent as environment context



const client = await insforge.db.read("clients", { id: clientId });



const supabase = createClient(

  client.supabase_project_url,   // e.g. https://xyzabc.supabase.co

  client.supabase_anon_key       // scoped to this client only

);



// Agent now reads/writes ONLY this client's isolated data
await supabase.from("leads").insert({ name, phone, stage: "New" });


# 4. OpenClaw Orchestrator

OpenClaw is the only component that touches every other layer. It does not do the work itself — it classifies incoming events, spawns the correct specialist agent, passes the right credentials, and monitors completion.

## 4.1 Identity Files

## 4.2 Master Router — Event Classification
Every event enters through the Master Router. It classifies the event type and dispatches to the correct agent with the correct client context attached.

INCOMING EVENT TYPES → DISPATCH TARGET

─────────────────────────────────────────────────────

new_sheet_row          → Lead Ingestion Agent

inbound_sms            → SMS Classifier Agent

cal_booking_confirmed  → Stage Update Agent + Notify Agent

sms_no_reply_48h       → SMS Follow-Up Agent

cron_0730              → Morning Report Agent

cron_1800              → Evening Digest Agent

cron_0900_monday       → Weekly Report Agent

cron_every_60m         → Telemetry Check Agent

cron_every_6h          → Lead Enrichment Sync

slack_command          → Parse intent → Route to agent
unknown                → Log + Slack alert to Dennis

Router model: Haiku. Classification is high-volume, low-complexity. Haiku handles this at fractions of a cent per event.

## 4.3 Cron Schedule (HEARTBEAT)


# 5. Complete Agent Roster

19 agents across 4 domains. Every agent has a single responsibility, a fixed model tier, scoped database access, and defined output. No agent has broader permissions than its task requires.

## 5.1 Lead Pipeline Agents


## 5.2 SMS Conversation Agents


## 5.3 Booking & Stage Agents


## 5.4 Reporting Agents



# 6. Core Revenue Workflow

This is the end-to-end flow that generates revenue for every client. Lead found → qualified → SMS conversation → appointment booked. Every step is automated. Human review is only required on SMS drafts before the first send.

## 6.1 Lead Found → Appointment Booked


## 6.2 No-Reply Follow-Up Path



# 7. Twilio SMS Architecture

Each client gets a dedicated Twilio phone number. All 2-way SMS conversations for that client flow through that number. OpenClaw manages the conversation state in the client's Supabase sms_threads table.

## 7.1 Twilio Configuration Per Client

## 7.2 SMS Message Rules (Enforced by QC Reviewer)
- Max 160 characters for single SMS — no concatenated messages on first contact
- Must include business name in first SMS: "Hi [Name], this is [Business] — ..."
- Must reference something specific — no generic openers
- One CTA per message — either a question OR a booking link, never both
- No pricing in first 3 messages — qualify first
- CASL-compliant: implied consent from publicly listed business phone number is sufficient for B2B SMS in Canada
- Opt-out always honoured within 10 seconds via Twilio auto-reply + Opt-Out Handler Agent


# 8. Cal.com Booking Architecture

Cal.com handles all appointment scheduling. Each client gets their own Cal.com account with a branded booking page. The Cal.com webhook fires into the Stage Update Agent on every booking confirmation.

## 8.1 Cal.com Configuration Per Client


# 9. Client Onboarding & White-Label Path

## 9.1 DFY Onboarding Checklist (Phase 1)
Every new client goes through this checklist. Target: client is live and generating first SMS conversations within 5 business days of signing.


## 9.2 White-Label Upgrade Path
As KlickSmart scales past 10 clients, the DFY model becomes a white-label product. The architecture already supports this — no rebuilding required.


## 9.3 Pricing Model


# 10. VPS Deployment Architecture

All agency infrastructure runs on a single Hetzner VPS. Client Supabase projects run in Supabase cloud (one project per client). Client Twilio numbers are managed centrally but billed per client.

## 10.1 Docker Compose Services

## 10.2 Infrastructure Costs (Agency Side)



# 11. Phased Build Sequence

Seven phases. Each phase is independently testable. Do not move to the next phase until the exit criteria is met. This sequence is designed to be executed in Claude Code with this document as context.



# 12. Outstanding Items




# Appendix A — Agent Model Assignment


# Appendix B — Webhook Endpoint Map


# Appendix C — VPS File Structure

/opt/klicksmart/

  docker-compose.yml

  .env                            # All secrets — NEVER commit to git

  openclaw/

    Soul.md                       # Agent identity + values

    User.md                       # Dennis + KlickSmart business context

    HEARTBEAT.md                  # Full cron schedule

    clients/

      torres-plumbing.md          # Client context file

      lee-hvac.md

      [one file per client]

    skills/

      lead-ingestion/SKILL.md

      sms-opener/SKILL.md

      sms-classifier/SKILL.md

      sms-responder/SKILL.md

      morning-report/SKILL.md

      [one folder per agent]

  insforge/

    migrations/001_clients.sql

    migrations/002_agent_log.sql

    migrations/003_agency_metrics.sql

  supabase-template/

    migrations/001_leads.sql      # Applied to EVERY new client project

    migrations/002_sms_threads.sql

    migrations/003_appointments.sql

    migrations/004_activities.sql

  webhook-receiver/

    index.js                      # Express app receiving Twilio + Cal.com events

    routes/twilio.js

    routes/cal.js

  crm-frontend/

    index.html                    # Full SPA

    nginx.conf

  gws/
    client_secret.json            # Google OAuth — NEVER commit

# Appendix D — Vertical Expansion Playbook

Adding a new vertical (e.g. electricians, landscapers) requires only three things:
- Update Lead Sniper to scrape the new vertical in the target service area
- Create a vertical-specific context file referenced by SMS Opener Agent for industry-specific pain points and hooks
- Register a new Twilio 10DLC campaign for the vertical (if the messaging angle differs from plumbing/HVAC)

No backend changes. No new agents. No new database tables. The architecture is vertical-agnostic by design.

| ELEVATOR
PITCH | "We install an AI system that finds leads, contacts them, follows up, and books appointments automatically — 24/7." |
| --- | --- |
| WHAT THIS
DOC COVERS | 1. The full 6-layer system stack with data flow
2. The two-database architecture (InsForge agency + Supabase per client)
3. Complete agent roster with model assignments and tool permissions
4. The core revenue workflow: Lead Found → SMS Conversation → Appointment Booked
5. Client onboarding template (DFY) and white-label upgrade path
6. VPS deployment architecture and Docker Compose service map
7. Phased build sequence ready for Claude Code execution |
| --- | --- |
| CLIENT PORTAL  What the client sees  ·  Supabase-backed dashboard
Leads table · Appointment calendar · SMS conversation log · Revenue metrics · Campaign status |
| --- |
| AGENCY MASTER  What you see  ·  InsForge dashboard
All clients · Pipeline health · Agent status · Revenue across accounts · Billing |
| --- |
| OPENCLAW  The AI brain  ·  Orchestrator + all sub-agents
Routes every trigger · Spawns specialist agents · Manages cron jobs · Holds Soul.md + User.md memory |
| --- |
| COMMUNICATION LAYER  How leads are contacted  ·  Twilio · Smartlead · Cal.com
Twilio: 2-way SMS conversations with leads  ·  Smartlead: cold email sequences (optional)  ·  Cal.com: appointment booking links + webhook confirmations |
| --- |
| DATA LAYER  Where everything is stored  ·  InsForge (agency) + Supabase (per client)
InsForge: agency ops, agent logs, billing, cross-client metrics  ·  Supabase: one isolated project per client — leads, SMS threads, appointments, notes |
| --- |
| LEAD SOURCE  Where leads come from  ·  Lead Sniper AI · Google Maps
Scrapes plumbers and HVAC contractors in Metro Vancouver · Exports to Google Sheet · Ingested by Lead Ingestion Agent every 6 hours |
| --- |
| Tool | Role | Accessed By | Who Pays |
| --- | --- | --- | --- |
| OpenClaw | AI orchestrator — runs all agents and cron jobs | Everything | KlickSmart (agency cost) |
| InsForge | Agency CRM + agent ops database + master dashboard | Agency only | KlickSmart (agency cost) |
| Supabase | Per-client database — leads, SMS, bookings (1 project per client) | OpenClaw + client portal | Per client (~$25/mo) |
| Twilio | 2-way SMS conversations with leads | OpenClaw SMS agents | Per client (usage-based) |
| Cal.com | Appointment booking — hosted scheduling pages + webhooks | OpenClaw + client portal | Per client ($12/mo) |
| Smartlead | Cold email sequences (optional add-on) | OpenClaw outreach agents | Per client ($39/mo) |
| Lead Sniper AI | Google Maps scraping for plumber/HVAC leads | Lead Ingestion Agent | KlickSmart (agency tool) |
| Hunter.io | Email finding + verification | Enrichment Agent | KlickSmart (agency cost) |
| Google Workspace CLI | Gmail + Sheets + Calendar access via MCP | Reporting agents | KlickSmart (agency cost) |
| PURPOSE | Tracks everything that belongs to KlickSmart as an agency: client accounts, agent health, billing, cross-client metrics, and the master ops log. No client lead data lives here. |
| --- | --- |
| Table | Key Fields | Used By |
| --- | --- | --- |
| clients | id, business_name, vertical, supabase_project_url, supabase_anon_key, twilio_number, cal_link, status, mrr, onboarded_at | Master dashboard, client provisioning |
| agent_log | id, client_id, agent_name, task_type, status, duration_ms, error_msg, created_at | Telemetry Check Agent, Mission Control |
| billing | id, client_id, plan, amount, billing_date, status | Agency reporting, Stripe integration |
| agency_metrics | date, total_clients, total_leads, total_appointments, total_replies, avg_conversion | Weekly agency report to Dennis |
| PURPOSE | Each client gets their own Supabase project. Total data isolation — one client's leads, SMS threads, and appointments are never co-mingled with another client's data. This is the architecture that lets you white-label. |
| --- | --- |
| Table | Key Fields | Used By |
| --- | --- | --- |
| leads | id, name, business_name, phone, email, address, vertical, source, score, stage, sms_opted_in, consent_date, created_at, updated_at | All pipeline agents, client portal |
| sms_threads | id, lead_id, direction (inbound/outbound), body, twilio_sid, sent_at, classification (POSITIVE/QUESTION/TIMING/OPT_OUT) | SMS agents, client portal conversation view |
| appointments | id, lead_id, cal_booking_uid, scheduled_at, status (pending/confirmed/no_show/completed), notes | Stage Update Agent, Cal.com webhook, client portal |
| notes | id, lead_id, content, author (agent name or "human"), created_at | All agents, client portal lead detail |
| activities | id, lead_id, action_type, metadata JSONB, created_at | Activity timeline in client portal |
| campaign_stats | date, leads_contacted, sms_sent, replies, appointments_booked, conversion_rate | Client dashboard metrics, weekly report |
| File | Contents |
| --- | --- |
| Soul.md | OpenClaw's persona: "Chief Revenue Officer for KlickSmart AI clients." Core values: never send without consent check, never book without lead confirmation, always log every action. Prevents generic chatbot drift. |
| User.md | Dennis's context: KlickSmart ICP (plumbers + HVAC, Metro Vancouver), active clients list, agency Slack channel IDs, Google Sheet IDs for Lead Sniper exports, Smartlead account ID, agency Hetzner VPS IP. |
| HEARTBEAT.md | Full cron schedule: which agents fire at what times, what they check, which Slack channel they report to, and what constitutes a failure condition requiring human escalation. |
| clients/*.md | One file per client: business name, vertical, Supabase project URL, Twilio number, Cal.com link, target service area, ICP (e.g. "homeowners in Burnaby/Coquitlam"), active campaign status. |
| Schedule | Agent | What It Does |
| --- | --- | --- |
| 07:30 AM daily | Morning Report | Pipeline summary, hot leads needing action, SMS reply digest, appointment count for today |
| Every 30 min | SMS Monitor | Check Twilio for inbound messages across all client numbers, dispatch to SMS Classifier |
| Every 6 hours | Lead Ingestion Sync | Read Lead Sniper Google Sheet for new rows, ingest to client Supabase |
| Every 60 min | Telemetry Check | Audit agent_log for failures, flag hallucinated completions, update Mission Control |
| 06:00 PM daily | Evening Digest | Action items, leads that need human touch, bounces, opt-outs processed |
| Monday 09:00 AM | Weekly Report | Write metrics to Google Sheet, post Slack card with week-over-week for each client |
| 48h after SMS sent | Follow-Up Trigger | If no reply to initial SMS, dispatch SMS Follow-Up Agent with new angle |
| Agent | Model | Trigger | Output | Tools | Writes To |
| --- | --- | --- | --- | --- | --- |
| Lead Ingestion | Haiku | New Google Sheet row (Lead Sniper) | Create lead in client Supabase, stage = "New" | gws Sheets, Supabase SDK | leads table |
| Lead Enrichment | Sonnet | New lead with no email/score | Add email, score 0-100, pain indicators, tech stack | Hunter.io API, EnrichLayer | leads.email, leads.score |
| CASL Guard | Haiku | Before any outbound contact | PASS or BLOCK — checks consent + opt-out list | Supabase (read-only) | None (gate only) |
| Signal Detection | Haiku | Batch of new enriched leads | JSON: signal_type, outreach_angle per lead | Supabase read | leads.signal_data |
| Agent | Model | Trigger | Output | Tools | Writes To |
| --- | --- | --- | --- | --- | --- |
| SMS Opener | Sonnet | Lead enriched + CASL cleared | Personalised opening SMS referencing signal | Twilio API, Supabase | sms_threads, leads.stage |
| SMS Classifier | Sonnet | Inbound SMS received (Twilio webhook) | Classify: POSITIVE / QUESTION / TIMING / OPT_OUT / UNKNOWN | Supabase read | sms_threads.classification |
| SMS Responder | Sonnet | Classification = POSITIVE or QUESTION | Draft contextual reply, include Cal.com link if POSITIVE | Supabase read, Twilio API | sms_threads (outbound) |
| SMS Follow-Up | Haiku | 48h cron — no reply to opener | New angle follow-up SMS (value-add, not repeat) | Twilio API, Supabase | sms_threads, leads.stage |
| Opt-Out Handler | Haiku | OPT_OUT classified in SMS | Stop all contact, log opt-out, update Supabase | Twilio API, Supabase | leads.sms_opted_in = false |
| SMS QC Reviewer | Sonnet | Any draft SMS before send | Score 1-10: tone, CASL compliance, CTA. PASS or REVISE | Supabase read | None (gate only) |
| Agent | Model | Trigger | Output | Tools | Writes To |
| --- | --- | --- | --- | --- | --- |
| Stage Update | Haiku | Cal.com webhook OR positive SMS classified | Move kanban stage, log activity in Supabase | Supabase SDK | leads.stage, activities |
| Appointment Notifier | Haiku | Cal.com booking confirmed | SMS confirmation to lead + Slack alert to client | Twilio API, Slack, Supabase | appointments, sms_threads |
| No-Show Handler | Haiku | Cal.com no-show event | Send re-booking SMS, update appointment status | Twilio API, Supabase | appointments.status, sms_threads |
| Agent | Model | Trigger | Output | Tools | Writes To |
| --- | --- | --- | --- | --- | --- |
| Morning Report | Sonnet | Cron 07:30 AM | Slack card: pipeline stats, hot leads, today's appointments | InsForge + all Supabase clients, Slack MCP | agency_metrics |
| Weekly Report | Sonnet | Cron Mon 09:00 AM | Google Sheet row + Slack summary per client | InsForge + Supabase clients, gws Sheets | campaign_stats |
| Evening Digest | Haiku | Cron 06:00 PM | Action items needing human review, opt-outs, bounces | InsForge + Supabase, Slack MCP | agent_log |
| Telemetry Check | Haiku | Cron every 60 min | Audit agent completions, flag failures, update Mission Control | InsForge agent_log | agent_log.status |
| 1 | Lead Sniper AI | Scrapes Google Maps for plumbers/HVAC contractors in Metro Vancouver. Exports new businesses to shared Google Sheet. |
| --- | --- | --- |
| 2 | Lead Ingestion Agent (Haiku) | Reads new Sheet rows every 6 hours. Creates lead record in client's Supabase project. Sets stage = "New". Attaches client context (vertical, service area). |
| 3 | Lead Enrichment Agent (Sonnet) | Hunter.io finds/verifies email. EnrichLayer adds company size, review data, tech signals. Scores lead 0-100. Stores enrichment on Supabase lead record. |
| 4 | Signal Detection Agent (Haiku) | Analyses enriched lead for buying signals (bad reviews, hiring signals, new location). Returns outreach_angle JSON stored on lead. |
| 5 | CASL Guard (Haiku) | Verifies no prior opt-out. Checks consent requirements. BLOCKS if non-compliant. PASSES lead to SMS queue. |
| 6 | SMS Opener Agent (Sonnet) | Drafts personalised opening SMS referencing the signal. Max 160 chars. References specific pain point. Includes client business name. Sends via Twilio. |
| 7 | SMS QC Reviewer (Sonnet) | Reviews draft for tone, CASL footer, CTA clarity. PASS → SMS sends. REVISE → returns to Opener with specific fixes. |
| 8 | Lead receives SMS | Twilio delivers SMS from client's dedicated number. Lead replies (or doesn't). |
| 9 | SMS Classifier Agent (Sonnet) | Twilio inbound webhook triggers classifier. Classifies reply: POSITIVE / QUESTION / TIMING / OPT_OUT / UNKNOWN. |
| 10 | SMS Responder Agent (Sonnet) | If POSITIVE: replies with value statement + Cal.com booking link. If QUESTION: answers specifically + soft CTA. If TIMING: logs for 30-day follow-up. |
| 11 | Cal.com booking | Lead clicks link, books appointment on client's Cal.com page. Webhook fires on confirmation. |
| 12 | Stage Update Agent (Haiku) | Receives Cal.com webhook. Updates lead stage to "Appointment Booked" in Supabase. Logs activity. |
| 13 | Appointment Notifier (Haiku) | SMS confirmation to lead. Slack alert to client with lead name, business, and appointment time. |
| 1 | 48h Cron Trigger | HEARTBEAT fires — checks all leads in "Contacted" stage with no inbound SMS in 48 hours. |
| --- | --- | --- |
| 2 | SMS Follow-Up Agent (Haiku) | Generates new-angle follow-up. Different hook from opener (case study result, seasonal angle, or competitor reference). Max 160 chars. |
| 3 | QC Reviewer (Sonnet) | Same QC gate as initial send. PASS or REVISE. |
| 4 | Second SMS sends | Twilio delivers. If no reply after 7 more days → third and final "break-up" SMS. Then lead moves to "Nurture" stage. |
| Config Item | Value / Notes |
| --- | --- |
| Phone number type | Local long code (10DLC) — matches client's area code. E.g. 604-XXX-XXXX for Metro Vancouver clients. |
| Inbound webhook | POST to https://[vps-ip]/webhooks/sms/inbound?client_id=[id] — triggers SMS Classifier Agent |
| Status callback | POST to https://[vps-ip]/webhooks/sms/status — logs delivery status to sms_threads |
| Opt-out keywords | STOP, UNSUBSCRIBE, CANCEL, END — Twilio auto-handles + webhook fires Opt-Out Handler Agent |
| Messaging Service | One Messaging Service per client — enables 10DLC compliance registration for Canadian SMS |
| Daily send limit | Max 200 SMS/day per number during warmup, scale to 500+ after 30 days of clean sending |
| Config Item | Value / Notes |
| --- | --- |
| Event type | "Free Consultation" or "[Service] Assessment" — 30-minute default. Client sets their own availability. |
| Booking page URL | cal.com/[client-slug]/consultation — sent in POSITIVE SMS responses |
| Confirmation webhook | POST to https://[vps-ip]/webhooks/cal/booking?client_id=[id] — triggers Stage Update Agent |
| Cancellation webhook | POST to https://[vps-ip]/webhooks/cal/cancel?client_id=[id] — reverts stage, queues re-booking SMS |
| No-show webhook | POST to https://[vps-ip]/webhooks/cal/noshow?client_id=[id] — triggers No-Show Handler Agent |
| Reminder SMS | Cal.com native 24h + 1h SMS reminder via Twilio integration — no agent needed for reminders |
| Plan | Cal.com Teams ($12/mo) — required for webhook support and team scheduling |
| Day | Task | Owner |
| --- | --- | --- |
| Day 1 | Create client record in InsForge (business name, vertical, service area) | Dennis |
| Day 1 | Provision new Supabase project using client template. Run schema migrations. | Claude Code / Dennis |
| Day 1 | Purchase Twilio local number (604/778 area code). Register 10DLC. Configure inbound webhook. | Dennis |
| Day 1 | Set up Cal.com account for client. Configure event type, availability, webhooks. | Dennis |
| Day 2 | Create client context file (clients/[name].md) in OpenClaw. Include ICP, service area, Twilio number, Cal.com URL. | Dennis |
| Day 2 | Configure Lead Sniper to scrape target vertical + service area. Point export to client Google Sheet. | Dennis |
| Day 3 | Run Lead Ingestion Agent manually on first batch. Verify leads appear in Supabase. | OpenClaw |
| Day 3 | Run Lead Enrichment Agent on first batch. Verify scores and emails attached. | OpenClaw |
| Day 4 | Draft first SMS opener using client context. Review with Dennis. Approve. | Dennis + OpenClaw |
| Day 5 | Send first batch of 20 SMS (warmup volume). Monitor replies. | OpenClaw (Twilio) |
| Day 5 | Verify client dashboard (Supabase-backed) showing leads, SMS threads, stage. | Dennis |
| Upgrade Step | What Changes | What Stays the Same |
| --- | --- | --- |
| Custom domain per client | crm.torresplumbing.com instead of klicksmart.ca/torres — Nginx routing config update | All backend logic unchanged |
| Client self-service portal | Add auth layer to CRM frontend (Supabase Auth) so client logs in directly | OpenClaw still runs everything |
| Branded SMS sender name | Twilio Verified Caller ID + client business name in SMS signature | Same Twilio infrastructure |
| Client manages own Cal.com | Transfer Cal.com account ownership to client, keep webhook URL pointed at KlickSmart VPS | Booking flow unchanged |
| Reseller billing | Client pays KlickSmart directly, Dennis pays Supabase/Twilio/Cal.com wholesale | Margin: ~60-70% at scale |
| Tier | Price | What's Included | Margin |
| --- | --- | --- | --- |
| DFY Starter | $997/mo | Setup + full automation for 1 vertical. Up to 500 SMS/mo. Dashboard access. Monthly report. | ~65% after stack costs |
| DFY Growth | $1,497/mo | Everything in Starter + cold email via Smartlead + 2 verticals + weekly report call. | ~60% after stack costs |
| White-Label | $497/mo (SaaS) | Client runs own portal. KlickSmart provides infrastructure + OpenClaw. Min 10 clients. | ~75% at scale |
| Setup Fee | $997 one-time | Supabase provisioning, Twilio setup, Cal.com config, first lead batch, SMS warmup. | ~80% margin |
| Service | Image | Port | Purpose |
| --- | --- | --- | --- |
| openclaw | openclaw/openclaw | 18789 (internal) | AI orchestrator. Mounts Soul.md, User.md, HEARTBEAT.md, clients/, skills/ |
| insforge | insforge/insforge | 7131 (internal) | Agency backend API + MCP server + Model Gateway |
| postgres | postgres:16 | 5432 (internal) | InsForge database. Persistent named volume. |
| crm-frontend | nginx:alpine | 80 (proxied) | Agency master dashboard + client portal SPA |
| webhook-receiver | node:22 | 3000 (internal) | Receives Twilio + Cal.com webhooks, dispatches to OpenClaw |
| nginx-proxy | nginx:alpine | 443 (public) | SSL termination. Routes /api → insforge, /webhooks → webhook-receiver, / → crm-frontend |
| Item | Monthly Cost | Notes |
| --- | --- | --- |
| Hetzner CX21 VPS | ~€6 (~$9) | 2 vCPU / 4GB RAM / 40GB SSD. Sufficient for 20+ clients. |
| OpenClaw Claude API | $100–200 | Haiku-first routing. Sonnet for SMS + reports. Scales with client count. |
| Google Workspace | $6/user | Dennis's account for gws CLI (Gmail, Sheets, Calendar) |
| Hunter.io | $49 | Starter — 500 email finds/mo. Upgrade as client count grows. |
| Lead Sniper AI | Agency tool | Already owned. Shared across all client campaigns. |
| InsForge | Self-hosted | No licence cost. Runs on the same VPS. |
| TOTAL AGENCY INFRA | ~$170–260/mo | Fixed cost regardless of client count up to ~20 clients. |
| UNIT ECONOMICS | Agency infra: ~$200/mo fixed
Per-client variable: Supabase ~$25 + Twilio ~$20 usage + Cal.com $12 = ~$57/mo per client
Revenue per DFY Starter client: $997/mo + $997 setup
At 5 clients: Revenue $4,985/mo · Costs ~$485/mo · Margin ~$4,500/mo (90%)
At 10 clients: Revenue $9,970/mo · Costs ~$770/mo · Margin ~$9,200/mo (92%) |
| --- | --- |
| Phase | Work | Exit Criteria |
| --- | --- | --- |
| Phase 1
Infrastructure | Provision Hetzner VPS. Install Docker + Compose. Deploy InsForge + PostgreSQL. Create InsForge clients table. Set up Nginx proxy with SSL. | InsForge dashboard loads at https://[domain]. Database has clients table. SSL certificate valid. |
| Phase 2
OpenClaw Core | Deploy OpenClaw container. Create Soul.md, User.md, HEARTBEAT.md. Connect InsForge MCP. Test with: "list all clients in the database." | OpenClaw responds with real InsForge data. MCP handshake confirmed. |
| Phase 3
First Client | Provision client Supabase project from template. Create clients/torres-plumbing.md. Purchase Twilio number. Configure Cal.com. Add client record to InsForge. | Client record in InsForge. Supabase project live with schema. Twilio number active. |
| Phase 4
Lead Pipeline | Build Lead Ingestion + Enrichment + CASL Guard + Signal Detection agents. Connect Lead Sniper Google Sheet. Run first manual batch import. | 10+ real leads in client Supabase. Enriched with scores. CASL check passing. |
| Phase 5
SMS Engine | Build SMS Opener + Classifier + Responder + Follow-Up + Opt-Out Handler agents. Deploy webhook-receiver service. Wire Twilio inbound webhook. | Send one real SMS to a test lead. Receive reply. Classifier correctly categorises it. Responder drafts appropriate reply. |
| Phase 6
Booking + Staging | Build Stage Update + Appointment Notifier + No-Show Handler agents. Configure Cal.com webhooks. Test full flow end-to-end. | Full flow test: Sheet row → SMS → reply → booking link → Cal.com confirmation → Supabase stage updated → Slack notification sent. |
| Phase 7
Dashboard + Reporting | Deploy CRM frontend. Wire InsForge agency view + Supabase client view. Build Morning Report + Weekly Report agents. Activate full HEARTBEAT cron. | Dashboard shows real data for first client. Morning report fires at 07:30 and posts to Slack. Weekly report writes to Google Sheet. |
| NOTE | These items must be resolved before the corresponding phase can complete. None block Phases 1-3. |
| --- | --- |
| Item | Blocks | Owner / Notes |
| --- | --- | --- |
| EnrichLayer API key | Phase 4 (Lead Enrichment Agent) | Account setup pending. Hunter.io is the email-only fallback. |
| Google OAuth credentials | Phase 2 (gws CLI for Sheets + reporting) | Google Cloud Console project. Enable Calendar, Drive, Gmail, Sheets APIs. 15-min setup. |
| Lead Sniper Google Sheet ID | Phase 4 (Lead Ingestion Agent) | Create shared Sheet. Configure Lead Sniper to export to it. Share with OpenClaw service account. |
| First client signed | Phase 3 | Need real client (plumber or HVAC) to provision Supabase + Twilio for. IDC can serve as internal test client in the meantime. |
| Twilio 10DLC registration | Phase 5 (SMS sends) | Required for Canadian local numbers. ~3-5 day approval. Register as soon as first client is signed. |
| Cal.com account per client | Phase 6 (booking flow) | Create Cal.com Teams account per client on onboarding. $12/mo per client. |
| IDC value prop copy (Kevan) | IDC-specific agents | Existing IDC build. Needed for Reply Handler prompt for advisor recruiting sequence. |
| Model | Use For (in this system) |
| --- | --- |
| Haiku (Tier 1)
~60% of tasks | Lead Ingestion · CASL Guard · Signal Detection · SMS Follow-Up · Opt-Out Handler · Stage Update · Appointment Notifier · No-Show Handler · Evening Digest · Telemetry Check · Master Router classification |
| Sonnet (Tier 2)
~38% of tasks | Lead Enrichment · SMS Opener · SMS Classifier · SMS Responder · SMS QC Reviewer · Morning Report · Weekly Report · Advisor Qualifier (IDC) |
| Opus (Tier 3)
<2% of tasks | Architecture decisions · High-stakes copy review when Sonnet is clearly insufficient · Never used in scheduled/automated tasks |
| Endpoint | Source | Triggers |
| --- | --- | --- |
| POST /webhooks/sms/inbound?client_id=X | Twilio | SMS Classifier Agent for client X |
| POST /webhooks/sms/status?client_id=X | Twilio | Log delivery status to sms_threads |
| POST /webhooks/cal/booking?client_id=X | Cal.com | Stage Update Agent + Appointment Notifier |
| POST /webhooks/cal/cancel?client_id=X | Cal.com | Stage revert + re-booking SMS queue |
| POST /webhooks/cal/noshow?client_id=X | Cal.com | No-Show Handler Agent |
| POST /webhooks/smartlead/reply?client_id=X | Smartlead | Reply Handler Agent (optional email path) |