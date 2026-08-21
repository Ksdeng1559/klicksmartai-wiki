# Klick2Client OS — Product Entity

**URL:** https://www.klick2client.com
**Agency:** KlickSmartAI (klicksmartai.ca)
**Type:** B2B Client Acquisition Operating System

---

## What It Is

Klick2Client OS is a **GTM Engineering product** — a B2B client acquisition operating system that transforms LinkedIn authority and expertise into a continuous, autonomous pipeline of qualified prospects.

- LinkedIn is the primary lead generation source
- Two independent entry paths: Content-Driven (warm) + Enriched Lead List (cold)
- Human-in-the-loop: Claude drafts, practitioner approves every message
- Full 360-day lifecycle engine with parallel LinkedIn + Email tracks

> *"The shift from 'I am prompting an AI' to 'I am managing a team' changes everything."*

---

## The 6-Layer Architecture

| Layer | Name | Responsibility |
|-------|------|----------------|
| 1 | Content Engine | LinkedIn authority content → reusable assets (hooks, value statements, proof points, CTAs) |
| 2 | Signal Intelligence | Continuous prospect monitoring via Brave, Tavily, Gemini Grounding + signal algorithm |
| 3 | Enrichment Layer | Python scripts build full prospect profile → primary output is the **Sales Battlecard** |
| 4 | LinkedIn Conversion Module | Profile analysis, activity scraping, personalized 3-touch sequence generation |
| 5 | Lifecycle Engine | 360-day parallel-track outreach (LinkedIn + Email) via Unipile |
| 6 | Intelligence Feedback Loop | Pre-send quality scoring + post-send conversion tracking → auto-adjusts strategy |

---

## Two Entry Paths

### Path 1 — Content-Driven (Warm)
1. Practitioner publishes authoritative LinkedIn content
2. Person likes/comments/shares → Unipile detects engagement
3. ICP filter applied → profile enriched via Unipile
4. Claude drafts DM referencing the specific post
5. Human approval queue → PSQ score + reasoning shown
6. Practitioner approves → Unipile sends → prospect enters lifecycle engine

### Path 2 — Enriched Lead List (Cold)
1. Lead Sniper HNW identifies ICP prospect (not yet engaged with content)
2. Python enrichment scripts build full profile
3. Signal intelligence runs (Brave, Tavily, Gemini, AI Now)
4. LinkedIn profile + activity scraped via Unipile
5. Claude drafts connection request + 3-touch DM sequence
6. Human approval queue → all drafts ranked by ICP fit score
7. Practitioner approves → sent in sequence → lifecycle engine

---

## Key Outputs

### Sales Battlecard (Primary Enrichment Output)
Two-page AI-generated intelligence brief delivered before every meeting. Always current, generated on demand.

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

### Pre-Send Quality Score (PSQ)
| PSQ Range | Meaning | Action |
|-----------|---------|--------|
| 90-100 | Highly specific, verifiable personal/company detail | Queue immediately |
| 75-89 | Good personalization, minor generic elements | Queue |
| 60-74 | Moderate personalization, missing specific hooks | Regenerate once → if still <75, queue amber |
| <60 | Generic/template-like, poor signal data | Regenerate twice → if still <60, queue red |

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| Database | Supabase (PostgreSQL) |
| AI | Claude API (Anthropic) |
| Unified Messaging | Unipile (LinkedIn, Email, WhatsApp) |
| Video Outreach | Dubb, Vidyard |
| Scheduling | APScheduler |
| Web UI | FastAPI + Jinja2 |
| AI Inference (local) | Ollama (qwen3-vl:8b, qwen2.5:3b) |
| Signal Sources | Brave, Tavily, Gemini, AI Now |
| Internal Knowledge | Onyx |
| Lead Generation | Lead Sniper HNW |

---

## Relationship to KlickSmartAI OS

| Klick2Client OS (product) | KlickSmartAI OS (Dennis's agency layer) |
|---------------------------|----------------------------------------|
| The full product — B2B client acquisition system | Dennis's agency delivery methodology |
| Supabase as database | DuckDB + MotherDuck for analytics |
| FastAPI + Jinja2 UI | Hermes Telegram interface |
| Lead Sniper HNW | WealthWireRadar signal system |
| Claude API (Anthropic) | Ollama local models |
| Phase-by-phase build | Client delivery using this methodology |

**KlickSmartAI OS adds to Klick2Client OS:**
- 147 MIT-licensed The Agency agents (workforce layer)
- Paperclip.ing human control plane model (Dennis as CEO)
- Multi-client agency delivery methodology
- DuckDB + MotherDuck for analytics
- Hermes as the orchestration layer

---

## 9-Phase Build Roadmap

| Phase | Deliverables |
|-------|-------------|
| 1 | Foundation — schema.sql, settings.py, supabase_client.py |
| 2 | Content Engine — content_library table, content parsing scripts |
| 3 | Enrichment + Battlecard — scripts, battlecard_generator.py, PDF export |
| 4 | Messaging Infrastructure — unipile_client.py, message_builder.py, lifecycle_agent.py |
| 5 | Signal Intelligence — signal_monitor.py (placeholder + algorithm injection) |
| 6 | LinkedIn Module — profile_analyzer, activity_scraper, linkedin_agent, sequence_builder |
| 7 | Feedback Loop — conversion_analyzer.py, unipile_receiver.py, lifecycle_runner.py |
| 8 | Kanban + KPI UI — board_logic, board_api, board.html, kpi_dashboard.html |
| 9 | Integration — main.py wires all services into single entry point |

---

## GTM Engineer Resources Connection

Explorium.ai's GTM Engineering use case page validates the Klick2Client OS architecture:

- Explorium's "Agentic Workflows" use case = Klick2Client OS's enrichment layer + lifecycle engine
- Explorium's "Always-Fresh CRM" = Klick2Client OS's signal intelligence + battlecard generation
- Explorium's B2B data layer for Claude Code (97.8% accuracy) = pattern for Klick2Client OS's enrichment pipeline
- Explorium explicitly publishes about OpenClaw/Claude Code integration = validates the GTM Engineer positioning

See: `gtm-engineer-resources/explorium-ai.md`