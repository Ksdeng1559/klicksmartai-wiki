---
title: Hermes GTM Skills Inventory
created: 2026-09-08
updated: 2026-09-08
type: reference
tags: [gtm, skills, catalog, hermes, agent]
sources: [~/.hermes/skills/gtm/]
related: [swan-gtm-skills.md]
---

# KlickSmartAI GTM Skills & Strategies Inventory

**Source:** `~/.hermes/skills/gtm/` (45 skill folders, loaded live into Hermes agent context).
**Purpose:** Reference catalog for Claude Code — pick the right skill for each GTM lane.

---

## 1. ICP & Targeting

| Skill | What it does |
|-------|--------------|
| `icp` | Defines and refines who the org sells to. Use for ICP discovery. |
| `icp-builder` | Build, validate, or expand a client's ICP. |
| `tam-builder` | Build a Total Addressable Market list — when the target market needs to become an account list. |
| `score` | Qualifies and scores accounts against ICP and buying signals. |

## 2. Account Intelligence

| Skill | What it does |
|-------|--------------|
| `account-intelligence-analyst` | Deep-dive account research (use when you need a single high-fidelity account profile). |
| `account-tier-scoring` | Production-grade account scoring + tiering. |
| `abm-engagement-scoring` | Account-level engagement scoring, buying group / DMU measurement. |

## 3. Lead Sources & List Building

| Skill | What it does |
|-------|--------------|
| `lead-sources-guide` | Choose lead sources + build prospect lists. |
| `list-architect` | Build B2B lead lists — ICP definition + shaping. |
| `leadsniper-cli` | Operate the LeadSniperAI CLI / platform. |
| `leadsniper-icm-pipeline` | Run LeadSniper against an ICM client workspace. |

## 4. Enrichment & Research

| Skill | What it does |
|-------|--------------|
| `gtm-enrichment-planner` | Plan enrichment skills + credit costs; **HITL approval gate** before any paid spend. |
| `research` | Researches a company, person, buying committee, signal, deal. |
| `pre-ma-offmarket-discovery` | Find off-market M&A candidates via succession signals. |

## 5. Signals & Buying Intent

| Skill | What it does |
|-------|--------------|
| `buying-signals-6` | Prioritize outreach / build signal stacks (six-signal framework). |
| `signal-interpreter` | Interpret a raw GTM signal — business event, trigger, news. |
| `citation-gap-outreach` | Outreach where the sources behind AI answers are known gaps. |
| `track-contact-job-changes` | Find which contacts in the CRM changed jobs recently. |

## 6. Outreach — Email

| Skill | What it does |
|-------|--------------|
| `cold-email-strategist` | Writing or fixing cold email — first-touch strategy. |
| `cold-email-first-touch` | Write the first cold email to someone. |
| `cold-email-4-sequence` | Build cold email campaigns (4-touch sequence). |
| `cold-email-templates-34` | 34 templates across use cases. |
| `cold-email-preflight` | **Right before launching** a cold email campaign — final QA gate. |
| `pain-is-the-pitch` | Fix generic copy — make pain the pitch. |

## 7. Outreach — Calls / LinkedIn / Warm Paths

| Skill | What it does |
|-------|--------------|
| `cold-call-scripts` | Train SDRs on calls / build call scripts. |
| `linkedin-abm-1to1-few-many` | Choose + run LinkedIn ABM motions (1:1 / few / many). |
| `warm-intro-intelligence` | Find warm intro paths into a target account. |
| `bridge-before-cold` | **Use before staging a prospect** and before drafting outreach. |
| `never-guess-an-email` | Have a target company but no verified contact → waterfall discovery. |

## 8. Positioning & Messaging

| Skill | What it does |
|-------|--------------|
| `positioning-and-story` | Fix messaging that describes what the product does, not why it matters. |
| `positioning-messaging-designer` | Design positioning + messaging frameworks for clients. |
| `category-of-one-positioning` | Founder / expertise-led businesses that need a unique category. |
| `reach-out` | Use whenever creating **any** outreach — cold email, LinkedIn, call script. |

## 9. Sales Process

| Skill | What it does |
|-------|--------------|
| `founder-led-sales` | Developers love the tool but nobody buys → founder-led motion. |
| `pipeline-review` | Reviews pipeline health before forecast calls or recurring reviews. |
| `call-scorecards` | Fix inconsistent call quality → scorecards + training. |
| `deal-desk-operations` | Stand up / operate a deal-desk function. |
| `cs-operations` | Customer success operations for B2B SaaS — post-sale retention. |
| `roi-proof-generator` | Build proof assets for renewals / QBRs / expansion. |

## 10. RevOps

| Skill | What it does |
|-------|--------------|
| `revops-hubspot` | HubSpot implementation patterns for revenue operations teams. |
| `lead-routing` | Lead routing strategy, assignment logic, round-robin patterns. |

## 11. SEO-Fed GTM

| Skill | What it does |
|-------|--------------|
| `seo-topic-prioritization` | A shaped topic list needs scoring and sequencing for content production. |

## 12. SDR Enablement

| Skill | What it does |
|-------|--------------|
| `sdr-outbound-rules` | Train SDRs, standardize outbound execution. |

## 13. Strategic / Governance

| Skill | What it does |
|-------|--------------|
| `strategic-intelligence-briefing` | Generate a Strategic Intelligence Briefing. |
| `wiki-source-of-truth-governance` | Enforce HITL validation gate before promoting AI-generated wiki content. |

---

## Recommended Run Order (typical campaign)

1. `icp` / `icp-builder` → lock ICP.
2. `tam-builder` → shape account universe.
3. `lead-sources-guide` + `list-architect` → source accounts.
4. `gtm-enrichment-planner` → plan enrichment + **HITL cost approval**.
5. `research` / `account-intelligence-analyst` → enrich.
6. `score` + `account-tier-scoring` → prioritize.
7. `buying-signals-6` + `signal-interpreter` → layer signals.
8. `bridge-before-cold` → pre-outreach staging.
9. `reach-out` → draft first-touch (email / LinkedIn / call).
10. `cold-email-preflight` → final QA before launch.
11. `pipeline-review` → ongoing forecast hygiene.
12. `cs-operations` + `roi-proof-generator` → post-sale retention + expansion.

---

## Notes for Claude Code

- Skills live in `~/.hermes/skills/gtm/<skill-name>/SKILL.md`. Load with `skill_view(name='gtm:<skill>')` (Hermes form) or read the file directly.
- Every skill respects **HITL** (human-in-the-loop) before any paid enrichment, outbound send, or wiki publish.
- The `gtm-enrichment-planner` is the **only** sanctioned gate before paid enrichment — never bypass it.
- `reach-out` is the universal "create any outreach" entry point when unsure which specialist skill to use.