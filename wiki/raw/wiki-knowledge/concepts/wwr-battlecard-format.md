---
title: WWR Battlecard Format
created: 2026-04-15
updated: 2026-04-16
type: concept
tags: [wwr, battlecard, outreach, coi, advisor, format]
sources: [raw/transcripts/wwr-implementation-plan-rev3.md]
related: [entities/wealth-wire-radar, concepts/wwr-signal-pipeline, concepts/wwr-relationship-manager]
---

# WWR Battlecard Format

## Standard Battlecard (ASCII Box)

```
┌─────────────────────────────────────────┐
│  HOT — Score 91                         │
│                                         │
│  James Kirkland                         │
│  Kirkland Civil Contracting Ltd         │
│  Vancouver, BC — Construction           │
│                                         │
│  WHY NOW                                │
│  BC Registry director change detected   │
│  22-year CCPC — signal 4 days old       │
│                                         │
│  FINANCIAL PROFILE                      │
│  Est. Net Worth:    $25–50M             │
│  Retained Earnings: $10–20M             │
│  Estate Tax Risk:   HIGH                │
│  Insurance Gap:     Likely              │
│                                         │
│  PLANNING ANGLES                        │
│  • Retained earnings fully taxable      │
│    on death without structure           │
│  • Family trust (2009) — estate         │
│    freeze opportunity                   │
│  • No buy/sell insurance detected       │
│                                         │
│  RECOMMENDED ANGLE                      │
│  "What happens to your retained        │
│   earnings when you step back?"         │
│                                         │
│  COI MATCH                              │
│  David Morrison, CPA — BC              │
│  Brief ready for your approval          │
│                                         │
│  [ Approve Outreach ] [ Activate COI ] │
│  [ View Full Profile ] [ Dismiss ]     │
└─────────────────────────────────────────┘
```

## Design Rules

- **ASCII box layout** — Telegram-safe, renders in any client/email/terminal
- **Signal age** is first-class citizen — "4 days old" in WHY NOW section
- **Tier badge + score** at the top (HOT / WARM / DEVELOPING + numeric score)
- **Action buttons** embedded at bottom
- **COI name** hidden from prospect — Sean's brief gets pattern intelligence only (anonymity principle)

## v2.0 RM Brief Upgrade (NOT YET BUILT)

When `pathfinder_agent.py` is complete, the battlecard adds a Relationship Manager Brief section:

| Score Band | RM Brief Display |
|---|---|
| 85–100 HOT PATH | Gold-bordered path section, connector name prominent |
| 70–84 WARM PATH | Standard path section with intro script |
| 50–69 VIABLE PATH | Path listed, advisor prompted to verify relationship strength |
| < 50 NO PATH | "No viable path — direct outreach recommended" |

## Outreach Templates

### v2.0 Path-Based Warm (NEW — collapses cold→warm)

> *"Hi John — I was speaking with David Chen at RBC recently — he's been working with your team on the Meridian transition — and your situation came up in the context of estate timing. I wanted to share a brief perspective on what we're seeing in the BC market right now…"*

References: connector name + shared_context_tags + prospect's signal event.

### v1.x Cold-Adjacent (Deprecated)

> *"Hi John — I noticed your recent corporate restructuring and wanted to reach out about tax-efficient wealth transfer strategies…"*

Referencing a public event the prospect already knows. No relationship context. Indistinguishable from cold email.

## Delivery Gaps (Open)

| Gap | Question |
|-----|----------|
| GAP-14 | Auto-deliver HOT/WARM battle cards, or manual approval gate? |
| GAP-15 | Portal view or email PDF for battle card delivery? |
| GAP-16 | COI intro — advisor-initiated only from battle card? |
