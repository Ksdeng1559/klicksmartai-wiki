---
type: CONCEPT
created: 2026-04-16
updated: 2026-04-16
confidence: 0.90
sources: [https://github.com/TheCraigHewitt/skills]
related: [[ceo-skills-framework]], [[sales-skills-framework]], [[cofounder-operating-skills]]
tags: [skills, context, setup, ai-skills, foundation]
status: active
---

# BUSINESS_CONTEXT.md — The Foundation File

The single most important setup step for using AI skills effectively. Both CEO and sales skills read this file automatically before generating output. Without it, advice is generic. With it, every skill is tailored to your actual stage, ICP, and priorities.

## File locations

| File | Used by |
|------|---------|
| `BUSINESS_CONTEXT.md` (project root) | All 10 CEO skills |
| `.agents/sales-context.md` | All 21 sales skills |

The sales-context file is more detailed for B2B-specific info; the business context covers the full operating picture.

## What to include

### Company fundamentals
- What you sell and your business model
- Company stage (pre-revenue / seed / growth / etc.)
- Team size

### Your role
- Personal focus areas day-to-day
- Current quarterly priorities (3 max)

### Market positioning
- ICP: who you sell to (be specific — "B2B SaaS, $5M–$30M ARR, 20–100 employees, using Salesforce" beats "mid-market SaaS companies")
- Core value proposition
- Differentiators (outcomes, not features)
- Before/after customer outcomes
- Sales motion: channels, deal size, cycle length
- Competitive landscape

### Operational metrics
- 3–5 key performance indicators
- Tech stack

### Content strategy (if relevant)
- Publishing channels
- Audience description
- Voice/tone

## Why specificity compounds

Craig Hewitt's framing: "mid-market SaaS companies" matches ~50,000 firms. "B2B SaaS, $5M–$30M ARR, 20–100 employees, using Salesforce" matches ~500. The more specific your context, the sharper every downstream skill output.

## Setup command

```bash
# Install and run the sales-context skill to build .agents/sales-context.md
npx skills@latest add TheCraigHewitt/skills/sales/sales-context
```

Then start a new Claude Code session and run `/sales-context` to walk through the 5-round setup interview.

## Related skills

- `sales-context` — interactive interview to build the sales version
- All CEO skills — auto-reference `BUSINESS_CONTEXT.md`
- All sales skills — auto-reference `.agents/sales-context.md`
