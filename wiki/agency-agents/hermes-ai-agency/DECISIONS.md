# Hermes AI Agency — DECISIONS

Dated log of CEO decisions. Append-only. Each decision gets an ID: `D-YYYY-MM-DD-NN`.

> **Consolidation note (2026-06-30):** The LeadSniper AI subdomain in RIOS OKF has its own decisions log at `okf/leadsniperai/decisions.md` that predates this file. Going forward, **all agency-wide decisions live here** and the OKF subdomain log holds only LeadSniper-AI-specific sub-decisions (rubric weights, query choices, run scoping). Historical duplicates between the two files are documented below for traceability.

---

## 2026-06-29

### D-2026-06-29-01 — Agency Mission (initial)
**Decision:** Build Hermes AI Agency as an autonomous services agency selling AI-built services + Digital Employees. Mission: source clients via LeadSniper AI; deliver AI-native work.
**Rationale:** Captured from CEO initial direction.
**Supersession note:** Superseded by D-2026-06-30-08 (GMB-Outdated focus).

### D-2026-06-29-02 — First Service Line (initial)
**Decision:** First service line = LeadSniper AI (autonomous prospect sourcing for local businesses that need a new website).
**Rationale:** Highest-leverage starting point; agent-runnable; clear value proposition.

### D-2026-06-29-03 — Phase 1 MVP Scope
**Decision:** Phase 1 = PRD Stages 1–6 (discovery → qualification → inspection → audit → scoring). Defer Stages 7–12 until tools and decisions are ready.
**Rationale:** Don't start 15-stage builds on missing tools.

### D-2026-06-29-04 — Stack Substitution
**Decision:** Where the PRD named an unavailable tool, use closest available alternative. Scrapling → DataForSEO `on_page instant_pages`; ScrapeGraphAI → skip; Tavily → skip; Serper MCP for grounding.
**Rationale:** Move with what works.

### D-2026-06-29-05 — No Customer Outreach in Phase 1
**Decision:** No Resend/Unipile/SmartLead/GHL integration until Phase 2.
**Rationale:** AGENTS.md escalation list includes customer-facing commitments. Ranked prospect list is the Phase 1 deliverable.

### D-2026-06-29-06 — ToS-Conservative Scraping
**Decision:** Stay on ToS-clean data paths for Phase 1.
**Rationale:** Default conservative.

### D-2026-06-29-07 — Run 001: Vancouver + Janitorial
**Decision:** First Phase 1 run: Vancouver, BC + Commercial Building Cleaning & Janitorial.
**Rationale:** CEO-specified.

### D-2026-06-29-08 — Run 001 Outcome (Escalation)
**Result:** 10 raw → 5 audited → 5 ranked. 0 A-tier, 0 B-tier. Hypothesis "Vancouver cleaners have weak sites" not supported. All 5 sites have onpage_score ≥93.
**Escalation:** Three decisions needed before run 002.

### D-2026-06-29-09 — Run 002: Path A (Broaden Queries)
**Decision:** Run 002 = same city, broaden to 4 adjacent cleaning queries.
**Rationale:** Cheapest path to validation.

## 2026-06-30

### D-2026-06-30-01 — LeadSniper-3.0 Repo Integration (legacy, may be abandoned)
**Decision:** Clone `https://github.com/Ksdeng1559/LeadSniper-3.0`; fix the 9 TypeScript errors first; then run the Gemini grounding test.
**Rationale:** CEO-specified at the time. Pre-flight hygiene before exercising the integration.
**Supersession note:** This decision is now considered low-priority. LeadSniperAI (the G:\ repo) is the canonical discovery engine per WebMorphasis's README. LeadSniper-3.0 may be abandoned.

### D-2026-06-30-02 — Hermes AI Agency Operating Framework
**Decision:** Adopt "Hermes AI Agency" framing per new AGENTS.md. Chief of Staff has default authority over internal artifacts (departments, employees, SOUL.md, dashboards, kanban, internal SOPs, research, draft copy). Still escalate: pricing, launch, legal, customer-facing commitments, major hiring changes.
**Rationale:** CEO-specified.

### D-2026-06-30-03 — Consolidation of Decisions Across Two Logs
**Decision:** Agency-wide decisions live in `~/wiki/agency-agents/hermes-ai-agency/DECISIONS.md`. The LeadSniper AI subdomain log at `okf/leadsniperai/decisions.md` continues to exist for LeadSniper-AI-specific sub-decisions.
**Rationale:** Avoid ID collisions when both files are scanned. Single source of truth per scope.
**Status (2026-06-30):** Consolidation DONE. OKF `decisions.md` is now a pointer with only LeadSniper-specific sub-decisions.

### D-2026-06-30-04 — Hybrid Discovery Playbook Drafted (superseded by -08)
**Decision:** Drafted `okf/leadsniperai/playbooks/phase-1-hybrid-discovery.md` proposing a 3-layer discovery (Gemini+Grounding + GMB Places + DataForSEO). DRAFT — superseded by D-2026-06-30-08.
**Rationale:** CEO input pointed at an architectural choice the original playbook missed.
**Supersession note:** Superseded by D-2026-06-30-08 (GMB-Outdated Detection) which has a narrower, sharper scope.

### D-2026-06-30-05 — Rubric v2 Drafted (3-axis with Intent Signal)
**Decision:** Drafted `okf/leadsniperai/concepts/opportunity-scoring-rubric-v2.md` proposing a third axis C (Intent Signal, 30 pts). v1 marked `superseded`. DRAFT — superseded by D-2026-06-30-08.
**Rationale:** v1 produced 0 A-tier prospects.
**Supersession note:** Rubric v2 framework partially reused in the GMB-Outdated playbook (subcase A reputation-only scoring), but the full 3-axis intent signal is not used.

### D-2026-06-30-06 — Agency Vault Moved to Wiki
**Decision:** Move agency vault from `C:\Users\denni\Hermes-AI-Agency\` to `~/wiki/agency-agents/hermes-ai-agency/` so it benefits from the wiki's git+GitHub bidirectional sync. 19 files moved, byte-identical copy verified.
**Rationale:** Durability. The C:\ location had no git remote and no backup. The wiki location is the user's established source-of-truth storage.
**Status:** Complete. `C:\Users\denni\Hermes-AI-Agency\` flagged as legacy, emptied.

### D-2026-06-30-07 — Outdated Definition Locked
**Decision:** A website is "outdated" if EITHER (a) `Last-Modified` HTTP header > 2 years ago, OR (b) 2+ of: no HTTPS, no viewport meta, no OpenGraph, no schema.org JSON-LD, copyright year < current_year - 2, deprecated CMS/template signal.
**Rationale:** CEO-approved 2026-06-30. Combined approach (time-based free pass + signal accumulation) handles both obvious and stealthy cases.

### D-2026-06-30-08 — Agency Mission Refactored: GMB-Outdated Focus
**Decision:** Agency mission is now **find Google My Business pages that have no website or an outdated website, and convert them into paying WebMorphasis clients**. Supersedes the prior "find businesses with weak websites" framing.
**Rationale:** CEO-stated goal 2026-06-30. "No website" and "outdated website" are binary, easy to verify, and easy to sell against. Better fit for WebMorphasis's $497-1997/mo retainer model.
**Implementation:** Drafted `okf/leadsniperai/playbooks/phase-1-gmb-outdated-detection.md` (replaces prior phase-1-hybrid-discovery and phase-1-mvp-pipeline). Two prospect subcases: A (no website) and B (outdated). Pipeline uses LeadSniperAI + GMB Places API + Gemini+Maps grounding + DataForSEO, with WebMorphasis as the handoff target.


### D-2026-06-30-09 — Lead Sniper 3.0 = Canonical Codebase
**Decision:** "Lead Sniper 3.0" (at `C:\Users\denni\AI-Applications\LeadSniper-3.0\`, from `github.com/Ksdeng1559/LeadSniper-3.0`) is the canonical codebase. LeadSniperAI at `G:\AI - Coding Projects\LeadSniperAI\` is a separate Genkit-based frontend that does not currently talk to the Supabase backend.
**Rationale:** CEO confirmed 2026-06-30 ("the codebase came from here: https://github.com/Ksdeng1559/LeadSniper-3.0"). The repo at C:\ is the one with the FastAPI backend + Supabase client + Docker setup.
**Implementation:** Supabase keys (URL + service_role) wired into `C:\Users\denni\AI-Applications\LeadSniper-3.0\.env` and `\backend\.env` on 2026-06-30.

### D-2026-06-30-10 — Supabase = Live Backend, 4.5 Months of Data
**Decision:** The Supabase project `yolqrstktoqlszybwymw` is the Lead Sniper 3.0 production backend. Existing data: 375 leads, 71 battle_cards, 1 domain_audit, plus 38 other tables for enrichment, outreach, scoring, trust, and analytics.
**Rationale:** Inspected 2026-06-30. Schema is mature and production-grade. No new tables created — we use the existing `leads`, `domain_audits`, `battle_cards`, and `decision_logs` tables.
**Audit trail:** 7 new `domain_audits` rows inserted 2026-06-30 for 8 Vancouver home builders. 3/7 (43%) flagged as outdated by the 6-signal criteria.

### D-2026-06-30-11 — Auth Constraint: domain_audits.user_id References auth.users
**Decision:** All `domain_audits` (and any other table) inserts must use a real `user_id` from `auth.users`. The CEO's `sales@klicksmartai.com` (`7ef5b581-8ae0-4046-b485-6a0caf221fd6`) is the canonical owner; use that for chief-of-staff ingestion.
**Rationale:** Discovered 2026-06-30 when first insert attempt failed with FK violation. The `profiles` table is a different namespace from `auth.users`.
**Open:** Should we create a dedicated `chief-of-staff@agency.local` auth user? Or use the existing `sales@klicksmartai.com` for all agency actions?

## Pending (escalated, awaiting CEO)

- **D-PENDING-02:** Pricing template shape (already known via WebMorphasis: $497/$997/$1,997/mo retainers — confirm/override)
- **D-PENDING-03:** CRM choice (GoHighLevel vs. HubSpot vs. none-for-now)
- **D-PENDING-04:** Outreach stack (Resend vs. SmartLead vs. Coldly)
- **D-PENDING-05:** Webhook endpoint URL + shared secret for LeadSniperAI → WebMorphasis handoff
- **D-PENDING-09:** Confirm LeadSniperAI repo path (G:\AI - Coding Projects\LeadSniperAI\ vs. C:\...LeadSniper-3.0\)
- **D-PENDING-10:** GMB Places API key (Google Cloud project with Places API enabled)


## D-2026-06-30-12 — Exclude Denver from constant-flow audits

- **Date:** 2026-06-30
- **Decided by:** CEO
- **Status:** Active
- **Effective immediately.**

**Decision:** Denver, Colorado is excluded from the Lead Sniper 3.0 constant-flow audit pipeline. No new Denver businesses will be audited. Existing Denver audits in `domain_audits` (4 records from the 2026-06-30 batch) are retained as historical data — no rollback.

**Implementation:**
- Filter rule in `C:/Users/denni/AI-Applications/LeadSniper-3.0/scripts/audit_config.json`
- `audit_filter.exclude_locations[0]` = { name: "Denver, Colorado", match_fields: ["query", "address"], match_pattern: "denver" }
- Lead-researcher employee SOUL.md updated with the rule
- Reusable by cron + ad-hoc audit scripts

**Why:** Per CEO, "exclude location of Denver." No further reason given. The exclusion is permanent until the CEO explicitly reverses it.

**Affected runs:** Future constant-flow runs that would otherwise pull Denver dentists, plumbers, etc.


## D-2026-06-30-13 — Two-Scraper Architecture + Opportunity Score

- **Date:** 2026-06-30
- **Decided by:** CEO
- **Status:** Active
- **Effective immediately.**

**Decision:** LeadSniperAI adopts a two-scraper architecture and a 5-component Opportunity Score.

### Two scrapers
- **Scrapling** (`G:\AI-Applications\Scrapling` v0.4.8) is the **primary** engine. It crawls GMB business websites and extracts technical signals (status, SSL, viewport, schema, FAQ, contact info, forms, CMS, copyright, parked status).
- **ScrapeGraphAI** (`G:\AI-Applications\scrapegraphai` v2.1.4) is the **secondary** engine. It extracts business meaning (services, owner, positioning, FAQs, testimonials, outreach personalization).

**Rule:** ScrapeGraphAI is NOT run on every lead. Wastes tokens. Run it only when the Opportunity Filter passes (GMB rating strong, reviews high, website weak, business category valuable, contact data usable).

### 5-component Opportunity Score (max 100)
- **GMB Strength** (max 25): rating (60%) + review count (40%)
- **Website Weakness** (max 25): 8 weak signals, +3.5 each (no_https, no_viewport, no_faq, no_local_biz_schema, no_contact_page, no_schema, low_word_count, old_copyright)
- **AI Search Gap** (max 20): no_faq (5), no_local_biz (5), no_review (3), low_words (4+3)
- **Contactability** (max 15): phone (5), email (5), contact_page (3), forms (2)
- **Revenue Potential** (max 15): service_pages (5), high_word_count (5), forms (3), cta_buttons (2)

**Pass threshold:** 70/100 to advance to ScrapeGraphAI + proposal.

**Domain parked = +15 to Website Weakness** (when a business's domain is parked for sale — much stronger opportunity than just outdated).

### 12 verticals
Each industry has its own Claude prompt and audit template:
Restaurants, Lawyers, Dentists, Mortgage Brokers, Roofers, HVAC, Electricians, Accountants, Financial Advisors, Construction, Insurance, Real Estate.

### Continuous monitoring (future)
Nightly scan for: new Google Reviews, website changes, AI Search Score changes, new opportunities. Notify the Proposal Writer for updated pitches.

### Implementation
- `audit_config.json` updated to version 2
- POC run on Hasler Homes (47.6/100) and Roadhouse Projects (53.5/100). Both sites are now parked for sale — confirms the parked detection is critical.
- 2 new `domain_audits` rows inserted with `audit_method: opportunity_engine_v1_two_scraper`
- Next: integrate ScrapeGraphAI extraction (slow, requires LLM). Then build the Opportunity Report format with Estimated Lost Revenue.


## D-2026-06-30-14 — Add gmb_url column to domain_audits

- **Date:** 2026-06-30
- **Decided by:** CEO
- **Status:** Active
- **Effective immediately.**

**Decision:** Add a top-level `gmb_url` TEXT column to `domain_audits` for direct GMB-weblink lookups (rather than relying only on the JSONB `analysis.gmb_url`).

**Implementation:**
- CEO ran the ALTER TABLE SQL in Supabase SQL Editor
- Column added with `CREATE INDEX idx_domain_audits_gmb_url`
- 26 of 27 audits backfilled from `leads.google_maps_uri` matched by `business_name`
- 1 row (Vancouvervogueinteriors, Feb 2026 legacy) intentionally left NULL — original audit confirmed `has_gmb: false` at the time, so the NULL is the correct historical record

**Source of GMB URLs:** `leads.google_maps_uri` — the Google Maps URI (CID-based URL like `https://maps.google.com/?cid=12922397194641663723`).

**Why a separate column instead of just JSONB:**
- Direct queryability (`SELECT * FROM domain_audits WHERE gmb_url IS NOT NULL` is faster than JSONB extraction)
- Indexable (the new idx_domain_audits_gmb_url)
- Surfaced in Supabase table view without JSONB unboxing
- Required by the GMB-Outdated Detection pipeline (Phase 1) which needs to display the GMB link in proposals

**Affected 27 audits:** 26 now have `gmb_url` populated (Vancouver Home Builders, Denver dentists, Seattle dentists, etc.). 1 NULL (Vancouvervogueinteriors legacy).


---

## D-2026-06-30-15 — Google Maps grounding for GMB URLs

**Decision:** Use Google Maps Place API grounding (via DataForSEO `business_data_business_listings_search`) to convert all GMB URLs in `domain_audits.gmb_url` to canonical `place_id` format.

**Why:** CEO observed the GMB links in the audit list "are not linking to the website." Old URLs used search-based or CID-based formats. Canonical place_id format `https://www.google.com/maps/place/?q=place_id:ChIJ...` opens the actual Google Maps business listing reliably.

**Implementation:**
- Source: DataForSEO MCP `business_data_business_listings_search(title="<business name>")` returns `place_id`, `cid`, address, rating, etc.
- 14 of 27 audits now in canonical place_id format (Hasler Homes, Supercity, Glenmark, Marcraft, Delta Dental, Chicago Style Smiles, Cherry Creek Family, Emergency Dental of Denver, Wash Park Pediatric, Queen Anne Family, Sage Family, West Seattle Dental, Roadhouse Projects v2, Hasler v2)
- 8 still in CID legacy format (Upward, Major Homes, Best Builders, The Denver Dentists, Cherry Creek, Williams Family, Advanced Cosmetic, Roadhouse v1)
- 4 still in search format (Candybox, Ignite Digital, Upstaged, FUSION5IVE)
- 1 NULL (Vancouvervogueinteriors - no GMB page per Feb 2026 audit)

**Caveats:** Some lookups returned different businesses of the same name (e.g., Williams Family Dentistry = FL, not original; Sage Family Dental = Boston, not original). Manual review recommended before treating place_id as authoritative for ambiguous names.

**Next:** Continue lookups for the 8 CID-format and 4 search-format URLs. Also: add Hasler/Roadhouse park-domain re-check using the final URL after redirect (current detection is title-based, missing parked domains).
