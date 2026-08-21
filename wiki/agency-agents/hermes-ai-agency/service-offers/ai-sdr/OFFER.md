---
service_offer_id: ai-sdr
status: draft
last_updated: 2026-06-30
parent_offer: leadsniperai
---

# AI SDR (AI Sales Development Rep) — Service Offer

> **Status:** DRAFT — first version. Built today from the Vancouver home builder pattern analysis.

## One-line description

**AI SDR finds local service businesses with proven quality but missing social proof (4.5+ stars with 1-25 reviews), and runs automated outreach + lead-generation to book them as WebMorphasis / AI-SEO retainer clients.**

## Why this exists

LeadSniperAI finds the **buyers** (businesses with outdated websites). AI SDR finds the **sellers** — businesses that have the quality but lack the customer volume to compete on Google. Both feed the same WebMorphasis/AI-SEO retainer model.

The pattern is consistent across trades (home builder, contractor, HVAC, roofer, plumber, etc.):

- 5.0★ rating with 1-4 reviews = the business is great, but Google doesn't show it
- 4.5-4.9★ with 5-15 reviews = growing but undiscovered
- 4.5+ with 15-25 reviews = established but undermarketed

These are all **high-quality businesses with a social-proof gap**, which is exactly what an AI-driven review generation + outbound campaign closes.

## Mission

> Find local service businesses with proven quality but missing social proof, run an AI-driven outreach campaign, and convert them into paying WebMorphasis / AI-SEO retainer clients.

## Service tiers (the AI SDR produces 3 different offers based on the gap)

| Tier | Trigger | Monthly Price | What the AI SDR does |
|---|---|---|---|
| **Reputation Builder** | 4.5+★ + 1-5 reviews | **$497/mo** | Email past customers asking for fresh 5-star reviews, auto-respond to every new GMB review within 1 hour, run a 90-day reactivation campaign |
| **Lead Generator** | 4.5+★ + 6-15 reviews | **$997/mo** | Identify in-market homeowners, personalized email to book estimates, 3-5 touch follow-up over 14 days, hand off qualified booked appointments |
| **Full Funnel** | 4.5+★ + 16-25 reviews | **$1,497/mo** | Outbound to expired listings + lookalike audiences, AI-qualified leads, monthly reporting on booked jobs vs spend |

Each tier includes:
- The AI SDR's core activities (review generation / lead gen / outbound)
- A monthly performance report (reviews gained, leads booked, jobs closed)
- A quarterly strategy call
- 3-month minimum term, no setup fees

## Who buys this (the downstream client)

Local service business owners in the trades — specifically:
- Home builders, contractors, renovators
- HVAC, plumbing, electrical, roofing
- Dentists, lawyers, accountants (verticals where review count drives GMB ranking)

The common trait: **a business that is excellent at the craft but undermarketed online.** These owners often say things like:
- "We're great at what we do, but Google doesn't show us"
- "We get 80% of work from word-of-mouth"
- "Our competitor has 200 reviews and ranks above us even though they're worse"

## What we deliver

For each AI SDR run:

1. **Ranked target list** — every qualifying business in the city/vertical, scored 0-100, tiered to one of the 3 service offers
2. **Personalized outreach email** — references the prospect's specific rating, review count, and gap (not a generic template)
3. **JSON persistence** — every target + outreach body saved to disk for compliance + replay
4. **.eml files** — one file per prospect, ready to send via Resend / SmartLead / Gmail
5. **Pipeline value summary** — total $/mo if all targets close

For the agency itself:

6. **Pattern reports** — e.g., "Vancouver home builders average 4.2 reviews; 60% are AI SDR Tier 1 candidates"
7. **Vertical sizing** — for each (vertical, city) pair, how many targets are out there at each tier
8. **Conversion data** — over time, track which tier / pattern / vertical converts to paying clients

## What makes us different

- **Pre-filtered by quality, not just by category.** We only target 4.5+★ businesses, so the AI SDR's outreach references a real strength, not a guess.
- **Service-tier-routed.** The email proposes the tier that matches the prospect's gap, not a one-size-fits-all pitch.
- **JSON + .eml pipeline.** Every outreach is persisted and replayable. No "we sent the email" hand-waving.
- **Vertical-agnostic.** Same pattern works for home builder, contractor, HVAC, dentist, lawyer. New vertical = 2-line config change.

## What we explicitly don't do

- We don't actually send the emails (yet). The script writes .eml files. Wire to Resend/SmartLead later.
- We don't track conversions. That requires sending + reply tracking + GHL sync.
- We don't manage campaigns. Each run is one-shot — would need a cron for continuous runs.
- We don't do cold-call or LinkedIn outreach. Email-first.

## Pricing (what the prospect pays)

| Tier | Monthly | Setup | Term |
|---|---|---|---|
| Reputation Builder | $497 | $0 | 3-month minimum |
| Lead Generator | $997 | $0 | 3-month minimum |
| Full Funnel | $1,497 | $0 | 3-month minimum |

**Pipeline value ceiling (per 10-target run, all close):** ~$9,500/month.

## Source-of-truth artifacts

- **AI SDR script:** `C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\ai_sdr.py`
- **JSON persistence:** `C:\Users\denni\AI-Applications\LeadSniper-3.0\outreach\ai_sdr_*.json`
- **Stub .eml files:** `C:\Users\denni\AI-Applications\LeadSniper-3.0\outreach\sent\*.eml`
- **Pipeline upstream:** LeadSniperAI's `leads` table in Supabase (vertical + city + rating + review_count + review_velocity + phone + website)

## How to run

```bash
# Find AI SDR targets in any vertical/city
py -3.14 "C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\ai_sdr.py" --vertical "home builder" --city "Vancouver"

# Different vertical
py -3.14 "C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\ai_sdr.py" --vertical "roofer" --city "Seattle"

# Save to CSV
py -3.14 "C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\ai_sdr.py" --vertical "contractor" --city "Vancouver" --csv leads.csv

# Persist JSON + send stub
py -3.14 "C:\Users\denni\AI-Applications\LeadSniper-3.0\scripts\ai_sdr.py" --vertical "home builder" --city "Vancouver" --persist --send
```

## What makes a target a target (the AI SDR criteria)

```
rating >= 4.5     # proven quality
1 <= reviews <= 25 # social proof gap (the opportunity)
not closed_forever  # business is still operating
has phone OR website  # we can contact them
has city + zip     # real address
```

Score formula (0-100):
- rating (0-5 normalized): 20%
- review_gap (1 = 100, 25 = 0): 30%
- has_phone: 15%
- has_website: 10%
- is_claimed: 10%
- is_local: 15%

## First run results (Vancouver home builders, 2026-06-30)

- **15 leads in vertical** → **10 AI SDR targets** (67% conversion to AI SDR target)
- **6 Reputation Builder** (5.0★ + 1-4 reviews) = $2,982/mo if all close
- **3 Lead Generator** (5.0★ + 11-15 reviews) = $2,991/mo if all close
- **1 Full Funnel** (5.0★ + 19 reviews) = $1,497/mo if all close
- **Total pipeline ceiling: $7,470/mo** from a single run

## Active employees on this offer

- `ai-sdr` (drafting) — runs the scoring + outreach generation
- `outreach-sender` (idle, ready) — wires the .eml files to Resend/SmartLead

## Supersedes / Conflicts

- (none yet — this is the first version)

## Next steps

1. **Add `ai_sdr_tier` and `outreach_body` columns to `leads` table** (CEO: run SQL)
2. **Wire .eml files to Resend or SmartLead for actual delivery**
3. **Add email-open + reply tracking to measure conversion**
4. **Add a cron to run daily on a different (vertical, city) per day**
5. **Build a dashboard showing AI SDR pipeline value over time**
