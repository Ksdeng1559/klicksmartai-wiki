# LeadSniperAI 3.0 — AI Employee Fit Scoring

## Purpose

This document defines the AI Employee Fit Score used by LeadSniperAI 3.0.

The score estimates whether a qualified business has observable operational conditions that may align with one or more AI Employee workflows.

The score must be based only on observable public signals.

Do not infer buying intent, urgency, budget, revenue loss, or willingness to purchase.

---

## Total Score

```text
100 points maximum
```

Scoring categories:

| Category | Max Points |
|---|---:|
| Missed Call / Response Risk | 30 |
| Lead Volume Potential | 25 |
| Process Complexity | 20 |
| Digital Conversion Gap | 15 |
| AI Readiness Signals | 10 |

If a signal cannot be verified, assign 0 points for that factor.

---

## 1. Missed Call / Response Risk — 30 Points

Measures whether the business appears vulnerable to missed calls, after-hours inquiries, or manual response gaps.

Observable signals:

| Signal | Points |
|---|---:|
| Phone number is primary or only intake method | 10 |
| Emergency, urgent, or time-sensitive service visible | 10 |
| Business hours are limited or after-hours demand is likely by vertical | 5 |
| No visible chat, booking, or instant intake pathway | 5 |

Examples of relevant verticals:
- Plumbing
- HVAC
- Electrical
- Restoration
- Roofing emergency repair
- Pest control
- Auto glass

---

## 2. Lead Volume Potential — 25 Points

Measures whether observable demand signals suggest enough inbound or search activity to justify automated intake or follow-up.

Observable signals:

| Signal | Points |
|---|---:|
| 15+ Google reviews | 5 |
| 50+ Google reviews | 5 additional |
| Appears in Google Maps results | 5 |
| Multiple services listed | 5 |
| Service area or multiple locations visible | 5 |

Do not assume lead volume from company size alone.

---

## 3. Process Complexity — 20 Points

Measures whether the business appears to handle multi-step customer intake or service workflows.

Observable signals:

| Signal | Points |
|---|---:|
| Multiple service categories | 5 |
| Quote / estimate required | 5 |
| Booking, inspection, consultation, or dispatch process visible | 5 |
| Commercial or emergency intake complexity visible | 5 |

Examples:
- Roofing inspection before estimate
- HVAC repair vs replacement
- Plumbing emergency vs scheduled job
- Commercial painting estimate
- MedSpa consultation booking

---

## 4. Digital Conversion Gap — 15 Points

Measures whether the website has observable conversion friction.

Observable signals:

| Signal | Points |
|---|---:|
| No CTA above the fold | 3 |
| Phone-only intake | 3 |
| No form or booking pathway | 3 |
| No visible trust indicators above the fold | 3 |
| Poor mobile usability or outdated layout | 3 |

This category should align with `docs/scoring/website-failure-rules.md`.

---

## 5. AI Readiness Signals — 10 Points

Measures whether the business appears to have enough digital infrastructure to support an AI Employee workflow.

Observable signals:

| Signal | Points |
|---|---:|
| Website is active and reachable | 2 |
| Contact form or booking form exists | 2 |
| Google Business Profile appears complete | 2 |
| Reviews are present | 2 |
| Business uses a domain email, CRM widget, chat widget, or online scheduler | 2 |

If readiness cannot be verified, assign 0.

---

## Fit Tiers

| Score | Tier | Meaning |
|---:|---|---|
| 80–100 | High Fit | Strong observable match for AI Employee workflow |
| 60–79 | Medium Fit | Several observable gaps and useful workflow fit |
| 40–59 | Watchlist | Some relevant signals, insufficient confidence |
| 0–39 | Low Fit | Weak observable fit or insufficient public data |

---

## Allowed AI Employee Types

Only recommend from this list:

1. AI Receptionist
2. AI After-Hours Answering Agent
3. AI Booking & Scheduling Agent
4. AI Lead Qualification Agent
5. AI Commercial Intake Agent
6. AI Emergency Call Triage Agent
7. AI Review Follow-Up Agent

---

## Recommendation Mapping

### AI Receptionist
Use when:
- Phone number is prominent
- No chat or intake workflow is visible
- Business depends on inbound inquiries

Neutral phrasing:

```text
AI Receptionist may align with the visible phone-first intake pathway.
```

### AI After-Hours Answering Agent
Use when:
- Business hours are limited
- Urgent service vertical
- After-hours demand may reasonably exist based on service type

Neutral phrasing:

```text
AI After-Hours Answering Agent may align with the visible time-sensitive service model.
```

### AI Booking & Scheduling Agent
Use when:
- Appointments, inspections, consultations, or estimates are visible
- Booking appears manual or unclear

Neutral phrasing:

```text
AI Booking & Scheduling Agent may align with the visible appointment or estimate workflow.
```

### AI Lead Qualification Agent
Use when:
- Multiple service categories are visible
- Quote/estimate flow exists
- Customer intent likely needs sorting before response

Neutral phrasing:

```text
AI Lead Qualification Agent may align with the visible multi-service inquiry flow.
```

### AI Commercial Intake Agent
Use when:
- Commercial services are visible
- Projects require scoping, site visits, or estimates

Neutral phrasing:

```text
AI Commercial Intake Agent may align with the visible commercial project intake requirements.
```

### AI Emergency Call Triage Agent
Use when:
- Emergency service is visible
- Same-day or urgent response is mentioned
- Vertical is emergency-heavy

Neutral phrasing:

```text
AI Emergency Call Triage Agent may align with the visible emergency service pathway.
```

### AI Review Follow-Up Agent
Use when:
- Google reviews are present
- Service business relies on trust signals
- Review volume is visible but not strongly featured on the site

Neutral phrasing:

```text
AI Review Follow-Up Agent may align with the visible review-dependent service category.
```

---

## Prohibited Recommendation Language

Do not say:

- They need an AI receptionist
- This will capture missed revenue
- This will increase bookings
- This will improve conversion
- This will pay for itself
- They are losing calls
- They are losing money

Use neutral analytical language only.

---

## Output Example

```yaml
AI Employee Fit Score:
  total: 72
  tier: Medium Fit
  categories:
    missed_call_response_risk: 20
    lead_volume_potential: 20
    process_complexity: 15
    digital_conversion_gap: 12
    ai_readiness_signals: 5
  opportunities:
    - type: AI Receptionist
      observed_signal: Phone number appears to be the primary intake method
      rationale: May align with visible phone-first inquiry handling
    - type: AI Booking & Scheduling Agent
      observed_signal: Estimates or appointments appear to be part of the service workflow
      rationale: May align with visible scheduling requirements
```
