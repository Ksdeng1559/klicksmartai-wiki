# Klick2Client OS — Product Definition v1.0

**Source:** Klick2Client_OS_Product_Definition_v1.0.docx
**Version:** 1.0
**Date:** 2026-04-18
**URL:** www.klick2client.com
**Status:** Core Framework — ** This is the basic framework to build on**

---

## What It Is

Klick2Client OS is a **B2B client acquisition operating system** that transforms LinkedIn authority and expertise into a continuous, autonomous pipeline of qualified prospects.

- Any B2B practitioner with expertise can deploy it
- LinkedIn is the primary lead generation source
- Two independent entry paths (warm + cold)
- Human-in-the-loop governance: Claude drafts, practitioner approves every message

> *"The shift from 'I am prompting an AI' to 'I am managing a team' changes everything."* — This is that shift, applied to B2B sales.

---

## The 6-Layer Architecture

| Layer | Name | Responsibility |
|-------|------|----------------|
| 1 | Content Engine | LinkedIn authority content → reusable downstream assets (hooks, value statements, proof points, CTAs) |
| 2 | Signal Intelligence | Continuous prospect monitoring via Brave, Tavily, Gemini Grounding + signal algorithm |
| 3 | Enrichment Layer | Python scripts build full prospect profile → primary output is the **Sales Battlecard** |
| 4 | LinkedIn Conversion Module | Profile analysis, activity scraping, personalized 3-touch sequence generation |
| 5 | Lifecycle Engine | 360-day parallel-track outreach (LinkedIn + Email) via Unipile |
| 6 | Intelligence Feedback Loop | Pre-send quality scoring + post-send conversion tracking → Claude auto-adjusts strategy |

---

## The Two Entry Paths

### Path 1 — Content-Driven (Warm)
1. Practitioner publishes authoritative LinkedIn content
2. Person likes/comments/shares → Unipile detects engagement
3. ICP filter applied → profile enriched via Unipile
4. Claude drafts DM referencing the specific post
5. **Human approval queue** → PSQ score + reasoning shown
6. Practitioner approves → Unipile sends → prospect enters lifecycle engine

### Path 2 — Enriched Lead List (Cold)
1. Lead Sniper HNW identifies ICP prospect (not yet engaged with content)
2. Python enrichment scripts build full profile
3. Signal intelligence runs (Brave, Tavily, Gemini, AI Now)
4. LinkedIn profile + activity scraped via Unipile
5. Claude drafts connection request + 3-touch DM sequence
6. **Human approval queue** → all drafts ranked by ICP fit score
7. Practitioner approves → sent in sequence → lifecycle engine

**Governance (both paths):** Claude drafts and scores. Practitioner approves. No exceptions.

---

## Pre-Send Quality Score (PSQ)

| PSQ Range | Meaning | Claude Action |
|-----------|---------|---------------|
| 90-100 | Highly specific, verifiable personal/company detail referenced | Queue immediately |
| 75-89 | Good personalization, minor generic elements | Queue |
| 60-74 | Moderate personalization, missing specific hooks | Regenerate once → if still <75, queue amber |
| <60 | Generic/template-like, poor signal data | Regenerate twice → if still <60, queue red with gap note |

---

## 360-Day Lifecycle Engine

**Parallel tracks (both always running):**
- **LinkedIn Track:** Connection Request → Touch 1 → Touch 2 → Touch 3
- **Email Track:** Day 0 → Day 30 → Day 60 → Day 90 → Day 180 → Day 270

**Kanban Pipeline Stages:**
1. First Contact → 2. Actual Contact → 3. Calendar Booked → 4. Final Proposal → 5. Close (Won/Lost)

**Reply handling:** Webhook fires → lifecycle pauses → Kanban card moves → human notification triggered.

---

## Sales Battlecard (Primary Enrichment Output)

**What it is:** Two-page AI-generated intelligence brief delivered to the advisor before every meeting. Generated on demand — always current.

**Page 1 — Who They Are:**
- Prospect identity (photo, name, title, company, location, tenure)
- Enrichment summary (previous roles, board positions, qualifications)
- **Why Now Signal** ← most important element (funding/M&A/property/regulatory/press/leadership change)
- LinkedIn Activity Highlights (3 most recent relevant signals)

**Page 2 — How to Have the Conversation:**
- Conversation Starters (grounded in prospect's own content/signals)
- Talking Points (4-6 bridges from prospect's situation to advisor's value prop)
- Relevant Content Reference (practitioner's LinkedIn post most relevant to this prospect)
- Next Step Suggestion (Claude-suggested, advisor decides)

---

## Technology Stack

| Layer | Technology | Role |
|-------|-----------|------|
| Language | Python | All business logic, enrichment scripts, agent orchestration |
| Database | Supabase (PostgreSQL) | Cloud-hosted, multi-client, source of truth |
| AI | Claude API (Anthropic) | Stage decisions, message generation, quality scoring |
| Unified Messaging | Unipile | LinkedIn, Email, WhatsApp outbound + inbound |
| Video Outreach | Dubb, Vidyard | Dubb: Chrome extension + CRM automation. Vidyard: AI avatars, Video Agent, enterprise integrations. Both increase human connection rate. |
| Scheduling | APScheduler | Python-native cron — nightly batch + continuous monitoring |
| Web UI / Webhooks | FastAPI + Jinja2 | Kanban board, KPI dashboard, Unipile webhook receiver |
| AI Inference | Ollama (local, KlickSmartAI OS) | Local model runtime (qwen3-vl:8b writing, qwen2.5:3b wiki, qwen3 reasoning), streaming, tool calling, vision, embeddings, web search. Host: host.docker.internal:11434 |
| HTTP Client | httpx (async) | Concurrent API calls |
| Data Validation | Pydantic | Validates data shapes between all layers |
| Signal Sources | Brave, Tavily, Gemini, AI Now | Real-time intelligence — news, web research, grounding |
| Internal Knowledge | Onyx | Enterprise AI search, 45+ permission-aware connectors (SharePoint, Confluence, Salesforce, Slack), self-hosted, SOC 2 Type II. For financial services: air-gapped capable, PIPEDA-aligned, battlecard enrichment from firm docs.
| Lead Generation | Lead Sniper HNW | Top-of-funnel prospect detection |

---

## File Architecture

Every file ≤300 lines of logic code. No exceptions.

| File | Responsibility |
|------|----------------|
| `scheduler/lifecycle_runner.py` | Nightly batch: queries contacts due, coordinates agents |
| `scheduler/signal_monitor.py` | Continuous signal watching, triggers re-personalization |
| `webhooks/unipile_receiver.py` | FastAPI inbound event handler for Unipile callbacks |
| `agents/lifecycle_agent.py` | Claude decides stage action and channel per contact |
| `agents/message_builder.py` | Claude generates email content per lifecycle stage |
| `agents/conversion_analyzer.py` | Evaluates personalization effectiveness, surfaces recommendations |
| `battlecard/battlecard_generator.py` | Assembles data sources, calls Claude for synthesis, renders two-page brief |
| `battlecard/pdf_exporter.py` | Converts battlecard to downloadable PDF on demand |
| `linkedin_module/profile_analyzer.py` | Fetches + parses LinkedIn profile via Unipile |
| `linkedin_module/activity_scraper.py` | Extracts posts and engagement as personalization hooks |
| `linkedin_module/linkedin_agent.py` | Claude generates and scores LinkedIn sequence content |
| `linkedin_module/sequence_builder.py` | Touch 1/2/3 logic, timing, channel rules |
| `intelligence/signal_monitor.py` | Signal algorithm placeholder, ready for injection |
| `kanban/board_api.py` | FastAPI routes serving Kanban and KPI dashboard |
| `kanban/board_logic.py` | Stage rules, parallel track resolution, card movement logic |
| `db/schema.sql` | All Supabase table definitions, indexes, RLS policies |
| `db/supabase_client.py` | All database read/write, no business logic |
| `integrations/unipile_client.py` | Unipile API wrapper, all channel send/receive |
| `config/settings.py` | Environment variables, stage constants, scoring thresholds |
| `main.py` | Starts APScheduler, FastAPI server, all background services |

---

## Database Schema (8 tables in Supabase)

| Table | Purpose |
|-------|---------|
| `contacts` | Enriched prospect profile from Lead Sniper HNW — master record |
| `content_library` | Parsed LinkedIn content assets: hooks, proof points, value statements, CTAs |
| `lifecycle_events` | Stage tracking per contact per channel — lifecycle state machine |
| `messages` | Every message sent + received across all channels via Unipile |
| `linkedin_sequences` | LinkedIn 3-touch sequence state, profile data, activity hooks |
| `signal_events` | Intelligence signals detected per contact, source-attributed, timestamped |
| `kanban_cards` | Pipeline stage per contact, parallel track statuses, override flags |
| `conversion_kpis` | Aggregated KPI data: funnel metrics, PSQ performance, signal attribution |

---

## 9-Phase Build Roadmap

| Phase | Name | Deliverables | Business Value |
|-------|------|-------------|----------------|
| 1 | Foundation | schema.sql, settings.py, supabase_client.py | Lead Sniper contacts flow into Klick2Client OS |
| 2 | Content Engine | content_library table, content parsing scripts | LinkedIn content becomes personalization source |
| 3 | Enrichment + Battlecard | enrichment scripts, battlecard_generator.py, PDF export | Fresh intelligence brief before every meeting |
| 4 | Messaging Infrastructure | unipile_client.py, message_builder.py, lifecycle_agent.py | Automated lifecycle emails running via Unipile |
| 5 | Signal Intelligence | signal_monitor.py (placeholder + algorithm injection) | Real-time intelligence triggers re-personalization |
| 6 | LinkedIn Module | profile_analyzer, activity_scraper, linkedin_agent, sequence_builder | Personalized 3-touch sequences with quality scoring |
| 7 | Feedback Loop | conversion_analyzer.py, unipile_receiver.py, lifecycle_runner.py | System surfaces conversion recommendations |
| 8 | Kanban + KPI UI | board_logic, board_api, board.html, kpi_dashboard.html | Full pipeline visibility + conversion analytics |
| 9 | Integration | main.py — wires all services into single entry point | One command runs entire Klick2Client OS |

---

## Vertical Adaptation (No Code Changes Required)

Configuration points per deployment:
- ICP Definition (titles, company sizes, sectors, geographies, signals)
- Wealth/Fit Score Threshold
- Signal Algorithm Parameters
- Content Library Themes
- PSQ Threshold
- Channel Priority Rules
- Lifecycle Timing
- Human Escalation Rules

**Example verticals:** Professional Services, Financial Services (HNW), Technology/SaaS, Recruitment

---

## Glossary

| Term | Definition |
|------|-----------|
| ICP | Ideal Client Profile — defined target prospect attributes |
| PSQ | Pre-Send Quality Score — 1-100 Claude score before sending |
| Sales Battlecard | Two-page AI-generated brief before every prospect meeting |
| Why Now Signal | The specific trigger making outreach timely right now |
| Signal Event | Detected piece of intelligence triggering re-personalization |
| Lifecycle Stage | One of 6 defined states in the 360-day lifecycle |
| Parallel Tracks | Simultaneous LinkedIn + Email tracks for the same prospect |
| Content Library | Structured store of parsed LinkedIn content assets |
| Touch | Single outbound message in a LinkedIn sequence |
| Revenue Decay | Progressive reduction in conversion probability over time |

---

## Relationship to KlickSmartAI OS

| Klick2Client OS (product) | KlickSmartAI OS (Dennis's agency layer) |
|--------------------------|----------------------------------------|
| The full product — B2B client acquisition system | Dennis's agency delivery methodology on top |
| Supabase as database | DuckDB + MotherDuck for analytics layer |
| FastAPI + Jinja2 UI | Hermes Telegram interface |
| Lead Sniper HNW | WealthWireRadar signal system |
| Claude API (Anthropic) | Ollama local models (qwen3-vl:8b, etc.) |
| Phase-by-phase build | Client delivery using this methodology |

**KlickSmartAI OS adds to Klick2Client OS:**
- 147 MIT-licensed The Agency agents (workforce layer)
- Paperclip.ing human control plane model (Dennis as CEO)
- Multi-client agency delivery methodology
- DuckDB + MotherDuck for analytics (replace Supabase for some clients)
- Hermes as the orchestration layer (replace/augment FastAPI)

---

## Source

- Document: `Klick2Client_OS_Product_Definition_v1.0.docx`
- Product: Klick2Client OS | www.klick2client.com | Confidential