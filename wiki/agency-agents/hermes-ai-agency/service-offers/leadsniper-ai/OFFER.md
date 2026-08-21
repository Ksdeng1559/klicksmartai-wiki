---
service_offer_id: leadsniperai
status: active_refactor
last_updated: 2026-06-30
---

# LeadSniperAI — Service Offer

> **Status:** ACTIVE — mission refactored 2026-06-30. Source of truth for the prospect-discovery half of the agency. (Previously named "LeadSniper AI" in the agency vault; renamed to "LeadSniperAI" to match the canonical repo and WebMorphasis naming convention.)

## One-line description

**LeadSniperAI finds Google My Business pages that have no website or an outdated website, in any city and category, and outputs a ranked list of qualified prospects for WebMorphasis outreach.**

## Mission (2026-06-30 refactor)

> Find Google My Business pages that have no website or an outdated website, and convert them into paying WebMorphasis clients.

This is sharper than the prior "find businesses with weak websites" framing. Two distinct subcases, both easy to verify and easy to sell against:

- **Subcase A — No website:** GMB listing has no `website_uri` (or a placeholder). Trivially detectable. The business exists, has customers, but has no online presence beyond GMB. The pitch is straightforward.
- **Subcase B — Outdated website:** GMB listing has a `website_uri` that resolves to a real site, but the site is outdated. "Outdated" is defined as: `Last-Modified` > 2 years ago, OR 2+ of [no HTTPS, no viewport meta, no OpenGraph, no schema.org JSON-LD, copyright year in footer < current year - 2, deprecated CMS].

## Who buys this (the downstream client)

The actual paying clients are **local service business owners** with a real GMB listing and either no website or an outdated one. The agency sells to them via WebMorphasis's $497/$997/$1,997/mo retainer model.

Primary verticals (per runs 001-002):
- Commercial cleaning / janitorial (proven in run 002)
- Dental, legal, HVAC, plumbing (planned expansion)

Out of scope (for now): franchises with ≥ 5 locations, e-commerce, B2B SaaS, multi-location chains.

## What we deliver

For each LeadSniperAI run:

1. **Ranked prospect CSV** — every qualified GMB page, scored 0-100, tiered A/B/C/D
2. **Per-prospect audit JSON** — Subcase B prospects get a HEAD + lightweight audit (Last-Modified, HTTPS, viewport, OG, schema, copyright year, CMS)
3. **Webhook push to WebMorphasis** — A/B-tier prospects are sent to `$WEBMORPHASIS_URL/api/v1/leads` for downstream discovery interview + FEED + retainer pitch
4. **Reflection file** — per-run reflection documenting tier breakdown, source contribution, patterns, and recommendations for next run

For the agency itself:

5. **Pipeline health metrics** — % prospects that are Subcase A vs B, average reputation, average outdated signal count
6. **Pattern reports** — e.g., "62% of outdated sites in Vancouver commercial cleaning use Wix 2015 templates"

## What makes us different

- **GMB-first, not "find a website, then audit it."** We start with the listing that already proves the business is real.
- **Binary classification.** No "weak" or "score 47." Either the site is missing, or it's outdated, or it's modern. Sales-ready language.
- **AI-Search awareness.** The outdated definition includes AI-Search-readiness signals (schema.org, OpenGraph), so prospects we identify are *known* to be invisible to ChatGPT, Perplexity, Gemini, etc.
- **End-to-end handoff.** The qualified prospect doesn't sit in a CSV — it gets pushed to WebMorphasis the same hour.

## What we explicitly don't do

- We don't contact the prospect directly. WebMorphasis handles outreach.
- We don't score the site quality. We score "outdatedness" only.
- We don't manage GMB profiles. We read them.
- We don't make ranking or traffic guarantees.

## Pricing (the agency sells this through WebMorphasis)

| Tier | Price | Description |
|---|---|---|
| Free Demo | $0 | Custom glassmorphism website demo (48-hour delivery) — WebMorphasis handles |
| Basic | $497/mo | AI chat + booking integration |
| Growth | $997/mo | Voice AI receptionist + reputation management |
| Premium | $1,997/mo | Full automation suite + priority support |

**Status:** These tiers come from WebMorphasis's existing service catalog. The agency does not need to re-decide pricing; it confirms or overrides.

## Source-of-truth artifacts

- **Prospect + audit pipeline:** `G:\AI - Coding Projects\LeadSniperAI\` (canonical)
- **Delivery + sales workflow:** `G:\AI - Coding Projects\WebMorphasis\`
- **Playbook (current):** `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\playbooks\phase-1-gmb-outdated-detection.md`
- **Outdated definition:** locked in D-2026-06-30-07
- **Agency decision log:** `~/wiki/agency-agents/hermes-ai-agency/DECISIONS.md`
- **Legacy run artifacts (still valid as reference):**
  - Run 001: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\outputs\vancouver-bc__commercial-cleaning-janitorial__2026-06-29\`
  - Run 002: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\outputs\vancouver-bc__commercial-cleaning-broad__2026-06-29\`

## Active employees on this offer

- `lead-researcher` (active) — runs the GMB discovery + dedupe + Subcase A/B split
- `site-auditor` (idle, ready) — runs Subcase B lightweight audit (HEAD + GET + 6-signal scan)

## Supersedes

- `phase-1-mvp-pipeline.md` (Serper + DataForSEO 2-layer)
- `phase-1-hybrid-discovery.md` (3-layer Gemini+GMB+DataForSEO)
- `opportunity-scoring-rubric-v2.md` (3-axis with intent signal — partial reuse only)
