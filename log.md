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
