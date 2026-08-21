# Obsidian — Home Lab & Self-Hosted Services Documentation

**Source:** [XDA Developers — "I use Obsidian to document my home lab and self-hosted services"](https://www.xda-developers.com/use-obsidian-document-home-lab-self-hosted-services/)  
**Author:** Adam Conway · Published Jun 21, 2025

---

## Core Philosophy

> "Obsidian isn't just a note-taker, which is why it's perfect for this project. With an incredible array of plugins, you can turn what would otherwise be a collection of notes into a full-on database."

The key insight: Obsidian becomes a **typed inventory database** through YAML frontmatter properties, not just a folder of markdown files.

---

## Folder Structure

```
0 - Meta/
    Templates/           ← note templates for each type
1 - Hardware/
    Network devices/     ← routers, switches, APs
    Servers/             ← hypervisors, bare metal
2 - Services/            ← all self-hosted services
3 - Automation/          ← Home Assistant, OPNsense rules, Backblaze B2
4 - Incidents/           ← crash logs, problem history
5 - Notes/               ← daily notes, changelogs
6 - Design/              ← Excalidraw network diagrams
```

**Naming convention:** Numbered prefixes force folder sort order. `1 - Hardware` always appears before `2 - Services`.

---

## YAML Properties (Frontmatter) — The Core Structure

Every note type has a typed schema. Example — server:

```yaml
---
type: server
hostname: "{{title}}"
role:
os:
ip:
mac:
cpu:
ram_gb:
disk_tb:
rack_u:
location: "{{location}}"
production: false
last_update: ""
tags:
  - server
---
```

**Property types used:**
- `type` — classifies the note (server, service, network-device, incident)
- `hostname` / `role` / `os` — server identity
- `ip` / `mac` — connection details
- `cpu` / `ram_gb` / `disk_tb` — hardware specs
- `location` — physical location
- `production` — boolean, marks live services
- `affected` — (incidents) links to affected service/server
- `tags` — Obsidian tag for filtering

---

## Dataview Queries — Live Tables from Properties

Dataview reads frontmatter and builds dynamic tables. Examples:

**Server inventory table:**
```dataview
TABLE WITHOUT ID file.link AS "File", hostname AS "Host", ip AS "IP", os AS "OS", last_update AS "Last updated"
FROM "1 - Hardware/Servers"
WHERE type = "server"
SORT hostname
```

**All pending tasks across services:**
```dataview
TABLE WITHOUT ID file.link AS "File", t.text AS "Task"
FROM "1 - Hardware" OR "2 - Services"
FLATTEN file.tasks AS t
WHERE !t.completed
SORT name, t.text
```
→ Dynamically shows every unchecked task across all servers and services. Clicking the file jumps to the note. Tasks auto-remove when checked off.

**Incidents affecting a service (via `affected` link):**
```dataview
TABLE WHERE affected = [[ServiceName]]
```
→ Shows all incidents tagged to a specific service.

---

## Plugins Used

| Plugin | Purpose |
|--------|---------|
| **Dataview** | Query frontmatter → live tables |
| **Excalidraw** | Network diagram drawing |
| **Advanced Tables** | Nicely formatted markdown tables |
| **Properties** | Core Obsidian plugin for typed frontmatter fields |
| **Backlinks** | Core Obsidian — links between related notes |
| **Templater** *(planned migration)* | Raise prompts for properties before creating note (replaces `{{title}}` variables) |

---

## Incidents Log

Tracks server crashes / problems with:
- Crash details and logs
- Timestamp
- `affected` property linking to the impacted server or service
- Use case: compare recurring crashes to identify patterns

---

## Automation Tracking

- Home Assistant automations (most important ones)
- OPNsense IP list auto-updates
- Backblaze B2 backup configs

---

## Why Obsidian Over Alternatives

Author tried **NetBox** and **HomeBox** — found them "too over-the-top." Obsidian wins because:
- Simple (plain Markdown underneath)
- Syncs anywhere
- Lives alongside other notes (not siloed)
- Fully customizable schema

---

## QuickStart for This Setup

1. Create numbered folders: `1 - Hardware/`, `2 - Services/`, etc.
2. Create template files for each note type (server, service, network device, incident)
3. Add typed frontmatter to each template
4. Enable Dataview plugin
5. Write your first Dataview query to populate a dashboard table
6. Add Excalidraw diagrams to `6 - Design/` for network topology

---

## Related

- [[obsidian-self-organizing-vault]] — Nolen Jonker's QuickAdd + Auto Note Mover + Claude self-organization system
- [[obsidian]] — Dennis's vault location and config
