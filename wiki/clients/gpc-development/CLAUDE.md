# CLAUDE.md — GPC Development

This file is the **entry-point adapter** for Hermes Agent and Claude Code. Both auto-load this file when you enter `/home/denni/wiki/clients/gpc-development/` — that's the contract.

## Workspace identity

| Field | Value |
|-------|-------|
| **Client** | GPC Development |
| **Slug** | `gpc-development` |
| **Domain** | `gpcdevelopment.ca` |
| **Market** | Canada (Vancouver, BC) — DataForSEO locationCode 2124 |
| **Language** | English |
| **Engagement** | SEO audit + organic inbound leads (Phase 1 quote pending) |
| **Compliance mode** | `none` (no securities raising in this engagement) |
| **Vertical** | `seo` (default for organic lead-gen engagements) |
| **Workspace mode** | Quick-mode (flat `projects/` until a recurring pipeline emerges) |
| **OpenSEO project ID** | `34afee19-d725-4073-b43f-1b76c6275c11` |

## The rule

**Every AI-generated artifact for GPC Development MUST land in `drafts/` first.**

Nothing is promoted to `projects/` or `deliverables/` until Dennis explicitly approves. This is the KlickSmartAI source-of-truth gate — binding on every agent (Hermes, Claude Code, subagents).

If a request would write directly to `projects/` or `deliverables/`, refuse and offer the draft route instead.

## What to read on entry

1. `IDENTITY.md` — workspace map, rules, stage gate
2. `CONTEXT.md` — task routing table, 5-stage pipeline
3. `_config/voice.md` — tone for GPC-facing artifacts
4. `_config/deliverables.md` — vertical artifact map (currently `seo`)
5. `_config/gtm-skills.md` — empty (this client has no GTM use-cases yet)
6. `drafts/seo/VALIDATION_QUEUE.md` — what's pending review

## When SEO work is requested

Read `~/.hermes/skills/seo-enrichment-planner/SKILL.md` for the **universal orchestration** (Plan → Discover → Enrich → Score → Outreach, HITL gate, cost model). Then check `_config/deliverables.md` for the **per-vertical binding** (which SEO skills are active for GPC, which are dormant).

Output goes to:
- `drafts/seo/<phase>-<date>-<topic>.md` — first-pass source Markdown
- `drafts-preview/seo/<phase>-<date>-<topic>.html` — styled preview (use `scripts/render-report.py`)
- `projects/seo/<phase>-<date>-<topic>.md` — promoted after user approval
- `deliverables/seo/<phase>-<date>-<topic>.html` — client-ready export after promotion

## DuckDB analytical mirror

Lives at `.local_tier/clients/gpc-development.duckdb`. Synced every 30 min by the `gpc-duckdb-sync` cron (job_id `e1db222ea84c`, scoped to project_id `34afee19-d725-4073-b43f-1b76c6275c11`). Use it for OLAP queries on keyword metrics, audit findings, rank snapshots, PAA scans — without round-tripping through the OpenSEO MCP.

Manual sync: `~/.hermes/scripts/sync-gpc-duckdb.py`

## Pitfalls (specific to this client)

1. **Canadian market.** Use `locationCode: 2124` for all SERP/keyword/PAA calls. CA-specific data.
2. **Vancouver-specific positioning.** Read `_config/voice.md` for tone — "Vancouver GC" not "general contractor" globally.
3. **Multifamily primary, custom-home secondary.** Project context is explicit on this. Don't recommend custom-home-first content unless the user redirects.
4. **Skip branded-developer SERPs.** Bosa, Concord Pacific, etc. — project context says these are uncompetitive for a single firm.
5. **Three test seeds in D1 from earlier sessions** (`test seo skill 1/2/3`) — should be cleaned up before any new PAA scans are flagged.

## Compatibility

| Aspect | Hermes Agent | Claude Code |
|--------|--------------|-------------|
| Auto-load | `CLAUDE.md` on folder entry | Same |
| Skill entry | `skill_view(name='seo-enrichment-planner')` etc. | `/seo-enrichment-planner` |
| MCP | OpenSEO + Serper + DuckDB | Same via `mcp-remote` |
| HITL gate | "yes" / "send it" / "approve" | Same |
| Source-of-truth | Enforced via this file | Same |

---

*This file is the protected rulebook — edits to CLAUDE.md are blocked by the Hermes safety layer unless Dennis explicitly approves a proposed diff.*
