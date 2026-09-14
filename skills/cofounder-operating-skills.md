---
type: SYNTHESIS
created: 2026-04-16
updated: 2026-04-16
confidence: 0.85
sources: [https://github.com/TheCraigHewitt/skills]
related: [[ceo-skills-framework]], [[sales-skills-framework]], [[business-context-md]]
tags: [cofounder, founder, operating-model, skills, ai-skills, synthesis]
status: active
---

# Cofounder Operating Skills — Synthesis

How cofounders at KlickSmartAI should use the Craig Hewitt AI skills library as a practical operating layer. This page synthesizes the CEO and sales skills into a cofounder-specific workflow.

## The core idea

These skills replace the "what should I ask the AI?" problem with structured, context-aware workflows. Instead of starting from a blank prompt, you invoke a skill that already knows how to run a weekly review, a discovery call, or a delegation audit — and it tailors itself to your business via `BUSINESS_CONTEXT.md`.

## Setup order (do this once)

1. **Create `BUSINESS_CONTEXT.md`** in your project root using the CEO template
2. **Create `.agents/sales-context.md`** using the `sales-context` skill interview
3. Install the skills library: `npx skills@latest add TheCraigHewitt/skills --full-depth`

After setup, every skill you run is automatically contextualized to KlickSmartAI.

## Cofounder operating rhythm

### Weekly (15 min each)
Use `weekly-review` every Friday or Monday. Each cofounder runs their own review independently, then shares the output async. This surfaces:
- What's actually moving the needle vs. what felt busy
- Energy levels (burn-out signal before it compounds)
- Divergence in priorities between cofounders (surface early)

### Quarterly (60–90 min, together)
Use `quarterly-review` as a cofounder session. The Keep/Kill/Start framework forces explicit alignment on what you're stopping — the hardest conversation. Output: `reviews/quarterly-review-[YYYY]-Q[N].md` committed to the wiki.

### Before hard decisions
Use `strategic-sparring` as a thinking partner before major calls: pricing changes, pivots, hiring decisions, partnership terms. The 5-phase structure (Understand → Map Options → Stress-Test → Consequences → Clarity) produces a documented decision record — useful for later post-mortems.

### Before every sales call
Stack two skills:
1. `prospect-research` — build intelligence brief on the company/contact
2. `discovery-call` — run structured SPIN-based discovery

Post-call: `call-debrief` within 2 hours to extract learnings and next steps.

## Skill stack by function

### Strategy
- `strategic-sparring` — major decisions
- `quarterly-review` — direction check
- `weekly-review` — execution rhythm

### Sales (founder-led)
- `sales-context` → `prospect-research` → `discovery-call` → `demo-script` → `objection-handling` → `proposal-pricing` → `negotiation`
- `pipeline-review` — weekly pipeline health audit
- `cold-email` + `outbound-sequence` — outbound motion

### Team
- `hiring` — role definition through hire/no-hire decision
- `delegation` — audit what founders are holding that shouldn't be
- `one-on-ones` — structured 1:1s for any direct reports

### Finance
- `financial-review` — monthly numbers check with real questions about runway, unit economics, pricing

### Content / distribution
- `content-repurpose` — turn one piece of content into a full week of distribution

## Decision record discipline

Every `strategic-sparring` session ends with a documented decision: choice made, key assumptions, triggers for revisiting. Commit these to `wiki/lessons/` with the crystallization protocol. The compounding value is in the audit trail — when you revisit a decision 6 months later, you can see what you assumed and whether it held.

## What these skills don't replace

- Customer calls and relationship judgment
- Domain expertise and product intuition
- Cofounder alignment conversations (do those live, not via AI)
- Legal, financial, and compliance decisions (refer to professionals)

## Tensions / open questions

- How well do the skills adapt to a non-US, non-SaaS context? (confidence: medium — needs field testing at KlickSmartAI)
- The RALPH coding workflow may conflict with existing dev processes — evaluate separately
- YouTube skills: relevant if KlickSmartAI pursues video distribution (currently unknown)
