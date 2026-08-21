# Hermes AI Agency — DASHBOARD

**Last updated:** 2026-06-30 (mission refactor: GMB-outdated focus)
**Chief of Staff:** Chief of Staff (me)
**Vault location:** `~/wiki/agency-agents/hermes-ai-agency/` (synced to GitHub via wiki pipeline)

## Agency mission (2026-06-30)

**Find Google My Business pages that have no website or an outdated website, and convert them into paying WebMorphasis clients.**

## What we sell

| Service | Status | Owner | Notes |
|---|---|---|---|
| **LeadSniperAI** — GMB No-Website / Outdated Detection | **Active, scaling** | lead-researcher | Phase 1 refactored 2026-06-30. See `service-offers/leadsniper-ai/`. |
| **WebMorphasis** — Website Rebuild Delivery | **Active, ready** | (WebMorphasis repo) | FEED framework, $497/$997/$1,997/mo retainers, DNA.md, 135 tests. Receives qualified leads via webhook from LeadSniperAI. |
| Digital Employees (AI receptionist, intake, booking, review workflows) | In design | (WebMorphasis Phase 3) | WebMorphasis handles once engagement signed. |

## What's running

| Job | Status | Output |
|---|---|---|
| LeadSniper AI Run 001 — Vancouver + janitorial | ✅ Complete (legacy) | `okf/leadsniperai/outputs/vancouver-bc__commercial-cleaning-janitorial__2026-06-29/` |
| LeadSniper AI Run 002 — Vancouver + 4 broader cleaning queries | ✅ Complete (legacy) | `okf/leadsniperai/outputs/vancouver-bc__commercial-cleaning-broad__2026-06-29/` |
| Agency vault moved: C:\ → ~/wiki/agency-agents/hermes-ai-agency/ | ✅ Complete | 19 files, byte-identical copy |
| GMB-Outdated Detection playbook drafted | ✅ Complete (awaiting CEO) | `okf/leadsniperai/playbooks/phase-1-gmb-outdated-detection.md` |
| LeadSniper-3.0 repo — TS build hygiene | ✅ Complete (legacy, may be abandoned) | `C:\Users\denni\AI-Applications\LeadSniper-3.0\` |
| LeadSniper-3.0 Gemini grounding test | ⏸ Paused — may not be needed; LeadSniperAI is the canonical repo | n/a |

## What's blocked (escalations to CEO)

| Blocker | Type | Impact |
|---|---|---|
| CEO approval of `phase-1-gmb-outdated-detection.md` playbook | Methodology | Can't run new GMB-outdated pipeline |
| GMB Places API key | Credentials | Falls back to Gemini+DataForSEO only (reduced signal) |
| WebMorphasis webhook endpoint URL + shared secret | Tool integration | Can't auto-handoff qualified prospects |
| Gemini API key for LeadSniperAI | Asset / credentials | Already provided 2026-06-30, needs wiring into LeadSniperAI env |
| Confirm LeadSniperAI repo path (vs. LeadSniper-3.0) | Asset / scope | Currently assumed `G:\AI - Coding Projects\LeadSniperAI\` |
| First paid customer | Commercial | No revenue yet |

## Active employees

| Role | Status | Notes |
|---|---|---|
| Chief of Staff (me) | Active | Operating coordinator, escalation handler, pipeline runner |
| lead-researcher | Active (lives in OKF vault) | Runs LeadSniper AI Steps 1-3 (discovery + qualification) |
| site-auditor | Hired but idle | Will run Subcase B outdated audit (lightweight GET, not full DataForSEO) |
| proposal-writer | Hired but idle | Will draft per-prospect audit summaries once first prospects land |
| content-writer | Not yet hired | Marketing copy, case studies — pending service offer + first engagement |
| sales-operations | Not yet hired | Outreach, CRM, pipeline — pending CRM choice |

## Pipeline numbers (latest run)

- Legacy (Phase 1 MVP, run 002):
  - Raw listings: 13
  - Qualified: 8
  - Audited: 8
  - Ranked: 8
  - Tier A: 0
  - Tier B: 0
  - Tier C: 7
  - Tier D: 1
- New (GMB-Outdated, run 001): not yet run

## This week's focus

1. Get CEO approval of GMB-Outdated Detection playbook
2. Confirm LeadSniperAI repo path (G:\AI - Coding Projects\LeadSniperAI\)
3. Wire GEMINI_API_KEY into LeadSniperAI env
4. Get GMB Places API key (or log fallback decision)
5. Get WebMorphasis webhook endpoint URL + shared secret
6. Then: execute GMB-Outdated Pipeline Run 001 (Vancouver, commercial cleaning)

## Notes

This dashboard should be updated by the chief of staff after every meaningful action. It is the primary context for resuming work in any future session.


## Architecture Update — 2026-06-30

**LeadSniperAI is now an AI Website Opportunity Engine**, not just a lead scraper.

The architecture is:
- **Hermes** = discovery + scoring (this team's job)
- **Claude Code** = audit + proposal + website rebuild + CMS generation

Two scrapers, used in sequence:
1. **Scrapling** (primary) — technical inspection of GMB business websites
2. **ScrapeGraphAI** (secondary) — business meaning extraction (only when score >= 70)

Opportunity Score (max 100) = GMB Strength + Website Weakness + AI Search Gap + Contactability + Revenue Potential.

12 verticals: Restaurants, Lawyers, Dentists, Mortgage Brokers, Roofers, HVAC, Electricians, Accountants, Financial Advisors, Construction, Insurance, Real Estate.

Future: continuous monitoring (nightly scans for new reviews, website changes, new opportunities).


### D-2026-06-30-15 update
- **GMB URLs upgraded to canonical place_id format** via DataForSEO Maps grounding
- 14/27 audits now open the actual Google Maps listing
- 8 still in CID format, 4 in search format, 1 NULL
