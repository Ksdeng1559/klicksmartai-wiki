---
type: CONCEPT
created: 2026-04-16
updated: 2026-04-16
confidence: 0.90
sources: [https://github.com/TheCraigHewitt/hermes-chief-of-staff]
related: [[hermes-agent-setup]], [[chief-of-staff-context-md]], [[cofounder-operating-skills]]
tags: [hermes, chief-of-staff, ai-agent, automation, inbox, tasks, relationships, skills]
status: active
---

# Hermes Chief of Staff OS

A 5-skill system built on top of Hermes Agent that automates the executive assistant layer — inbox, tasks, follow-ups, and daily operating rhythm. Unlike the CEO/sales skills (which are prompt-based for Claude Code sessions), this system runs autonomously on a cron schedule.

## Core Philosophy

> "The Chief of Staff doesn't do the work — you make sure the right work gets done."

Four principles:
1. **Decision Authority Tiers** — Act / Draft / Escalate. Owner defines the boundary once; assistant operates within it.
2. **Canonical Files** — One file per domain. `tasks/current.md` is the only task list. `relationships/current.md` is the only follow-up tracker.
3. **Rhythm Over Reactivity** — Automated sweeps on schedule. Silence when nothing needs attention.
4. **Separation of Planning and Doing** — Task prep happens nightly; owner reviews in the morning. No mid-day reorganization without direction.

## The 5 Skills

### chief-of-staff (orchestrator)
Coordinates the other skills. Three modes:
- **Morning briefing**: tasks + calendar + inbox highlights + follow-ups due today
- **EOD review**: what was done, what carries forward, tomorrow's preview
- **Ad-hoc triage**: surfaces 3 most critical items by urgency × impact × backlog age

### executive-assistant (communications hub)
Runs every 15 minutes during business hours via heartbeat cron.

**Three-tier authority:**
| Tier | Action | Examples |
|------|--------|---------|
| Act | Handle autonomously | Archive newsletters, decline spam, confirm receipts |
| Draft | Prepare, await approval | Client replies, new contact scheduling, commitments |
| Escalate | Surface immediately | Financial, legal, VIP contacts, press |

Returns `HEARTBEAT_OK` when nothing needs attention. Does NOT send follow-up emails (that's relationship-manager's job).

### daily-task-manager (task file)
Maintains `workspace/tasks/current.md` as the single source of truth.

File structure:
```
## Today → ## Next Up → ## Rules → ## Done
(optional: ## Recurring, ## Backlog, ## Recurring Reminders)
```

Rules: never delete Done items, use YYYY-MM-DD dates, prefix CoS-assigned tasks with `[CoS - date]`.

### daily-task-prep (nightly automation)
Runs at 2 AM. Prepares tomorrow's clean list while owner sleeps:
1. Adds weekday recurring tasks
2. Promotes backlog items due tomorrow
3. Advances recurring reminder dates
4. Syncs calendar events (if MCP available)
5. Reorders by: explicit priority → due date → recurring → calendar → other

Returns `HEARTBEAT_OK` if no changes needed.

### relationship-manager (follow-up cadence)
Default cadence: Touch 1 (day 2) → Touch 2 (day 5) → Touch 3 (day 7) → Escalate

Each entry tracks: context, last contact, next follow-up, touch #, status, notes.

After 3 unanswered touches: escalates to owner with task `[CoS] Decision needed: [Name] — 3 attempts, no response`.

Health report format:
```
Overdue (action needed): [Name] — [N days overdue], Touch #[N]
Due this week: [Name] — due [date]
Cold contacts (30+ days): [Name] — last contact [date]
```

## Maturity Levels

| Level | Skills | Setup time | What you get |
|-------|--------|------------|--------------|
| **Level 1 — Personal EA** | executive-assistant + daily-task-manager | 15–20 min | Inbox triage + persistent task list |
| **Level 2 — Founder** | + relationship-manager + daily-task-prep | 30–45 min | Follow-up cadence + nightly prep |
| **Level 3 — Full CoS** | + chief-of-staff orchestrator | 45–60 min | Morning briefings + EOD reviews |

Recommended for cofounders: start at Level 2, add Level 3 when the briefings add value.

## Configuration: CHIEF_OF_STAFF_CONTEXT.md

Single file that all 5 skills read. Key sections:
- Personal details (name, timezone, role, company)
- Communication (email accounts, calendars, tone, escalation channel)
- Authority levels (Act / Draft / Escalate boundaries)
- Work hours (start, end, quiet hours, meeting defaults)
- Tools available (which MCPs are connected)
- Follow-up preferences (cadence, VIP contacts)
- Business context (strategic notes)

Set up once. All skills stay in sync automatically.

## Installation path (Hermes Agent)

Skills live at `~/.hermes/skills/` in WSL. Workspace files at wherever you configure.

See [[hermes-agent-setup]] for full installation context.

## Difference from CEO/sales skills

| | CEO/sales skills | Chief of Staff OS |
|--|------------------|-------------------|
| Invocation | Manual — you trigger in Claude Code | Autonomous — cron runs on schedule |
| Frequency | On-demand | Continuous (every 15 min + nightly) |
| Platform | Claude Code / any AI | Hermes Agent specifically |
| Scope | Decision support, strategy | Operational execution layer |

Both complement each other: CEO/sales skills for thinking and decision-making, CoS OS for the execution and communication layer.
