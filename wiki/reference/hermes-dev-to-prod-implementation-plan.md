# Hermes Dev-to-Production Implementation Plan v1.1

**Source:** KlickSmartAI — April 2026  
**Author:** Dennis Eng  
**System:** Hermes Agent Framework  
**Dev:** Local Windows Machine  
**Production:** Railway (Linux, always-on)  
**Knowledge Layer:** Obsidian Git (Phase A) + LiveSync CouchDB (Phase B)

---

## 1. Overview

### 1.1 Purpose
Complete implementation plan for a professional dev-to-production pipeline. Local Windows machine = development server. Railway = always-on production. Obsidian sync: Phase A (Git-based, immediate) + Phase B (CouchDB LiveSync on Railway).

### 1.2 Core Principle
**Local Hermes = build/test/validate. Railway Hermes = 24/7 client-facing production.** Never build directly on production.

| Environment | Purpose | Who Sees It |
|------------|---------|-------------|
| LOCAL — Hermes Dev | Build, test, iterate safely | Dennis only |
| RAILWAY — Production | Always-on agents serving clients 24/7 | Clients, candidates, IDC portal |
| OBSIDIAN GIT — Phase A | GitHub vault sync — immediate, zero infra | Dennis on any device |
| GITHUB — Bridge | Version control + deployment trigger | Railway auto-deploys on push |

### 1.3 What Gets Built
- **GitHub repo** — private, branching: main=prod, dev=development
- **Railway project** — Phase A: 1 service (Hermes Master Agent). Phase B adds CouchDB + Cloudflare Tunnel
- **Local dev environment** — mirrored structure to production, `.env` for dev keys
- **Phase A sync** — Obsidian Git via GitHub (auto-commit every 60min, 15GB free)
- **Phase B sync** — Obsidian LiveSync via CouchDB on Railway (Week 3-4)

---

## 2. Full Architecture

### 2.1 Dev-to-Production Flow
Code flows: **Local → GitHub → Railway**. Knowledge flows: **Railway agents → Obsidian → CouchDB**.

| Step | Action | Result |
|------|--------|--------|
| 1 | Write/modify agent code locally | Changes in local dev only |
| 2 | Test locally against dev sandbox | Validate before client exposure |
| 3 | `git commit` + push to dev branch | Code versioned — not deployed |
| 4 | Merge dev → main on GitHub | Triggers automatic Railway deploy |
| 5 | Railway detects main update | Pulls + redeploys Hermes |
| 6 | Production agents restart | Live clients get updated behaviour |
| 7 | Agent activity → local vault → Git sync | Vault available on any device |

### 2.2 Railway Service Architecture

| Service | Technology | Role | Est. Cost |
|---------|-----------|------|-----------|
| hermes-agents | Python 3.11 / Linux | Master + sub-agents + heartbeats | $10-15/mo |
| couchdb-sync (B) | CouchDB 3.x Docker | Phase B real-time sync | $5-10/mo |
| tunnel (B) | Cloudflare Tunnel | Phase B HTTPS to CouchDB | Free |
| **Phase A Total** | 1 service | Hermes agents + Obsidian Git | **$10-15 CAD/mo** |

### 2.3 Local Dev Environment Structure
```
C:\HermesAgent\
├── agents\
│   ├── master_agent.py
│   ├── whatsapp_handler.py
│   ├── telegram_handler.py
│   ├── resume_processor.py
│   ├── screening_agent.py
│   ├── enrichment_agent.py
│   ├── scoring_agent.py
│   └── presentation_agent.py
├── souls\
│   ├── sophia_idc.json
│   ├── marcus_idc.json
│   └── elena_idc.json
├── obsidian\
│   └── vault_writer.py
├── db\
│   └── schema.py
├── .env                    (DEV keys — never in GitHub)
├── .gitignore
├── railway.toml
├── Procfile
└── requirements.txt
```

### 2.4 GitHub Branching Strategy

| Branch | Purpose | Rule |
|--------|---------|------|
| main | Production (Railway deploys) | Never commit directly — merge from dev only |
| dev | Development (your working branch) | All daily work here |
| feature/X | New agent or feature | Branch from dev → merge back to dev |

---

## 3. Implementation Phases

### Phase 1 — GitHub Setup (30-45 min)
1. Create private repo `hermes-recruitment`
2. Create `.gitignore` (protects `.env`, `*.db`, `*.duckdb`, `__pycache__/`, `*.pyc`, `*.log`, `.DS_Store`, `node_modules/`, `couchdb-data/`, `couchdb-etc/`)
3. Initialize git locally
4. Create dev branch
5. First commit + push to dev
6. Verify on GitHub

### Phase 2 — Railway Project Setup (45-60 min)
1. Log into railway.app
2. Create project `hermes-recruitment`
3. Add service → Deploy from GitHub repo
4. Set deployment branch to `main`
5. Add all environment variables
6. Create `Procfile`: `web: python agents/master_agent.py`
7. Create `requirements.txt`
8. Trigger first deployment + verify logs

### Phase 3 — Obsidian Git Setup (Phase A, 15-20 min)
1. Create private repo `klicksmartai-vault`
2. Install Obsidian Git plugin
3. Connect to vault repo
4. Auto-commit: 60 min, auto-push enabled
5. Test: create note → verify on GitHub within 60 min

**Zero-cost sync:** vault backup, full version history, 15GB free, no Railway dependency.

### Phase 4 — WhatsApp Channel Integration (60-90 min)
Integration of WhatsApp webhook into Railway production environment.

### Phase 5 — Telegram Webhook Reconnection (15-20 min)
1. Get Railway public URL
2. Register Telegram webhook: `https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://your-app.railway.app/webhook/telegram`
3. Test message → confirm Railway Hermes responds
4. Verify via `getWebhookInfo`

### Phase 6 — Hermes Vault Writer Module (3-5 hours)
Python module for agents to write structured markdown to Obsidian vault. Files auto-committed by Obsidian Git.

- Candidate session notes on every interaction
- Heartbeat writes `System-Status.md` every 15 min
- Grade A/B candidates → auto-generated candidate note
- Build: local → test → push to GitHub main → Railway redeploy

### Phase 7 — Phase B: CouchDB LiveSync (Future, 45-60 min, Week 3-4)
1. Add CouchDB Docker service to Railway
2. Set credentials + persistent volume
3. Install Self-hosted LiveSync plugin in Obsidian
4. Connect to Railway CouchDB
5. Update `vault_writer.py` for CouchDB writes
6. Real-time sync across all devices
7. **Phase A Git backup remains active**

---

## 4. Obsidian Vault Structure

```
KlickSmartAI-Vault/
├── Agents/                    (Auto-written by Hermes)
│   ├── Sophia/
│   │   ├── Active-Candidates.md
│   │   ├── Session-Log-YYYY-MM-DD.md
│   │   └── Escalation-Queue.md
│   ├── Marcus/
│   │   ├── Grading-Queue.md
│   │   └── Grade-History.md
│   └── Elena/
│       ├── Video-Sessions.md
│       └── Completion-Log.md
├── Clients/
│   └── IDC/
│       ├── Candidates/        (One note per candidate)
│       ├── Pipeline/
│       ├── Decisions/
│       └── IDC-Overview.md
├── KlickSmartAI/
│   ├── System-Status.md       (Heartbeat writes here)
│   ├── Fee-Tracker.md
│   ├── Mission-Log.md
│   └── MRR-Dashboard.md
├── Projects/
│   ├── Hermes-PRD/
│   ├── LeadSniperAI/
│   ├── CSE/
│   └── MineTeck/
└── Daily/                     (Personal daily notes)
    └── YYYY-MM-DD.md
```

### Candidate Note Format (auto-generated for Grade A/B)

```
# Sarah Chen — Grade A Candidate
**Score:** 87/100  |  **Tier:** A — Priority
**Province:** BC   |  **Source:** WhatsApp
**Current Role:** RE/MAX Realtor (6 years)
**Received:** 2026-04-30 10:42

## AI Recommendation
Strong network of 340+ homeowner clients...

## Score Breakdown
- Network Size: 92/100
- Communication: 88/100
- FS Aptitude: 80/100
- Entrepreneurial: 85/100
- Coachability: 87/100
- Availability: 79/100

## Pipeline Stage
- [x] Resume received
- [x] Screening passed — Grade A
- [x] Video interview completed
- [x] Enrichment done
- [ ] IDC review pending
- [ ] Decision recorded
```

### System Status Note Format (heartbeat every 15 min)

```
# Hermes System Status
**Last Updated:** 2026-04-30 14:30

## Agent Health
- Sophia: ACTIVE — 247 candidates in care
- Marcus: ACTIVE — 3 resumes in queue
- Elena: ACTIVE — 2 video sessions open

## Today's Pipeline
- Resumes received: 12
- Screened: 9
- Grade A: 2  |  Grade B: 3
- Video completed: 3
- IDC review pending: 6

## Channels
- WhatsApp: CONNECTED
- Telegram: CONNECTED
- MotherDuck: CONNECTED
- CouchDB Sync: ACTIVE
```

---

## 5. Daily Development Workflow

### 5.1 Standard Build Session

| Step | Action | Command/Tool |
|------|--------|-------------|
| START | Pull latest from GitHub | `git pull origin dev` |
| BUILD | Open Claude Code with agent file | Focused task per file |
| TEST | Run Hermes locally | `python agents/master_agent.py` |
| VERIFY | Test against dev sandbox | Dev WhatsApp/Telegram test bot |
| COMMIT | Save to dev branch | `git add . && git commit -m 'description'` |
| PUSH | Upload to GitHub dev | `git push origin dev` |
| DEPLOY | Merge dev → main | `git checkout main && git merge dev` |
| CONFIRM | Watch Railway logs | Railway dashboard → Deployments |

### 5.2 Agent Build Rules

| Rule | Rationale |
|------|-----------|
| Max 350 lines per agent file | Keeps files reviewable, Claude Code works best focused |
| One agent file = one responsibility | Easier to test, debug, replace |
| All secrets via env vars | Never hardcode keys |
| Test locally before pushing to main | Production never sees broken agents |
| Meaningful commit messages | Readable git history |
| Log every action to MotherDuck | Full audit trail |

### 5.3 Pushing a New Soul to Production
1. Create new soul JSON in `souls/` folder
2. Define all 10 soul attributes
3. Test locally with new soul loaded
4. Create/modify agent Python file (≤350 lines, import soul at startup)
5. Test full agent flow, heartbeat
6. Commit both files to dev: `git add souls/new_agent.json agents/new_agent.py`
7. Merge dev → main → Railway auto-deploys (2-3 min)
8. Watch Railway logs to confirm

---

## 6. Environment Variables

### Local `.env` (Dev — never pushed)
```
ENVIRONMENT=development
LOG_LEVEL=DEBUG
TELEGRAM_BOT_TOKEN=***
TELEGRAM_WEBHOOK_SECRET=***
WHATSAPP_API_KEY=***
WHATSAPP_PHONE_NUMBER=***
WHATSAPP_WEBHOOK_SECRET=***
ANTHROPIC_API_KEY=***
TAVILY_API_KEY=***
OPENAI_API_KEY=***
MOTHERDUCK_TOKEN=***
DUCKDB_PATH=./db/hermes_dev.duckdb
COUCHDB_URL=***
COUCHDB_USER=***
COUCHDB_PASSWORD=***
COUCHDB_DB=obsidian-vault
```

### Railway (Production)
Same keys but with production values. Set in Railway dashboard → Variables tab.

---

## 7. Timeline

| Phase | Name | Low (hrs) | High (hrs) | Timeline |
|-------|------|-----------|------------|----------|
| 1 | GitHub repos (2 repos) | 0.5 | 0.75 | Day 1 AM |
| 2 | Railway project + Hermes deploy | 0.75 | 1.0 | Day 1 AM |
| 3 | Obsidian Git setup | 0.25 | 0.25 | Day 1 PM |
| 4 | WhatsApp integration | 1.0 | 1.5 | Day 1 PM |
| 5 | Telegram webhook reconnect | 0.25 | 0.5 | Day 1 PM |
| 6 | Vault writer module | 3.0 | 5.0 | Day 2 |
| 7 | Phase B CouchDB (future) | 0.75 | 1.0 | Week 3-4 |
| **TOTAL** | | **5.75-6.0** | **10.0** | **1-2 days (A)** |

### Day-by-Day
- **Day 1 AM:** GitHub repos + Railway deploy
- **Day 1 PM:** Obsidian Git live + WhatsApp + Telegram reconnect + full smoke test
- **Day 2:** Vault writer module build + test + deploy
- **Week 3-4:** Phase B CouchDB LiveSync

### Monthly Cost
| Service | Cost |
|---------|------|
| Railway Hermes | $10-15 CAD |
| Railway CouchDB (Phase B) | $5-10 CAD |
| Railway volume | $0.25/GB CAD |
| Cloudflare Tunnel | Free |
| GitHub | Free |
| Plugins | Free |
| **Total** | **$15-25 CAD/mo** |

---

## 8. Immediate Next Steps

1. **Create private GitHub repo** `hermes-recruitment` → Foundation for everything
2. **Share Hermes folder path** on Windows machine → Claude Code generates exact git commands
3. **Share Hermes main entry point** with Claude Code → Generates Procfile + requirements.txt for Railway

Day 1 complete = Hermes on Railway before end of day.
