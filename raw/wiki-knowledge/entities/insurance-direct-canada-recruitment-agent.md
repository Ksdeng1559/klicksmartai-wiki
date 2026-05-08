# Insurance Direct Canada — AI Recruitment Agent

**Status:** IN PROGRESS — Phase 0 gate
**Stack:** Hermes Agent · DuckDB · **Gemma 4 Vision** · Discord · WhatsApp · Telegram
**Feedback Model:** Batch review every 10 candidates → Dennis overrides → rubric update
**Last Updated:** 2026-04-26

---

## What HUBERT-X Is

24/7 AI recruitment portal for Insurance Direct Canada. Receives resumes via **WhatsApp (primary)**, Discord (admin/community), and Telegram (testing) using native Hermes connections. Scores candidates using the IDC rubric via **Gemma 4 Vision**, delivers qualified candidates to Dennis for hire decisions. Uses a **batch feedback loop** so the rubric self-improves based on Dennis's corrections.

**Core question MVP answers:** "Does AI prescreening identify candidates who convert to productive advisors — faster and cheaper than manual recruiting?"

---

## Architecture

```
CANDIDATE ──► WHATSAPP BOT (PRIMARY)
        └──► DISCORD BOT (COMMUNITY/ADMIN) 
        └──► TELEGRAM BOT (TESTING/BACKUP)
                   │
                   ▼
            NATIVE HERMES CONNECTION
                   │
                   ▼
      HERMES (Gemma 4 Vision + Cross-Platform Deduplication)
            │               │               │
            │          RIA: parse resume   │
            │          SIM: score rubric   │
            │          FSE: route band     │
            │            Unified Candidate_UUID
            │               │               │
            └───────────────┼───────────────┘
                            │
                ┌───────────┼───────────┐
                │           │           │
            Qualified     Trainable        Reject
            (≥60)         (40-59)          (<40)
                │           │           │
                └───────────┴───────────┘
                            │
                 Every 10 candidates (cross-platform)
                            │
                            ▼
                 DENNIS BATCH REVIEW CARD
                 (Discord DM)
                            │
                 Dennis corrects wrong decisions
                            │
                 Rubric calibrated for next batch
```

---

## Track 1 MVP Scope

**Inbound multi-platform flow:**
1. `/start` or platform equivalent → PIPEDA consent
2. Name collection
3. Email collection  
4. Resume (PDF upload or paste)
5. Cross-platform deduplication check (Candidate_UUID)
6. Gemma 4 Vision screens → score/band/action
7. Candidate receives: Qualified / Trainable / Rejection message via same platform
8. Every 10 candidates (aggregated across all platforms): Dennis Batch Review Card on Discord

**CSV import flow (outbound prospecting):**
1. Dennis imports CSV of prospects
2. Gemma 4 Vision drafts personalized LinkedIn outreach message
3. Dennis reviews and sends manually (MVP)

---

## Feedback Loop (Core Design)

**Every 10 candidates → Dennis receives a Batch Review Card:**
- All 10 decisions summarized (name, score, band, action)
- Dennis corrects any wrong decisions
- Corrections → rubric/prompt adjustments
- **After 3 consecutive clean batches (no corrections):** that scoring category = calibrated

**This is the "until it fails" mechanism:**
- M2.7 runs until Dennis sees a pattern of errors
- Batch size of 10 is small enough to catch drift fast, large enough to avoid noise
- No automatic fallback chain — Dennis is always in the loop

---

## DuckDB Tables

- `candidates` — name, email, resume, state, source, candidate_uuid
- `user_mapping` — cross-platform user ID mapping (platform, user_id, candidate_uuid)
- `screening_results` — Gemma 4 Vision scores, breakdown, band, action
- `consent_log` — PIPEDA compliance, never deleted
- `follow_up_queue` — D1/D3/D7 sequence
- `batch_review_queue` — every scored candidate for Dennis review
- `rubric_calibration_log` — tracks all rubric changes

---

## Scoring Rubric (IDC-Calibrated, Gemma 4 Vision)

| Category | Weight | Max |
|----------|--------|-----|
| Core Sales Capability | 35% | 35 |
| Insurance / Financial Fit | 25% | 25 |
| Licensure | 20% | 20 |
| Commitment Signals | 10% | 10 |
| Trainability | 10% | 10 |

**Band thresholds:**
- ≥ 80 → Elite (Tier A) — Qualified + priority alert
- 60–79 → Strong (Tier B) — Qualified
- 40–59 → Trainable (Tier C) — Holding message + follow-up
- < 40 → Reject (Tier D) — Auto-reject

---

## Track 2 — Advisor Poach (After Track 1 Stable)

Targeted outreach to licensed, producing advisors. No rubric scoring — intent signals only (Gemma 4 Vision scored).

**Auth:** `nlm login --provider openclaw --cdp-url http://172.21.128.1:9222`
**Notebook:** `0faae8a0-146b-4928-a2b5-469ed2df6005` — https://notebooklm.google.com/notebook/0faae8a0-146b-4928-a2b5-469ed2df6005

---

## Canonical Files

| File | Purpose |
|------|---------|
| `HUBERT_X_Implementation_Playbook.md` | TDD-first build plan — **start here** |
| `HUBERT_X_PDD_MVP.md` | Canonical build spec |
| `hubert_x_problem_definition.html` | Why it exists — market problem |
| `HUBERT-X_Recruitment_Workflow.html` | Visual workflow |
| `~/.hermes/skills/project/insurance-direct-canada-recruitment-agent/` | Hermes skill |

---

## Key IDC Stakeholders

| Person | Role |
|--------|------|
| **Binh Nguyen** | CEO — Insurance Direct Canada · https://www.linkedin.com/in/ben-nguyen-canada/ |
| **Russ Smart** | Consultant — runs training, former recruiting lead · https://www.linkedin.com/in/russsmart/ |
| Kevin Panoncic | Hiring Manager — primary screener, tracks new hire performance · https://www.linkedin.com/in/kevan-penonzek-2b592314/ |

---

## Phase 0 Gates (Dennis Must Answer)

| # | Question | Blocks |
|---|----------|--------|
| Q1 | Intro video URL? | Task 7 |
| Q2 | Calendly/scheduling link? | Task 7 |
| Q3 | Bot isolation — separate instance or skill route? | Task 2 |
| Q4 | PIPEDA consent text — legal review? | Go-live |
| Q5 | First recruitment list — format, source? | Task 11 |
| Q6 | LinkedIn outreach — manual or Aimfox? | Task 11 |

---

## PIPEDA Note

If candidate data is collected (name, email, resume), PIPEDA applies. Consent screen required. BC/ON/AB scope only — Quebec (QPAMP) and mortgage brokers (OSMV) out of scope unless separate addenda created.
