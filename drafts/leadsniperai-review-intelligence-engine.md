---
title: Review Intelligence Engine — Core Design
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [how-to, technology, research, finance]
sources: [LeadSniper-3.0 repo, DataForSEO Business Listings API, Gemini Grounding]
related: [leadsniperai-gmb-signal-engine, lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop]
---

# Review Intelligence Engine — Core Design

**The core differentiator of LeadSniperAI:** read the reviews and comments, gather sentiment, detect the business phase, and recommend the best service — driven by review score AND review count.

> Reviews are the diagnosis. Every review theme is a service need. The business phase tells you which service to lead with.

## 1. Why this is the core

LeadSniperAI 3.0 currently:
- Extracts review snippets via Gemini grounding — **then discards them**
- Buckets leads by pure math: `categorize_lead(rating, review_count)` → Premium/Growth/Crisis/Startup
- Calculates a rescue number (stars needed to reach 4.2) — **but never reads what the reviews say**

**The gap:** rating + count tell you *how healthy* a business is. Review content tells you *what to sell them*. The reviews are already being fetched — they're just not analyzed.

**The insight (the "secret identity" of review data):**
> Every negative review theme is a service need. Every positive theme is a growth opportunity. The mix of themes + the review count + the score = the business phase. The phase selects the best-fit service.

## 2. Architecture

```
Reviews + Comments (GMB grounding + DataForSEO reconfirmation)
        ↓
┌─────────────────────────────────────────────┐
│ 1. SENTIMENT LAYER                          │
│    Classify each review: theme + tone +     │
│    urgency + sentiment score                │
└─────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────┐
│ 2. PHASE DETECTION                          │
│    Startup / Growth / Established /         │
│    Overloaded / Declining                   │
│    ← review COUNT (velocity) + SCORE        │
│      (health) + theme mix                   │
└─────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────┐
│ 3. SERVICE RECOMMENDER                      │
│    Best-fit service per phase + theme:      │
│    AI receptionist, booking, review-        │
│    recovery, SEO, CRM, automation           │
└─────────────────────────────────────────────┘
        ↓
Signal Report Card → GO/HOLD/DROP → outreach with the actual proof
```

## 3. Sentiment Layer

### 3.1 Theme taxonomy (the service-need categories)

| Theme | Example review text | Implied service need |
|-------|-------------------|---------------------|
| `booked_out` | "3 week wait for appointment" | AI booking / capacity |
| `phone_leak` | "Can't get anyone on the phone" | AI receptionist / missed-call recovery |
| `pricing` | "Expensive, hidden fees" | Pricing transparency / offer reframe |
| `quality` | "Workmanship was poor" | Quality / process fix |
| `slow_service` | "Took forever, no updates" | CRM / workflow automation |
| `no_show` | "Technician never showed" | Scheduling / dispatch fix |
| `communication` | "No response to my emails" | Follow-up automation |
| `outdated` | "Website says closed, actually open" | Website / GMB hygiene |
| `praise` | "Best service, highly recommend" | Review generation / growth |
| `growth_signal` | "They're expanding, hiring" | Growth capital / services |
| `loyalty` | "Been coming for years" | Retention / reactivation |

### 3.2 Sentiment scoring
- Each review: `sentiment: positive | negative | neutral`, `sentiment_score: -1.0..1.0`, `theme`, `urgency: low|medium|high`
- **Composite sentiment:** weighted by recency (newer reviews matter more)
- **Theme distribution:** % of reviews per theme → the dominant theme = the primary service need

## 4. Phase Detection

Phase is a function of **count × score × themes**:

| Phase | Review count | Score | Theme mix |
|-------|-------------|-------|-----------|
| **Startup** | < 20 | any | sparse, mixed |
| **Growth** | 20–100 | ≥ 4.2 | praise-dominant, some booked_out |
| **Established** | 100–1000 | ≥ 4.2 | praise + loyalty |
| **Overloaded** | high velocity (30d) | ≥ 4.0 | booked_out + phone_leak + slow_service |
| **Declining** | any | < 4.2 or dropping | pricing + quality + no_show + communication |

**Velocity matters:** review count in last 30 days (vs. total) reveals:
- High velocity + praise → growth (sell growth services)
- High velocity + complaints → overload (sell capacity)
- Low velocity + declining score → neglect (sell reputation recovery)
- New reviews accelerating after silence → reactivation moment

**Rescue number (existing, keep):** `rating < 4.2 → stars needed to reach 4.2` — pairs with phase detection: declining + high rescue number = crisis, declining + low rescue number = early warning.

## 5. Service Recommender

### 5.1 Phase → primary service

| Phase | Lead service | Secondary |
|-------|-------------|-----------|
| Startup | Review generation + GMB hygiene | Website presence |
| Growth | Review generation + SEO | Booking automation |
| Established | AI receptionist + retention | Upsell automation |
| Overloaded | AI receptionist + booking system | Capacity planning |
| Declining | Review recovery + reputation | Process fix (root theme) |

### 5.2 Theme → service mapping (the "what to sell")

| Dominant theme | Service | Proof hook |
|---------------|---------|-----------|
| phone_leak | AI call answering | "I noticed 8 reviews mention not getting through" |
| booked_out | Online booking + AI triage | "3-week waits in 6 recent reviews" |
| slow_service | CRM + follow-up automation | "5 reviews mention delays with no updates" |
| no_show | Dispatch/scheduling fix | "2 no-shows mentioned last month" |
| pricing | Offer/pricing clarity | "4 reviews mention surprise pricing" |
| communication | Auto-response + review replies | "11 unanswered reviews" |
| outdated | Website + GMB sync | "Reviews say 'closed' but you're open 24/7" |
| praise | Review-generation campaign | "12 five-stars this month — let's get more" |

## 6. Two-Axis Model — Reviews + Website

The full diagnosis combines **two independent axes**:

| Reviews (Axis 1) | Website (Axis 2) | Business reality | Lead service |
|---|---|---|---|
| Great (4.9★) | **No website** | All digital demand uncaptured | **Website build** |
| Great | **Outdated** (5+ yrs) | Trust erosion, lost mobile | **Website modernisation** |
| Great | **Slow** (PageSpeed <50) | High bounce, lost leads | **Speed optimization** |
| Bad (3.8★) | No website | Double problem | Review recovery + build |
| Great | **No booking/click-to-call** | Phone-only intake leak | Booking + click-to-call |
| Great | **No after-hours intake** | After-hours demand lost | AI answering |
| Great | Great | Established | Growth/retention |

### Website Axis assessment inputs

| Input | What it flags | Service |
|-------|--------------|---------|
| `website` missing | `no_website` status (score 0) | Website build |
| `page_speed_score` <50 | Poor performance | Speed optimization |
| `page_speed_score` 50-89 | Needs improvement | Speed optimization |
| `has_booking` false | No online booking | Booking system |
| `has_click_to_call` false | No mobile click-to-call | Mobile click-to-call |
| `has_contact_form` false | Phone-only intake | Contact form / intake fix |
| `has_after_hours_intake` false | After-hours demand lost | After-hours intake / AI answering |
| `mobile_friendly` false | Not mobile responsive | Mobile redesign |
| `years_old` ≥5 | Dated design/tech | Website modernisation |

**Status logic:** score 0 (no website) / <40 critical / 40-69 needs_work / ≥70 healthy.

### Priority logic (verified)

- **No website + review health ≥60 → Website build is #1** (the "reputation but no capture" case — highest-value lead)
- **Website critical → all website services rank priority 1** alongside review services
- **Website needs_work → priority 2; healthy → priority 3**
- Recommendations re-sorted by priority for a clean ranked list

### Posture

| Posture | When |
|---------|------|
| `urgent_capture` | No website OR critical website — demand uncaptured |
| `reputation_fix` | Review health <40 but website ≥50 — reputation is the problem |
| `opportunity` | Both axes reasonably healthy — growth play |

## 7. Data inputs

| Source | What it provides | Status |
|--------|-----------------|--------|
| **Gemini grounding** (`/search`) | Business list + positive/negative snippets | ✅ Existing (snippets discarded today) |
| **DataForSEO Business Listings** | **`place_topics`** (aggregated review themes + counts — the sentiment signal, no text needed), rating distribution, attributes, place_id, is_claimed, work hours, website/phone/address reconfirmation | ✅ Verified working + wired (auto-fetch) |
| **OpenWebNinja** (via Deepline) | Google Maps reviews, review details, business posts | ✅ Verified working |
| **PageSpeed Insights** | Performance score, Core Web Vitals, mobile-friendliness (free tier; 429 without key at volume) | ✅ Wired (graceful degradation) |

### Auto-fetch flow (verified end-to-end)

One `POST /api/v1/analyze-reviews` call with `auto_fetch_reviews: true` + `auto_audit_website: true`:
1. DataForSEO discovers the business → rating, review count, website auto-captured
2. **`place_topics` → theme bridge** converts aggregated review themes into the sentiment taxonomy (positive AND negative profiles verified: 4.9★ Milani → health 100 praise; complaint-heavy profile → health 25, `booked_out` dominant)
3. PageSpeed audits the website → performance score feeds the website axis
4. Phase detection + service recommendations across both axes

**Note:** DataForSEO on this account tier does NOT return raw review text (the `google/reviews` endpoints 404) — but `place_topics` + `rating_distribution` ARE the aggregated sentiment, which is sufficient for the diagnosis.

## 7. Implementation plan

### Phase 1 — Backend service (`review_intelligence.py`)
1. `analyze_reviews(reviews: List[str]) -> SentimentReport` — theme + tone + sentiment per review (Gemini, JSON)
2. `detect_phase(count, score, sentiment_report, velocity) -> Phase` — deterministic rules + theme mix
3. `recommend_service(phase, themes) -> List[ServiceRecommendation]` — theme → service mapping
4. `/api/v1/analyze-reviews` endpoint — takes review list (or lead_id), returns full report

### Phase 2 — Wire into pipeline
- `/search` keeps review snippets (already does)
- New enrichment step: after DataForSEO reconfirmation, run review analysis → store phase + services on the lead
- Signal Report Card includes sentiment summary + phase + recommended service

### Phase 3 — CLI (Printing Press)
- Regenerate CLI with `/analyze-reviews` endpoint
- **Compound command:** `leadsniper-pp-cli analyze-business --business "Milani Plumbing"` → discovery + reconfirmation + sentiment + phase + services in one call

### Phase 4 — Vertical packaging
- Per-vertical theme taxonomies (mortgage, business funding, home services differ)
- Per-vertical service catalogs

## 8. Success metrics

- ≥90% of businesses get a phase classification
- ≥80% of recommended services trace to a specific review theme (auditable proof)
- Human review confirms ≥75% of phase classifications
- Outreach led by review-grounded hooks beats generic hooks (target: ≥5% reply rate)

## 9. The demonstration (Milani Plumbing example)

Reviews would reveal: 4.9★, 2,884 reviews, themes = praise + loyalty (established), some booked_out (capacity pressure) → **phase: Established-overloaded** → services: AI receptionist + review generation. The hook: "12 recent reviews mention wait times — here's how we handle overflow calls."

---

*Core design 2026-08-05. Replaces the "add-on" framing in the GMB signal proposal — Review Intelligence IS the product; GMB grounding + DataForSEO + phase + service rec are its inputs.*
