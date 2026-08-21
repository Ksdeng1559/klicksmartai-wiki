# LeadSniperAI 3.0 — Eligibility Rules

## Purpose

This document defines the mandatory qualification rules for determining whether a business can enter the LeadSniperAI diagnostic workflow.

The system must use observable public information only.

Do not fabricate, infer buying intent, or claim revenue impact.

---

## Absolute Eligibility Test

A business must meet all four conditions below.

1. Listed on Google Maps
2. Has a website URL
3. Provides a local, offline service
4. Appears currently operational

If any condition fails, the business is marked:

```text
DISQUALIFIED
```

---

## Eligibility Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| google_maps_listed | boolean | yes | True only if visible in Maps or Maps data source |
| website_url | string | yes | Must be a valid public URL |
| local_offline_service | boolean | yes | Must provide a service delivered locally/offline |
| appears_operational | boolean | yes | Based on visible hours, reviews, site activity, or Maps status |
| eligibility_status | enum | yes | Eligible / Disqualified |
| disqualification_reason | string | conditional | Required when status is Disqualified |

---

## Local Offline Service Definition

Qualifies:
- HVAC
- Plumbing
- Roofing
- Painting
- Landscaping
- Junk removal
- Pest control
- Dental
- Veterinary
- MedSpa
- Local professional services with offline delivery

Does not qualify:
- Pure ecommerce
- Pure SaaS
- Affiliate sites
- National franchise pages with no local operator visibility
- Lead aggregator pages
- Directories
- Media sites

---

## Operational Status Signals

Acceptable observable signals:
- Business hours shown
- Recent Google reviews
- Active phone number
- Active website
- Recent site updates
- Visible booking/contact pathway
- Maps profile appears open

If operational status cannot be verified, mark:

```text
Unknown
```

Unknown operational status should usually result in Watchlist unless another mandatory condition fails.

---

## Demand Signal Test

Only one demand signal is required to proceed.

Valid demand signals:
- 15+ Google reviews
- Phone number listed on Maps
- Business hours shown as open
- Appears anywhere in Google Maps results

If no demand signal is observable, mark:

```text
LOW PRIORITY
```

Do not disqualify solely because demand signals are weak.

---

## Final Eligibility Decision Logic

```text
IF google_maps_listed = false → Disqualified
ELSE IF website_url is missing → Disqualified
ELSE IF local_offline_service = false → Disqualified
ELSE IF appears_operational = false → Disqualified
ELSE IF no demand signal → Low Priority
ELSE → Eligible for Website Revenue Leak Review
```

---

## Governance Rules

Allowed language:
- No visible...
- Appears to rely on...
- Not publicly listed...
- Unknown
- Observable signal

Disallowed language:
- They are losing money
- They need this
- Guaranteed ROI
- They are desperate
- They will buy
- This will increase revenue

---

## Output Example

```yaml
Eligibility:
  google_maps_listed: true
  website_url: https://example.com
  local_offline_service: true
  appears_operational: true
  demand_signal_present: true
  eligibility_status: Eligible
  disqualification_reason: null
```
