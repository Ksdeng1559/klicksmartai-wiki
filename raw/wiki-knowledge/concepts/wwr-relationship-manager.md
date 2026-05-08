---
title: WWR v2.0 Relationship Manager
created: 2026-04-15
updated: 2026-04-16
type: concept
tags: [wwr, relationship-manager, pathfinding, coi, proximity-scorer, v2, architecture]
sources: [raw/transcripts/wwr_prd_v2_relationship_manager.md]
related: [entities/wealth-wire-radar, concepts/wwr-signal-pipeline, concepts/wwr-proximity-scorer, concepts/wwr-battlecard-format]
---

# WWR v2.0 Relationship Manager

## Architectural Shift

**Old (v1.x):** *Does the advisor know someone in the prospect's industry?* → one-hop lookup, category filter.

**New (v2.0):** *What is the shortest path from this advisor to this prospect, how strong is each edge, and which connector yields the highest probability of a warm introduction?* → scored path graph traversal.

## Node Type Taxonomy

| Node Type | Role | Description |
|-----------|------|-------------|
| **RM (Relationship Manager)** | Root node | The advisor/subscriber. Source of contact graph. Root of every path computation. |
| **Connector** | Intermediate node | 1°/2°/3° contact. Has strength score (0–100), recency, industry, shared context tags. Replaces v1.x COI category. |
| **Prospect** | Target node | HNW individual from signal engine. Holds signal context: event type, WWR score, cluster, urgency. |
| **Relationship Edge** | Weighted, directed, time-decaying | strength (0–100), recency_days, industry_overlap (bool), shared_context (tags), computed edge_score |

## Pathfinder Logic

BFS traversal from RM → Prospect. MAX_DEGREES = 4. PROXIMITY_SCORE_FLOOR = 50 (paths below this are pruned).

**Path example:**
```
RM (Advisor) ──── C1 (1° CPA) ──── C2 (2° Banker) ──── HNW (Prospect)
Path Strength: 82/100 · Best Intro: C1 (CPA) · Degrees: 3 · Action: Warm Intro Request
```

**Hard Rule:** `TenantIsolationError` on any cross-tenant traversal attempt. Every query scoped to single `subscriber_id` via `TenantContext`.

## Proximity Score

Composite of 5 factors. Max raw: 165 pts → normalized to 0–100.

| Component | Value | Notes |
|-----------|-------|-------|
| Base: Degree Distance | `100 − (Degrees × 15)` | 4°=40, 3°=55, 2°=70, 1°=85 |
| + Relationship Strength | 0–30 pts | recency × interaction_depth × mutual_context |
| + Event Relevance | 0–25 pts | connector industry match to signal cluster |
| + Timing | 0–20 pts | signal recency modifier (same scale as WWR scorer) |
| + Shared Context | 0–10 pts | deal, geography, association overlap |

## Action Thresholds

| Score Band | Label | Action | Window |
|---|---|---|---|
| 85–100 | **HOT PATH** | Immediate warm intro request | 24h |
| 70–84 | **WARM PATH** | Warm intro — schedule | 72h |
| 50–69 | **VIABLE PATH** | Assess connector strength first | advisor judgment |
| < 50 | **NO PATH** | Direct outreach recommended | — |

## v2.0 vs v1.x

| Area | v1.x | v2.0 |
|------|------|------|
| COI Layer | `coi_mapper.py` — 1°/2° lookup, 6 category weights | `relationship_manager.py` — full graph, scored edges, multi-tenant |
| Path Finding | Static category lookup | BFS/DFS graph traversal, 1–4 degree path construction |
| Proximity Score | Category weight only (6 values) | Composite: 5 components, max 165 → 0–100 |
| Battlecard Output | COI name + intro script | Full proximity brief — path diagram, scored connectors |
| Outreach Generation | Cold template with COI name | Path-based warm framing — collapses cold→warm |
| Multi-Tenant | RLS via Supabase (deprecated) | `subscriber_id` filter + `TenantContext` wrapper |
| Learning Layer | Not defined | `connector_effectiveness.py` — tracks reply/conversion rates |

## Build Order

1. signal_parser smoke test → DDL (`rm_nodes`, `rm_edges`, `rm_path_results`) → `relationship_manager.py` → `proximity_scorer.py` → `pathfinder_agent.py` → Battlecard RM Brief upgrade → path-based outreach engine

## Module Specs

| Module | Lines | Responsibility |
|--------|-------|----------------|
| `relationship_manager.py` | ≤350 | Import/upsert contacts, graph retrieval, edge updates. All scoring delegates to `proximity_scorer.py`. |
| `pathfinder_agent.py` | ≤350 | BFS traversal, calls `relationship_manager.py` + `proximity_scorer.py`. Returns `PathfinderResult`. RM-02: ≤3s for 500 nodes. |
| `proximity_scorer.py` | ≤350 | Score computation. All constants from `config.py`. Single `score_path()` method. |
| `connector_effectiveness.py` | ≤350 | Phase 2 learning layer. Reply → +10, meeting → +20, no response 30d → −5, COI referral → +30. |

## DDL — RM Graph Tables

```sql
-- rm_nodes: All nodes in the relationship graph
CREATE TABLE rm_nodes (
    node_id         VARCHAR PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR,
    subscriber_id   VARCHAR NOT NULL,
    node_type       VARCHAR NOT NULL,  -- 'RM' | 'CONNECTOR' | 'PROSPECT'
    full_name       VARCHAR,
    title           VARCHAR,
    company         VARCHAR,
    industry        VARCHAR,
    linkedin_url    VARCHAR,
    coi_category    VARCHAR,
    province        VARCHAR,
    imported_from   VARCHAR,  -- 'unipile' | 'crm' | 'manual'
    created_at      TIMESTAMP DEFAULT now(),
    updated_at      TIMESTAMP DEFAULT now()
);

-- rm_edges: Weighted directed edges
CREATE TABLE rm_edges (
    edge_id             VARCHAR PRIMARY KEY,
    subscriber_id       VARCHAR NOT NULL,
    from_node_id        VARCHAR NOT NULL,
    to_node_id          VARCHAR NOT NULL,
    relationship_type   VARCHAR,   -- 'direct' | 'inferred' | 'shared_group'
    strength            FLOAT DEFAULT 50.0,
    recency_days        INTEGER,
    industry_overlap    BOOLEAN DEFAULT FALSE,
    shared_context_tags VARCHAR[],
    edge_score          FLOAT,
    created_at          TIMESTAMP DEFAULT now(),
    last_interaction_at TIMESTAMP
);

-- rm_path_results: Stored pathfinder outputs
CREATE TABLE rm_path_results (
    result_id           VARCHAR PRIMARY KEY,
    subscriber_id       VARCHAR NOT NULL,
    prospect_id         VARCHAR NOT NULL,
    path_node_ids       VARCHAR[],
    degrees             INTEGER,
    best_connector_id   VARCHAR,
    proximity_score     FLOAT,
    action_threshold    VARCHAR,  -- HOT_PATH | WARM_PATH | VIABLE_PATH
    outreach_status     VARCHAR DEFAULT 'pending',
    converted           BOOLEAN DEFAULT FALSE,
    created_at          TIMESTAMP DEFAULT now()
);
```
