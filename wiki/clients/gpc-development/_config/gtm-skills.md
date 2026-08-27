# GTM Skills — GPC Development

**Empty binding.** GPC Development's current engagement is SEO-only (organic inbound lead generation). There are no GTM (go-to-market) use-cases bound.

## What this means

- The agent will not propose cold-outreach, signal-based outbound, ABM, or any other GTM motion for this client.
- If GPC adds an investor-facing component, capital raise, or syndication, this file needs updating.
- If GPC adds an outbound component (email to general contractors, partner outreach), update this file.

## When to update

| Trigger | Action |
|---|---|
| GPC asks for an outreach campaign | Bind `signal-based-outbound` + update this file |
| GPC raises capital | Switch `compliance_mode` to `securities`, add Reg D 506(b) overlay |
| GPC wants ads | Bind `by-role_demand-gen`, add paid ads |
| GPC adds partnership motion | Bind `ai-abm-targeting` |

## Universal HITL gate (default)

When GTM skills are added later, the gate is:
1. `gtm-enrichment-planner` produces cost plan + workflow
2. Present to Dennis → wait for "yes"
3. On approval, run the skills
4. Output → `drafts/email/` or `drafts/outreach/` first (source-of-truth gate)
5. Promote to `projects/` + `deliverables/` only on Dennis's signature

## Deepline CLI rule (when GTM skills activate)

Per `~/.hermes/skills/gtm-enrichment-planner/SKILL.md`, the universal rule is:
- Use `deepline plays` (prebuilt workflows) — **NEVER** `deepline tools execute` directly.
- Canada (GPC's market) → **Limadata** provider
- US → Enformion / OpenSOSData

This rule applies only when GTM skills are bound. Not currently active for GPC.
