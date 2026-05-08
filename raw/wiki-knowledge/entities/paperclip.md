---
title: Paperclip.ing
created: 2026-04-17
updated: 2026-04-17
type: reference_model
tags: [paperclip, autonomous-company, agent-orchestration, business-model, inspiration]
url: https://paperclip.ing
pricing: Open source (self-hosted), SaaS offering
github: https://github.com/paperclip-ui/paperclip
---

# Paperclip.ing — Reference Model for KlickSmartAI

## What It Is

**Paperclip.ing** is "the human control plane for AI labor." It lets you run an autonomous company where you (the human) act as CEO — hiring agents, setting goals, approving work, and monitoring budgets. Agents wake on heartbeats, execute tasks, and route delegation up/down the org chart.

**Tagline:** "Hire AI employees, set goals, automate jobs and your business runs itself."

**Quote:** *"The shift from 'I am prompting an AI' to 'I am managing a team' changes how you think about what."* — yashns1

---

## Core Product Features

### 1. Org Chart
- Hierarchical structure: CEO → CTO → COO → CMO → individual contributors
- Each agent has a boss, title, job description
- Reporting lines and delegation flows

### 2. Goal Alignment
- Every task traces back to the company mission
- Company goal → Project goal → Agent goal → Task
- Agents know what to do and why

### 3. Heartbeats
- Agents wake on a schedule (e.g., every 4 hours)
- Check work, act, report back
- Delegation flows up and down automatically

### 4. Cost Control
- Monthly budgets per agent
- Agents stop when budget is hit
- No runaway costs

### 5. Governance (Human in the Loop)
- You're the board
- Approve hires, override strategy, pause or terminate any agent

### 6. Bring Your Own Agent
- Any agent, any runtime
- Works with: OpenClaw, Claude, Codex, Cursor, Bash, HTTP
- If it can receive a heartbeat, it's hired

### 7. Ticket System
- Every conversation traced
- Every decision explained
- Full tool-call tracing and audit log

### 8. Multi-Company
- One deployment, many companies
- Complete data isolation
- One control plane for your portfolio

---

## How It Works

```
1. Define the goal
   "Build the #1 AI note-taking app to $1M MRR."

2. Hire the team
   CEO, CTO, engineers, designers, marketers —
   any bot, any provider.

3. Approve and run
   Review the CEO's strategy.
   Set budgets. Hit go.
   Monitor from the dashboard.
```

---

## Why This Is the Model for KlickSmartAI

| Paperclip.ing | KlickSmartAI Implementation |
|---|---|
| Org chart | Client divisions: Finance, Legal, Sales, Marketing, Engineering |
| Goal alignment | Klick2Client OS delivery methodology |
| Heartbeats | Hermes cron jobs (daily 6AM PT, 15-min inbox sweeps) |
| Cost control | Self-hosted stack = $0 marginal cost per client |
| Human governance | Dennis = Chief of Staff, human-in-the-loop on all decisions |
| Bring your own agent | The Agency (147 MIT-licensed agents) + custom agents |
| Ticket system | Hermes session tracking + Google Sheets task management |
| Multi-company | Each client engagement = separate agent configuration |

---

## KlickSmartAI as the Self-Hosted Version

| Paperclip.ing (Funded Startup) | KlickSmartAI (Dennis's Build) |
|---|---|
| Hosted SaaS | Self-hosted on WSL/Ollama |
| Monthly subscription | One-time methodology |
| Closed source | Open agents (MIT) |
| Scales through funding | Scales through methodology |
| Vendor lock-in | Full ownership |

---

## Key Quote for Selling KlickSmartAI

> *"The shift from 'I am prompting an AI' to 'I am managing a team' changes how you think about what."*

This is the pitch. You're not selling AI tools. You're selling **an AI workforce that runs like a company.**

---

## Next Step

See: [[agency-agents]] for the agent workforce (MIT-licensed)
See: [[klick2client-os]] for the delivery methodology
See: [[hermes-agent]] for the orchestration layer

## Related
- [[klick2client-os]] — Dennis's operating system for AI consulting
- [[agency-agents]] — 147 MIT-licensed specialist agents
- [[hermes-agent]] — Nous Research AI agent (orchestration layer)
