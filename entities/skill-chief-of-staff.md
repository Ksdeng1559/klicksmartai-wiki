---
title: chief-of-staff-briefing (skill)
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, skill, briefing, chief-of-staff, daily, hitl]
sources: []
confidence: high
---

# chief-of-staff-briefing (skill)

**Fourth-most-loaded skill (99 uses).** Daily Chief of Staff routine —
morning briefing doc, daily task prep, HITL outreach briefings, EOD inbox
sweep, cron HITL audit.

## Trigger
- `morning briefing`, `daily briefing`, `chief-of-staff briefing`
- `daily task prep`, `task enrichment`, `backlog maintenance`
- `end-of-day sweep`, `EOD report`
- Scheduled cron (2 AM daily-task-prep, 7:57 AM briefing, every 15 min
  executive-assistant heartbeat, 9:47 + 14:47 relationship manager, ~6 PM EOD)

## Daily rhythm
| Time | Routine |
|------|---------|
| 2:00 AM | `daily-task-prep` (Section A) → `~/tomorrow-tasks.md` + sheet |
| 7:57 AM | `chief-of-staff` briefing (Section B) → Google Doc + Gmail draft |
| On-demand | HITL outreach scan (Section C) → direct decision briefing |
| Every 15 min (8 AM–9 PM) | `executive-assistant` heartbeat |
| 9:47 + 14:47 | `relationship-manager` follow-up cadence |
| ~6 PM | `executive-assistant` EOD sweep |

## Canonical IDs / paths
- Task sheet: `1gZdR1MdNlCjjHiLE29dML4EeK-y6F56zuf9LcwtzTuQ`
- Drive folder: `1uscboXl45xn6SOrXa9Rc7FeUMa2kJthx`
- Briefing template: `1xwr0fnQhzvVq_Rkf38YUMXaf3IwWOfR1ahvwqctKIrY`
- Relationship tracker: `~/.hermes/relationships/current.md` (canonical,
  fallback `~/wiki/commercial-relationships/`)

## Sections
- **A:** Daily task prep (cron, 2 AM). Empty-tomorrow pivot to "Triage Day"
  structure.
- **B:** Morning briefing (cron, 7:57 AM). Direct Drive + Docs + Gmail pipeline.
- **C:** HITL outreach briefing (on-demand). 3 lines max per item, binary
  APPROVE/REDIRECT.
- **D:** EOD inbox sweep (cron, ~6 PM). 6-bucket classification + bulk archive.
- **E:** Cron HITL audit (unattended). 7-step dual-schema, run-mode decision tree.
- **F:** Afternoon re-verify addendum (same-day second pass; writes separate file).

## Key rules
- Never auto-send. All Gmail output is draft only.
- "Looks good" ≠ approval. Wait for explicit send instruction.
- `[SILENT]` when nothing actionable.
- Verify Gmail draft financial figures — known corruption pattern strips `$`.

## See also
- [[Skill-Google-Workspace]] — primary tool
- [[Entity-Hermes-Webui]] — separate surface; coexists
- [[Gateway-Restart-Procedure]]