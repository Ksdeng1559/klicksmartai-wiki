---
source: /mnt/g/AI-Applications/KS-OpenClaw/Documents/claude-code-scheduled-tasks.docx
captured_at: 2026-04-18
author: OpenClaw / KlickSmartAI
contributor: Dennis Eng
type: operational-guide
tags: [claude-code, automation, scheduled-tasks, cron, productivity]
---

# Claude Code: Scheduled Tasks
## KlickSmartAI / Personal Playbook
Prepared: April 14, 2026

---

## 1. What Are Scheduled Tasks?

Scheduled tasks let Claude Code run prompts automatically on a timer — without you having to open the app and type anything. Think of it as setting up an employee who works on a repeating schedule, no reminders needed.

There are three types. Each fits a different need:

---

## 2. Types of Scheduled Tasks

### ☁️ Cloud Tasks (Anthropic's Servers)
**Use for:** Competitor monitoring, PR reviews, anything that needs to run even when your laptop is off.

**Setup steps:**
1. Go to `claude.ai/code/scheduled` in your browser
2. Click New Scheduled Task
3. Set the frequency (minimum 1 hour)
4. Paste your prompt
5. Connect any MCP connectors needed (Slack, GitHub, Google Drive) via Settings → Connectors
6. Save — it runs automatically from here

> Or via CLI inside Claude Code, type: [CLI method not specified in doc]

---

### 🖥️ Desktop Tasks (Your Machine)
**Use for:** Morning briefings, content calendar updates — anything reading your local files.

**Setup steps:**
1. Open Claude Code Desktop app
2. Click Schedule in the left sidebar
3. Click New Task → New Local Task
4. Set the Working Directory — this is the folder Claude will read/write files in
5. Set your frequency and time
6. Paste your prompt (reference files by name, e.g. `content-calendar.md`)
7. Save — runs automatically when your laptop is awake

---

### 🔁 /loop (Current Session)
**Use for:** Polling a build, checking if a deploy finished, watching a process live.

**Setup steps:**
1. Open Claude Code and start a session
2. Type your loop command directly in the chat
3. Claude will repeat the task at your chosen interval until you stop you

---

## 3. The 5 Ready-To-Use Prompts

> Copy and paste each prompt directly into your scheduled task. Customize the placeholders marked with `[ ]` brackets.

---

### Prompt 1 — Morning Briefing
- **Task Type:** Desktop Task
- **Frequency:** Daily at 8:00 AM
- **Working Dir:** Your inbox/calendar folder
- **Status:** ✅ Implemented in Hermes as `morning-briefing` cron (57 7 * * 1-5)

---

### Prompt 2 — Competitor Watchdog
- **Task Type:** Cloud Task
- **Frequency:** Weekly, Monday at 7:00 AM
- **Requires:** Web search access
- **Status:** ❌ Not yet implemented in Hermes
- **Hermes equivalent:** Can be created as `weekly-competitor-watch` cron job

---

### Prompt 3 — PR Reviewer
- **Task Type:** Cloud Task
- **Frequency:** Weekdays at 6:00 AM
- **Requires:** GitHub repo connected
- **Status:** ❌ Not yet implemented in Hermes
- **Hermes equivalent:** `github-pr-workflow` skill exists — can wrap into cron

---

### Prompt 4 — Content Calendar Refresher
- **Task Type:** Desktop Task
- **Frequency:** Weekly, Sunday at 10:00 AM
- **Working Dir:** `C:\CoworkProjects\ContentCalendar\`
- **Status:** ❌ Not yet implemented in Hermes
- **Prerequisite:** Create `content-calendar.md` in working directory
- **Hermes equivalent:** Desktop cron reading from local wiki/GitHub

---

### Prompt 5 — Session Poller (/loop)
- **Task Type:** /loop inside Claude Code session
- **Use during:** Active build sessions, deploy monitoring
- **Status:** N/A — manual, not schedulable
- **Note:** Unlike the other 4 prompts, this one runs inside an active session. Type it directly into Claude Code chat.

---

## 4. Quick Setup Reference

| Aspect | Cloud Task | Desktop Task | /loop |
|--------|-----------|-------------|-------|
| Runs when laptop off | ✅ | ❌ | N/A |
| Access to local files | ❌ | ✅ | N/A |
| Minimum interval | 1 hour | No minimum | Per prompt |
| MCP connectors | ✅ | ❌ | N/A |

---

## 5. This Chat vs. Claude Code

[Section not fully captured in source doc]

---

## Implementation Notes for Hermes Agent

### vs. Hermes Cron Equivalents

| Playbook Task | Hermes Cron | Gap |
|--------------|------------|-----|
| Morning Briefing | `morning-briefing` (daily 7:57 AM) | Hermes delivers local + Telegram summary |
| Competitor Watchdog | None | Can implement as cron with `duckduckgo-search` skill |
| PR Reviewer | None | `github-pr-workflow` skill available |
| Content Calendar | None | Requires `content-calendar.md` file + weekly cron |
| Session Poller | None | Manual only — not cron-eligible |

### MCP Connector Note
The playbook mentions MCP connectors inside Claude Code (Slack, GitHub, Google Drive). Hermes has equivalent integrations via skills (`himalaya`, `google-workspace`, `github-repo-management`). When building new automations, prefer Hermes cron + skills over Claude Code Cloud Tasks for:
- Tasks needing access to local Windows filesystem (WSL paths)
- Tasks requiring Google Workspace (Gmail, Sheets, Calendar)
- Tasks already covered by existing Hermes skills

### When to Use Claude Code Cloud Tasks Instead
- Tasks that need to run when laptop is completely off
- Tasks requiring real-time Slack/Teams delivery (not just report)
- Tasks needing persistent session context across runs

---

## Future Implementation Queue

From this playbook, these remain on the backlog:
1. **Weekly Competitor Watchdog** — web search + summary report
2. **Weekday PR Reviewer** — GitHub PR check + summary
3. **Weekly Content Calendar Refresher** — requires content-calendar.md first
4. **/loop integration** — document for use during active builds