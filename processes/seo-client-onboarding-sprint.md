---
title: SEO Client Onboarding Sprint — End-to-End Operating System
created: 2026-08-26
updated: 2026-08-26
type: process
tags: [how-to, guide, technology, icm, openseo, seo, onboarding, sprint]
sources: [skills/client-onboarding-sprint, skills/icm-client-workspace-setup, skills/audit-page-gate]
related: [lead-sniperai-cli-os, honcho-multi-agent-wiring, content-growth-strategies]
---

# Executive Summary

This document defines the operating system for onboarding a new SEO client — from cold-start to first-touch artifact in approximately 70 minutes of wall-clock time.

The system is designed around one principle:

> **Show value before asking for budget.** Every SEO client engagement begins with a free, gatekept audit artifact that demonstrates competence and identifies the work. Spending happens only AFTER the client signs.

The system supports one connected commercial rail:

```plain text
SEO Client Onboarding
Identify prospect + capture domain
→ scaffold ICM workspace (identity, voice, gatekeeping)
→ create OpenSEO project (linked to workspace)
→ run pilot site audit (10 pages, ~$0.30)
→ build 3 gatekept client-facing drafts (1-page visual + long-form + quote)
→ Dennis approves
→ promote to projects/ + deliverables/, send to prospect
→ on signature → execute engagement (Phase 1-4 per quote sheet)
```

The initial rule is:

> **Workspace before audit, audit before artifacts, artifacts before signature, signature before spend.** Each phase gates the next. If the prospect signs after Phase 3 (the artifacts), the engagement starts immediately. If they don't sign, you've spent ~$0.30 in credits and produced a reusable audit artifact — no waste.

# 1. System Outcome

## Primary outcome

Build a repeatable SEO client onboarding sprint that converts a cold prospect into an audit-engaged prospect in under 70 minutes, with all artifacts gatekept against internal-cost disclosure.

## Economic drivers

The system supports revenue through:

- **Fixed-fee SEO engagements** (Foundation, Keyword Research, Content, Reporting phases)
- **Monthly retainers** for ongoing management
- **Project-based work** (site migrations, content rewrites)
- **Audit-to-engagement conversion** (the first-touch artifact IS the sales tool)

## Trust-meter doctrine

Prospect trust starts at zero.

- Receiving a free audit requires approximately 6/10 trust.
- Signing an engagement requires approximately 7/10 trust.
- Renewing the engagement (month 6+) requires approximately 8/10 trust.

Every system interaction must increase trust through:

- **Insight before mechanics** — show what we found, not how we found it
- **Specificity** — real numbers (issue counts, page counts), not handwavy claims
- **Vancouver/market-aware** language (or whatever market the client is in)
- **No-disclosure of method** — never reveal internal tools, costs, or sequencing

Trust is reduced by:

- Generic audit templates (looks like every other agency)
- Quoting exact tool costs ("DataForSEO charges $X per credit")
- Revealing internal skill names or workflow architecture
- Promising specific ranking positions or traffic numbers
- Hiding the price ("let's get on a call to discuss pricing")

# 2. Process Phases

## Phase 0 — Pre-flight (5 min)

**Inputs:** Client name, domain, market, principals (optional), engagement type (optional).

**Steps:**
1. Verify slug uniqueness against `/home/denni/wiki/clients/`
2. Normalize slug to kebab-case
3. Confirm market code (CA=2124, US=2840, UK=2826)
4. Confirm OpenSEO container is healthy
5. Confirm python-markdown is installed

**Outputs:** Verified inputs.

**Failure mode:** Slug collision — abort and pick a different slug.

## Phase 1 — ICM workspace scaffold (15 min)

**Skill:** `icm-client-workspace-setup`

**Goal:** Client workspace exists at `~/wiki/clients/<slug>/` with correct identity, voice, and gatekeeping infrastructure.

**Steps:**
1. Create folder tree (CLAUDE.md, IDENTITY.md, CONTEXT.md, README.md, _config/, projects/, drafts/, deliverables/, drafts-preview/, skills/)
2. Write 5 _config files (voice.md, conventions.md, deliverables.md, glossary.md, gtm-skills.md)
3. Write per-folder READMEs
4. **Surface CLAUDE.md proposed diff for explicit user approval** (Hermes safety layer blocks autonomous writes)
5. On approval, write CLAUDE.md
6. Run verifier — expect 19/19 pass

**Outputs:** Verified workspace, awaiting CLAUDE.md approval.

**Failure mode:** User declines CLAUDE.md write — workspace is degraded (agents won't auto-load ICM routing without it). Offer to skip with manual routing.

## Phase 2 — OpenSEO + DuckDB mirror (10 min)

**Skills:** `openseo-project-intake` (project creation), `d1-to-duckdb-mirror` (mirror pattern)

**Goal:** OpenSEO knows about the client; DuckDB analytical mirror is operational.

**Steps:**
1. OpenSEO `create_project` — capture `projectId` (required for ALL future calls)
2. OpenSEO `update_project_context` — write business overview, current goal, positioning, brand voice
3. OpenSEO `run_site_audit` — pilot with `maxPages: 10` (min allowed by tool), `runLighthouse: False`
4. Poll `get_audit_status` until `status == "completed"`
5. Pull all issues via `get_audit_issues` (paginate by severity: critical, warning, info, limit 200)
6. Pull pages via `get_audit_pages`
7. Copy GPC sync script template → adapt for new client
8. Place sync script at `~/wiki/clients/<slug>/scripts/sync-<slug>-duckdb.py`
9. Copy to `~/.hermes/scripts/` for cron discoverability
10. Schedule cron: `cronjob create` with `no_agent=True`, `script=<name>.py`, `schedule=every 30m`, `workdir=<workspace>`

**Outputs:** OpenSEO project synced; DuckDB mirror operational with cron sync.

**Failure modes:**
- `auditId` missing — verify field is `structuredContent.auditId`, not `result.auditId`
- DuckDB views fail on empty tables — create empty fallback tables with the right schema
- Cron uses LLM-driven prompt instead of direct script — change to `no_agent=True`

## Phase 3 — Client-facing artifacts (30 min)

**Skill:** `audit-page-gate` (gatekeeping discipline)

**Goal:** Three drafts ready for Dennis's review — diagnosis + long-form + quote.

### 3a. Visual 1-page audit (HTML, self-contained)

The first-touch artifact. Self-contained HTML with inline SVG.

**5 visual sections:**
1. Score card (SEO health 0-100, color-coded)
2. Issue fingerprint (SVG radar, 7 issue categories)
3. Priority ladder (P1/P2/P3 with single-line actions per rung)
4. Impact bars (3 before/after comparisons)
5. Engagement timeline (4 horizontal steps: Foundation → Growth → Polish → First signals)

**File:** `drafts-preview/seo/audit-1page-<date>-<slug>.html`
**Companion stub:** `drafts/seo/audit-1page-<date>-<slug>.md` (1-2 KB describes the artifact)

### 3b. Long-form audit (Markdown)

For clients who want depth. Same gatekept content, expanded prose.

**7 sections:**
1. At a glance
2. What we audited
3. What we found
4. What it means (for you)
5. Recommended actions (P1/P2/P3)
6. Why this matters for SEO
7. What changes once these are fixed
8. Next step (CTA)

**File:** `drafts/seo/audit-<date>-<slug>.md`
**Preview:** `drafts-preview/seo/audit-<date>-<slug>.html` (rendered via `scripts/render-report.py`)

### 3c. Quote sheet (Markdown)

Internal-facing (not for client unless they ask). Quoted phases, fixed fees, signature line.

**7 sections:**
1. Executive summary
2. What we audited
3. What we found
4. Engagement quote (4 phases)
5. Pricing
6. What's included / what's NOT
7. Work order signature line

**File:** `drafts/seo/audit-quote-<date>-<slug>.md`
**Preview:** `drafts-preview/seo/audit-quote-<date>-<slug>.html`

### Gate check (all three)

Before writing, verify NO occurrence of:
- Tool names (DataForSEO, Serper, On-Page.ai, etc.)
- Credit cost numbers (~$30, $0.018, etc.)
- Specific target keywords (general categories OK)
- Phase / day detail (Day 1: title tags)
- Engagement pricing in the audit pages ($8,000 quote belongs in quote sheet only)
- Internal skill names (site-audit, paa-demand-mining)

**Outputs:** 3 drafts in `drafts/seo/`, 2 HTML previews in `drafts-preview/seo/`.

**Failure mode:** Gate violation — reword immediately. Run gate_checks programmatically before declaring done.

## Phase 4 — VALIDATION_QUEUE + Approval gate (5 min)

**Goal:** Dennis knows what's pending and can sign off.

**Steps:**
1. Update `drafts/seo/VALIDATION_QUEUE.md` with all 3 drafts as `pending Dennis review`
2. Surface drafts to Dennis (mention paths, sizes, key takeaways)
3. **Wait for explicit approval** — never auto-promote

**Approval patterns:**
- "approve all three" → promote all three
- "approve 1-page only" → promote just the visual
- "clean up + approve" → remove test seeds, then promote
- "tweak <thing>" → update draft, re-validate

**Outputs:** Three rows in VALIDATION_QUEUE, `pending Dennis review`.

## Phase 5 — Promote + send (10 min, post-approval)

**Skill:** `openseo-data-export`

**Goal:** Approved drafts become client-ready deliverables.

**Steps:**
1. For each approved draft: `mv` from `drafts/seo/` → `projects/seo/`
2. Render to HTML via `scripts/render-report.py` → `deliverables/seo/`
3. Export DuckDB views to CSV → `deliverables/seo/csv/`
4. Update VALIDATION_QUEUE row to `promoted` with date
5. Send to client (email body is gated — Dennis writes or approves first)

**Outputs:** Promoted artifacts in `projects/` + `deliverables/`. Client receives first-touch artifact.

# 3. Cost & Time

## Per-client onboarding cost

| Component | Cost |
|---|---|
| ICM workspace scaffold | $0 |
| OpenSEO create_project | free |
| OpenSEO update_project_context | free |
| OpenSEO pilot audit (10 pages) | ~$0.30 |
| OpenSEO get_audit_issues / get_audit_pages | free |
| DuckDB mirror initial sync | $0 |
| 3 client-facing drafts | $0 |
| HTML preview rendering | $0 |
| Cron schedule | $0 |
| **Total** | **~$0.30 per new client** |

## Per-client onboarding time

| Phase | Wall-clock |
|---|---|
| 0. Pre-flight | 5 min |
| 1. ICM scaffold | 15 min |
| 2. OpenSEO + DuckDB | 10 min |
| 3. Artifacts (3 drafts) | 30 min |
| 4. VALIDATION_QUEUE + Approval gate | 5 min (mostly waiting) |
| 5. Promote + Send | 10 min |
| **Total** | **~70 min** |

After Dennis approves + signs engagement, add 30-45 min for Phase 1 work (fixing all audit issues) before client receives first deliverable.

# 4. Recurring Engagement Pattern

After the client signs, the engagement follows the same 5-phase shape, expanded:

```
Phase 1 — Foundation (Week 1-2)
  Fix all audit issues
  Per-issue tracking in VALIDATION_QUEUE.md

Phase 2 — Keyword research (Week 3-4)
  5 seed keywords × 300 related each
  SERP intelligence on top 20
  PAA + social mining for demand discovery
  Content brief: 8 priority articles

Phase 3 — Content production (Week 5-10)
  8 SEO articles (1,500-2,500 words each)
  On-page optimization via content-optimization skill
  Internal linking refresh
  Outbound authority links

Phase 4 — Monthly measurement loop (Week 11-12 + ongoing)
  Rank tracker (top 25 keywords, monthly)
  GA4 + GSC reports (monthly)
  PAA refresh (quarterly)
  Content refresh as needed
```

Each phase produces artifacts via the same workflow: drafts → VALIDATION_QUEUE → approval → promote → deliver.

# 5. Per-Client Inputs (Configuration Template)

When starting a new client sprint, collect these inputs first:

| Input | Example | Source |
|---|---|---|
| `client_name` | "GPC Development" | User |
| `client_slug` | "gpc-development" | Auto-derived from name (kebab-case) |
| `client_domain` | "gpcdevelopment.ca" | User |
| `market_code` | 2124 (Canada) | DataForSEO location code |
| `language_code` | "en" | User |
| `principals` | "Tak Ho, Zulliy Alnahas" | User |
| `engagement_type` | "SEO audit + organic inbound leads" | User |
| `compliance_mode` | "none" / "securities" / "privacy" | User (depends on engagement) |
| `verticals` | ["seo"] | Default |
| `default_voice` | "default" / "punchy" / "editorial" | User |
| `engagement_start_date` | TBD | Set on signature |
| `quote_total` | $8,000 | Calculated from quote sheet |
| `payment_terms` | "50/25/25%" | Default |

# 6. Failure Modes & Recovery

| Failure | Detection | Recovery |
|---|---|---|
| Slug collision | `ls` fails | Pick different slug |
| OpenSEO container down | `docker ps` empty | Restart via `openseo-deploy` skill |
| Pilot audit fails | `get_audit_status` returns `failed` | Inspect `error_code`, retry with smaller `maxPages` |
| DuckDB views fail on empty tables | `Catalog Error` in view creation | Create empty fallback tables with right schema |
| Gate violation detected | Manual review or programmatic check | Reword draft, re-validate |
| User declines CLAUDE.md | User says "skip" | Workspace operates in degraded mode (manual routing) |
| Cron sync fails | Check cronjob status | Manually run `~/.hermes/scripts/sync-<slug>-duckdb.py` |
| OpenSEO `auditId` missing | Field returns null | Verify script reads `structuredContent.auditId`, not `result.auditId` |
| Quote sheet pricing disputed | User review | Update phases, re-render |
| Client doesn't sign | Days/weeks pass | No-cost — audit artifact remains in drafts/ for future re-use |

# 7. Related Skills

| Skill | When |
|---|---|
| `icm-client-workspace-setup` | Just workspace scaffold (no audit) |
| `audit-page-gate` | Gatekeeping discipline (apply to any client-facing report) |
| `seo-enrichment-planner` | When client signs and engagement begins (credit planning) |
| `site-audit` | When audit data is needed (this skill calls it) |
| `openseo-project-intake` | Just OpenSEO setup (no workspace) |
| `openseo-data-export` | Promote drafts to projects/ + deliverables/ |
| `openseo-deploy` | Restart container if needed |
| `d1-to-duckdb-mirror` | General D1→DuckDB pattern (not client-specific) |
| `hermes-mcp-cmd-windows` | WSL+cmd.exe MCP install pattern (for setup) |
| `github-fork-fallback` | If pushing code changes upstream (rare) |

# 8. Pattern Provenance

| Origin | Date | Notes |
|---|---|---|
| GPC Development engagement | 2026-08-26 | First end-to-end run; all phases verified |
| This process doc | 2026-08-26 | Skill + doc shipped together |
| Veritas Developments | (future) | Next replication candidate (securities mode) |
| Spectra Holdings | (future) | Faith-framed — will need custom voice.md |

# 9. Future Work

| Improvement | Owner | Notes |
|---|---|---|
| Reusable script template for `sync-<slug>-duckdb.py` | Dennis | Currently copy from GPC + edit project ID |
| Auto-pilot mode (skip HITL on subsequent clients after template proven) | Future | Not safe until 2-3 replications |
| CRM integration (auto-log prospects + sent artifacts) | Future | Once prospect pipeline volume warrants |
| Client-facing portal (link to `deliverables/seo/`) | Future | Once first client asks for it |

---

*This document is the source of truth for SEO client onboarding. Any change to the sprint workflow should update both this doc AND the `client-onboarding-sprint` skill in `~/.hermes/skills/`.*
