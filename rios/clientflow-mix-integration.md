# RIOS × ClientFlow × MIX Dashboard — Integration Spec

> **Status:** Draft · Active  
> **Source files:** `wiki/drafts/research/crm-financial-pros/buildout-1/spec.html`, `wiki/drafts/research/crm-financial-pros/buildout-1/index.html`, `mix-mortgage-intelligence-exchange/dashboard/index.html`  
> **Parent:** `rios/README.md`, `rios/architecture.md`  
> **KlickSmartAI · CONFIDENTIAL — Internal Use Only**

---

## What These Three Files Represent

These documents form the operational core of the financial-professionals vertical — the intake layer, the marketing layer, and the ops-monitoring layer.

| File | Role | Output |
|------|------|--------|
| `spec.html` | Product requirements + API + data model | Intake workflow, qualification engine, routing logic |
| `index.html` | Marketing landing page | Lead capture, trust signals, social proof |
| `dashboard/index.html` | Operations dashboard | Pipeline monitoring, KPI tracking, activity feed |

---

## The Missing Integration

ClientFlow and MIX Dashboard exist as standalone products. RIOS is the intelligence layer that connects them:

```
Signal detected
    ↓
ClientFlow intake (spec.html) — captures, qualifies, routes
    ↓
RIOS intelligence layer — scores, builds battlecard, routes to vertical SIP
    ↓
MIX Dashboard (dashboard/index.html) — tracks pipeline, monitors KPIs, surfaces activity
    ↓
Outreach execution (SendGrid / Vidyard / Unipile)
    ↓
RIOS learning loop — updates scores, battlecard, next-best-action
```

---

## ClientFlow Spec — Key Intelligence Inputs

From `spec.html`:

### Lead Qualification Flow
- Target: 90-second intake → qualified lead
- Signals captured: firm type, AUM target, practice area, years of experience, client profile
- Qualification output: match score (0–100%), routing recommendation

### Core Entities (from data model)
- **Lead** — name, firm, contact, source, status, score, assigned_advisor, intake_completed_at
- **Advisor** — name, specialties, capacity, current_load, vertical
- **IntakeSession** — session_id, lead_id, questions_answered, qualification_score, routing_decision
- **Opportunity** — opportunity_id, lead_id, stage, value_estimate, next_action, closed_at

### API Design (from spec.html)
- `POST /intake` — submit intake form, returns qualification result
- `GET /leads` — list leads with filters
- `GET /leads/:id` — lead detail with battlecard
- `POST /intake/session` — start intake session
- `PUT /intake/session/:id` — update session answers
- `GET /intake/session/:id/result` — get qualification result
- `POST /leads/:id/qualify` — re-run qualification

### Qualification Scoring (from spec.html)
- Practice area match (mortgage / insurance / wealth)
- AUM / revenue target alignment
- Client base profile fit
- Advisor capacity availability
- Urgency signals (renewal window, rate change, business event)

---

## MIX Dashboard — Key Intelligence Outputs

From `dashboard/index.html`:

### KPI Cards (6 metrics)
1. Active Subscribers — pipeline volume
2. Pipeline Value — deal value in motion
3. Leads This Week — intake velocity
4. Deals Closed — conversion output
5. Active Agents — capacity utilization
6. Revenue MTD — revenue intelligence

### Pipeline Activity Sparkline
- 7-day rolling activity trend
- Used for signal detection (spikes, drops, anomalies)

### Activity Feed
- Real-time agent actions: submitted, moved, commented, closed, flagged, created, assigned
- Source attribution per action
- Time-decay sorting (most recent first)

### Open Deals Database
- Columns: Name, Status (done/progress/review/todo/blocked), Assignee, Due, Priority
- Filtered: Status ≠ Done
- Sorted: Updated time

---

## How ClientFlow Feeds RIOS

```
ClientFlow intake completes
    ↓
Lead created with qualification_score + routing_decision
    ↓
RIOS triggers:
  1. Battlecard generation (who, why now, what to say, next action)
  2. SIP vertical routing (mortgage / insurance / wealth)
  3. Relationship graph update (known_connections, warm_intro_paths)
  4. Opportunity record creation (opportunity_id, lead_id, stage, value_estimate)
  5. MIX Dashboard update (new row in open deals DB)
 ↓
Outreach drafted → approved → sent
    ↓
RIOS learning loop:
  - response / no response
  - engagement level
  - meeting booked / not booked
  - score update
```

---

## How MIX Dashboard Monitors RIOS Health

| MIX KPI | RIOS Health Signal |
|---------|-------------------|
| Active Subscribers | Pipeline volume — are new leads entering? |
| Pipeline Value | Opportunity value — are deals growing? |
| Leads This Week | Intake velocity — is ClientFlow converting visitors? |
| Deals Closed | Conversion rate — is RIOS scoring accurately? |
| Active Agents | Capacity utilization — are advisors overloaded? |
| Revenue MTD | Outcome revenue — is outreach producing revenue? |

---

## Conversation State Machine (from SIP) → MIX Status Mapping

| SIP State | MIX Status | Trigger |
|-----------|-----------|---------|
| NEW_LEAD | `todo` | Signal detected, intake not started |
| ENGAGED | `progress` |2+ opens, 1+ click, or LinkedIn view |
| CURIOUS | `review` | Reply with question or info request |
| OBJECTION | `blocked` | Price/timing/competitor/trust objection |
| READY | `review` | Expressed booking interest |
| NURTURE | `todo` | 30 days no engagement |
| REMOVED | `done` | Unsubscribe — suppress permanently |

---

## Data Flow: spec.html → dashboard/index.html

```
ClientFlow spec.html (intake engine)
    ├── Lead Qualification API
    │ ↓
    │ qualification_score + routing_decision
    │       ↓
    ├── DuckDB local scoring (RIOS)
    │       ↓
    ├── Battlecard generation (RIOS)
    │       ↓
    ├── SendGrid / Vidyard outreach
    │       ↓
    └── MIX Dashboard (dashboard/index.html)
            ├── KPI update (leads, pipeline value)
            ├── New row in open deals DB
            ├── Activity feed entry
            └── Sparkline trend update
```

---

## Vertical Routing (from SIP Framework)

Every lead from ClientFlow is routed to one of three verticals before battlecard generation:

| Vertical | Profile | Compliance | Key Signals |
|----------|---------|-----------|-------------|
| **Mortgage** | Mortgage Strategist — Wealth Optimizer | MODERATE | rate_drop, refi_volume, renewal_window, equity_extraction |
| **Insurance** | Insurance Advisor — Protection First | STRICT | hiring_advisor, business_sale, policy_lapse, estate_planning |
| **Wealth** | Wealth Advisor — Strategic Capital Deployment | STRICT | liquidity_event, executive_comp,ipo_funding, inherited_wealth |

---

## Battlecard Generation Trigger

When ClientFlow returns `qualification_score >= 70%`, RIOS automatically generates a battlecard:

```json
{
  "battlecard_id": "auto-[lead_id]-[timestamp]",
  "target_person": { "from_lead": true },
  "why_now": "qualification_score [X]% — [routing_decision]",
  "opportunity_summary": "[vertical] — [practice_area] — [AUM/revenue_target]",
  "relationship_context": { "known_connections": [], "warm_intro_paths": [] },
  "recommended_message": {
    "email_subject": "[vertical] [pain_point] — [specific_signal]",
    "email_body": "[SIP-compliant hook from offer_map.json]"
  },
  "next_best_action": "[state_machine_next_state]",
  "score": {
    "opportunity_score": "[from_lead_model]",
    "relationship_score": "[from_graph]",
    "urgency_score": "[from_signal_type]",
    "overall_priority": "[computed]"
  }
}
```

---

## What's Built vs. What's Next

### Built (sample/mock data)
- `dashboard/index.html` — MIX Dashboard with mock connector, seed KPIs, static deals DB
- `spec.html` — ClientFlow product spec (design reference, not operational code)
- `index.html` — ClientFlow marketing landing page

### Required for Production
- [ ] ClientFlow intake API — wire spec.html endpoints to real data store
- [ ] DuckDB scoring layer — connect qualification scores to RIOS battlecard generation
- [ ] SIP Injection Agent — route every lead to correct vertical before battlecard
- [ ] MIX Dashboard connector — replace mock with live ClientFlow + RIOS data feed
- [ ] SendGrid integration — outbound from battlecard recommended_message
- [ ] Unipile integration — relationship capture + LinkedIn sync
- [ ] Learning loop — score updates on outreach outcome

---

## Companion Documents

- `rios/README.md` — RIOS system overview
- `rios/architecture.md` — RIOS v4.9 full architecture
- `rios/sip-framework.md` — Subscriber Injection Profile framework
- `rios/battlecard-schema.md` — Battlecard JSON schema
- `wiki/drafts/research/crm-financial-pros/buildout-1/spec.html` — ClientFlow product spec (source)
- `wiki/drafts/research/crm-financial-pros/buildout-1/index.html` — ClientFlow landing page (source)
- `mix-mortgage-intelligence-exchange/dashboard/index.html` — MIX Dashboard (source)
