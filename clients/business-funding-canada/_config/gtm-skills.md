---
type: SkillBinding
title: "Business Funding Canada — GTM Skills"
status: active
generated: 2026-10-02
verified: 2026-10-02
---

# GTM Skills (per-client binding)

> Per-client binding for the GTM skills library. Universal orchestration = `gtm-enrichment-planner`. This file declares **which skills BFC uses**, **role mappings**, **client-specific overrides**, and the **universal HITL gate**.

## 1. Bound GTM use-cases

| Use case | Primary skills | Status |
|----------|-----------------|--------|
| `signal-based-outbound` | `buying-signals-6`, `signal-interpreter` | ⏸️ parked (no live outreach yet) |
| `contact-data-enrichment` | `gtm-enrichment-planner`, `find-qualified-titles`, `never-guess-an-email` | ⏸️ parked |
| `automated-lead-qualification` | `score` | ⏸️ parked |
| `by-role_revops` | (RevOps function) | ⛔ blocked — no live pipeline yet |

## 2. Role mappings

| Role | Skill binding | Status |
|------|---------------|--------|
| Founder-led sales (Dennis) | `founder-led-sales`, `pain-is-the-pitch` | ✅ live |
| Cold email (outreach) | `cold-email-strategist`, `cold-email-4-sequence` (post-preflight) | ⏸️ parked |
| AI-SDR (if Hired) | `by_role_ai-sdr` | ⛔ blocked — no SDR hire planned |

## 3. Client-specific overrides

| Motion | Status | Reason |
|--------|--------|--------|
| Cold email outreach to SMB leads | ⏸️ parked | Need express-consent flow + CASL compliance gate before any send |
| Demand-gen paid ads (Google / Meta) | ⛔ blocked | Compliance-heavy; defer until first 5 content articles are live and CASL flow is approved |
| ABM targeting (named accounts) | ⛔ blocked | Site doesn't have ICP + tiering yet |
| Partner / broker channel outreach | ⏸️ parked | No channel deck drafted |
| Lender-anchor recruitment | ⏸️ parked | Need first lender LOI template |

## 4. Universal HITL gate (binding)

Every GTM tool invocation requires Dennis's explicit "yes" before spend:

```
[GTM-PLAN]
Use case: <use-case-name>
Workflow:  <list of skill invocations>
Cost:      <$X.XX credits / API calls>
Output:    <where the result will land — must be drafts/>
Approval:  awaiting / approved / denied
```

**No paid enrichment runs without "yes" from Dennis.** Same pattern as `seo-enrichment-planner`.

## 5. Runtime pattern

1. Read `gtm-enrichment-planner` SKILL.md for stack layers (Plan → Discover → Enrich → Score → Outreach) + credit-cost model.
2. Read this file for **bound skill names + role mappings + overrides**.
3. Compose runtime plan = intersect layers × bindings × overrides.

## 6. When this workspace goes live (first cold send)

The first outbound motion will need:
1. ICP defined (industry × ticket × geography).
2. CASL consent flow on form.
3. 3-touch cold email sequence in `drafts/email/`.
4. Approval via `drafts/VALIDATION_QUEUE.md`.

Don't bypass any of the four.