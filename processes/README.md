# Processes Index

The operating systems and runbooks that govern KlickSmartAI's core operations.

| Process | Type | Last updated | Owner |
|---|---|---|---|
| [SEO Client Onboarding Sprint](seo-client-onboarding-sprint.md) | SEO engagement runbook | 2026-08-26 | Dennis + Hermes |
| [LeadSniperAI CLI — Signal-Based Cold Email OS](lead-sniperai-cli-os.md) | Outbound operating system | 2026-08-23 | Dennis |
| [Honcho Multi-Agent Wiring](honcho-multi-agent-wiring.md) | Cross-LLM memory architecture | (check file) | Dennis + Hermes |
| [Wiki Sync Pipeline](wiki-sync-pipeline.md) | Obsidian ↔ wiki bidirectional sync | (check file) | Dennis |
| [Content Growth Strategies](content-growth-strategies.md) | Content marketing patterns | (check file) | Dennis |

## How to use this folder

- **New client?** Start with `seo-client-onboarding-sprint.md` (if SEO) or `lead-sniperai-cli-os.md` (if outbound).
- **Building a skill?** Use `workflow-pattern-architect` as the meta-skill to translate patterns.
- **Documenting an existing skill?** Match the style in `lead-sniperai-cli-os.md` (frontmatter + executive summary + numbered sections).
- **Editing an existing process?** Update both the markdown doc AND any linked skills (in `~/.hermes/skills/`) — they're paired.

## Pairing convention

Every process doc in this folder has a corresponding skill in `~/.hermes/skills/`. The skill is the **runnable pattern**; the doc is the **human-readable explanation**. Update both together.

| Doc | Skill |
|---|---|
| seo-client-onboarding-sprint.md | client-onboarding-sprint |
| lead-sniperai-cli-os.md | (research/lead-sniper-ai-cli) |
| honcho-multi-agent-wiring.md | honcho-* skills |
| wiki-sync-pipeline.md | wiki-graphify-sync |
| content-growth-strategies.md | (no paired skill yet) |

## Adding a new process

1. Pick a domain or pattern that needs documenting
2. Write the doc in this folder (frontmatter + executive summary + numbered sections)
3. Write the runnable skill in `~/.hermes/skills/<name>/SKILL.md`
4. Add a row to this index
5. Commit both to the wiki git repo

The pattern is: docs explain **why** + **what**; skills explain **how**.
