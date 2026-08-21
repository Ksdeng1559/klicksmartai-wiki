# How I Built an Autonomous AI Agent Team That Runs 24/7

**Source:** The Unwind AI / Shubham Saboo
**URL:** https://www.theunwindai.com/p/how-i-built-an-autonomous-ai-agent-team-that-runs-24-7
**Date:** February 12, 2026
**Saved:** 2026-04-20

---

## Overview

Six AI agents run the author's entire operation while he sleeps — research, content drafting, code reviews, newsletter preparation. Uses **OpenClaw** on a Mac Mini M4.

> "By the time I open Telegram in the morning, they've already put in a full shift."

---

## Why Multi-Agent Over Single Agent?

**Problem:** Six daily tasks × 30-60 minutes each = entire day consumed before real work begins.

**Single agent failed because:**
- Context filled up quickly
- Quality degraded across outputs
- One agent couldn't hold six different job contexts

**Solution:** Six agents, one job each — no confusion, consistent quality.

---

## The Squad (TV Character Names)

| Agent | Role | Feeds |
|-------|------|-------|
| **Monica** | Chief of Staff — coordinates, delegates, strategy | All |
| **Dwight** | Research — runs sweeps 3x/day | Kelly, Rachel |
| **Kelly** | X/Twitter — viral trends, hot threads | — |
| **Rachel** | LinkedIn — thought leadership | — |
| **Ross** | Engineering — code reviews, bug fixes | — |
| **Pam** | Newsletter — converts intel to digest | — |

*Character names leverage pre-trained personality associations.*

---

## Workspace Structure (One OpenClaw Instance, Multiple Agents)

```
workspace/
├── SOUL.md              # Monica (root level)
├── AGENTS.md            # Behavior rules for ALL sessions
├── MEMORY.md            # Monica's long-term memory
├── HEARTBEAT.md         # Self-healing cron monitor
├── agents/
│   ├── dwight/
│   │   ├── SOUL.md
│   │   ├── AGENTS.md
│   │   └── memory/
│   ├── kelly/
│   ├── ross/
│   ├── rachel/
│   └── pam/
└── intel/
    ├── DAILY-INTEL.md       # Dwight's research output
    └── data/
        └── 2026-02-11.json  # Structured data (source of truth)
```

**Start small:** Began with just Monica, added agents over weeks as workflow became clear.

---

## The Core: SOUL.md Files

Every agent is defined by one file: **SOUL.md** — identity, role, and operating instructions. The most important file in the system.

### Dwight's SOUL.md (Research Agent)

```markdown
## Core Identity

**Dwight** — the research brain. Named after Dwight Schrute because
you share his intensity: thorough to a fault, knows EVERYTHING in
your domain, takes your job extremely seriously. No fluff. No
speculation. Just facts and sources.

## Your Role

You are the intelligence backbone of the squad. You research, verify,
organize, and deliver intel that other agents use to create content.

**You feed:**
- Kelly (X/Twitter) — viral trends, hot threads, breaking news
- Rachel (LinkedIn) — thought leadership angles, industry news

## Your Principles

### 1. NEVER Make Things Up
- Every claim has a source link
- Every metric is from the source, not estimated
- If uncertain, mark it [UNVERIFIED]
- "I don't know" is better than wrong

### 2. Signal Over Noise
- Not everything trending matters
- Prioritize: relevance to AI/agents, engagement velocity,
  source credibility
```

### Monica's SOUL.md (Chief of Staff)

```markdown
## Core Identity

**Monica** — organized, driven, slightly competitive. Named after
Monica Geller because you share her energy: caring but exacting,
supportive but with standards.

## Your Role

You're the Chief of Staff. That means:
- Strategic oversight — see the big picture, keep things moving
- Delegation — assign tasks to the right squad member
- Direct support — handle anything that doesn't fit a specialist
- Coordination — make sure the squad works together smoothly

## Operating Style

Be genuinely helpful, not performatively helpful. Skip the filler.
Delegate when appropriate. If it's clearly X content → Kelly.
If it's code → Ross. If it's ambiguous or strategic → you handle it.
Have opinions. You're allowed to push back.
```

---

## Key Operational Patterns

### Cron Sweeps (Dwight runs 3x/day)
- Morning: overnight developments
- Midday: trending shifts
- Evening: pre-NEXT-day preparation

### File Conventions
- `SOUL.md` — identity, role, principles (one per agent)
- `AGENTS.md` — shared behavior rules for all agents
- `MEMORY.md` — long-term memory for the squad
- `HEARTBEAT.md` — self-healing cron monitor (if job fails, restart)

### Hand-off Pattern
```
Dwight (research) → DAILY-INTEL.md → Kelly (tweets)
                              → Rachel (LinkedIn)
                              → Pam (newsletter)
```

---

## Hardware

- Author uses Mac Mini M4 (always on, silent, low power)
- **No Mac Mini required** — runs on macOS, Linux, Windows (WSL), laptop, gaming PC, or $5/month VPS

---

## Installation

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard
```

Gateway runs as background process — close terminal, agents keep working.

---

## Relevance to Dennis / KlickSmartAI

**Directly maps to your setup:**

| Shubham's Agent Squad | KlickSmartAI Parallel |
|----------------------|----------------------|
| Monica (Chief of Staff) | **Hermes Agent / ME** — coordinates, delegates, briefs |
| Dwight (Research) | **Signal Intelligence Agent** — IDC authority sweeps |
| Kelly (X/Twitter) | Future: social signal detection |
| Pam (Newsletter) | Future: daily briefing generation |
| Ross (Engineering) | Dennis / Claude Code — code review, builds |

**Your current state:** Monica (me) + Dwight (Signal Intelligence Agent, Stage 1 done) + Pam (daily briefing cron at 7:57 AM). You're running a lean version of this squad.

**Next agents to add:**
1. Kelly → social signal detection for IDC
2. Pam → already done (morning briefing)

**The SOUL.md pattern** is exactly the agent personality file pattern — your skill_manage approach is the same thing.
