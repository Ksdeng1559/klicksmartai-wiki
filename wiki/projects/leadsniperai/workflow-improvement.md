---
title: LeadSniperAI Workflow & Search Results Improvement Plan
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, research, how-to]
sources: [notion: LeadSniperAI Workflow & Search Results Improvement Plan]
related: [lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop, deepline]
---

# Purpose
Improve LeadSniperAI’s current discovery, enrichment, scoring, verification, and outreach workflow so that search results are more accurate, explainable, reusable, and commercially valuable.
This document extends the existing LeadSniperAI CLI specification and focuses on strengthening the quality of the search pipeline rather than simply increasing lead volume.
# 1. Current-State Assessment
## Existing Strengths
- Local business discovery by niche and city
- Gemini-assisted search and enrichment
- Tavily and Apify enrichment paths
- SEO audit and outreach generation
- Batch import and export
- FastAPI backend suitable for CLI orchestration
- Existing scoring and website-failure concepts
## Current Weaknesses
- Too much responsibility is placed on the LLM for both finding and judging facts
- Search results may contain incomplete, stale, duplicated, or weakly grounded business information
- Website issues are not consistently validated through direct crawling
- Unknown values can be confused with confirmed deficiencies
- Search results are not yet ranked by a robust commercial opportunity model
- No formal adversarial refutation pass exists before outreach
- Search evidence is not consistently preserved beside every result
- Search runs are not fully resumable, checkpointed, or provider-aware
# 2. Target Workflow
```plain text
Campaign profile
      ↓
Candidate discovery
      ↓
Identity resolution
      ↓
Eligibility screening
      ↓
Website crawl
      ↓
Technical and conversion audit
      ↓
Business and contact enrichment
      ↓
Deterministic scoring
      ↓
Adversarial refutation
      ↓
QA gates
      ↓
Qualified opportunity record
      ↓
Outreach draft / CRM / marketplace
```
# 3. Search Architecture
## 3.1 Discovery Layer
Use structured or licensed search providers to generate candidate businesses.
Recommended order:
1. DataForSEO local and SERP data
2. Approved local-business or Places-compatible provider
3. Gemini grounded search for supplemental verification
4. Public business directories and company websites
Each discovery result must include:
- Provider
- Provider record ID
- Business name
- Address
- City and region
- Website
- Phone
- Category
- Rating and review count when licensed
- Source timestamp
- Raw source reference
## 3.2 Identity Resolution
Before enrichment, normalize each candidate into one canonical business identity.
Match signals:
- Normalized business name
- Domain
- Phone number
- Street address
- Provider place ID
- Geographic coordinates
Output:
```json
{
  "business_id": "biz_123",
  "canonical_name": "Example Plumbing Ltd.",
  "domain": "exampleplumbing.ca",
  "phone": "+16045550123",
  "match_confidence": 0.96,
  "matched_source_ids": ["dfs_123", "place_456"]
}
```
## 3.3 Duplicate Prevention
Deduplicate at three levels:
- Within the current search run
- Across previous campaigns
- Across previously delivered marketplace inventory
Duplicate keys:
- Domain
- Phone
- Address
- Place ID
- Fuzzy name plus city
# 4. Eligibility Screening
Create hard eligibility gates before expensive crawling or enrichment.
## Required checks
- Active operating business
- Local or offline service business
- Target geography match
- Target category match
- Not a government entity
- Not a directory or marketplace
- Not a national chain when excluded by profile
- Valid identity confidence above threshold
## Suggested CLI
```bash
leadsniper qualify eligibility \
  --campaign campaign_123 \
  --minimum-confidence 0.80
```
## Result states
- `eligible`
- `ineligible`
- `manual_review`
# 5. Website Crawl and Evidence Collection
Add a Playwright-based crawler operated through LeadSniperAI CLI workers.
## Pages to inspect
- Homepage
- About
- Contact
- Services
- Booking or request-quote page
- Location pages
## Extracted signals
- Primary CTA
- Contact form
- Click-to-call
- Online booking
- Live chat
- After-hours intake
- Trust badges
- Testimonials
- Team or owner information
- Service-area coverage
- Broken links
- Mobile viewport
- Schema markup
- Social profiles
- Technology indicators
## Crawler command
```bash
leadsniper crawl website \
  --lead lead_123 \
  --pages home,about,contact,services \
  --block images,fonts,video \
  --retry 2 \
  --json
```
Every observation must store:
- Claim
- Source URL
- Selector or page location where practical
- Screenshot reference when useful
- Observation timestamp
- Confidence
- Raw extracted value
# 6. Technical Search and Website Audit
## PageSpeed and Core Web Vitals
Capture:
- Performance
- Accessibility
- SEO
- Best practices
- LCP
- CLS
- INP or TBT proxy
- FCP
## Search visibility audit
Use DataForSEO for:
- Local pack visibility
- Organic ranking keywords
- Commercial-intent keywords
- Keyword volume
- CPC
- Competitors
- SERP overlap
- Local landing-page gaps
## Required distinction
- `verified_data`: sourced from a structured provider or direct measurement
- `estimated_data`: AI-generated interpretation
- `unknown`: insufficient evidence
Unknown must not be scored as a confirmed failure.
# 7. Multi-Dimensional Scoring
Replace a single vague score with separate deterministic dimensions.
## Recommended scores
- Eligibility Score
- Website Failure Score
- Search Opportunity Score
- AI Employee Fit Score
- Contactability Score
- Business Capacity Score
- Evidence Confidence Score
- Commercial Priority Score
## Example final priority formula
```plain text
Commercial Priority =
  20% Eligibility
+ 20% Website/Search Problem Severity
+ 20% AI Employee Fit
+ 15% Business Capacity
+ 10% Contactability
+ 10% Evidence Confidence
+  5% Freshness
```
Weights must be configurable by campaign profile.
## Example CLI
```bash
leadsniper score opportunity \
  --lead lead_123 \
  --profile profiles/bc-plumbing-ai-receptionist.json \
  --explain
```
# 8. Opportunity Classification
Suggested opportunity classes:
- `digital-foundation-gap`
- `missed-call-opportunity`
- `booking-friction`
- `reputation-recovery`
- `local-seo-gap`
- `mobile-conversion-gap`
- `after-hours-intake-gap`
- `review-automation-fit`
- `hidden-gem`
- `not-qualified`
Each classification must include:
- Supporting observations
- Contradicting evidence
- Score breakdown
- Confidence
- Recommended offer
# 9. Adversarial Refutation Pass
Before outreach, run a second process whose job is to disprove the diagnosis.
Examples:
- Search for hidden external booking links
- Check whether chat opens only after interaction
- Verify whether a contact form exists on a subpage
- Confirm whether the business is still active
- Check whether a stronger website exists on another domain
- Confirm that the observed deficiency is current
## CLI
```bash
leadsniper refute lead_123
```
## Outcomes
- `confirmed`
- `partially_refuted`
- `refuted`
- `inconclusive`
Refuted signals must be removed from scoring and outreach.
# 10. QA Gates
A lead cannot become outreach-ready unless all required gates pass.
## Core QA gates
- Identity verified
- Business active
- No unresolved duplicate
- Required evidence present
- Opportunity score above campaign threshold
- At least one confirmed problem signal
- Contact status acceptable
- No prohibited claim in outreach
- No unsupported revenue-loss statement
- No placeholder content
- Freshness within campaign policy
## Standard rejection codes
- `BUSINESS_INACTIVE`
- `IDENTITY_UNVERIFIED`
- `DOMAIN_MISMATCH`
- `DUPLICATE_BUSINESS`
- `PREVIOUSLY_DELIVERED`
- `INSUFFICIENT_EVIDENCE`
- `OBSERVATION_REFUTED`
- `CONTACT_UNVERIFIED`
- `SCORE_BELOW_THRESHOLD`
- `NO_COMMERCIAL_FIT`
- `STALE_RESULT`
# 11. Provider Failover and Search Reliability
Create a provider router rather than hard-coding a single search source.
```yaml
local_discovery:
  primary: dataforseo
  fallback:
    - approved_places_provider
    - gemini_grounded_search
  retries: 3
  backoff: exponential
  stop_on:
    - unauthorized
    - invalid_location
```
## CLI
```bash
leadsniper providers status
leadsniper providers test
leadsniper providers failover --show-policy
```
Record provider usage, cost, latency, errors, and result count for every search.
# 12. Campaign Profiles
Represent each search strategy as a reusable profile rather than hard-coded logic.
```json
{
  "name": "BC Plumbing AI Receptionist",
  "vertical": "plumbing",
  "geography": {
    "country": "CA",
    "province": "BC",
    "cities": ["Vancouver", "Burnaby", "Surrey"]
  },
  "offer": "ai_receptionist",
  "requirements": {
    "active_business": true,
    "public_phone": true,
    "minimum_reviews": 10
  },
  "signals": {
    "phone_only_intake": 20,
    "no_after_hours_option": 20,
    "no_online_booking": 15,
    "slow_mobile_site": 10
  },
  "exclusions": {
    "national_chains": true,
    "government_entities": true
  }
}
```
Run with:
```bash
leadsniper campaign run \
  --profile profiles/bc-plumbing-ai-receptionist.json
```
# 13. Search Results Data Model
Every qualified search result should contain:
```json
{
  "business": {},
  "identity": {},
  "discovery_sources": [],
  "website_observations": [],
  "technical_metrics": {},
  "search_visibility": {},
  "contacts": [],
  "scores": {},
  "classifications": [],
  "refutation_results": [],
  "qa_status": {},
  "recommended_offer": {},
  "outreach_drafts": {},
  "freshness": {},
  "delivery_history": {}
}
```
# 14. Search Quality Metrics
Track both volume and quality.
## Pipeline metrics
- Candidates discovered
- Identity-match rate
- Eligibility pass rate
- Website crawl success rate
- Enrichment completion rate
- Duplicate rate
- Refutation rate
- QA pass rate
- Average evidence confidence
- Cost per qualified opportunity
- Time per qualified opportunity
## Commercial metrics
- Positive reply rate
- Meeting-booked rate
- Opportunity acceptance rate
- Buyer dispute rate
- Duplicate-delivery rate
- Lead freshness at delivery
- Conversion by opportunity class
- Revenue per qualified opportunity
# 15. Search Optimization Loop
```plain text
Search run
   ↓
Qualified and rejected results
   ↓
Outcome tracking
   ↓
Reason-code analysis
   ↓
Weight and filter adjustments
   ↓
New campaign profile version
```
Review monthly:
- Which signals predict replies?
- Which signals predict meetings?
- Which search providers produce the best qualified-opportunity rate?
- Which verticals have the lowest cost per accepted lead?
- Which rejection reasons occur most often?
- Which score thresholds are too strict or too weak?
# 16. Convex Workflow Recommendation
Use Convex as the operational state and queue layer.
Recommended objects:
- `campaigns`
- `search_requests`
- `search_runs`
- `businesses`
- `lead_candidates`
- `crawl_jobs`
- `enrichment_jobs`
- `observations`
- `scores`
- `qa_results`
- `outreach_assets`
- `deliveries`
- `provider_events`
Suggested worker command:
```bash
leadsniper worker start \
  --queues discovery,crawl,audit,enrichment,qa \
  --poll-interval 30
```
# 17. Implementation Phases
## Phase 1 — Search quality foundation
- Canonical business identity
- Deduplication
- Provider provenance
- Eligibility gates
- Progressive persistence
## Phase 2 — Direct evidence
- Playwright crawler
- PageSpeed audit
- Search visibility audit
- Evidence objects
- Unknown-versus-false handling
## Phase 3 — Decision quality
- Deterministic multi-score engine
- Opportunity classification
- Refutation pass
- QA gates
- Rejection reason codes
## Phase 4 — Operational reliability
- Convex job queues
- CLI workers
- Retry and checkpoint support
- Provider failover
- Cost tracking
## Phase 5 — Commercial optimization
- Campaign profiles
- Multi-channel outreach packs
- Marketplace evidence bundles
- Delivery memory
- Outcome-based scoring calibration
# 18. Acceptance Criteria
The improved workflow is ready for production testing when:
- Every lead has a canonical business identity
- Every score can be explained by stored evidence
- Unknown values are never treated as confirmed failures
- Duplicate businesses are blocked before paid enrichment
- Search runs can resume after interruption
- Refuted claims are removed automatically
- Qualified leads pass explicit QA gates
- Search provider, timestamp, cost, and confidence are stored
- Outreach drafts use confirmed observations only
- Search quality can be measured by campaign, provider, vertical, and opportunity class
# 19. Immediate Next Actions
1. Define the canonical business and evidence schemas.
2. Add provider provenance to current search responses.
3. Implement deduplication before enrichment.
4. Build the Playwright crawler as a CLI worker.
5. Add PageSpeed and DataForSEO audit adapters.
6. Implement separate score dimensions.
7. Add the refutation and QA stages.
8. Add Convex queue and checkpoint objects.
9. Create the first campaign profile for BC plumbers and AI receptionist opportunities.
10. Connect search outcomes back into scoring calibration.
# 20. Source and Design Notes
This plan is informed by:
- The current LeadSniperAI 3.0 architecture and FastAPI capabilities
- The existing LeadSniperAI CLI specification
- Independent analysis of source-visible lead-intelligence workflow patterns
Do not copy source code from repositories whose licences prohibit reuse. Reimplement architectural concepts independently and retain appropriate source attribution in internal research notes.