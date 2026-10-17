# KomstructionComOS — Client Workspace

**Created:** 2026-10-16
**Project:** BC Commercial Mortgage Intelligence & Lead Generation Marketplace
**Source-of-truth repo:** https://github.com/Ksdeng1559/KonstructionComOS
**Local clone:** `/mnt/g/AI - Coding Projects/KonstructionCommercialOS`

## Canonical Project Context (from GitHub repo, pulled 2026-10-17)

### What the product is
**KonstructionComOS — Construction Intelligence & Capital Origination OS** — a multi-tenant B2B SaaS for discovering early construction opportunities, identifying project stakeholders, and managing financing outreach. BC first, then Canada + US (with appropriately licensed data).

### Primary buyers (from `docs/PRD.md` §1)
1. **Commercial mortgage and development finance brokers** ← our #1 lead source
2. General contractors and specialist subcontractors
3. Developers and land acquisition teams
4. Architects and engineering firms
5. Private lenders, debt funds and capital advisors

### Customer promise
Turn early-stage construction activity into qualified B2B relationships and financing opportunities. BC first.

### MVP scope (from `docs/PRD.md` §3)
- **P0:** Clerk orgs + Supabase tenant isolation (RLS), BC project registry, source/provenance, manual + CSV ingest, stakeholders, search/filter/score, financing pipeline stages, interaction history, audit trail, admin roles.
- **P1:** Scheduled municipal/provincial permit ingest, entity dedup, enrichment via contracted providers, project alerting, saved lists, export, Stripe billing.
- **P2:** AI briefings, geospatial heatmap, automated source change detection, lender fit + compliant outbound orchestration.

### Stack
- **Public site:** https://clearconnectcom.lovable.app/ (Vite + React 18 + Tailwind 3)
- **Authenticated SaaS:** Next.js 15 + React 19 + Tailwind 4 in this GitHub repo
- **Auth:** Clerk Organizations
- **DB:** Supabase PostgreSQL with RLS (`amgknqnhiscryvcfeoyj.supabase.co`)
- **Storage/hosting:** Vercel + Supabase; optional Railway workers
- **Current scaffold status:** dashboard uses synthetic fixtures; schema has RLS enabled but no access policies; no production CRUD or billing

### Compliance gates
- **BC Mortgage Services Act** (in force 2026-10-13) — regulatory
- **CASL** — contact eligibility + suppression + unsubscribe before marketing
- **PIPEDA** + applicable provincial privacy controls
- **Canadian securities/mortgage regulations** — consult counsel for regulated workflows
- **Non-goals:** No automated credit approval, no funding guarantee, no scraping behind access controls, no non-consensual mass marketing

### Open decisions (from PRD §15 — still open as of 2026-10-17)
- [ ] Exact legal relationship between lead-gen company, brokerage, partners
- [ ] Permitted compensation model: sponsorship / advertising / referral / other
- [ ] Borrowers choose named brokerage vs. request matching among disclosed partners
- [ ] Final CRM/CMS stack and hosting jurisdiction
- [ ] Data licensing for proprietary commercial property statistics
- [ ] Broker response SLA, verification cadence, retention period
- [ ] Brand, domain, bilingual/French-language expansion requirements

## Active Research (2026-10-17)

### OpenSEO Project State
- **OpenSEO Project:** KommercialConnect
- **Project ID:** `7f4bbe03-f30f-4eeb-b648-d64985be70a1`
- **URL:** http://127.0.0.1:3005/p/7f4bbe03-f30f-4eeb-b648-d64985be70a1
- **Saved keywords:** 38 (all tagged with multiple provenance tags)
- **Market:** Canada (locationCode 2124, languageCode en)
- **Auth:** Self-hosted, `local-admin / admin@localhost`, no credits cost (DataForSEO API key bypasses OpenSEO credit system)

### Research artifacts
| File | Purpose |
|---|---|
| `research/openseo-keyword-metrics-2026-10-17.json` | 14 BC + construction keywords with full DataForSEO metrics |
| `research/openseo-serp-scans-2026-10-17.json` | Top-5 BC SERP scans (100 results each) |
| `research/serp-analysis-2026-10-17.md` | 4.5 KB written analysis of BC SERP competitor landscape |
| `research/openseo-multifamily-serp-2026-10-17.json` | 5 multifamily SERP scans |
| `research/multifamily-serp-analysis-2026-10-17.md` | 4.4 KB written analysis of multifamily niche |
| `research/openseo-pbr-serp-2026-10-17.json` | 10 PBR + multifamily SERP scans |
| `research/pbr-serp-analysis-2026-10-17.md` | 8.4 KB written analysis of PBR construction financing niche |
| `research/openseo-serp-competitors-2026-10-17.json` | 69-competitor map across 5 keywords |
| `research/serp-competitor-analysis-2026-10-17.md` | 8.9 KB strategic competitor analysis |
| `research/openseo-bc-gap-serp-2026-10-17.json` | 10 BC-local gap SERP scans (where find_serp_competitors returned 0) |
| `research/bc-gap-serp-analysis-2026-10-17.md` | 8.2 KB written analysis of BC gap terms |
| `research/openseo-project-file-2026-10-17.json` | 267-keyword contaminated project file (NOT pushed, kept as contamination reference) |
| `research/openseo-project-file-2026-10-17.md` | 9.6 KB written summary of the contaminated set |
| `research/_render_project_file.py` | MD renderer for the project file (kept per policy) |
| `research/keyword-research-2026-10-17.json/.md` | 78-keyword prior broad-CA pull (contaminated) |

## SEO Strategy (Final Recommendations)

### Blue Ocean Priorities (zero commercial SERP competition)
1. **`/vancouver-purpose-built-rental-loan/`** — 0 lenders in top 10, news only, federal PBR funding driving searches
2. **`/apartment-construction-loan-program-bc/`** — 260/mo, $13.66 CPC, only 1 lender (LendCity) in top 10

### Beatable Targets (commercial competition exists but is generic)
3. **`/purpose-built-rental-construction-financing-vancouver/`** — your phrasing, blue ocean
4. **`/multifamily-construction-loans-vancouver/`** — 10/mo + commercial intent, 3 generic lenders in top 10
5. **`/construction-financing-vancouver/`** — 10/mo, 8 lenders in top 10 but satbirbhullar is the only BC-specific player
6. **`/cmhc-aclp-bc-developer-guide/`** — beat LendCity's 2024 ACLP guide with a 2026 version

### Outrank Targets (saturated but the brand is generic)
7. **Vancity + CCCU** own the brand-page game for 3 BC terms. Out-author them on long-tail PBR + multifamily + developer-specific BC content.

## Known Blockers (2026-10-17)
- **Domain for KommercialConnect is TBD** — no domain set in OpenSEO project yet (PRD §15 still has "brand, domain" as open)
- **Project context feature unavailable** — self-hosted OpenSEO (upstream) has 24 tools; `get_project_context` / `update_project_context` are not exposed (they exist in the older LAN-pubs fork). Project context will need to live in the wiki + repo for now.
- **No mcp__openseo__* tools loaded in this Hermes session** — direct `/mcp` JSON-RPC path works fine, will be native after gateway restart
- **Memory at 99% capacity** — no new memory entries accepted

## Next Actions
1. Decide on KommercialConnect brand + domain (PRD §15 open decision)
2. Build `/vancouver-purpose-built-rental-loan/` content piece (top blue ocean)
3. Build `/apartment-construction-loan-program-bc/` content piece (highest volume)
4. Run `audit satbirbhullar.ca` and `audit lendcity.ca` to model their content depth before writing
5. Re-run keyword metrics in 60-90 days to track whether PBR-driven terms grow
