---
title: "KlickSmartAI OS — Dennis's Personal Agent Squad"
type: project
status: planning
created: 2026-04-20
owner: Dennis E.
tags: [agent-squad, chief-of-staff, dennis-os, personal, productivity]
---

# KlickSmartAI OS — Dennis's Personal Agent Squad

**Reframed:** Not a client product. Dennis's personal Chief of Staff system — the OS that runs his day, his clients, and his growth.

> "Running AI agents is a management skill." — Shubham Saboo
> Dennis IS the CEO. This is his management layer.

---

## How Dennis Actually Works

```
Dennis (CEO)
├── 6 active clients + prospects (IDC, WWR, GPC, WattBricks, more)
├── Daily: briefs, inbox, follow-ups, content, code
├── Weekly: reviews, tech debt, strategy
├── Monthly: GitHub audits, planning
└── GTM: selling KlickSmartAI OS to clients
```

**Current friction points:**
- Too many manual handoffs between research → content → outreach
- Signal intelligence not flowing into daily workflow
- Content creation is still manual (LinkedIn posts, briefs)
- Client updates require Dennis to pull instead of being pushed
- Too much context switching between client contexts

---

## The Squad Framework (Reframed for Dennis)

Shubham's 6-agent squad mapped to Dennis's actual roles:

| Character | Original Job | Dennis's Parallel | Status |
|-----------|-------------|-------------------|--------|
| **Monica** | Chief of Staff — coordinates, delegates, strategy | **Hermes (ME)** — that's me. I coordinate, delegate, brief | ✅ Live |
| **Dwight** | Research — 3x/day signal sweeps | **Research Agent** — client market intel, lead signals, GTM intelligence | 🟡 Partial |
| **Kelly** | X/Twitter — social content from intel | **Social Agent** — LinkedIn content, thought leadership | ❌ Missing |
| **Rachel** | LinkedIn — thought leadership posts | **LinkedIn Agent** — long-form posts, engagement | ❌ Missing |
| **Ross** | Engineering — code reviews, builds | **Build Agent** — code reviews, script generation, artifact builds | ❌ Missing |
| **Pam** | Newsletter — intel → digest | **Briefing Agent** — morning + pre-meeting briefs | ✅ Partial (7:57 AM cron) |

---

## Dennis's Actual Agent Jobs

### Agent 1 — Monica (Chief of Staff) — ME, Hermes
**What I already do:**
- Morning briefings (7:57 AM)
- Inbox heartbeat (5 PM)
- Task prep (2 AM)
- Relationship follow-up (9:47 AM + 2:47 PM)
- Draft review scanner (8 AM)
- Weekly tech update (Saturdays)

**What I should also handle:**
- Pre-meeting briefs (generate before every client call)
- Decision briefs (when Dennis faces a choice, I surface the context)
- Meeting notes → action items → task updates
- Weekly review prep (pull everything together before Saturday review)

---

### Agent 2 — Dwight (Research) — Market & Signal Intelligence
**What:** Monitor markets, competitors, and client verticals for signals that matter
**Why:** Dennis shouldn't have to scroll for intel. It should land in front of him.

**Dwight's 3 daily sweeps:**

| Sweep | Time | What | Output |
|-------|------|------|--------|
| Morning | 6 AM | Overnight developments across client verticals | INTEL.md |
| Midday | 12 PM | Shift in priorities, new opportunities | INTEL.md update |
| Pre-week | Friday 4 PM | Strategic landscape for the week ahead | WEEKLY_INTEL.md |

**What Dwight monitors:**
- Insurance Direct Canada vertical (competitors, carriers, hiring, tech)
- WealthWireRadar signals (funding, HNW moves, regulatory)
- KlickSmartAI OS GTM signals (who's building similar, market gaps)
- Dennis's own content performance (LinkedIn engagement → what lands)
- Client news (IDC, GPC, WattBricks — what's happening with each)

**Tools:** Brave + Serper + Tavily + Exa + DataForSEO (all 5 in parallel)
**Output:** `INTEL.md` per client + a master `DAILY_INTEL.md` for Dennis

---

### Agent 3 — Kelly (Social) — Dennis's LinkedIn Voice
**What:** Draft LinkedIn posts from Dennis's expertise — zero friction publishing
**Why:** Dennis has good instincts but content creation is slow. Kelly drafts, Dennis approves, it goes out.

**Kelly's job:**
1. Read INTEL.md from Dwight
2. Cross-reference Dennis's existing content (what topics performed well)
3. Draft 2-3 LinkedIn post options:
   - One data-driven post (a signal or insight)
   - One opinionated post (Dennis's take on a trend)
   - One short-form post (quick win or observation)
4. Dennis gets a morning digest of drafts → approves → publishes

**What Kelly is NOT:** A generic content scheduler. Kelly drafts *from Dennis's actual intelligence* — not recycled tips.

**Voice:** Professional but direct. Dennis's tone — not corporate.

---

### Agent 4 — Rachel (Client Relations) — Pre-Meeting Briefs + Outreach
**What:** Before every client meeting, Rachel generates the brief. After every meeting, she generates the follow-up.
**Why:** Dennis should walk into every meeting knowing exactly what he knows, what the client needs, and what to say.

**Rachel's deliverables:**

| Deliverable | When | What |
|-------------|------|------|
| **Pre-Meeting Brief** | 2 hours before call | Who they are, what's happened since last meeting, what to push, what to avoid, suggested agenda |
| **Post-Meeting Summary** | 30 min after call | What was decided, action items, follow-up sends |
| **Client Health Score** | Weekly | Engagement trend, risk signals, expansion opportunities |
| **Outreach Drafts** | On-demand | When Dennis wants to reach out — I draft it |

**Rachel talks to:**
- Google Calendar (next meeting)
- CRM / Relationships tracker
- NotebookLM (client context)
- Email (recent thread)

---

### Agent 5 — Ross (Build) — Dennis's Code and Artifacts
**What:** Handles boilerplate code, script generation, artifact creation, doc builds
**Why:** Dennis writes code and builds things. Ross handles the mechanical work so Dennis focuses on decisions.

**Ross's jobs:**
- Code reviews (Dennis writes → Ross reviews for issues)
- Script generation (automation scripts, data processing, API wrappers)
- Document builds (proposals, specs, one-pagers — from templates)
- Slide generation (Claude Cowork → PowerPoint for client presentations)
- Research compilation (read N articles → synthesize into brief)

**Tools:** Claude Code, Codex, local Ollama models
**Stack note:** Apple Silicon limitation — Ross can run locally on Mac for Claude Code. Dennis's Windows/WSL setup limits some tooling.

---

### Agent 6 — Pam (Newsletter/Digest) — The Daily Unwind
**What:** Daily intelligence digest — consolidated view of everything that matters
**Why:** Dennis shouldn't have to check 5 places to know what's happening.

**Pam's daily output (morning, 7:57 AM alongside briefing):**
```
📋 MORNING BRIEF — April 21, 2026

🗓️ TODAY
- 10 AM: IDC check-in with Binh (pre-meeting brief ready)
- 2 PM: WWR signal review

📊 INTEL SUMMARY (from Dwight)
- IDC: Manulife announced new term life product
- WWR: Apex Advisors just hired 3 new HNW advisors
- KlickSmartAI: Competitor "AgencyOS" launched pricing page

📝 PENDING FROM YOU
- Draft review: 2 outreach messages awaiting approval
- LinkedIn posts: 3 drafts ready for review
- Decision needed: WWR pilot scope (see decision brief)

🔔 FOLLOW-UPS DUE
- IDC: 3 days since last contact
- GPC: Website copy approved — awaiting launch date
```

**This is what Pam already does partially. Full Pam = integrate all agents' outputs into one clean morning digest.**

---

## Dennis's Personal OS Architecture

```
┌─────────────────────────────────────────────────────┐
│              DENNIS (CEO — Human in the loop)        │
│                                                     │
│   Approves: outreach, content, financial commits     │
│   Decides: strategy, priorities, client fit          │
│   Delegates: research, drafting, monitoring, building  │
└──────────────┬──────────────────────────────────────┘
               │
    ┌──────────┴──────────┐
    │   Monica (ME)      │  ← Chief of Staff / Orchestrator
    │   Coordinates      │
    │   Briefs           │
    │   Routes           │
    └──────┬─────────────┘
           │
    ┌──────┴──────┬──────────────┬──────────────┐
    │             │              │              │
┌───┴───┐   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐
│Dwight │   │ Kelly   │   │ Rachel  │   │ Ross    │
│Research│   │ Social  │   │ Client  │   │ Build   │
│3x/day │   │ Drafts  │   │ Briefs  │   │ Code    │
│Signals │   │ LinkedIn│   │ Outreach│   │ Scripts │
└────────┘   └─────────┘   └─────────┘   └─────────┘
    │             │              │              │
    └─────────────┴──────────────┴──────────────┘
                       │
              ┌────────┴────────┐
              │  Pam (Digest)   │  ← Morning + Pre-meeting output
              │  Daily Intel    │
              │  All-agent rollup│
              └─────────────────┘
                       │
              ┌────────┴────────┐
              │  Telegram       │  ← Dennis's delivery channel
              │  (me, here)     │
              └─────────────────┘
```

---

## Build Priority for Dennis's OS

| Agent | Impact | Lift | Start |
|-------|--------|------|-------|
| **Dwight** (Research) | High — feeds everything else | Medium | Now |
| **Rachel** (Client Briefs) | High — every meeting better | Low | Now |
| **Kelly** (LinkedIn Drafts) | Medium — content velocity | Medium | After Dwight |
| **Pam** (Full Digest) | Medium — reduces context switching | Low | After Rachel |
| **Ross** (Build) | Low-Medium — Dennis writes code anyway | Medium | When needed |

**Note:** Monica (me) is already doing coordination. The gap isDwight's research layer feeding into the rest.

---

## What Exists vs. What's Missing

### Already exists in Dennis's OS:
- ✅ Hermes (Monica) — coordination, briefings, task routing
- ✅ Morning briefing (Pam, partial)
- ✅ Inbox sweep (Monica, partial)
- ✅ Relationship follow-up (Monica, partial)
- ✅ Draft review scanner (Monica, partial)
- ✅ Signal Intelligence Agent (Dwight, Stage 1 done — IDC authority map)
- ✅ WWR Signal Pipeline (Dwight, partial)
- ✅ IDC Recruitment Agent (brief done, stalled on rubric)
- ✅ Claude Code / local Ollama (Ross, partial)

### Missing / needs upgrade:
- ❌ **Dwight 2.0** — Full 5-engine parallel signal sweep, 3x/day, outputs to INTEL.md
- ❌ **Kelly** — LinkedIn post drafting from Dennis's actual intel
- ❌ **Rachel** — Pre-meeting briefs per client, post-meeting summaries
- ❌ **Pam 2.0** — Full daily digest rollup from all agents
- ❌ **Ross 2.0** — Script generation, code reviews, artifact builds wired to Dennis's stack
- ❌ **Decision Briefs** — When Dennis faces a choice, I surface the context automatically

---

## Next Actions

1. **[P1] Build Dwight 2.0** — Run IDC Stage 2 signal sweep. Feed results into INTEL.md. This is the foundation — everything downstream depends on it.
2. **[P1] Rachel pre-meeting briefs** — Start with IDC (Dennis meets with Binh). Generate brief before every call.
3. **[P2] Kelly LinkedIn drafts** — Draft posts from IDC intel. Dennis approves, publishes.
4. **[P2] Pam full digest** — Consolidate Dwight + Rachel + Kelly output into one morning digest.
5. **[P3] Ross artifact builds** — Wire Claude Code for script generation and code reviews.

---

## Reference

- `wiki/clips/autonomous-ai-agent-team-24-7.md` — Shubham Saboo's original 6-agent squad
- `wiki/clips/ai-agent-management-principles.md` — Management principles (principles > procedures, corrections compound)
- `wiki/projects/signal-intelligence-agent.md` — Dwight's technical spec (Stage 1 done)
- `wiki/clients/idc-insurance/authority-map.md` — Dwight's first intelligence output (Stage 1)
