# HERMES AGENT — MISSION CONTROL
## Multi-Tenant Operations Guide

---

## Overview

Hermes Agent is the AI operations system for running outreach campaigns on behalf of multiple clients. Mission Control is the command center for that system.

**Core principle:** Every client gets an isolated Project Folder. Every agent run, wiki file, and company record lives inside it. Agents never cross project boundaries.

If Hermes Agent is the engine, Mission Control is the cockpit.

**Built for:**
- Managing multiple client campaigns simultaneously
- Running agents with full client context loaded
- Keeping every company record isolated per client
- Chat and Cowork sessions scoped to a project
- Spawning ad-hoc agents against a project
- Scheduling recurring outreach without manual triggers
- Tracking outputs, replies, and pipeline status per client
- Operating as a system, not a one-off tool

---

## 1. Project Folders

The foundation of multi-tenant operations. One folder per client. Every agent run, wiki file, and company record lives inside it.

### Creating a Project Folder

On onboarding a new client, create their Project Folder first. Define:
- Client name (used as folder name)
- Vertical (HVAC, plumbing, pest control, cleaning, electrical, multi-vertical)
- Target geography (city or region)
- Output directory path
- Assigned agents (typically all 8, plus optional chat/cowork/spawn)
- Slack channel for hot-lead alerts
- Cal.com link for booking discovery calls

Project Folders are isolated. No shared wiki files. No cross-contamination.

### Folder Structure

```
~/.hermes/projects/
  ├── klicksmart-ai/              ← own pipeline
  ├── client-a-hvac/              ← first paying client
  ├── client-b-plumbing/          ← second paying client
  └── client-c-multivertical/     ← third paying client
```

Inside each Project Folder:

```
<project>/
  ├── wiki/
  │   ├── soul.md                 ← brand voice
  │   ├── user.md                 ← client profile
  │   ├── agents.md               ← agent roster + prompts
  │   ├── icp.md                  ← ideal customer profile
  │   └── companies/              ← one file per business touched
  ├── inputs/                     ← CSVs, lead lists, drop zones
  ├── outputs/                    ← generated artifacts
  ├── logs/                       ← timestamped run logs
  ├── chat/                       ← chat session transcripts
  ├── cowork/                     ← cowork artifacts + state
  └── spawn/                      ← ad-hoc spawned agent runs
```

### Project Dashboard

Each Project Folder gives you visibility into:
- Active agent runs (scheduled + spawn)
- Active chat and cowork sessions
- Scheduled jobs and next run times
- Recent run history (last 24h, 7d, 30d)
- Output artifacts by type
- Companies touched this week
- Hot leads awaiting follow-up
- Slack channel and Cal.com link

---

## 2. Wiki Files

The memory of each project. Every agent — scheduled, chat, cowork, or spawned — loads the wiki files for its assigned project before every task. This is what makes each campaign feel custom-built for that client.

### The Four Files

**soul.md** — Brand voice, operating principles, forbidden word list. Controls tone across every email AGT-006 writes for this campaign.

**user.md** — Client profile: goals, preferences, prior attempts, what to avoid. Agents use this to write outputs the client will actually approve.

**agents.md** — Agent roster, system prompts, email templates, company write-back format. One copy per project. Customized per vertical.

**icp.md** — Ideal Customer Profile: target size, rating thresholds, geographic scope, AI gap indicators. AGT-002 and AGT-005 reference this on every run.

### Updating Wiki Files

Updates happen at the project level, never globally. A change to `icp.md` in `client-a-hvac` does not affect `client-b-plumbing`. Review each project's wiki files monthly. Agents inherit changes on the next run.

### File Size Rule

All wiki files stay under 350 lines. Context bloat slows agents and increases cost. Files exceeding 350 lines get split into focused reference files.

---

## 3. Agents

Defined in each project's `agents.md`. Each agent has one job. Assignment is deliberate.

### The 8-Agent Roster (Phase 1)

| Agent | Role |
|-------|------|
| AGT-001 | Orchestrator — reads lead list, checks companies folder, dispatches downstream agents, skips contacted |
| AGT-002 | GMB Scout — pulls GMB data, classifies against icp.md, flags AI gap signals |
| AGT-003 | Web Auditor — structured website audit, scores contact forms/booking/mobile/AI gap density, creates company file |
| AGT-004 | Review Intel — reads 10–20 recent GMB reviews, extracts sharpest personalization insight |
| AGT-005 | Pattern Match — classifies into 1 of 5 patterns, selects matching email template |
| AGT-006 | Email Forge — writes cold email under 120 words, validates against soul.md |
| AGT-007 | Reply Watch — monitors Smartlead, classifies intent, fires Slack alert for hot leads |
| AGT-008 | Morning Brief — runs 7:30 AM PT, posts pipeline status to Slack, pure reporting |

### Assignment Per Project

Each project defines its own agent assignments in `agents.md`. Most projects use all 8. A minimal campaign might skip AGT-004. The loadout is per-project — never shared.

---

## 4. Interaction Modes

Three modes for working against a project. All are project-scoped, all load the same wiki files, all write to the same outputs and logs.

### Chat Session

A persistent, multi-turn conversation with a project-aware assistant. The chat knows the project's soul, user, agents, and ICP. Use it for:
- Asking "what's the status of client-a-hvac?"
- Drafting a one-off outreach email that doesn't fit the cold batch
- Investigating why a lead was scored a certain way
- Reviewing and editing a wiki file interactively

Chat sessions are stored in `chat/` and persist across reloads. The full transcript is searchable from Mission Control.

### Cowork

Long-running, multi-step work that crosses agent boundaries. A Cowork session is a goal like "audit the website for the 12 leads in this CSV and produce a comparison report." The session:
- Plans the work upfront (lists the steps)
- Dispatches one or more agents (AGT-002, AGT-003, AGT-005) as needed
- Holds state between steps in `cowork/`
- Surfaces intermediate results for review
- Produces a final deliverable in `outputs/`

Cowork is the right mode when the work doesn't fit a single agent and you want to stay in the loop.

### Agent Spawn

An ad-hoc, one-off agent run triggered from Mission Control. Use Spawn to:
- Re-run AGT-003 on a single company after a website change
- Run AGT-006 with a custom template override for a specific vertical
- Test a new agent prompt against a known input
- Diagnose a failed run by re-running with the same input

Spawned runs are isolated, logged, and stored in `spawn/`. They never touch the scheduled pipeline. They can be promoted into the regular agent roster after they prove out.

### Mode Comparison

| | Chat | Cowork | Spawn |
|---|------|--------|-------|
| Multi-turn | yes | yes | no |
| Multi-agent | no | yes | no |
| Persists state | yes | yes | no |
| Hits outputs/ | optional | yes | yes |
| User review between steps | yes | yes | no |
| Use for | Q&A, drafting | complex tasks | one-off runs |

---

## 5. Most Common Workflows

### Workflow 1: Onboard a New Client

1. Create the project folder under `~/.hermes/projects/`
2. Copy the wiki template (`soul.md`, `user.md`, `agents.md`, `icp.md`)
3. Edit each wiki file for this client: vertical, geography, voice, ICP thresholds
4. Create empty `companies/`, `inputs/`, `outputs/`, `logs/`, `chat/`, `cowork/`, `spawn/` folders
5. Configure agent system prompts in `agents.md` to load this project's wiki files
6. Run a test task with AGT-002 on 3 GMB listings to verify wiki files are loading
7. Confirm company files are being written to the correct `companies/` folder

### Workflow 2: Run a Lead Batch

1. Export a GMB lead list from Lead Sniper AI
2. Drop the CSV into the project's `inputs/` folder
3. Trigger AGT-001 for this project
4. AGT-001 checks `companies/` — skips any already-contacted businesses
5. Remaining leads flow through AGT-002 → AGT-003 → AGT-004 → AGT-005 → AGT-006
6. Emails are loaded into Smartlead for sequencing
7. Review the output log before approving the Smartlead send

**Note:** Never load emails into Smartlead without reviewing the output log first. Check for pattern mismatch, voice drift, and word count.

### Workflow 3: Respond to a Hot Lead

1. AGT-007 detects a reply and classifies it as INTERESTED
2. Slack alert fires to the client's notification channel
3. Open the company file from Mission Control for full context (audit score, pattern, email sent)
4. Open a Chat session against the project and draft a manual reply
5. Send via Smartlead or trigger a follow-up sequence
6. Book a discovery call via Cal.com
7. Update the company file with outcome: booked, declined, or ghosted

### Workflow 4: Review Morning Brief

AGT-008 posts a brief to Slack at 7:30 AM per project. Includes:
- Leads processed since last brief
- Emails sent
- Replies received and classified
- Hot leads awaiting action
- Sequence health (bounces, unsubscribes)

Review the brief before starting work each day. A hot lead listed is the first task.

### Workflow 5: Switch Between Client Projects

Hermes runs multiple projects simultaneously. To switch:
1. In Mission Control, select the target project from the sidebar
2. All wiki context, agent configs, and company records load for that project
3. Chat, Cowork, and Spawn sessions triggered from this view operate within this project only
4. Morning briefs and Slack alerts are already separated by project channel

**Note:** Never trigger a run without confirming the active project first. A misfire writes to the wrong folder.

### Workflow 6: Use Chat for a Quick Task

1. Select the active project
2. Open a Chat session
3. Ask: "Draft a re-engagement email for [Company] referencing their new service line"
4. Chat loads the project wiki files, the company file, and the email templates
5. Review the draft, request edits in-thread
6. Approve and export to `outputs/` or send directly via Smartlead

### Workflow 7: Use Cowork for a Complex Task

1. Select the active project
2. Start a Cowork session with a goal: "Compare audit scores across the 8 leads in this CSV and rank them by fit"
3. Cowork plans: read CSV → run AGT-002 on each → run AGT-003 on each → aggregate → output report
4. Review the plan, approve
5. Watch the steps execute, intervene if any step needs adjustment
6. Final report lands in `outputs/`

### Workflow 8: Spawn an Ad-Hoc Agent Run

1. Select the active project
2. Open Spawn
3. Pick an agent (e.g., AGT-006)
4. Provide a target company file or new input
5. Optionally override the email template
6. Run
7. Output lands in `spawn/` and the company file is updated

---

## 6. Scheduler

Hermes supports recurring automation via scheduled jobs. Each project has its own scheduler.

### Creating a Scheduled Job

Define:
- Project
- Agent to trigger
- Cron expression
- Enabled or disabled state

You can:
- Run immediately for testing
- Enable or disable without deleting
- View next run time
- Review run history per job

The system prevents overlapping runs by default.

### Recommended Schedules

| Job | Cron | When |
|-----|------|------|
| AGT-008 — Morning Brief | `30 7 * * 1-5` | Mon–Fri 7:30 AM PT per project |
| AGT-007 — Reply Watch | `0 * * * *` | Every hour, polls Smartlead |
| Lead Batch Run | `0 9 * * 1` | Mon 9:00 AM PT, AGT-001 on new list in `inputs/` |

---

## 7. Company Records

Every business touched in a campaign gets a record in the project's `companies/` folder. The system of record for who was contacted and what happened.

### What Gets Written

- AGT-003 creates the company file after the web audit
- AGT-006 appends email send data
- AGT-007 appends reply status
- Chat and Cowork sessions can append notes and outcomes

Each file contains:
- Company name, domain, location, vertical
- Assigned business pattern
- GMB rating and review count
- Website audit score and AI gap identified
- Email sent status and template variant used
- Smartlead sequence status
- Reply received and intent classification
- Outcome: booked, declined, ghosted, in-progress

### The Duplicate Gate

AGT-001 reads `companies/` before dispatching any downstream agent. If `email_sent` is true, the company is skipped. Non-negotiable. Protects Smartlead deliverability and CASL compliance.

### Cross-Project Isolation

Company records live inside the project folder. A business contacted for client A is not flagged for client B. Each client's `companies/` folder is fully independent.

---

## 8. Outputs and Logs

Each project has an `outputs/` folder and a `logs/` folder. Chat, Cowork, and Spawn each have their own subfolders.

### Outputs

- Drafted emails (before Smartlead import)
- Website audit reports
- Morning brief archives
- Reply classification summaries
- Chat session exports
- Cowork final deliverables
- Spawn run artifacts

**Do not delete output files.** They are the campaign audit trail.

### Logs

Every agent run — scheduled, chat, cowork, or spawn — writes a timestamped log. Logs record:
- Which agent ran
- Which project it ran against
- Start and end time
- Companies processed
- Errors and skips
- For chat/cowork: token usage and step count

Review logs after every major batch run. Failed writes and pattern mismatches surface first.

---

## 9. Execution Architecture

When any task runs against a project — scheduled, chat, cowork, or spawn:

1. Mission Control triggers the agent or session for the active project
2. Agent loads the project's wiki files (`soul.md`, `user.md`, `agents.md`, `icp.md`)
3. Agent reads the `companies/` folder to check for existing records
4. Agent executes its task and writes outputs to `outputs/` (or `chat/`, `cowork/`, `spawn/`)
5. Run is logged to `logs/` with timestamp and result
6. Company files are updated in `companies/` as needed

All execution is project-scoped. All outputs and logs are tracked. Nothing runs against a client's data without that project's context loaded.

---

## 10. Operational Best Practices

- Keep projects isolated. One client, one folder. No shared wiki files.
- Confirm the active project before triggering any run — scheduled, chat, cowork, or spawn
- Review email outputs before loading into Smartlead
- Check the morning brief before starting work each day
- Respond to hot leads before running new lead batches
- Review logs after every batch run. Errors compound if ignored.
- Update `icp.md` and `soul.md` monthly. Agents inherit changes immediately.
- Keep wiki files under 350 lines. Split if they grow.
- Use the scheduler for anything that runs more than once a week
- Use Chat for ad-hoc drafting, Cowork for multi-step tasks, Spawn for one-off agent runs
- Do not promote a Spawn agent into the roster until it has been run cleanly at least 5 times

Treat Hermes as infrastructure. Not a chat tool.

---

## 11. Mission Control (The New Layer)

Mission Control wraps the entire Hermes system. The command center that turns Hermes from a one-off tool into a true multi-tenant operations system.

**Built for:**
- Visualizing all client projects at once
- Triggering agent runs against a specific project (scheduled, chat, cowork, or spawn)
- Viewing run history, outputs, and logs across all modes
- Managing the scheduler for every project
- Viewing the company records per project
- Providing a single interface to operate the entire system

**Mission Control is the interface for the system. Mission Control is not the system.**

### Architecture

Mission Control is a single-page web application. A thin read/write layer over the existing project folders and the Hermes gateway. It does not host agents. It does not host wiki files.

- **Reads:** project folders + gateway state
- **Writes:** through the gateway for runs and schedules; direct file writes for wiki edits and approval flows
- **Chat/Cowork/Spawn:** the SPA opens a streaming WebSocket to the gateway, which dispatches to the appropriate backend (Hermes chat runtime, cowork orchestrator, or direct agent runner)

### Sections of Mission Control

**1. Project List (Sidebar)**

Lists all project folders under `~/.hermes/projects/`. For each project:
- Client name and vertical
- Hot leads (visible at a glance)
- Companies touched this week
- Last activity timestamp
- Active agent runs (scheduled + spawn + active cowork)
- Status badge: RUNNING / IDLE / ERROR

**2. Active Project Header**

The currently selected project. Always visible. Shows:
- Project name, vertical, geography
- Status badge (RUNNING / IDLE / ERROR)
- Slack channel link
- Cal.com link
- Quick action: New Chat / New Cowork / New Spawn / Open Scheduler

**3. Tabs**

- **Overview** — pipeline status chart, recent run history (across all modes), companies touched this week, hot leads awaiting follow-up, token/cost summary
- **Companies** — list of all company records, search, filter by pattern/AI gap/status, click a company for detail panel (audit, pattern, email, reply, outcome, related chat sessions)
- **Chat** — list of chat sessions for this project, click to open a session, ability to start a new one, full transcript view, export to `outputs/`
- **Cowork** — list of cowork sessions, status (planning / running / awaiting review / complete), click to view plan and step-by-step progress, ability to intervene at any step
- **Spawn** — list of one-off agent runs, click to view inputs/outputs/logs, ability to re-run with same input, promote to scheduled job if it has been run cleanly 5+ times
- **Outputs** — list of output files across all modes, click to preview or download
- **Scheduler** — list of scheduled jobs, for each: project, agent, cron, enabled, next run, run history, run immediately for testing
- **Logs** — list of log files, click to tail in a viewer
- **Wiki** — list of wiki files (`soul.md`, `user.md`, `agents.md`, `icp.md`), click to view/edit in a side panel, file size indicator (warn if >350 lines)

### Interaction Mode Launchers

Three primary buttons in the Active Project Header:
- **New Chat** — opens a chat session against the active project, streams responses
- **New Cowork** — opens a goal input, plans the work, awaits approval, executes
- **New Spawn** — opens an agent picker + input form, runs the agent, shows output

All three are project-scoped. The active project is locked in for the duration of the session.

### Status Visibility

Mission Control surfaces the health of every running thing in real time:
- Scheduled jobs: next run countdown, last run result
- Active spawns: progress bar, current step
- Active cowork: step list with status (pending / running / done / failed)
- Active chats: token usage, message count

---

## 12. What Hermes Enables

You now have:
- Isolated multi-client campaign management
- Persistent agent memory across every run
- Three interaction modes per project: Chat, Cowork, Spawn
- Automatic duplicate prevention via the companies folder
- Pattern-matched, personalized cold emails at scale
- Self-reporting pipeline via AGT-008 morning briefs
- Hot lead alerts without manual monitoring
- Full output and log traceability per client
- A scheduling system that runs campaigns while you sleep
- A single interface to operate the entire system

This is how you move from prompting to operating.

---

## 13. Phase 2 — Voice Response (LiveKit Agents)

**Phase 2 is not part of the initial build. Activate after Phase 1 is stable and generating revenue.**

Phase 2 extends Hermes with a voice layer built on LiveKit Agents. It introduces three new agents (AGT-009, AGT-010, AGT-011) and changes nothing in the Phase 1 system. Wiki files, company records, outputs, logs, scheduler, and Mission Control UI all keep working as designed.

### What LiveKit Agents Does

LiveKit Agents is a Python framework for building real-time voice AI. It connects a phone call to a three-stage pipeline:

- **STT** — speech-to-text converts the caller's voice to text
- **LLM** — the language model reasons and generates a response
- **TTS** — text-to-speech converts the response back to audio

A **VAD** (voice activity detection) model handles turn-taking. Calls are routed via a SIP trunk into a LiveKit room where the agent is already waiting.

### The Three Voice Use Cases

**AGT-009 — Voice Briefing (Phase 2, first build)**

You call in instead of reading the morning brief on Slack. The agent reads your pipeline status aloud: leads processed, emails sent, hot leads waiting. You can ask follow-up questions mid-call.

Example: "Which hot leads came in today?" — it reads from the companies folder live.

This is a two-way voice conversation grounded in real Hermes data.

**AGT-010 — Hot Lead Callback (Phase 2, second build)**

When a prospect calls back after receiving your cold email, this agent answers. It qualifies the call, confirms their interest, gathers availability, and books the Cal.com slot. You receive a Slack alert with the booked time. You never pick up the phone.

**AGT-011 — Outbound Discovery Call (Phase 3 only)**

AGT-001 detects a hot reply and triggers an outbound SIP call to the prospect. The agent introduces KlickSmart AI and walks them through one audit finding.

**Requires regulatory clearance before building. Do not build until Phase 3.**

### Phase 2 Stack

| Component | Choice | Cost |
|-----------|--------|------|
| LiveKit Cloud | Hosted real-time communication + SIP routing | Free tier includes 10,000 min/month |
| SIP Trunk | Twilio or Telnyx | ~$1/month + per-minute rates |
| Deepgram Nova-3 | STT — standard for LiveKit Agents pipelines | ~$0.004/min |
| ElevenLabs or Cartesia | TTS — ElevenLabs for voice quality, Cartesia for latency | $0.15–$0.30 per 1,000 chars |
| Silero VAD | Voice activity detection | Open source, no cost |
| Agent Worker | Python process running the LiveKit agent | Runs on the Hetzner VPS alongside Hermes (no new infra) |

### Estimated Monthly Cost (AGT-009, personal use)

- LiveKit Cloud: free tier
- SIP trunk and phone number: $1
- Deepgram (30 min/month): under $1
- ElevenLabs (10,000 chars/month): under $2
- **Total: under $5/month**

### How AGT-009 Connects to Hermes

The voice agent reads from the same folder structure as all other agents. It loads the morning brief output from `outputs/` at call time. It queries the companies folder via `function_tool` calls mid-conversation. No separate database. No sync layer. Same files, accessed live.

### Phase 2 Build Sequence

1. Phase 1 stable: email pipeline running, first client signed
2. Set up LiveKit Cloud account and configure a SIP trunk
3. Write AGT-009 voice briefing agent in Python
4. Connect to Hermes `outputs/` folder via `function_tool`
5. Test inbound call flow end to end
6. Deploy to Hetzner VPS when that migration occurs
7. Build AGT-010 after AGT-009 is stable in production

### Regulatory Notes for Outbound Voice (AGT-011)

AGT-009 and AGT-010 are inbound or initiated by you. No regulatory issues. AGT-011 is automated outbound. Canadian CRTC Telemarketing Rules apply.

**Before building AGT-011:**

- Calling hours must be 8:00 AM to 9:00 PM local time for the recipient
- Caller identity must be clearly stated at the start of every call
- An opt-out mechanism must be offered and honoured immediately
- Calling a business does not exempt you from these requirements
- Review CASL interaction: automated voice plus prior email to the same prospect requires careful consent mapping

### File Placement

LiveKit Agents uses Python. Keep AGT-009 and AGT-010 in their own files inside the project folder. Do not merge them into existing agent files.

Voice agents do not replace the Phase 1 system. They read from the same `outputs/` and `companies/` folders and write to the same `logs/`. Mission Control's Overview tab adds a "Recent Voice Calls" panel when Phase 2 is enabled. Nothing else in the UI changes for Phase 2.

---

*Hermes Agent — KlickSmart AI — Built on THE SPRINT methodology by Matt Ganzak / ScaleUP Media*
*Automate the pain. Not the shiny features.*
