---
title: GTM Enrichment HITL Gate
created: 2026-08-11
updated: 2026-08-11
type: pattern
tags: [pattern, gtm, enrichment, hitl, governance, deepline]
sources: []
confidence: high
---

# GTM Enrichment HITL Gate

Rule of thumb + skill routing for paid-enrichment work.

## Rule
**No paid enrichment runs without explicit user approval.** LeadSniperAI's
`mcp__leadsniper__enrich_lead` / Deepline plays consume credits. The user
approves by replying "yes" (or equivalent) to the skill's plan output.

## Pipeline
1. **Pilot run** — produce a credit-cost + sample-size plan via the
   `gtm-enrichment-planner` skill. Present to user.
2. **HITL gate** — wait for user approval.
3. **Execute** — run the actual enrichment only after approval.
4. **Report** — credit spend, hit rate, sample quality.

## Stack
- **swan** skill (`gtm/`) — GTM workflows
- **deepline** skill (`deepline/`) — paid plays (prebuilt, not custom tools)
- **LeadSniperAI** — actual enrichment backend, exposed via MCP

## Deepline provider notes
- **Limadata** = Canada. **Enformion / OpenSOSData** = US-only.
- Plays run prebuilt (no custom tool execution).
- Verified emails via waterfall.

## See also
- [[Search-Provider-Rotation]]
- [[LeadSniper-Sgi]]
- [[Hermes-Governance-Hitl-Channel]]