---
title: Offer-Gap Signal Engine — Proposal (DRAFT — signals to be investigated and confirmed)
created: 2026-08-05
updated: 2026-08-05
type: proposal
status: draft
tags: [how-to, technology, research, proposal]
sources: [LeadSniper-3.0 repo, LeadSniperAI CLI OS spec, review-intelligence engine, AI Agency Growth Diagnosis flow]
related: [lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop, leadsniperai-review-intelligence-engine, leadsniperai-gmb-signal-engine-proposal]
---

# Offer-Gap Signal Engine — Proposal

**Status: DRAFT. All signal definitions below are hypotheses pending investigation and confirmation against real businesses before production use.** Confidence: 55% until validated.

## 1. Problem

The AI Agency Growth Diagnosis flow lists **Offer gaps** as a signal family, but it is the only one of the six with no dedicated CLI command or detection path. Today it is inferred informally from review themes + `generate-recommendations`. That is not a first-class, evidence-backed signal.

**Definition (working):** An offer gap is observable demand for a product/service that a business could credibly sell but does not currently offer, price, or capture. Demand is proven by external evidence; absence of the offer is proven by the business's own surfaces (website, GMB, listings).

The distinction that matters:
- **Revenue Leakage** = demand exists AND offer exists, but capture fails (phone-only intake, no booking).
- **Offer Gap** = demand exists AND offer does NOT exist (no page, no pricing, no capability).

## 2. Detection inputs (all exist in the CLI today)

| # | Input | Generator | What it proves |
|---|-------|-----------|----------------|
| 1 | Review themes | `analyze-reviews` (11-theme taxonomy) | Customers asking for X ("do you do X?", "wish they offered Y"), praising adjacent capability |
| 2 | Q&A / owner responses | GMB grounding (proposed engine) | Unanswered "do you do X?" questions = unserved demand |
| 3 | Website services audit | `analyze-reviews` website axis + SiteDoctor | No page/pricing for service X; services list omits X |
| 4 | Keyword demand | `seo-audit` keywords (volume/CPC) | High-volume X keywords where target has no page / doesn't rank |
| 5 | Competitive offers | `seo-audit` competitors + Tavily `competitive_advantages` | Competitors offer X; target doesn't |
| 6 | Hiring intent | `search-hiring` roles | Hiring role implies new capability (plumber hiring HVAC techs = expansion) |
| 7 | News / expansion | `search-news`, Tavily `growth_signals` | Category change, new service announcement, new location |
| 8 | Social | `social-enrich` | Posting about X, no offer page |

## 3. Detection rules (hypotheses to test)

1. **Review-demand rule:** ≥3 reviews in 30d referencing a capability not listed on the website → offer-gap candidate.
2. **Q&A rule:** ≥2 unanswered questions of form "do you do X" → offer-gap candidate.
3. **Keyword-absence rule:** top-20 keyword by volume in the vertical's keyword set where target has no ranking page → offer-gap candidate (requires keyword→service mapping).
4. **Competitor rule:** ≥2 of top-5 competitors offer X, target does not → offer-gap candidate (weakest evidence alone — do NOT use alone).
5. **Hiring-expansion rule:** new role family absent from current services → offer-gap candidate (requires 60–90d recency).

## 4. Confirmation standard (non-negotiable before outreach)

An offer gap is NOT a signal until confirmed. Confirmation = evidence object per the CLI OS spec (Section 6.1):

```json
{
  "claim": "Demand for emergency after-hours service with no offer page",
  "evidence_type": "offer_gap",
  "sources": [
    {"kind": "review_theme", "id": "<review-id>", "quote": "Wish they handled after-hours emergencies", "observed_at": "..."},
    {"kind": "website_observation", "url": "https://example.ca/services", "finding": "no emergency service page", "observed_at": "..."},
    {"kind": "competitor_offer", "url": "https://competitor.ca/emergency", "observed_at": "..."}
  ],
  "confidence": 0.0,
  "confirmation_status": "unconfirmed",
  "expires_at": null
}
```

**Confirmation ladder (must climb before use):**
1. **DETECTED** — rule fired (automated, low cost). Not usable.
2. **VERIFIED** — human or second-pass AI checks primary sources: demand quote is real, offer is genuinely absent. Usable as research signal.
3. **CONFIRMED** — both demand AND absence verified, plus the business's actual service line checked (phone call or site crawl). Usable in outreach copy.
4. **EXCLUDED** — business does offer X (site nav, pricing page, employee claims) → suppressed, feeds back as false-positive training data.

Minimum standard for outreach: **CONFIRMED with ≥2 independent evidence sources** (one demand-side, one offer-side).

## 5. CLI contract (canonical OS spec additions)

```bash
leadsniper signal scan --family offer-gap --business <id> --vertical marketing-agencies
leadsniper signal classify --id <signal-id> --family offer-gap
leadsniper signal confirm --id <signal-id>            # moves DETECTED → VERIFIED after source check
leadsniper signal explain --id <signal-id>            # evidence narrative for human review
leadsniper signal exclude --id <signal-id>            # false positive → training feedback
```

Placement in priority order: offer-gap sits **between Revenue Leakage and Capacity Overload** — it is unserved demand (revenue-grade) but requires confirmation before it earns that rank. Recommend composite-score weight: evidence quality +2, signal strength +2 when confirmed.

## 6. Offer-gap → agency service mapping (for the AI Agency Growth Diagnosis use case)

Once confirmed, the gap maps to an agency deliverable:

| Confirmed offer gap | Agency service to sell |
|---------------------|------------------------|
| Demand for service X, no page/pricing | New service line + landing page build |
| High-volume X keywords, no ranking page | SEO content program for X |
| No booking for high-demand service | Booking/intake system |
| No after-hours capability, emergency positioning | AI answering / missed-call recovery |
| Competitors offer X (reviews praise X) | Service expansion + GMB/service-area update |
| Category expansion visible in hiring/news | Offer modernization + positioning |

## 7. Validation plan (the "investigate and confirm" phase)

Do NOT build the full engine first. Run a 2-week validation:

1. **Sample:** 20 real businesses across 2 verticals (10 marketing-agencies targets, 10 local-services).
2. **Run detection rules only** (Section 3) — collect candidates.
3. **Manual ground-truth check:** for each candidate, confirm whether the business actually offers the service (site crawl + call if ambiguous).
4. **Score precision/recall per rule.** Target: precision ≥70% per rule before any rule is enabled for outreach.
5. **Log exclusions as training data** — feed back into rules.
6. **Reject/promote rules:** drop rules below precision floor; keep those above with their evidence templates.

Output: a `signals.yaml` vertical-package entry (per CLI OS spec §7) with validated rules, thresholds, and evidence templates.

## 8. Open decisions

- Keyword→service mapping source (DataForSEO vs. hand-curated per vertical)
- Whether Q&A extraction needs the GMB engine first (it is a dependency for rule 2)
- Confirmation step: human-in-loop vs. LLM second-pass (recommend LLM second-pass + human on anything used in outreach)
- Score weights in composite model
- Which vertical ships the first validated ruleset

## 9. Confidence

- Overall engine: 55% (hypothesis stage — rules untested)
- Rules 1 & 3 (reviews, keywords): 70% confidence of viability
- Rules 2 & 6 (Q&A, hiring): 40% — depend on GMB engine and role-to-capability mapping quality

Update this document after the validation run; promote to `wiki/processes/` only when precision targets are met.
