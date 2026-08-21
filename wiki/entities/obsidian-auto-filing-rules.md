---
title: "Obsidian Auto-Filing Rules — KlickSmartAI Wiki"
type: reference
tags:
  - obsidian
  - vault-config
last_updated: "2026-04-19"
---

# Obsidian Auto-Filing Rules

Setup: QuickAdd + Auto Note Mover. Apply tags to any note → it moves itself.

---

## Auto Note Mover Rules

| Trigger Tag | Destination Folder | Note Type |
|-------------|-------------------|-----------|
| `#entity` | `entities/` | company, tool, person, platform |
| `#concept` | `concepts/` | framework, playbook, method, process |
| `#raw` | `raw/drafts/` | unprocessed source documents |
| `#template` | `templates/` | reusable templates |
| `#project` | *(root — manually filed)* | project tracking |
| `#meeting` | *(root — manually filed)* | meeting notes |
| `#agent` | `agency-agents/` | AI agent specs and tests |

> **Note:** Tags are **case-sensitive**. `#Entity` and `#entity` are different. Always use lowercase for Auto Note Mover triggers.

---

## QuickAdd Commands to Create

| Command Name | Template File | Destination |
|-------------|--------------|-------------|
| `New Entity Note` | `templates/entity-template.md` | `entities/` |
| `New Concept Note` | `templates/concept-template.md` | `concepts/` |
| `New Raw Doc Note` | `templates/raw-template.md` | `raw/drafts/` |
| `New Project Note` | `templates/project-template.md` | *(root)* |
| `New Meeting Notes` | `templates/meeting-notes-template.md` | *(root)* |

---

## Frontmatter Schema Summary

### `entities/`
```yaml
type: entity
category: company | tool | person | platform | service
url:
pricing:
status: active | inactive | exploring | deprecated
tags: [entity]
related: []
```

### `concepts/`
```yaml
type: concept
domain: sales | marketing | ops | recruiting | engineering | finance | legal
source:
status: draft | active | archived
tags: [concept]
related: []
```

### `raw/drafts/`
```yaml
type: raw
source_type: docx | pdf | transcript | notes | draft | reference
project:
status: raw | processed | archived
tags: [raw]
related: []
```

### `projects/`
```yaml
type: project
project: gpc-development | wattbricks | wealth-wire-radar | hubert-x | klick2client-os
status: exploring | active | paused | complete
priority: P1 | P2 | P3
due_date:
tags: [project, project-name]
stakeholders: []
```

---

## Vault Cleanup — Apply After Setup

After QuickAdd + Auto Note Mover are running:

1. Tag existing `entities/` notes with `#entity`
2. Tag existing `concepts/` notes with `#concept`
3. Tag `raw/` notes with `#raw`
4. Move root-level docs to appropriate folders
5. Delete the duplicate `insurance-direct-canada-recruitment-agent.md` in `concepts/`

Auto Note Mover will pick them up and file them.
