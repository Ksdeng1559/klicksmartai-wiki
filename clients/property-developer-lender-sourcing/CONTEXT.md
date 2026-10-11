# CONTEXT

## When to enter this workspace

Enter when a **new property developer engagement** lands, OR when a current developer needs new capital sourcing work (refinance, new project, expansion, recapitalization).

Do NOT enter for:
- Marketing / SEO / lead-gen work (use the marketing methodology workspaces)
- Residential mortgage broker leads (different lane)
- Pure equity-only fund-of-fund or family-office direct investing (different workspace)

## Required reading on entry

1. `IDENTITY.md` — workspace purpose, scope, what it produces
2. `_config/compliance.md` — 4-lane compliance routing
3. `library/methodology/01-intake.md` — what to capture
4. `drafts/VALIDATION_QUEUE.md` — HITL gate

## Current state (as of 2026-10-10)

- Workspace: **scaffolded, empty** — no entities, no projects, no library entries
- Library: empty templates only, ready to be populated deal-by-deal
- Reference engagement: `~/wiki/clients/veritas-developments/` (Veritas Development Group LLC, 2026-08 onwards) — borrow methodology + lender profiles as validated, not as copy

## Stage transitions

| Stage | What it means | Entry condition |
|---|---|---|
| `00-template` | Workspace is a blank methodology | Initial scaffold |
| `10-engaged` | Developer signed engagement letter; intake starts | Dennis + sponsor sign |
| `20-intake` | Project facts captured; entity record created | Intake artifact promoted |
| `30-stack-design` | Capital stack model drafted | Stack design promoted |
| `40-tam-built` | Lender universe tiered + fit-scored | TAM CSV promoted |
| `50-outreach-drafted` | 7-touch sequence drafted | Outreach playbook promoted |
| `60-active-outreach` | Sponsor executing outreach | First touch sent |
| `70-term-sheet` | Term sheet received, under evaluation | TS logged |
| `80-closing` | Commitment received, closing prep | Signed LOI/TS |
| `90-closed` | Capital closed, post-close capture | Funded |
| `99-archived` | Engagement ends | Per engagement letter |

## Routing rules

- Intake → entity record (in `entities/`) AND project intake (in `projects/<slug>/01-intake.md`)
- Library population → after first engagement validates the entry (don't pollute library with unverified data)
- Cross-workspace borrow → from Veritas when validated; from other client workspaces only after Dennis approval
