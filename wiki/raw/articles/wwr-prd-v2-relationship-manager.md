# WWR PRD v2.1 — Full Stack Implementation Plan
## WealthWireRadar · KlickSmart AI

**Document ID:** WWR-PRD-CORE-002  
**Version:** 2.1 · April 2026 · Confidential  
**Supersedes:** v2.0 (April 2026)  
**Author:** Dennis E. / KlickSmart AI  
**Stack:** MotherDuck (DuckDB) + FastAPI + Python 3.11 + React 19 + Firebase + Railway

**v2.1 Changes from v2.0:**
- Added §0A: Current build status and gap registry (derived from graph analysis 2026-04-16)
- Added §0B: Stage 8+9 joint deploy specification (new — previously undocumented)
- Added §0C: GAP-19 PIPEDA compliance requirements (formalised from gap registry)
- Updated §10 build order to reflect confirmed stage completion and Railway deploy sequence
- Added §11: Acceptance criteria for technical implementation plan

---

## §0A — Current Build Status

All stages 0–7b are complete and tested. The system is blocked at Stage 8 (Railway deploy), not by engineering gaps.

| Stage | Description | Status | Notes |
|-------|-------------|--------|-------|
| 0 | Precondition verification | ✅ Complete | |
| 1 | Quad-engine search (`tri_engine_search.py`) | ✅ Complete | Serper + Tavily + Brave fan-out |
| 2 | Signal parser (`signal_parser.py`) | ✅ Complete | |
| 3 | Signal classifier (`signal_classifier.py`) | ✅ Complete | Composite score, tier, clusters |
| 4 | PV mapper (`preliminary_viewpoint_mapper.py`) | ✅ Complete | 18-field profile, ICP gate |
| 5 | Hermes tools (`wwr_tools.py`) | ✅ Complete | 7 tools wired |
| 6 | MotherDuck schema | ✅ Complete | Migrations 001–010 deployed |
| 7 | Master COI module (mock data) | ✅ Complete | 15 mock profiles |
| 7b | RM v2.0 modules (mock data) | ✅ Complete | `relationship_manager.py`, `pathfinder_agent.py`, `proximity_scorer.py` built |
| **8** | **FastAPI → Railway deploy** | 🔜 **NEXT** | Joint deploy with Stage 9 |
| **9** | **React 19 frontend → Railway wire-up** | 🔜 **NEXT** | Joint deploy with Stage 8 |
| 10 | CRM Phase 1 — Unipile onboarding | 🔒 Blocked | GAP-19 (PIPEDA) |
| 11 | Battlecard generator (production) | 🔜 After Stage 10 | |
| 12 | Connector effectiveness learning layer | 🔜 Phase 2 | |
| 13–14 | Phases 3–4 | 🔜 Future | |

**Test coverage:** 57 unit tests + 69 smoke tests — all passing.

**Graph analysis finding (2026-04-16):** 39 of 96 system nodes are currently blocked by GAP-19. The entire v2.0 product activates in a 5-stage cascade on GAP-19 resolution. The system degrades gracefully to v1.x behaviour (battlecards without warm paths) after Stage 8+9 deploy.

---

## §0B — Stage 8+9: Joint Railway Deploy Specification

> **Critical:** Stage 8 (FastAPI) and Stage 9 (React frontend) **must be deployed together** as a single Railway operation. Deploying FastAPI without the frontend leaves the system live but invisible — Sean has no login surface and cannot approve outreach. Graph analysis confirms a bidirectional dependency: `CRM Frontend --serves--> FastAPI`.

### Deploy Checklist

**Pre-deploy (both stages must be ready):**
- [ ] FastAPI backend passes all endpoint smoke tests locally
- [ ] React 19 frontend connects to local FastAPI successfully
- [ ] Environment variables documented for Railway injection
- [ ] MotherDuck connection string validated from Railway environment
- [ ] Firebase Auth configured for production domain
- [ ] Health check endpoint (`/health`) returns 200

**Railway configuration:**
- [ ] FastAPI service: Python 3.11 runtime, `uvicorn app:app --host 0.0.0.0 --port $PORT`
- [ ] React frontend service: Node 22, build command `npm run build`, serve via Railway static
- [ ] Environment variables set: `MOTHERDUCK_TOKEN`, `OPENROUTER_API_KEY`, `FIREBASE_CONFIG`, `JWT_SECRET`
- [ ] Custom domain configured for frontend (Sean's login URL)
- [ ] CORS configured: frontend domain whitelisted in FastAPI

**Post-deploy verification:**
- [ ] Sean can log in via frontend
- [ ] At least one battlecard visible in dashboard
- [ ] Battlecard displays signal data, ICP score, financial profile
- [ ] "No viable path — direct outreach recommended" displays correctly (expected pre-GAP-19)
- [ ] Google Workspace MCP drafts outreach to Gmail correctly

---

## §0C — GAP-19: PIPEDA Compliance Requirements

GAP-19 is the single root blocker for the v2.0 product. Resolution unlocks 39 nodes including `relationship_manager.py`, `pathfinder_agent.py`, `proximity_scorer.py`, and the full warm outreach pipeline.

### What PIPEDA Requires for Unipile Contact Import

| Requirement | Implementation |
|-------------|---------------|
| Informed consent | Advisor must explicitly consent to importing their contact graph into WWR at onboarding |
| Purpose limitation | Contact data used only for path-finding within that advisor's tenant — never shared, never used for cross-subscriber matching |
| Data minimisation | Import only: name, title, company, LinkedIn URL, interaction recency. No email addresses, no phone numbers in `rm_nodes` |
| Retention limit | Contact data deleted within 30 days of advisor offboarding |
| Access and correction | Advisor can view, edit, or delete any connector node via the CRM frontend |
| Breach notification | Any `TenantIsolationError` must be logged, alerted, and treated as a potential breach event |

### PIPEDA Compliance Checklist (Pre-Stage 10)

- [ ] Privacy policy updated to include relationship graph data processing
- [ ] Onboarding consent screen: explicit checkbox for Unipile contact import
- [ ] `rm_nodes` table: no PII beyond name/title/company/LinkedIn URL
- [ ] `TenantContext` audit logging: every graph query logged with timestamp, subscriber_id, query type
- [ ] Data deletion endpoint: `DELETE /advisor/{id}/contact-graph` implemented and tested
- [ ] Sean's review: confirm PIPEDA approach before importing real contacts

---

## §1 — Product Vision

WealthWireRadar (WWR) is a signal-driven intelligence platform for Canadian financial advisors. It detects HNWI wealth inflection events from public registries and news, scores them against an ICP, builds intelligence battlecards, and routes warm outreach through a scored relationship path.

**The core insight:** cold outreach to wealthy prospects fails. Warm introductions through trusted connectors succeed. WWR automates the path from public signal to warm introduction, making the advisor the first call instead of a cold email.

**Subscriber:** Wayne Stone — Westward Advisors Ltd.
**Platform owner:** Dennis E. — KlickSmart AI
**Master COI:** Sean Carey — Westward Advisors Ltd.

---

## §2 — ICP Definition

**Target prospects:** BC/AB/ON High Net Worth Individuals

| Criterion | Threshold |
|-----------|-----------|
| Net worth | $25M+ |
| Corporate taxable income | $2M+ (alternative qualifier) |
| Business type | Owner-operator: construction, manufacturing, real estate, professional services |
| Trigger events | CCPC succession, director change, business sale, corporate restructuring |

**ICP Gate:**

| Tier | NW Confidence | Income Confidence | Outreach Window |
|------|--------------|-------------------|-----------------|
| QUALIFIED | >= 70% | >= 70% | 24 hours |
| PROBABLE | 40-69% | 40-69% | 72 hours |
| DEVELOPING | < 40% | < 40% | Not briefed |

---

## §3 — Full System Architecture

```
SIGNAL LAYER  (built)
Hermes Agent (6AM PT daily cron)
  wwr_search (Serper + Tavily + Brave fan-out)
  signal_parser.py (entity extraction, structured signal)
  signal_classifier.py (composite score, tier, 8 clusters)
  preliminary_viewpoint_mapper.py (18-field PV, ICP gate)
  wwr_resolve_identity (LinkedIn URL, competitor gate, dedup)

STORAGE LAYER  (built)
  wwr_store_signal -> MotherDuck (wwr_production)
  Tables: signals, entities, pv_profiles, outreach_queue
  RM Tables: rm_nodes, rm_edges, rm_path_results (migrations 001-010)

RELATIONSHIP LAYER  (built, mock data - blocked by GAP-19 for real data)
  relationship_manager.py (graph import, retrieval, edge updates)
  pathfinder_agent.py (BFS traversal, 1-4 degrees, MAX 500 nodes)
  proximity_scorer.py (composite 0-100, 5-component formula)

GENERATION LAYER  (Stage 11)
  battlecard_generator.py (ASCII battlecard + RM Brief)
  outreach_engine.py (path-based template selection)
  Google Workspace MCP (Gmail Draft push)

API + FRONTEND LAYER  (Stage 8+9)
  FastAPI Backend (Railway)
  React 19 + Firebase Frontend (Railway)
  Sean Carey browser -> approve outreach -> activate COI

LEARNING LAYER  (Phase 2)
  connector_effectiveness.py (reply/conversion tracking)
  Unipile webhooks -> edge strength updates
```

---

## §4 — Signal Clusters and Scoring

Eight signal clusters with recency age modifiers:

| Cluster | Signal Type | Source | Age Modifier |
|---------|-------------|--------|-------------|
| Director change | BC/AB Registry | Registry scrape | x1.20 (0-7 days) |
| Business sale | News + Registry | Multi-engine | x1.10 (8-30 days) |
| Property transfer | Land Titles | Registry | x1.00 (31-90 days) |
| CCPC succession | CRA triggers | Signal inference | x0.85 (91-180 days) |
| Corporate restructuring | SEDAR/News | Multi-engine | x1.10 (8-30 days) |
| Executive departure | Registry/News | Multi-engine | x1.00 (31-90 days) |
| Acquisition target | News | Multi-engine | x1.10 (8-30 days) |
| Insurance gap detected | Signal inference | PV mapper | x0.90 (signal-dependent) |

---

## §5 — Relationship Manager Node Architecture

### Node Type Taxonomy

| Node Type | Role | Key Fields |
|-----------|------|-----------|
| RM (Relationship Manager) | Root - path origin | subscriber_id, indexed contact network |
| Connector | Intermediate - path bridge | strength (0-100), recency_days, industry_overlap, shared_context_tags |
| Prospect | Target - path destination | event_type, wwr_score, cluster, urgency |
| Relationship Edge | Weighted, directed, time-decaying | strength, recency_days, industry_overlap, shared_context_tags, edge_score |

### Proximity Score Formula

| Component | Max Points | Calculation |
|-----------|-----------|------------|
| Base: Degree Distance | 85 | 100 - (degrees x 15) |
| Relationship Strength | 30 | recency x interaction_depth x mutual_context |
| Event Relevance | 25 | Connector industry match to signal cluster |
| Timing | 20 | Signal recency modifier (mirrors WWR scorer) |
| Shared Context | 10 | Deal / geography / association overlap |
| Total (normalised) | 0-100 | Raw max 165 -> normalised |

### Action Thresholds

| Score | Label | Action | Window |
|-------|-------|--------|--------|
| 85-100 | HOT PATH | Immediate warm intro | 24h |
| 70-84 | WARM PATH | Schedule warm intro | 72h |
| 50-69 | VIABLE PATH | Advisor judgment | - |
| < 50 | NO PATH | Direct outreach | - |

---

## §6 — Battlecard Format

```
+------------------------------------------+
|  HOT - Score 91                          |
|                                          |
|  [Prospect Name]                         |
|  [Company] · [Province] · [Industry]    |
|                                          |
|  WHY NOW                                 |
|  [Signal type] detected                  |
|  [X]-year CCPC - signal [N] days old    |
|                                          |
|  FINANCIAL PROFILE                       |
|  Est. Net Worth:    $[X]-$[Y]M          |
|  Retained Earnings: $[X]-$[Y]M          |
|  Estate Tax Risk:   HIGH/MED/LOW         |
|  Insurance Gap:     Likely/Unlikely      |
|                                          |
|  PLANNING ANGLES                         |
|  · [Planning angle 1]                   |
|  · [Planning angle 2]                   |
|  · [Planning angle 3]                   |
|                                          |
|  RECOMMENDED ANGLE                       |
|  "[Outreach hook]"                       |
|                                          |
|  RELATIONSHIP PATH  (v2.0 only)         |
|  [Connector name], [Title]              |
|  Path: [X] degrees · Score: [X]/100    |
|  Action: HOT PATH / WARM PATH           |
|                                          |
|  [ Approve Outreach ] [ Activate COI ]  |
|  [ View Full Profile ] [ Dismiss ]      |
+------------------------------------------+
```

Design rules:
- ASCII box layout — Telegram-safe, renders in any client or email
- Signal age is first-class in WHY NOW section
- Tier badge and score at top
- Relationship Path section hidden when action_threshold = NO PATH
- Anonymity Principle: COI brief never names the prospect

---

## §7 — Module Specifications

### relationship_manager.py (350 lines max)

| Method | Inputs | Returns |
|--------|--------|---------|
| import_contact_graph() | subscriber_id, unipile_contacts[] | Upserts contacts as Connector nodes |
| get_contact_graph() | rm_node_id, depth=4 | Adjacency list, subscriber-scoped |
| update_edge_strength() | connector_id, interaction_type, timestamp | Updates edge weight |
| find_connectors_for_prospect() | prospect_linkedin_url, subscriber_id | Connectors with industry/geo overlap |
| get_rm_node() | subscriber_id | Root RM node for pathfinder |

### pathfinder_agent.py (350 lines max)

PathfinderResult output schema:

| Field | Type | Description |
|-------|------|-------------|
| found | BOOLEAN | True if viable path exists |
| path | UUID[] | Ordered node IDs RM to Prospect |
| degrees | INTEGER | Hops (1-4) |
| best_connector | ConnectorNode | Recommended intro node |
| proximity_score | FLOAT | 0-100 normalised |
| action_threshold | VARCHAR | HOT_PATH / WARM_PATH / VIABLE_PATH / NO_PATH |
| recommendation | VARCHAR | Human-readable intro recommendation |
| alt_paths | PathResult[] | Up to 2 alternatives |

Performance requirement (RM-02): 3 seconds max for graph of 500 connector nodes.

### proximity_scorer.py (350 lines max)

Single public method: score_path(path) -> float (0-100).
All formula constants sourced from config.py.
Never called directly by Battlecard generator.

### connector_effectiveness.py (350 lines max, Phase 2)

| Event | Trigger | Edge Update |
|-------|---------|------------|
| Reply received | Unipile webhook | edge_strength +10 |
| Meeting booked | Calendar event | edge_strength +20, converted=TRUE |
| No response (30d) | Cron | edge_strength -5 |
| COI referral | CRM tag | edge_strength +30, connector promoted to anchor |

---

## §8 — MotherDuck Schema

```sql
CREATE TABLE IF NOT EXISTS rm_nodes (
    node_id         VARCHAR     PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR,
    subscriber_id   VARCHAR     NOT NULL,
    node_type       VARCHAR     NOT NULL,
    full_name       VARCHAR,
    title           VARCHAR,
    company         VARCHAR,
    industry        VARCHAR,
    linkedin_url    VARCHAR,
    coi_category    VARCHAR,
    province        VARCHAR,
    imported_from   VARCHAR,
    created_at      TIMESTAMP   DEFAULT now(),
    updated_at      TIMESTAMP   DEFAULT now()
);

CREATE TABLE IF NOT EXISTS rm_edges (
    edge_id             VARCHAR     PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR,
    subscriber_id       VARCHAR     NOT NULL,
    from_node_id        VARCHAR     NOT NULL,
    to_node_id          VARCHAR     NOT NULL,
    relationship_type   VARCHAR,
    strength            FLOAT       DEFAULT 50.0,
    recency_days        INTEGER,
    industry_overlap    BOOLEAN     DEFAULT FALSE,
    shared_context_tags VARCHAR[],
    edge_score          FLOAT,
    created_at          TIMESTAMP   DEFAULT now(),
    last_interaction_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS rm_path_results (
    result_id           VARCHAR     PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR,
    subscriber_id       VARCHAR     NOT NULL,
    prospect_id         VARCHAR     NOT NULL,
    path_node_ids       VARCHAR[],
    degrees             INTEGER,
    best_connector_id   VARCHAR,
    proximity_score     FLOAT,
    action_threshold    VARCHAR,
    outreach_status     VARCHAR     DEFAULT 'pending',
    converted           BOOLEAN     DEFAULT FALSE,
    created_at          TIMESTAMP   DEFAULT now()
);
```

---

## §9 — Functional Requirements

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| RM-01 | Unipile import: classify contacts as Connector nodes. Min 50 contacts to activate RM graph. | P0 | Blocked GAP-19 |
| RM-02 | Pathfinder: 3s max for 500-node graph. MAX_DEGREES=4. Prune paths below PROXIMITY_SCORE_FLOOR=50. | P0 | Built |
| RM-03 | Every HOT/WARM battlecard (WWR Score >= 60) must include RM Brief with PathfinderResult. | P0 | Stage 11 |
| RM-04 | All RM graph queries scoped to single subscriber_id via TenantContext. TenantIsolationError on violation. | P0 | Built |
| RM-05 | Outreach engine selects template by action_threshold. Gmail Draft via Google Workspace MCP. | P1 | Stage 11 |
| RM-06 | relationship_manager.py max 350 lines. No scoring logic. Delegates all scoring to proximity_scorer.py. | P0 | Built |
| RM-07 | Path results stored in rm_path_results. Conversion events update converted=TRUE and edge_strength. | P1 | Built |
| RM-08 | All Proximity Score constants defined in config.py. No hardcoded values in pathfinder or scorer. | P0 | Built |
| RM-09 | CRM sync updates edge_strength on: email sent, reply, meeting booked, referral. Daily cron. | P1 | Blocked GAP-19 |
| RM-10 | connector_effectiveness.py: learning layer. Global aggregates only - no subscriber-identifiable data. | P2 | Phase 2 |
| ST-01 | FastAPI + React frontend jointly deployed to Railway. Sean can log in. Battlecards visible. | P0 | Stage 8+9 |
| ST-02 | FastAPI health check endpoint (/health) returns 200. MotherDuck connection validated on startup. | P0 | Stage 8+9 |
| ST-03 | Frontend: battlecard list, battlecard detail, approve/dismiss actions. Firebase Auth for login. | P0 | Stage 8+9 |
| PD-01 | PIPEDA consent screen at onboarding. Explicit checkbox for Unipile contact import. | P0 | Blocked GAP-19 |
| PD-02 | rm_nodes: no PII beyond name/title/company/LinkedIn URL. No email, no phone. | P0 | Designed |
| PD-03 | TenantContext audit log: every graph query logged with timestamp, subscriber_id, query type. | P0 | Stage 10 |
| PD-04 | Data deletion endpoint: DELETE /advisor/{id}/contact-graph. | P0 | Stage 10 |

---

## §10 — Build Order

### Immediate — Stage 8+9: Railway Joint Deploy

1. Clone repo: Ksdeng1559/Sovereign-2.0, branch feature/wwr-crm-v1-westward
2. Validate FastAPI endpoints locally against MotherDuck
3. Validate React frontend against local FastAPI
4. Configure Railway services (see §0B checklist)
5. Joint deploy: FastAPI + React frontend to Railway
6. Verify Sean's login and battlecard visibility
7. Outcome: v1.x-quality pilot available — signal intelligence, no warm path yet

### After Stage 8+9 — Pilot Preparation (GAP-20)

- Schedule Sean + Wayne Stone discovery call
- Confirm pilot scope: approval workflow (GAP-14), delivery format (GAP-15), COI workflow (GAP-16)
- Confirm PIPEDA compliance approach with Sean

### Stage 10 — PIPEDA Resolution + Unipile Onboarding

1. Update privacy policy
2. Build onboarding consent screen
3. Implement DELETE /advisor/{id}/contact-graph
4. Implement TenantContext audit logging
5. Run Sean through onboarding: import real Unipile contact graph
6. Seed rm_nodes and rm_edges from real contact data
7. Outcome: Full v2.0 product activates — HOT/WARM/VIABLE paths in battlecards

### Stage 11 — Production Battlecard + Outreach Pipeline

1. battlecard_generator.py production implementation
2. RM Brief injection using live PathfinderResult
3. outreach_engine.py — path-based template selection
4. Gmail Draft push via Google Workspace MCP
5. End-to-end test: Hermes 6AM cron -> signal -> ICP gate -> path -> battlecard -> Gmail draft
6. Outcome: Full automated outreach pipeline live

### Phase 2 — Learning Layer

1. connector_effectiveness.py implementation
2. Unipile reply webhooks -> edge strength updates
3. Conversion tracking (converted=TRUE)
4. Global aggregate model
5. Outcome: Relationship intelligence moat begins compounding

---

## §11 — Acceptance Criteria for Technical Implementation Plan

The technical implementation plan must address the following for each stage.

### Stage 8+9 — Railway Deploy

- [ ] Railway service configuration for FastAPI (Python 3.11, uvicorn)
- [ ] Railway service configuration for React 19 frontend (Node 22, static build)
- [ ] Full environment variable manifest (all secrets required at deploy time)
- [ ] MotherDuck connection validation test from Railway environment
- [ ] Firebase Auth production configuration
- [ ] CORS configuration (frontend domain whitelisted)
- [ ] End-to-end smoke test plan: login -> view battlecard -> approve outreach
- [ ] Rollback procedure if deploy fails

### Stage 10 — PIPEDA + Unipile Onboarding

- [ ] PIPEDA compliance checklist (all items in §0C)
- [ ] Onboarding flow: consent screen -> Unipile OAuth -> contact import -> graph seed
- [ ] import_contact_graph() production implementation with real Unipile API
- [ ] Audit logging for TenantContext (timestamp, subscriber_id, query type)
- [ ] Data deletion endpoint implementation and test
- [ ] Minimum viable import test: 50 contacts -> rm_nodes populated -> pathfinder returns result

### Stage 11 — Production Battlecard + Outreach

- [ ] battlecard_generator.py production implementation
- [ ] RM Brief injection: PathfinderResult -> battlecard template
- [ ] HOT_PATH / WARM_PATH / NO_PATH template variants implemented
- [ ] Google Workspace MCP integration: Gmail Draft creation tested
- [ ] Full pipeline test: Hermes 6AM cron -> signal -> ICP gate -> path -> battlecard -> Gmail draft in Sean's inbox

### Performance Requirements

- [ ] RM-02: Pathfinder 3s max for 500-node graph (benchmark required)
- [ ] FastAPI battlecard list endpoint: 500ms max
- [ ] Daily cron: full signal scan + path mapping completes before 7AM PT

### Open Decisions to Resolve Before Stage 11

| Gap | Question |
|-----|----------|
| GAP-14 | Auto-deliver HOT/WARM battlecards or manual approval gate? |
| GAP-15 | Portal view or email PDF for battlecard delivery? |
| GAP-16 | COI intro — advisor-initiated only from battlecard? |

---

## §12 — Cron Schedule

| Frequency | Job | Module | Notes |
|-----------|-----|--------|-------|
| Daily 6AM PT | Signal scan + entity extraction | tri_engine_search.py + signal_parser.py | Running |
| Daily | Path mapping for new HOT/WARM prospects | pathfinder_agent.py | After battlecard queue |
| Daily | Edge strength update from CRM activity | relationship_manager.py | Unipile + GHL sync |
| Daily | Outreach draft generation + Gmail push | outreach_engine.py + Google Workspace MCP | HOT 24h, WARM 72h |
| Weekly | Re-score stale paths (>14 days, not converted) | pathfinder_agent.py + proximity_scorer.py | |
| Weekly | Connector effectiveness aggregate | connector_effectiveness.py | Phase 2 |
| On-onboard | Initial Unipile contact graph import | relationship_manager.import_contact_graph() | Min 50 contacts |

---

## §13 — Repo Reference

- GitHub: Ksdeng1559/Sovereign-2.0
- Branch: feature/wwr-crm-v1-westward
- Status: Not yet cloned locally — all docs in cache
- Action required: Clone repo before Stage 8+9 deploy can begin

---

*KlickSmart AI · WWR-PRD-CORE-002 · Version 2.1 · April 2026 · Confidential*
*Full Stack Implementation Plan · Supersedes PRD v2.0*
