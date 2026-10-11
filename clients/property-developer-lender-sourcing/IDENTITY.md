---
workspace: property-developer-lender-sourcing
type: methodology-template
sponsor: KlickSmartAI
status: active
created: 2026-10-10
audience: KlickSmartAI team + future property developer clients
---

# Property Developer Lender Sourcing — Methodology Workspace

## What this is

A **reusable methodology + library** for sourcing debt and equity capital for property developer clients. Each new developer engagement gets a sub-project under `projects/`, populated from the intake, scoring, and outreach templates in `library/methodology/`, and matched against the lender universe in `library/lenders/`.

This is **not** a single client engagement. It is the playbook that gets re-applied.

## What it produces

For each developer project:

1. **Intake artifact** — captured sponsor, asset, market, deal size, stage, overlays, timeline
2. **Capital stack design** — 5-layer model (senior debt → mezz → pref equity → JV equity → sponsor equity) sized to the deal
3. **Lender shortlist** — tiered universe (Tier 1 local / Tier 2 regional-FFO / Tier 3 institutional / Tier 4 international) with fit scores
4. **Outreach sequence** — 7-touch plan customized to lane (debt vs equity), jurisdiction, and referral channel
5. **Referral-channel map** — law-firm / CPA / wealth-mgr / broker pathways
6. **Compliance-routed deliverables** — every artifact classified into Lane 1-4 with appropriate disclaimers

## What it does NOT do

- Originate mortgages (Lane 2)
- Solicit securities (Lane 4)
- Provide legal, tax, or investment advice
- Fabricate lender data

## Source methodology

Borrowed from the Veritas Development Group LLC engagement (2026-08 onwards, in `~/wiki/clients/veritas-developments/`). All methodology, scoring, and compliance routing was first validated there; this workspace generalizes it.

## Folder layout

| Folder | Purpose |
|---|---|
| `_config/` | voice, conventions, glossary, compliance |
| `entities/` | developer / sponsor entity records (one per project) |
| `projects/` | per-developer sub-projects (promoted after validation) |
| `drafts/` | AI-generated work-in-progress; HITL-gated |
| `deliverables/` | promoted client-facing outputs |
| `library/lenders/` | lender profiles + index |
| `library/capital-stack/` | stack design templates + layer coverage |
| `library/methodology/` | intake, tiering, scoring, outreach, compliance, referral, deliverable templates |

## How to start a new developer project

1. Read this IDENTITY.md and `CONTEXT.md`
2. Read `library/methodology/01-intake.md` and capture project facts
3. Save intake to `entities/<developer-slug>.md` + `projects/<developer-slug>/01-intake.md`
4. Run `library/methodology/04-tam-tiering.md` against the intake
5. Pull matching lenders from `library/lenders/`
6. Score per `library/methodology/03-scorecard.md`
7. Draft outreach per `library/methodology/04-outreach-playbook.md`
8. Route compliance per `_config/compliance.md` + `library/methodology/05-compliance-routing.md`
9. Promote validated drafts to `projects/<developer-slug>/` and `deliverables/`

## Owner

KlickSmartAI. Maintainer: Hermes (Chief of Staff AI). All promoted artifacts require Dennis approval per `drafts/VALIDATION_QUEUE.md`.
