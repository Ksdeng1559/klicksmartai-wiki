# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-04-15] create | Wiki initialized
- Domain: General knowledge — persistent cross-session memory
- Structure created with SCHEMA.md, index.md, log.md
- Subdirectories: raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/

## [2026-04-15] create | Initial pages
- Created [[entities/dennis-e.md]] and [[concepts/about-this-wiki.md]]
- Updated [[index.md]] with 2 initial pages

## [2026-04-15] ingest | Hermes Agent research
- Brave Search query: "Hermes AI agent news" — 10 results returned
- Created [[entities/hermes-agent.md]] — Nous Research self-improving AI agent, 64K+ GitHub stars
- Created [[raw/articles/hermes-agent-research.md]] — raw source data from Brave Search
- Updated [[index.md]] — added hermes-agent page, bumped total to 4 pages

## [2026-04-15] ingest | Hermes Agent setup guide
- Source: Alex P.'s Medium article (March 29, 2026) — full VPS setup walkthrough
- Created [[concepts/hermes-agent-setup-guide.md]] — setup guide concept page with install commands, model selection, Telegram setup, skill documents, 24/7 service, and security checklist
- Created [[raw/articles/hermes-agent-complete-setup-guide.md]] — full raw article for reference
- Updated [[index.md]] — bumped total to 5 pages

## [2026-04-16] create | WWR wiki transfer — WealthWireRadar permanently stored
- Created [[entities/wealth-wire-radar.md]] — project overview, ICP, stack, implementation stages, open gaps
- Created [[concepts/wwr-signal-pipeline.md]] — 9-step pipeline flow, 8 signal clusters, built modules, Hermes skills
- Created [[concepts/wwr-relationship-manager.md]] — v2.0 architecture (BFS pathfinding, proximity scoring, action thresholds), node taxonomy, DDL schema
- Created [[concepts/wwr-battlecard-format.md]] — ASCII format, v2.0 RM brief upgrade, outreach templates
- Updated [[index.md]] — added 4 WWR pages (total: 9)
- Sources: WWR implementation plan Rev 3, WWR PRD v2.0 (relationship manager), WWR pipeline architecture
- Note: repo not yet cloned locally — blocking Stage 8 (Railway deploy)
- Architecture plan created at [[.hermes/plans/2026-04-15_152000-lead-distribution-agent-architecture.md]]
- 7-agent system: Intake → Enrichment → Scoring → Routing → Sales Agents × N + COI Coordinator + Compliance
- Output layer added: Google Docs for battle cards + CSV/webhook for CRM
- Prospect battle cards and COI battle cards designed (dense, call-scannable format)
- Two parallel delivery paths: human-facing (Docs) and system-facing (CRM webhook)
- Plan updated Rev 2 with output layer details
- Status: awaiting Dennis's GitHub repo URL for existing app review

## [2026-04-15] doc | WWR PRD v2.0 Relationship Manager Node Architecture
- Document ID: WWR-PRD-CORE-002, v2.0 April 2026
- Major upgrade from v1.x COI mapper → full relationship graph with scored edges
- New node taxonomy: RM (root), Connector (1-3°), Prospect (target), Relationship Edge (weighted, directed, time-decaying)
- Three new modules: relationship_manager.py (replaces coi_mapper.py), pathfinder_agent.py (BFS/DFS), proximity_scorer.py (scoring)
- One Phase 2 module: connector_effectiveness.py (learning layer)
- Proximity Score formula: Degree Distance + Relationship Strength + Event Relevance + Timing + Shared Context (max 165, normalized to 100)
- Action thresholds: HOT_PATH 85-100, WARM_PATH 70-84, VIABLE_PATH 50-69, NO_PATH <50
- Path-based messaging collapses cold→warm by referencing shared context in opening line
- RM-02: Pathfinder must compute within 3 seconds for up to 500-node graph
- MotherDuck schema: rm_nodes, rm_edges, rm_path_results — all queries tenant-scoped via TenantContext
- Build order: signal_parser.py → DDL → relationship_manager.py → proximity_scorer.py → pathfinder_agent.py → Battlecard upgrade → Outreach engine
- coi_mapper.py fully superseded — do not build v1.x COI layer

## [2026-04-15] plan | WWR Implementation Plan Rev 4
- Rev 4 plan created at [[.hermes/plans/2026-04-15_wwr-implementation-plan-rev3.md]]
- README.md (Sovereign-2.0) used as ground truth — overrules PRD assumptions
- CRITICAL: signal_parser.py, tri_engine_search.py, preliminary_viewpoint_mapper.py,
  wwr_tools.py, Hermes config+skills, all migrations 001-010, AND 57 unit + 69 smoke
  tests — ALL BUILT ✅ — not "spec complete" or "stubbed"
- README Implementation Stages: Stages 1-7b complete, Stage 8 (Railway deploy) is NEXT
- v2.0 Relationship Manager (WWR-PRD-CORE-002) is a NEW build track on top of v1.x
  — not yet built, separate from Stages 1-7b
- Repo location unknown — Dennis to find Sovereign-2.0 on machine (blocking Stage 8)
- Wiki updated as relationship graph + MotherDuck dual storage pattern
- 3 open questions for Dennis: GAP-14, GAP-15, GAP-16
- PIPEDA (GAP-19) confirmed as critical path blocker for Stage 10 (CRM Phase 1)
- Next action: Dennis locates repo → Stage 8 Railway deploy begins

## 2026-04-16 — WWR GAP-19 Decision Brief
- Filed decision brief: [[queries/wwr-gap19-decision-brief]]
- Stage 8+9 confirmed as joint deploy requirement

## [2026-04-16] ingest | Claude + LinkedIn Prompt Library (John Peslar / Zevari)
- Source: zevari.ai article (Apr 8, 2026) — 18 workflows, 131 skills, 6 GTM personas
- Created [[raw/articles/claude-linkedin-prompt-library]] — full article stored as raw reference
- 6 personas: GTM Engineers, Content Creators, SDRs, Recruiters, Consultants, Agency Owners
- 25 core skills: Ghostwriter Protocol, ICP Scoring, DISC profiling, Outreach Frameworks (Pain/Value/Authority-Led), Lead Magnet pipeline, safety system
- Skill chains: Radar→Ideation→Creator→Post, Industry Pulse→Topic Briefer→Post Writer, etc.
- Companion to AI Chief of Staff (same author, same Zevari product stack)

## [2026-04-16] create | GPC Development Ltd. client entry
- New website project — client details from Telegram with Tak Ho (Apr 16, 2026)
- Created [[entities/gpc-development]] — principals Zulliy Alnahas + Tak Ho, contacts, emails needed
- Reference sites: Renditionconstruction.com, Etroconstruction.com
- Flag: Fatima Nahhas "I send you 200" — needs clarification

## [2026-04-16] ingest | AI Chief of Staff — 28 Dispatch Delegation Frameworks (John Peslar / LeadPanther)
- Source: LeadPanther article (Mar 23, 2026) — 28 frameworks, 4-Element Delegation Formula
- Created [[raw/articles/ai-chief-of-staff-dispatch-frameworks]] — full article stored as raw reference
- 4-Element Delegation: Context, Constraint (most critical), Format, Verification
- 28 frameworks across 8 categories: Revenue/Sales, Content/Marketing, Inbox/Comms, Client Management, Ops/File, Strategic Review
- Rule of Three: manual task once=fine, twice=notes, 3x=build a framework
- Automated Chains: combine frameworks into sequences — one click, total visibility
- Companion to Zevari LinkedIn library (same author, same ecosystem)

## [2026-04-16] create | WattBricks.com project entry
- New project created at [[entities/wattbricks]] — domain: wattbricks.com
- Brand intel gathered from wattbricksbattery.com (Shopify, 4 products, orange/Poppins brand)
- WattBricks Energy Independence.pdf extracted — 15-slide NotebookLM deck
- "The Energy Paradox" — Canada energy crisis + residential independence positioning
- Slides 1-3 extracted to [[raw/drafts/wattbricks-energy-independence-deck]]; slides 4-15 pending

## [2026-04-16] create | Client Onboarding SOP
- [[raw/drafts/website-build-onboarding-sop]] — full 6-stage SOP from discovery to post-launch
  - Stage 1: Discovery Call (D1-D9, P1-P4, PR1-PR3 questionnaire)
  - Stage 2: Deposit & Contract ($ deposit → Google Sheet journal tracker)
  - Stage 3: Content Collection (logo, colours, fonts, copy, images, domain)
  - Stage 4: PRD & Wireframe (PRD doc + Figma/Canva blueprint)
  - Stage 5: Design & Build (2 revisions, responsive, QA, launch)
  - Stage 6: Post-Launch (final invoice, admin training, 30-day support)
- [[entities/gpc-onboarding]] — GPC-specific tracker, D1-PR3 partially filled (deposit done)
- Client Assets questionnaire embedded in SOP (send to every new client)
- Drive folder: 1EJLeJ7wGG-DAum_R8B-AxSLh1tH8Fbls

## [2026-04-16] create | Alexander Eng Toy Nissan GT-R
- [[entities/alexander-eng-toy-nissan-gtr]] — yellow die-cast Nissan GT-R, blue/white stripes, number "2", black spoiler, silver rims
- Owner: Alexander Eng (son of Dennis Eng)
- Photo: /home/denni/.hermes/image_cache/img_8ebb9f182c52.jpg

---
[2026-04-27 21:48 UTC] Added wiki page: whatcom-county-housing-developers.md
Type: research entity
Action: Ingested live research into entities/ + updated index.md
Source: Live web research (Cascadia Daily, cityofbellingham.gov, whatcomcounty.us)
Notes: 5 CDFI-aligned affordable housing developers in Whatcom County with active projects + contact intel. Ready for outbound pipeline.

[2026-06-10] create | context7
Action: Ingested Upstash Context7 repo (github.com/upstash/context7) for future Hermes Agent installations. Captures: purpose, trigger phrases, operating modes (CLI+Skills vs MCP), one-command setup, manual MCP config for Hermes, all 5 npm packages, auto-trigger rules. Cross-linked to hermes-agent, exa, tavily, serper, brave-search.
Source: github.com/upstash/context7 (v0.5.1, 57k stars)
Notes: Recommended for all future Hermes installs to prevent hallucinated APIs.

[2026-06-10] create | klicksmartai-wiki-architecture
Action: Ingested full README + AGENTS.md + SCHEMA.md + hermes/directives.md + hermes/memory-architecture.md + klick2client-os.md from github.com/Ksdeng1559/klicksmartai-wiki. Captures: branch governance (master=memory, workflow/research/archive for development), wiki-llm read-and-merge gate, knowledge consolidation lifecycle, tech stack (Hermes, wiki-llm, Claude, ChatGPT, Gemini, Graphify, Pinecone, DuckDB, MotherDuck), full directory structure, sync sequence, Hermes operating directives (2-layer memory, multi-LLM shared knowledge, daily 8PM PST cron), upgrade triggers, Klick2Client OS 6-layer architecture with PSQ scoring, future install reference. Cross-linked to context7, klicksmartai, dennis-eng, graphify, pinecone, hermes-agent.
Source: github.com/Ksdeng1559/klicksmartai-wiki (1 star, 1 contributor, last push 2026-06-10)
Notes: Critical reference for any future Hermes install that needs to join this ecosystem. Also documents the local working copy at G:\AI-Applications\Hermes Agent\wiki\ as the Obsidian vault.

[2026-06-10] create | entities-and-projects-index
Action: Ingested full contents of entities/ (51 files) and projects/ (7 files) from github.com/Ksdeng1559/klicksmartai-wiki. Built a single searchable index grouped by category: People, Companies/Orgs, AI Models/Agents, Search/Data APIs, Data/Memory Infra, Business/Sales Tools, Real Estate/Finance, Frameworks. Captured detail pages for Signal Intelligence Agent (3-stage pipeline, 5-engine search, MiniMax via Ollama), IDC Insurance Direct Canada (client details, stakeholders, $2B+ coverage scale), and KlickSmartAI Agent Squad (6-agent framework mapped to Shubham Saboo model with status indicators). Documented project subdirectories: commercial-mortgage-os (4 files), mortgage-broker-os (6 files), klicksmartai-com-gtm-site (SPEC), rios-mortgage-intelligence-exchange (architecture).
Source: github.com/Ksdeng1559/klicksmartai-wiki/entities and /projects
Notes: Use this index for fast lookups without GitHub. Individual entity pages are still on GitHub - this page provides the discoverability layer.

[2026-06-10] create | wiki-folders-index
Action: Pulled and indexed all wiki subfolders from github.com/Ksdeng1559/klicksmartai-wiki: clients/ (4 active + 2 historical with full file lists), concepts/ (13 files - capital-stack 22.5K is largest, WWR pipeline 9-step, First 100 Clients playbook), reference/ (2 files), architecture/agents/ (division-based architecture), spectra/ (capital-stack + whatcom-county), hermes/ (directives + 6 skills), operations/, ops/outreach/, queries/. Captured Spectra Holdings corporate detail (ICF construction 28-45 days, Revvo APU 93% electricity reduction, 20K+ home pipeline), Breakthrough Management grant funding focus, WWR 9-step pipeline with engine fan-out, and Division-Based Agent Architecture (Intelligence → Strategy → Execution → Quality).
Source: github.com/Ksdeng1559/klicksmartai-wiki (all subfolders)
Notes: Complete folder inventory. Use this for navigation; individual files still on GitHub. Last 24 folders listed as TBD - can be pulled in future sessions.

[2026-06-10] create | daily-wiki-sync setup
Action: Set up automated daily wiki sync per hermes/directives.md (8PM PST cron). Created Python sync script at C:\Users\denni\AppData\Local\hermes\scripts\daily-wiki-sync.py (git fetch → merge → push → graphify update), wrapper at run-daily-wiki-sync.bat, and registered Hermes cron job (ID e779970fb9a4, schedule "0 20 * * *", no-agent mode, workdir wiki). Tested manually: successfully committed and pushed 5 new wiki pages (context7, klicksmartai-wiki-architecture, entities-and-projects-index, wiki-folders-index) and 2 updated files (index.md, log.md, entities/spectra-holdings-group.md). Pulled 66 commits (1,946 file changes) from origin without conflict.
Source: hermes cron create
Notes: Job will fire at 8:00 PM PST daily. REQUIRES hermes gateway to be running - currently gateway is stopped. To enable: run "hermes gateway install" to register as Windows Scheduled Task (will prompt for UAC elevation). Also attempted direct schtasks registration but requires admin elevation. Once gateway runs, the cron will fire automatically.
- 2026-08-04: Ingested Swan GTM Skills from Notion (swan-gtm/gtm-skills) → gtm-engineer-resources/07-gtm-skills/swan-gtm-skills.md; updated gtm-engineer-resources/index.md
- 2026-08-04: Ingested LeadSniperAI Signal-Based Cold Email SOP from Notion (SOP-Signal-Based-Cold-Email-System-Using-LeadSniperAI) → processes/lead-sniperai-signal-cold-email-sop.md (43 sections + infra standard); updated index.md Playbooks
- 2026-08-04: Added Deepline (GTM contact enrichment waterfall, 97+ providers) from deepline.com/docs/quickstart → gtm-engineer-resources/01-data-enrichment/deepline.md; updated resource index
- 2026-08-04: Updated Deepline wiki entry with verified play commands (deprecated tools execute), full tool/play catalog (2,001 tools, 15 plays), pilot results (4/5 emails, 80% hit rate)
- 2026-08-04: Updated Deepline entry — local business toolkit (openwebninja, serper maps, enformion SMB owner, opensosdata) with live tests + US-only Enformion pitfall
- 2026-08-04: Added Canada coverage section to Deepline entry — Limadata verified as Canada-capable provider (company enrich + person contacts); Firmable BYOK; Enformion/OpenSOSData US-only
- 2026-08-04: Added hiring-signal toolkit to Deepline entry — CrustData v3 primary (Canada filters live-tested), PredictLeads/Theirstack/Sentrion supporting, native monitors gated, SOP §4.2/§8.1 integration
- 2026-08-05: Ingested LeadSniperAI CLI master OS spec from Notion (33 sections, canonical command taxonomy, dual-rail economics, Notion ops layer) → processes/lead-sniperai-cli-os.md; updated index.md
- 2026-08-05: Ingested all 6 LeadSniperAI Notion docs → projects/leadsniperai/ (Marketplace PRD, CLI PRD, Workflow Improvement, Marketplace OS, Venture OS, Integration API Catalog) + folder index; updated index.md
- 2026-08-05: Ingested LeadSniper-3.0 GitHub repo (clone → raw/repos/LeadSniper-3.0); reviewed README, GROUNDING-TEST-GUIDE, vertex_audit.py, tavily_intelligence.py, endpoints.py, lead.py. Wrote GMB-grounding signal engine proposal for business-funding vertical → drafts/leadsniperai-gmb-signal-engine-proposal.md; updated index.md
- 2026-08-05: Converted LeadSniperAI 3.0 to agent-native CLI via Printing Press v4.30.1 — Go toolchain installed, OpenAPI spec generated (25 endpoints), leadsniper-pp-cli generated + verified live (doctor/search/batches/MCP). Doc: projects/leadsniperai/cli-conversion-printing-press.md
- 2026-08-05: BUILT Review Intelligence Engine (core differentiator) — review content → sentiment/themes → phase detection (count×score×themes) → service recommendations. Backend: services/review_intelligence.py + /api/v1/analyze-reviews endpoint (verified live: overloaded phase, 3 services w/ proof basis). Tuned rules engine (phone_leak/no_show/pricing edge cases). Regenerated CLI with analyze-reviews command (28 endpoints). Design: drafts/leadsniperai-review-intelligence-engine.md
- 2026-08-05: Added WEBSITE INFRASTRUCTURE AXIS to Review Intelligence — no-website/outdated/slow/weak-intake detection (assess_website), combined two-axis diagnosis (combine_diagnosis) with priority logic (no-website+good-reviews = Website build #1; critical website = services priority 1). Verified scenarios A (4.9★ no website → urgent_capture → Website build #1) + B (4.6★ critical website → 6 website services ranked #1). Design doc updated §6.
- 2026-08-05: Wired auto-population into Review Intelligence — DataForSEO auto-fetch (business discovery → place_topics theme bridge → rating/review_count/website capture) + PageSpeed auto-audit (website axis). Verified end-to-end: Milani Plumbing auto → 4.9/2884, health 100 praise, phase established, website needs_work. place_topics bridge verified on negative profile (health 25, booked_out dominant). New services: dataforseo_business.py, website_audit.py; DATAFORSEO creds in config.
- 2026-08-05: Setup backend/.env (git-ignored) — Tavily + DataForSEO from Hermes env, placeholders for Gemini/Apify/Supabase. Final CLI regen with auto-fetch flags. Verified full-stack via CLI: analyze-reviews --business-name Milani --auto-fetch-reviews → rating 4.9/2884, place_topics sentiment health 100, phase established, website needs_work, 2 services.
- 2026-08-05: Wired leadsniper MCP server into Hermes — stdio → leadsniper-pp-mcp (57 tools incl. analyze-reviews_analyze_reviews). Registered via hermes config set; verified connected 66ms.
- 2026-08-05: Built Executive Summary generator — backend/app/services/executive_summary.py (rules-templated, works without Gemini; LLM path stubbed for when key arrives) + POST /api/v1/executive-summary endpoint. Verified live: Milani Plumbing full 8-section client-ready markdown from DataForSEO auto-fetch + place_topics + review intelligence + contact.
- 2026-08-05: Updated hermes-skills-hub.md — refreshed from docs Bundled Skills Catalog (71 skills/13 categories, server-rendered canonical source; hub page is client-rendered 88k+ registry). Added local install inventory (474 skills, 10 bundled-but-missing listed with restore command).
- 2026-08-06: Ingested Swan GTM Skills library full mirror (267 SKILL.md, 45 authors) → raw/swan-gtm/ + raw/wiki-knowledge/entities/swan-gtm-gtm-skills.md; LeadSniper SGI PRD from Notion → raw/wiki-knowledge/entities/leadsniper-sgi-prd.md; search stack → raw/wiki-knowledge/concepts/search-stack.md


## [2026-08-28] publish | Veritas Developments — 3 audit deliverables released via Phase C pipeline
- Backfilled 3 RELEASED SEO audit deliverables from Veritas client workspace DuckDB to wiki:
  - audit-audit-v4-2026-08-28 — SEO Audit — veritasdevelopmentgroupllc.com (v4) (3816 words)
  - audit-client-score-2026-08-28 — Client Score — Veritas Development Group LLC (1490 words)
  - audit-cover-memo-v4-2026-08-28 — Cover Note — SEO Audit v4 (1043 words)
- Created [veritas-developments](entities/veritas-developments.md) entity page (canonical client entry; cross-links all 3 audits + growth program pilot)
- Added 3 audit rows to index.md `## Audits`; added 1 entity row to `## People & Companies`
- Source: `~/wiki/clients/veritas-developments/.local_tier/clients/veritas-developments.duckdb` (Phase A schema v1.1.0)
- This is the **first publish through the Phase C pipeline** — establishes the DuckDB → wiki flow


## [2026-08-28] publish | veritas-developments — 3 deliverable(s) published to wiki
- Published via `publish-workspace-to-wiki` skill (script: publish_client_to_wiki.py)
- Deliverables:
  - `audit-v4-2026-08-28` — SEO Audit — veritasdevelopmentgroupllc.com (v4) (3816 words)
  - `client-score-2026-08-28` — Client Score — Veritas Development Group LLC (1490 words)
  - `cover-memo-v4-2026-08-28` — Cover Note — SEO Audit v4 (1043 words)
- Entity page: `entities/veritas-developments.md`
- Index rows added: 3 audit row(s) + 1 entity row (if new)
