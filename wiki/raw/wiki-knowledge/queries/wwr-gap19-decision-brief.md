---
title: "WWR GAP-19 Decision Brief: What Resolves, What Doesn't, What's Next"
created: 2026-04-16
updated: 2026-04-16
type: DECISION_BRIEF
tags: [wwr, gap-19, pipeda, graph-analysis, decision, pilot-readiness]
sources: [graphify-out/graph.json]
related: [entities/wealth-wire-radar, concepts/wwr-signal-pipeline, concepts/wwr-relationship-manager]
method: graphify-path-traversal
confidence: 0.95
status: active
---

# WWR GAP-19 Decision Brief
## Derived from Graphify Knowledge Graph — 2026-04-16

**Method:** Shortest-path and BFS traversal of the Hermes Agent knowledge graph (96 nodes, 124 edges). All findings are EXTRACTED or INFERRED edges — no hallucination.

---

## Finding 1 — The Entire Build Is Functionally Complete

Stages 0–7b are built and tested (57 unit + 69 smoke tests passing). The signal pipeline runs. MotherDuck is populated. The relationship manager, pathfinder, and proximity scorer are built. The battlecard generator works. The CRM frontend exists.

**The product is not incomplete. It is blocked by one compliance gap.**

---

## Finding 2 — GAP-19 Is the Single Root Blocker

GAP-19 (PIPEDA compliance for real advisor contact data) blocks **39 of 96 nodes** in the knowledge graph — including every node on the end-to-end pilot path to Wayne Stone.

### Activation Cascade on GAP-19 Resolution

| Stage | What Activates |
|-------|---------------|
| 0 (immediate) | Unipile import, Subscriber COI Network |
| 1 | `relationship_manager.py`, `connector_effectiveness.py` |
| 2 | MotherDuck RM tables, `pathfinder_agent.py`, Proximity Score |
| 3 | `proximity_scorer.py`, ICP Gate + Proximity Score dual qualification, Battlecard RM Brief, Path-Based Outreach Engine, FastAPI fully populated |
| 4 | CRM Frontend shows real battlecards, warm outreach templates, Google Workspace MCP drafting, Anonymity Principle enforced |
| 5 | Sean Carey sees HOT/WARM/VIABLE paths, Master COI Network activates, `wwr_resolve_identity` feeds real identity |

**Every node on the ICP Gate → Proximity Score → Battlecard → Sean Carey → Master COI path is currently blocked by GAP-19 and unlocked by its resolution.**

---

## Finding 3 — The Critical Path to Wayne Stone Is 7 Hops

```
Unipile (real contact import)
    ↓  populated_via
relationship_manager.py
    ↓  writes_to
MotherDuck (rm_nodes / rm_edges)
    ↓  feeds_into
FastAPI Backend (Railway)
    ↓  serves
CRM Frontend (React 19 + Firebase)
    ↓  used_by
Sean Carey (approves warm intro)
    ↓  manages
Westward Advisors Ltd.
    ↓  subscriber
Wayne Stone ← first real prospect briefed
```

Wayne Stone is already safe (he is a stakeholder node, not a system component). Every hop between Unipile and Wayne Stone is currently blocked. All 7 hops activate on GAP-19 resolution.

---

## Finding 4 — Stage 8+9 Should Be a Joint Deploy

The graph shows `CRM Frontend --serves--> FastAPI` as a bidirectional dependency. Deploying FastAPI (Stage 8) without the frontend (Stage 9) leaves the system live but invisible to Sean — no login surface, no way to approve outreach. **Stage 8 and Stage 9 should be treated as a single Railway deploy.**

---

## Finding 5 — What GAP-19 Does NOT Block

The signal pipeline is entirely safe and running:

```
wwr_search → signal_parser → wwr_classify → wwr_map_pv → wwr_generate_brief → wwr_store_signal → MotherDuck
```

Hermes already runs this daily at 6AM. Battlecards are being generated. They reach Sean's browser after Stage 8+9 but show **"No viable path — direct outreach recommended"** on every card until GAP-19 is resolved.

This means Wayne Stone can receive a v1.x-quality battlecard immediately after Stage 8+9 deploy — signal intelligence, ICP score, financial profile, planning angles — just without the warm introduction path. This is a usable pilot.

---

## Recommended Build Order

| Priority | Action | Unblocks |
|----------|--------|---------|
| 1 | Stage 8+9 joint deploy (FastAPI + Frontend → Railway) | Sean sees battlecards in browser |
| 2 | GAP-20: Schedule Sean + Wayne Stone discovery call | Confirm pilot scope and PIPEDA approach |
| 3 | GAP-19: Resolve PIPEDA compliance for Unipile contact import | 39 nodes, full v2.0 product, Wayne Stone warm path |
| 4 | Seed `rm_nodes` / `rm_edges` from Unipile | Entire relationship graph activates |

---

## Open Decisions

| Gap | Question | Impact |
|-----|----------|--------|
| GAP-14 | Auto-deliver HOT/WARM battlecards or manual approval gate? | Outreach cadence |
| GAP-15 | Portal view or email PDF for battlecard delivery? | Frontend scope |
| GAP-16 | COI intro — advisor-initiated only from battlecard? | Sean's workflow |
| GAP-19 | PIPEDA compliance approach for real contact data | 39 nodes, full v2.0 |
| GAP-20 | Schedule Sean + Wayne Stone discovery call | Pilot start date |

---

## Source

This brief was derived entirely from graph traversal of `graphify-out/graph.json` (96 nodes, 124 edges, built 2026-04-16). No content was inferred beyond what the graph contains. All paths are EXTRACTED or INFERRED edges with confidence scores 0.7–1.0.

To re-run the analysis:
```
/graphify query "what does GAP-19 block?" --graph "G:/AI-Applications/Hermes Agent/graphify-out/graph.json"
/graphify path "Unipile" "Wayne Stone"
/graphify path "ICP Gate" "Sean Carey"
```
