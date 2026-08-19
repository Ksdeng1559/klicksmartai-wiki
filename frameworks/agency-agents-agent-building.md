# Agency-Agents Framework — Reference for Building AI Agents

> Source framework: https://github.com/msitarzewski/agency-agents (MIT, cloned at `~/wiki/agency-agents/`, 289 files)
> Purpose: Use as a **reference/template** for architecting new AI agents and orchestrating multi-agent work.
> This doc is the distilled "how to build an agent" playbook extracted from the repo. Read the raw repo for the full roster.

---

## 1. What the framework is

A collection of ~250 specialized AI agent definitions grouped into **divisions** (Engineering, Design, Marketing, Sales, Paid Media, Product, Project Mgmt, Testing, Support, Spatial Computing, Specialized, Finance, Game Dev, Academic). Each agent is a single markdown file encoding:

1. **Frontmatter** — `name`, `description`, `color`, `emoji`, `vibe` (one-line personality)
2. **Identity & Memory** — role, personality, what it remembers, its experience
3. **Core Mission** — the specialist's deliverables, not generic duties
4. **Critical Rules** — domain-specific non-negotiables
5. **Technical Deliverables** — concrete outputs with code/format examples
6. **Workflow Process** — step-by-step operating procedure
7. **Communication Style** — how it talks/reports
8. **Success Metrics** — measurable quality bars
9. **Advanced Capabilities** — growth edge, what it gets better at

There is also a `hermes-ai-agency/` subfolder that adapts this into a **SOUL.md / PROFILE.md / AGENTS.md** operational format (Hermes-native) and a `strategy/` layer (NEXUS) with playbooks, handoff templates, and runbooks.

---

## 2. The agent file template (copy this)

```markdown
---
name: <Role Name>
description: <One-line specialization: what it's expert at>
color: <accent color>
emoji: <emoji>
vibe: <one-line personality>
---

# <Role Name> Agent Personality

You are **<Role Name>**, an expert <domain> who <one-line mission>.

## 🧠 Your Identity & Memory
- **Role**: <primary objective>
- **Personality**: <character traits>
- **Memory**: <what it retains across runs>
- **Experience**: <why it's authoritative>

## 🎯 Your Core Mission
### <Area 1>
- <specific deliverables>
### <Area 2>
- <specific deliverables>

## 🚨 Critical Rules You Must Follow
### <Rule Area>
- <non-negotiable behaviors>

## 📋 Your Technical Deliverables
<!-- Concrete outputs: code blocks, templates, report formats, exact schemas -->

## 🔄 Your Workflow Process
### Step 1: <Name>
- <actions>
### Step N: <Name>
- <actions>

## 💭 Your Communication Style
- <how it reports, sample phrases>

## 🎯 Your Success Metrics
You're successful when:
- <measurable outcome>
- <measurable outcome>

## 🚀 Advanced Capabilities
- <what it compounds/learns>
```

**Key insight — this is NOT a generic "act as a developer" prompt.** The differentiator is: strong personality + concrete deliverables + success metrics + proven workflows. If the new agent you're designing lacks any of these four, it's a prompt, not an agent.

---

## 3. The SOUL.md adaptation (Hermes-native)

For Hermes, the framework converts raw agent definitions into `SOUL.md` (voice + scope + constraints) + `PROFILE.md`. The canonical structure (see `~/wiki/agency-agents/hermes-ai-agency/employees/chief-of-staff/SOUL.md`):

```markdown
---
employee_id: <id>
status: active
reports_to: CEO
department: <dept>
---

# <Role> — SOUL

## Voice
- Direct. No fluff.
- Surfaces bad news before good news.
- Always explains *why*, not just *what*.
- References specific evidence (file paths, run numbers).
- Treats the CEO as the only escalation point.

## Mission
<one-line purpose>

## Scope of authority
**Default — no approval needed:**
- <autonomous actions>

**Escalate to CEO:**
- <requires approval actions>

## Working style
1. Read first. 2. Plan second. 3. Build third. 4. Verify fourth. 5. Reflect fifth.

## Constraints
- Never fabricate. Never break escalation rules. Never leak secrets. Always cite evidence.

## What good looks like
- <observable outcomes that prove it's working>
```

This maps 1:1 to KlickSmartAI's **Decision Authority** governance (autonomous / draft-for-review / escalate) — bake the permission matrix into the SOUL.

---

## 4. Orchestration model (NEXUS)

The repo's `strategy/` layer provides an orchestration doctrine you can reuse when coordinating multiple agents. Core ideas worth adopting:

| Pattern | What it is | Why it matters |
|---------|-----------|----------------|
| **Parallel workstreams** | Run independent tracks (product, growth, quality, brand) simultaneously | 40-60% timeline compression vs sequential |
| **Dev↔QA loop** | Implement → Evidence Collector tests → PASS/FAIL → loop back | 3-attempt max; catches ~95% of defects pre-integration |
| **Evidence-based gates** | No phase advances without proof (screenshots, test output) | Kills "fantasy approvals" (A+ with no evidence) |
| **Standardized handoffs** | Fixed context-continuity format at every boundary | Multi-agent projects fail at handoffs 73% of the time without this |
| **Reality Checker default = NEEDS WORK** | Final certifier requires overwhelming evidence to say READY | Prevents premature production deployment |
| **3 modes** | Full (all agents, 12-24wk) / Sprint (15-25, 2-6wk) / Micro (5-10, 1-5d) | Right-sized orchestration per task |

**Hermes equivalent:** `delegate_task` (parallel subagents, bounded by `delegation.max_concurrent_children`) replaces the manual "spawn agent" calls in the playbooks. The **Dev↔QA loop** and **evidence gates** map to `testing-reality-checker`-style review plus KlickSmartAI's "verify the artifact, don't trust the self-report" rule.

---

## 5. Using this to BUILD agents in Hermes

Combine this framework with the `agent-factory` skill (`~/.hermes/skills/autonomous-ai-agents/agent-factory/SKILL.md`), which uses an **Architect → Fabricate → Govern** workflow:

1. **Architect** — pick a role from the roster or write a new one using the template in §2. Decide model per task weight (reasoning/deep vs task-execution vs creative).
2. **Fabricate** — audit `skills_list`, curate the 10-25 skills the agent actually needs (noise reduction). Generate a `config.yaml` override + `skills.json`.
3. **Govern** — write a strict `SOUL.md` using the §3 format, with a permissions matrix (autonomous / draft-for-review / escalate).

Deploy to `~/.hermes/agents/<name>/` (config.yaml + SOUL.md + skills.json). Verify with a "Turing test" — a complex task, confirming it honors its SOUL constraints and uses its curated tools.

---

## 6. Most reusable reference files in the clone

| Path (`~/wiki/agency-agents/`) | What it gives you |
|------------------------------|-------------------|
| `specialized/agents-orchestrator.md` | Full orchestration pipeline (spec→PM→Architect→Dev↔QA→Reality Checker) |
| `strategy/coordination/agent-activation-prompts.md` | Ready-to-paste prompts per role |
| `strategy/coordination/handoff-templates.md` | Standardized handoff/QA/escalation formats |
| `strategy/playbooks/phase-0..6.md` | Phase-by-phase activation sequences |
| `strategy/runbooks/scenario-*.md` | MVP, enterprise-feature, campaign, incident scenarios |
| `hermes-ai-agency/` | SOUL.md / PROFILE.md / AGENTS.md operational vault |
| `examples/nexus-spatial-discovery.md` | 8-division parallel deployment worked example |
| `specialized/agentic-identity-trust.md` | Agent identity/auth/audit design |
| `specialized/specialized-mcp-builder.md` | Building MCP servers to extend agents |

---

## 7. Governance note

This is a **reference framework**, not an installed Hermes plugin — the earlier "enable agency-agents-router plugin" request was based on a misremembering; no such plugin exists. To use it, either read files directly from the clone or copy the template/SOUL patterns into new agent definitions per §5. No code install required.
