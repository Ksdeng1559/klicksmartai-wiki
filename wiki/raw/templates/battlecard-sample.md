---
title: WWR Battle Card Sample
created: 2026-04-15
type: raw
source: provided by Dennis E. / KlickSmart AI — Wealth Wire Radar
---

# WWR Battle Card — Sample Format

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
│  "What happens to your retained         │
│   earnings when you step back?"         │
│                                         │
│  COI MATCH                              │
│  David Morrison, CPA — BC              │
│  Brief ready for your approval          │
│                                         │
│  [ Approve Outreach ] [ Activate COI ]  │
│  [ View Full Profile ] [ Dismiss ]      │
└─────────────────────────────────────────┘
```

## Field Mapping

| Section | Field | Source |
|---------|-------|--------|
| Tier badge + Score | HOT 91 | signal_classifier.py → composite WWR score |
| Name | James Kirkland | entity_name from signal_parser |
| Company | Kirkland Civil Contracting Ltd | entity_name from signal |
| Location + Industry | Vancouver, BC — Construction | province + icp_category |
| WHY NOW | BC Registry director change + signal age | wwr_classify + signal_date |
| Est. Net Worth | $25–50M | pv_07 (inferred) |
| Retained Earnings | $10–20M | pv_18 |
| Estate Tax Risk | HIGH | pv_09 |
| Insurance Gap | Likely | pv_11 + age/tenure |
| Planning Angles | Bullet list | Claude Sonnet via battlecard_generator.py |
| Recommended Angle | One-line question | Section 08 Video DM angle + AI |
| COI Match | David Morrison, CPA | coi_mapper.py (Section 18) |
| Action buttons | Approve / Activate / View / Dismiss | UI layer — portal or email |

## Key Design Notes

- ASCII box format — no rendering dependency, works in Telegram, email, terminal
- Signal age is first-class — "4 days old" in WHY NOW header
- COI section shows brief status — "ready for your approval" (Sean's gate)
- Action buttons are part of the card itself — not just information
- Score + tier badge prominently at top
- Recommended angle uses the Video DM angle language from Section 08
