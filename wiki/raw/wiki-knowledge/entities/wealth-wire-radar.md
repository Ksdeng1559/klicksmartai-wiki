---
title: WealthWireRadar — Signal-Driven Intelligence for Canadian Financial Advisors
url: https://github.com/Ksdeng1559/Sovereign-2.0 (feature/wwr-crm-v1-westward)
category: signal-intelligence, crm, financial-advisors, multi-agent
product-owner: Dennis E. (KlickSmartAI)
client: Westward Advisors Ltd. (Wayne Stone, subscriber)
---

# WealthWireRadar (WWR)

**WealthWireRadar** is a signal-driven intelligence platform for Canadian financial advisors — built on Hermes Agent, it detects HNWI wealth inflection signals and generates Battlecard intelligence briefs for path-based outreach.

---

## Core Function

1. **Signal Detection** — Monitors for wealth triggers (business sales, director changes, CCPC succession, retained earnings)
2. **Battlecard Generation** — AI-generated 2-page intelligence brief before every advisor meeting
3. **COI Routing** — Path-based referral network (proximity scorer + BFS pathfinder)
4. **Outreach Orchestration** — Multi-channel delivery via Unipile (LinkedIn, email, SMS)

---

## ICP (Ideal Client Profile)

- **Geography:** BC / AB / ON
- **Net Worth:** $25M+ (HNWI)
- **Corporate Income:** $2M+ corporate taxable income
- **Profile:** Owner-operators in construction, manufacturing, real estate, professional services
- **Triggers:** Business sale, director change, CCPC succession, retained earnings

---

## ICP Qualification

| Score | Action |
|-------|--------|
| ≥70% NW + ≥70% income confidence | **HOT** — 24hr outreach |
| 40–69% | **WARM** — 72hr |
| <40% | **DEVELOPING** — not briefed |

---

## Architecture

```
Hermes Agent (NousResearch — daily 6AM PT)
  → wwr_search (Serper + Tavily + Brave)
  → signal_parser
  → wwr_classify
  → wwr_map_pv
  → wwr_resolve_identity
  → wwr_match_coi
  → wwr_generate_brief
  → wwr_store_signal
  → FastAPI Backend (Railway)
  → React 19 + Firebase Frontend
  → MotherDuck (DuckDB) — multi-tenant
  → Unipile — CRM comm layer
```

---

## Signal Pipeline (9 Steps — ALL BUILT)

| Step | Module | Status |
|------|--------|--------|
| 1 | `tri_engine_search.py` (Serper + Tavily + Brave) | ✅ Built |
| 2 | `signal_parser.py` | ✅ Built |
| 3 | `signal_classifier.py` | ✅ Built |
| 4 | `preliminary_viewpoint_mapper.py` | ✅ Built |
| 5 | `wwr_resolve_identity()` | ✅ Built |
| 6 | `wwr_match_coi()` | ✅ Built |
| 7 | `wwr_generate_brief()` | ✅ Built |
| 8 | `wwr_store_signal()` | ✅ Built |
| Stage 5 | `wwr_tools.py` (7 Hermes tools) | ✅ Built |

---

## Dubb Integration — Video Outreach for WWR

WealthWireRadar generates qualified Battlecards → **Dubb** creates personalized video outreach → delivered via **Unipile** → tracked in **WealthWireRadar CRM**.

### The WWR → Dubb Workflow

```
Battlecard Generated (WWR)
    ↓
Dubb: Personalized video message recorded
    ↓
Unipile: Delivered via LinkedIn DM / Email / SMS
    ↓
Prospect watches video → 30-40% LinkedIn response rate
    ↓
Meeting booked → Battlecard upgraded to Meeting Brief
```

### Elite Insurance Proof Point (Same Vertical)

**Elite Insurance of Merrillville** (life insurance agency) — CEO Sean Grant, 20+ years:
- Same challenge: crowded, commoditized market — how to stand out
- Solution: Dubb personalized video for each client
- Result: Positioned as leading figure in competitive market
- Quote: *"It's invaluable to my business. I can confidently say it's priceless."*

**For WWR subscribers (financial advisors/insurance agents):**
- Same differentiation challenge
- Same solution: personalized video outreach per Battlecard prospect
- Same result: stand out from advisors sending text-only emails

### Video Outreach Statistics for Financial Advisors

- Video email response: **25–30%** vs 5% text-only
- LinkedIn + video response: **30–40%**
- SMS response: **45%**
- 60%+ of sales teams using video report higher response rates

---

## Battlecard Format

```
┌─────────────────────────────────┐
│  HOT — Score 91                 │
│  James Kirkland                 │
│  Kirkland Civil Contracting Ltd │
│  Vancouver, BC — Construction   │
│                                 │
│  WHY NOW                        │
│  [signal rationale + age]      │
│                                 │
│  FINANCIAL PROFILE              │
│  Est. Net Worth / Retained      │
│                                 │
│  PLANNING ANGLES                │
│  [retained earnings / trust]   │
│                                 │
│  RECOMMENDED ANGLE              │
│  [cold email / intro question]  │
│                                 │
│  OUTREACH: [Video Message 🔴]   │
│  COI MATCH                      │
└─────────────────────────────────┘
```

---

## Open Gaps

| Gap | Description | Blocking |
|-----|-------------|---------|
| GAP-14 | Auto-deliver HOT/WARM battlecards or manual approval? | No |
| GAP-15 | Portal view or email PDF for battlecard delivery? | No |
| GAP-16 | COI intro — advisor-initiated only? | No |
| GAP-19 | PIPEDA legal review before real advisor data | **YES — blocks Stage 10** |

---

## Related

- [[boss-raas]] — BOSS Revenue OS (extends WWR framework into Financial Services RaaS)
- [[boss-sip]] — Subscriber Intake Profile for onboarding
- [[dubb]] — Video communication (outreach layer for WWR)
- [[unipile]] — CRM / communication layer
- [[motherduck]] — DuckDB analytics layer
