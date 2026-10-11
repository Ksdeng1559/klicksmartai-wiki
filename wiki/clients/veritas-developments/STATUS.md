---
title: "Veritas Developments — STATUS"
type: workspace-status
last_updated: 2026-10-10
maintainer: agent:hermes
approver: Dennis Eng
okf_version: "0.2"
---

# Veritas Developments — Status

## 2026-10-10 — Notion sync (5-week delta, atomic CRM pivot)

**Source:** Notion search + 4 page fetches + 4 database queries
**Delta report:** `drafts/notion-sync-2026-10-10.md` (239 lines, full detail)
**Author:** agent:hermes

### What changed

- **Architecture pivot** — Veritas converts to **Atomic CRM + Supabase** as primary CRM (2026-10-08 ADR, approver Dennis). Frappe/ERPNext plan from 2026-08-29 is now **legacy**.
- **4 new top-level Notion pages** mirrored as read-only references:
  - `drafts/notion-mirror/capital-relationship-os-2026-10-08.md` (canonical CRM impl source)
  - `drafts/notion-mirror/dev-os-architecture-2026-10-01.md` (13-layer architecture, M&A Radar, Capital Markets OS)
  - `drafts/notion-mirror/real-estate-capital-os-pilot-2026-09-20.md` (CONFLICT — predates pivot, still says "Frappe")
  - `drafts/notion-mirror/investor-white-paper-2026-09-08.md` (6-paper portfolio, HITL workflow)
- **4 Notion databases** queried for live state (Opportunity & Capital Radar, Cockpit, Tasks & MITs, Master Projects)
- **Active opportunities** (Opportunity Score): 89 = CRE Financing Platform; 89 = 30-Day BD & Capital Sprint; 84 = Prime Lee's Summit; 83 = Construction & Renovation Opportunity Engine; 81 = Stonehaven Estates
- **7 active MITs** captured (Dennis: 3, David: 2, Daniel: 1, Peaches: 1)

### What was archived (per no-delete standing rule)

- `drafts/veritas-development-os/JOB.md` (Frappe/ERPNext 5-phase build plan, 2026-08-29) → `_archive/veritas-development-os-frappe-2026-08-29/JOB.md` with `_archive/veritas-development-os-frappe-2026-08-29/STATUS.md` recording:
  - **superseded_by** (2 Notion page IDs)
  - **supersession_decision** (source: Notion ADR, approver: Dennis Eng, summary: Atomic CRM + Supabase pivot)
  - **change_log_sections**: 6 (Required New Supabase Tables) + 17 (Compliance and Governance Guardrails)

### What still needs you (HITL)

Three new gate items added to `drafts/VALIDATION_QUEUE.md`:
- **Item 6** — Atomic CRM Capital OS 5-sprint build: which prep step to start (staging Supabase project, two-tenant isolation test, Clerk Organizations, securities counsel)?
- **Item 7** — Investor White Paper Paper 1: should I prep the research plan + claim register for your evidence-quality review?
- **Item 8** — Real Estate Capital OS Pilot Frappe-pivot conflict: (a) update the Notion page now, (b) add a single ADR callout, (c) leave with conflict note?

### Open wiki work (not part of this sync, still pending)

- CLIENT-SCORE 2026-08-28 2-item debt: Daniel Reg-D adjacency, David KC Business Journal PR pitch
- Methodology library: 28-file template at `~/wiki/clients/property-developer-lender-sourcing/` ready for any future property developer (Veritas remains reference, library empty by design)

### Standing rules preserved

- All AI-generated material lands in `drafts/` first; HITL before promotion
- Never delete superseded content — move + update STATUS.md
- No fabricated contact/org data into CRM rows
- Self-host all credential storage (use [REDACTED] in any exported summary)
- "it looks fine" is the close, no essay
