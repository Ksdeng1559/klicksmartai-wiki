# LeadSniperAI 3.0 — Website Failure Rules

## Purpose

This document defines the observable website conversion failures used by LeadSniperAI 3.0.

The system identifies website revenue infrastructure weaknesses without making unsupported claims about revenue loss, buying intent, or business outcomes.

---

## Website Failure Threshold

Only one observable website conversion failure is required for the business to proceed to qualification review.

Qualifying failures:

1. No clear headline explaining what the business does
2. No call-to-action above the fold
3. Phone-only contact with no form or booking pathway
4. Poor mobile usability
5. Slow, cluttered, or outdated layout
6. Generic or stock copy with no specificity
7. No trust indicators visible above the fold

---

## Failure Categories

### 1. Hero Failure

A hero failure occurs when the first visible screen does not clearly answer:

```text
What does this business do?
Who does it serve?
Where does it serve?
What should the visitor do next?
```

Observable signals:
- Vague headline
- Brand-only headline
- No location context
- No service clarity
- No visible next step

Allowed phrasing:

```text
No visible headline explaining the service, location, or next step.
```

---

### 2. CTA Failure

A CTA failure occurs when there is no visible action above the fold.

Observable signals:
- No request quote button
- No booking button
- No call button
- No contact button
- CTA appears only far down the page

Allowed phrasing:

```text
No visible call-to-action above the fold.
```

---

### 3. Phone-Only Trap

A phone-only trap occurs when the website appears to rely only on phone calls for intake.

Observable signals:
- Phone number visible but no form
- No booking widget
- No quote request pathway
- No chat or intake workflow

Allowed phrasing:

```text
Appears to rely on phone-only intake with no visible form or booking path.
```

---

### 4. Slow Response Gap

A slow response gap occurs when no immediate intake or routing method is visible.

Observable signals:
- No online booking
- No request quote form
- No contact workflow
- No live chat
- No after-hours pathway

Allowed phrasing:

```text
No visible instant intake or request pathway.
```

---

### 5. Mobile Friction

Mobile friction occurs when the site appears difficult to use on a mobile device.

Observable signals:
- Tiny text
- Overlapping elements
- Hard-to-tap buttons
- Horizontal scrolling
- Slow-loading page
- CTA not visible on mobile

Allowed phrasing:

```text
Mobile usability issues are visible and may create visitor friction.
```

---

### 6. Trust Deficit

A trust deficit occurs when trust indicators are not visible early in the visitor journey.

Observable signals:
- No reviews above the fold
- No licenses or certifications visible
- No project photos
- No before/after examples
- No awards, associations, or proof points
- No team or owner credibility

Allowed phrasing:

```text
No visible trust indicators above the fold.
```

---

### 7. Generic Copy

Generic copy occurs when website language does not show specificity.

Observable signals:
- Generic slogans
- No service-area specificity
- No vertical-specific language
- No emergency/same-day/specialty clarity when relevant
- Stock-like service descriptions

Allowed phrasing:

```text
Website copy appears generic and does not clearly distinguish service scope or location.
```

---

## Website Type Classification

Use one of the following:

### None
No website is present.

### Basic
Placeholder, broken, very thin, or incomplete website.

### Brochure
Informational website with limited or no conversion infrastructure.

### Semi-Functional
Some capture exists, but intake appears manual or limited.

### Conversion-Enabled
Clear CTA, trust signals, routing, and intake pathways are visible.

---

## Final Override Test

After website review, answer:

```text
Could a real customer land on this website and reasonably fail to convert?
```

If yes:

```text
QUALIFIED
```

If no:

```text
DISQUALIFIED
```

This final override test takes priority over all other scoring logic.

---

## Prohibited Claims

Do not say:

- They are losing money
- This is costing them revenue
- They need a new website
- This will increase conversion
- This will generate more leads
- Guaranteed improvement

Use neutral diagnostic language only.

---

## Output Example

```yaml
Website Revenue Readiness:
  Website Type: Brochure
  Conversion Failures Observed:
    - No visible CTA above the fold
    - Appears to rely on phone-only intake
    - No visible trust indicators above the fold
  Intake Method Visible: Phone number only
  Final Override Test: Yes
  Qualification Status: Qualified
```
