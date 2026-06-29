<!-- converted from claude-code-scheduled-tasks.docx -->

KLICKSMARTAI  /  PERSONAL PLAYBOOK
Claude Code: Scheduled Tasks
Your step-by-step guide to building automations that run while you sleep.
Prepared: April 14, 2026
# 1. What Are Scheduled Tasks?
Scheduled tasks let Claude Code run prompts automatically on a timer — without you having to open the app and type anything. Think of it as setting up an employee who works on a repeating schedule, no reminders needed.

There are three types. Each fits a different need:



# 2. How To Set Up Each Type
## ☁️  Cloud Tasks (Anthropic's Servers)
Use for: Competitor monitoring, PR reviews, anything that needs to run even when your laptop is off.

Setup steps:
- Go to claude.ai/code/scheduled in your browser
- Click New Scheduled Task
- Set the frequency (minimum 1 hour)
- Paste your prompt
- Connect any MCP connectors needed (Slack, GitHub, Google Drive) via Settings → Connectors
- Save — it runs automatically from here

Or via CLI inside Claude Code, type:


## 🖥️  Desktop Tasks (Your Machine)
Use for: Morning briefings, content calendar updates — anything reading your local files.

Setup steps:
- Open Claude Code Desktop app
- Click Schedule in the left sidebar
- Click New Task → New Local Task
- Set the Working Directory — this is the folder Claude will read/write files in
- Set your frequency and time
- Paste your prompt (reference files by name, e.g. content-calendar.md)
- Save — runs automatically when your laptop is awake


## 🔁  /loop (Current Session)
Use for: Polling a build, checking if a deploy finished, watching a process live.

Setup steps:
- Open Claude Code and start a session
- Type your loop command directly in the chat
- Claude will repeat the task at your chosen interval until you stop it

Example command to type in Claude Code:



# 3. The 5 Ready-To-Use Prompts
Copy and paste each prompt directly into your scheduled task. Customize the placeholders marked with [ ] brackets.

## Prompt 1 — Morning Briefing
Task Type: Desktop Task  |  Frequency: Daily at 8:00 AM  |  Working Dir: Your inbox/calendar folder



## Prompt 2 — Competitor Watchdog
Task Type: Cloud Task  |  Frequency: Weekly, Monday at 7:00 AM  |  Requires: Web search access



## Prompt 3 — PR Reviewer
Task Type: Cloud Task  |  Frequency: Weekdays at 6:00 AM  |  Requires: GitHub repo connected



## Prompt 4 — Content Calendar Refresher
Task Type: Desktop Task  |  Frequency: Weekly, Sunday at 10:00 AM  |  Working Dir: C:\CoworkProjects\ContentCalendar\

First, create your content calendar file. Save it as content-calendar.md in your working directory with this format:



## Prompt 5 — Session Poller (/loop)
Task Type: /loop inside Claude Code session  |  Use during: Active build sessions, deploy monitoring

Unlike the other 4 prompts, this one runs inside an active session. Type it directly into Claude Code chat.



# 4. Quick Setup Reference


# 5. This Chat vs. Claude Code
Important distinction to understand:



— End of Playbook —
| Task Type | Min Interval | Runs When | Can Access |
| --- | --- | --- | --- |
| ☁️  Cloud Tasks | 1 hour | Laptop OFF | GitHub repos, Slack, Google Drive via MCP |
| 🖥️  Desktop Tasks | 1 minute | Laptop AWAKE | Local files, all your MCP servers |
| 🔁  /loop | 5 minutes | Session open | Everything in your current Claude Code session |
| 💡 Dennis's rule of thumb: Use Cloud Tasks for weekly reports and monitoring (Competitor Watchdog, PR Reviewer). Use Desktop Tasks for anything touching your local files (Content Calendar, Morning Briefing). Use /loop for quick polling during active build sessions. |
| --- |
| /schedule weekly competitor review on Mondays at 7am |
| --- |
| ⚠️  Windows file path tip: Always use C:\CoworkProjects\ as your working directory. Do NOT use D: or G: drives — Cowork silently blocks saves to secondary drives. Move files to G: manually after. |
| --- |
| /loop every 5 minutes: check if the build in /home/dennis/project has finished |
| --- |
| ⚠️  /loop stops when you close the session. It is not persistent. Use it only for active monitoring during a work session. |
| --- |
| Prompt #1 — Morning Briefing |
| --- |
| You are my executive assistant preparing a morning briefing.
 
1. Check my inbox for unread emails from the last 12 hours. Categorize them:
   - URGENT (needs response today)
   - IMPORTANT (needs response this week)
   - FYI (no action needed)
 
2. Review today's calendar. For each meeting:
   - Who's attending
   - What it's about
   - One thing I should prepare or review beforehand
 
3. Check my task list for anything due today or overdue.
   Flag the top 3 priorities.
 
4. Write a brief "Today's Game Plan" with my top 3 focus areas
   based on everything above.
 
Format the output as a clean, scannable briefing. Keep each section
short. Lead with what needs my attention most. |
| 💡 Connect Google Calendar and Gmail via MCP connectors in Desktop app Settings → Connectors for full automation. Without connectors, point the working directory at a local notes folder. |
| --- |
| Prompt #2 — Competitor Watchdog |
| --- |
| You are a competitive intelligence analyst. Every week, monitor key
competitors and report what changed.
 
Competitors to monitor:
- [COMPETITOR 1 URL]
- [COMPETITOR 2 URL]
- [COMPETITOR 3 URL]
 
For each competitor:
 
1. Visit their website and check:
   - Pricing page: any changes to plans, pricing, or packaging?
   - Homepage: new messaging, positioning shifts, feature highlights?
   - Blog/changelog: new product announcements or feature launches?
 
2. Run a web search for "[competitor name] news" and
   "[competitor name] announcement" from the past 7 days.
 
3. Summarize findings:
   [Competitor Name]
   - What's new (features, launches, announcements)
   - Pricing changes (if any)
   - Messaging shifts
   - Threat level: Low / Medium / High
 
4. End with a "So What?" section: 2-3 bullet points on what this
   means for us and any actions to consider.
 
If nothing changed, say "No significant changes detected." Don't pad. |
| 💡 Add a Slack MCP connector so Claude posts this report directly to your #competitive-intel channel. Go to claude.ai Settings → Connectors to connect Slack. |
| --- |
| Prompt #3 — Automated PR Reviewer |
| --- |
| You are a senior code reviewer. Every morning, review all open
pull requests on this repository.
 
For each open PR:
 
1. Read the PR description and all changed files.
 
2. Check for:
   - Bugs or logic errors
   - Security concerns (SQL injection, XSS, exposed secrets,
     hardcoded credentials)
   - Performance issues (N+1 queries, unnecessary re-renders,
     missing indexes)
   - Code quality (naming, readability, missing error handling)
   - Test coverage (are new features tested?)
 
3. If the PR looks good, approve it with a brief comment.
 
4. If issues are found, leave specific inline comments on the
   problematic lines. Be constructive, not nitpicky. Focus on
   things that could cause real problems.
 
5. After reviewing all PRs, create a summary with:
   - Total PRs reviewed
   - PRs approved
   - PRs with issues flagged
   - Any recurring patterns you noticed
 
Skip draft PRs. Prioritize PRs open for more than 24 hours. |
| 💡 Enable Allow unrestricted branch pushes when setting up the Cloud Task if you want Claude to push suggestions. For review-only, default permissions are fine. |
| --- |
| | Date       | Topic                          | Format | Status  | Notes |
|------------|--------------------------------|--------|---------|-------|
| 2026-04-21 | How AI is changing insurance   | Blog   | Planned |       |
| 2026-04-28 | 5 ways to automate client onbo | Video  | Planned |       |
| 2026-05-05 | LinkedIn content strategy 2025 | Email  | Planned |       | |
| --- |
| Prompt #4 — Content Calendar Refresher |
| --- |
| You are a content strategist keeping my pipeline relevant and fresh.
 
My content calendar is stored in content-calendar.md in the working
directory. Each row contains: Date | Topic | Format | Status | Notes.
 
Your weekly task:
 
1. Read the full content calendar file.
 
2. For each PLANNED item:
   - Search the web to check if it's still relevant
   - Flag as STALE if outdated, overdone, or no longer timely
   - Flag as KEEP if still strong
 
3. For each STALE item, suggest a replacement:
   - Find a trending angle on the same general theme
   - Keep the same Format (blog/video/email/etc.)
   - Write a new Topic + brief hook (1 sentence)
 
4. Update content-calendar.md directly:
   - Replace STALE topics with your suggested replacements
   - Add "Refreshed [date]" note in the Notes column
   - Leave KEEP items unchanged
 
5. Create weekly-content-review.md with:
   - How many items were reviewed / refreshed
   - Top 3 trending themes you noticed this week
   - One "bold idea" worth adding to the pipeline
 
Save both files when done. |
| Prompt #5 — Build/Deploy Session Poller |
| --- |
| /loop every 5 minutes:
 
Check the build status in [YOUR PROJECT DIRECTORY].
 
1. Look for any error logs or failure signals in the last 5 minutes.
2. If the build is COMPLETE: notify me with a summary of what finished.
3. If the build FAILED: show me the last 20 lines of the error log.
4. If still RUNNING: just say "Still running — [timestamp]" so I know
   you're watching.
 
Stop looping automatically once the build completes or fails. |
| ⚠️  Remember: /loop dies when you close the Claude Code session. Only use it while actively working. For persistent monitoring, convert to a Desktop Task instead. |
| --- |
| Prompt | Type | Frequency | Where To Set It Up |
| --- | --- | --- | --- |
| Morning Briefing | Desktop Task | Daily 8:00 AM | Claude Code Desktop → Schedule → New Local Task |
| Competitor Watchdog | Cloud Task | Mon 7:00 AM | claude.ai/code/scheduled → New Scheduled Task |
| PR Reviewer | Cloud Task | Weekdays 6:00 AM | claude.ai/code/scheduled → New Scheduled Task |
| Content Calendar Refresher | Desktop Task | Sun 10:00 AM | Claude Code Desktop → Schedule → New Local Task |
| Session Poller | /loop | During session | Type /loop directly in Claude Code chat |
| claude.ai Chat (This Interface) | Claude Code (Separate App) |
| --- | --- |
| Conversational — you type, Claude responds | Executes tasks autonomously on a schedule |
| Nothing happens unless you initiate it | Runs without you once configured |
| Great for planning, drafting, designing | Great for automation, file changes, monitoring |
| No scheduler — reactive only | Full scheduler: Cloud, Desktop, and /loop modes |
| Use here: prep and refine your prompts | Use here: paste prompts and set the timer |
| 🎯 Your workflow: Use this Claude chat to design and refine your prompts → then open Claude Code to set the schedule and let it run on autopilot. |
| --- |