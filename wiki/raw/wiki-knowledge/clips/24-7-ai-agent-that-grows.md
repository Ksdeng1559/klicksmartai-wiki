# How to Run a 24/7 AI Agent that Grows with You

**Source:** The Unwind AI / Shubham Saboo
**URL:** https://www.theunwindai.com/p/how-to-run-a-24-7-ai-agent-that-grows-with-you
**Date:** April 14, 2026
**Saved:** 2026-04-20

---

## The Problem

Running six agents on OpenClaw — constantly updating SOUL.md files, pruning stale memory, repeating same corrections. Agents weren't getting better. The author was getting better at managing them.

> "Most agents can store context. Far fewer can turn completed work into reusable method."

---

## OpenClaw vs Hermes Agent — Parallel Test

| System | Monica's Role | Learning Loop Owner |
|--------|---------------|---------------------|
| OpenClaw Monica | Research, content drafting | Both (author + agent) |
| Hermes Monica | Chief of staff | Agent (more autonomous) |

### Key Difference

| OpenClaw Monica | Hermes Monica |
|-----------------|---------------|
| Improves when author notices problem and teaches fix | Closes more of the loop herself |
| Stores what is explicitly taught | Turns finished work into future procedure |
| Depends on both author + agent | Author can inspect, edit, or delete — but doesn't have to initiate |

---

## What Made Hermes Different

### 1. Self-Generated Skills

Agent wrote files the author didn't create. Example: `local-writing-canon-analysis/SKILL.md` — captured editorial rules from completed work:
- Keep the compounding thesis
- Avoid framing new topics as product comparisons
- Center pieces on outcomes like memory and reuse

> "The default behavior, turning completed work into reusable procedure, was new."

### 2. Intelligent Recall

Hermes surfaced exact troubleshooting arc from weeks-old conversation — nobody manually promoted it into memory.

### 3. Self-Maintenance Example

After a Telegram gateway failure, Monica: hit the problem → solved it → wrote the playbook herself.

Generated skill: `autonomous-ai-agents/hermes-telegram-gateway-recovery/SKILL.md`

> "Mistake goes in. Procedure comes out."

---

## What Still Breaks

1. **Hallucinated Confidence** — Agent inferred completeness from partial data and moved forward with unearned confidence
2. **Status Screen Deception** — "launchd said the service was running. The live responder was dead. Status screens flatter you. Logs tell the truth."
3. **Variable Skill Quality** — Some generated skills were too generic, captured wrong abstraction level

> "Agents still hallucinate confidence. Self-improvement is not self-verification."

---

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
```

- Detects OpenClaw on Mac Mini, offers to import settings
- Walks through Telegram BotFather setup
- Tip: Use a frontier model — the learning loop needs strong reasoning

---

## Key Lessons

| Lesson | Application |
|--------|-------------|
| Self-generated procedures | Let agent write its own SKILL.md files from completed work |
| Logs > status screens | Verify health via logs, not status indicators |
| Self-improvement ≠ self-verification | Human review still needed to catch hallucinated confidence |
| Agents that grow themselves | The goal is to close more of the learning loop autonomously |

---

## Relevance to Dennis

Dennis already runs Hermes Agent (me). Key takeaways:
- My skill_manage pattern aligns with "mistake goes in, procedure comes out"
- My log-based verification is correct (not just status checks)
- Self-generated skills = the autonomous maintenance loop Shubham describes
- Dennis's role is to review/approve, not initiate every correction
