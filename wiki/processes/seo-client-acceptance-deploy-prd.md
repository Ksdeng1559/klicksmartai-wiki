# PRD — SEO Client Acceptance & Deploy Pipeline

**Owner:** Dennis Eng (KlickSmartAI)
**Author:** Hermes Agent
**Created:** 2026-08-30
**Status:** DRAFT (awaiting Dennis sign-off)
**Decision:** build the PRD first; scaffolding + wiring later

---

## 1. Problem

KlickSmartAI delivers an SEO audit + CLIENT-SCORE report today, but the **acceptance-to-cash-to-deployment loop is fully manual**:

1. Audit produced → email to client
2. Client says "yes" → **no automated billing capture** (Stripe invoice is hand-built)
3. Deposit received → **no automated workflow trigger**
4. Agency team completes the work → **no automated deploy to a client-facing URL**

Every step has friction + manual coordination cost. Two real clients (gpc, veritas) are about to go through this loop. The pattern needs to become a **reusable, repeatable, agency-grade pipeline** so each new SEO engagement ships in hours, not days.

## 2. Goals

| # | goal | measure |
|---|---|---|
| G1 | **one-click client acceptance** — client opens report, clicks accept, payment is captured, agency workflow fires | <60s from click to confirmation |
| G2 | **50% deposit, 50% on completion** Stripe billing | Stripe Checkout session auto-generated |
| G3 | **automated agency workflow** — accepted engagement spawns kanban tickets, workspace data, audit baseline | tier-2 duckdb + supabase + kanban populated without manual entry |
| G4 | **automated per-client deploy** — client gets a unique URL (`<slug>.klicksmartai.com` or custom) showing their live audit score, work-in-progress, and deliverables | Vercel deployment live in <5 min |
| G5 | **single shared backend** — Railway hosts one service, multi-tenant by `client_slug`; scales without per-client infra overhead | one Railway service, many workspaces |
| G6 | **HITL gates preserved** — Stripe charge + Railway deploy + Vercel production deploy are NOT autonomous; they queue for owner approval | every external side-effect requires Dennis's "go" |

## 3. Non-goals

- **Not** building Stripe Connect / multi-vendor payouts — single KlickSmartAI merchant account only.
- **Not** building a full client-portal with messaging, file uploads, contracts — out of scope for v1. The CLIENT-SCORE + a single "accept + pay deposit" page is the v1 surface.
- **Not** building automatic SEO work execution — the audit recommendations still need human agency team. The pipeline only automates: acceptance → billing → workflow trigger → deploy.
- **Not** replacing the seo-client-onboarding-sprint.md intake flow — that PRD feeds into this one. We assume client + intake are already complete before the report ships.

## 4. Users & Roles

| role | description | actions |
|---|---|---|
| **Client** (Tak Ho, Zulliy Alnahas / David Poole, Daniel Bailey) | The end customer who receives the report | read report, click "accept", pay deposit, watch progress |
| **Agency owner** (Dennis) | KlickSmartAI operator | reviews report quality, approves HITL gates, signs off on phase-2 billing, signs off on deploy |
| **Agency worker** (human or AI) | the dev/content team who executes the SEO work | picks up kanban tickets, makes changes, marks done |
| **System** (Hermes) | the orchestrator | drives the state machine from `REPORT_SENT` → `ACCEPTED` → `WORK_IN_PROGRESS` → `DELIVERED` |

## 5. The Pipeline — state machine

```
[1] REPORT_SENT
     │  client receives CLIENT-SCORE link (email + portal URL)
     ▼
[2] CLIENT_VIEWING
     │  Stripe Checkout session auto-created server-side;
     │  portal page polls session state every 5s;
     │  "accept + pay $X deposit" CTA visible
     │
     ├── click "accept" → server records intent →
     │   Stripe Checkout opens in iframe/redirect
     │
     ├── click "decline" → state = DECLINED, end
     │
     └── never click → 7-day expiry reminder email, then EXPIRED
     ▼
[3] DEPOSIT_PAID   ←  Stripe webhook → supabase row update
     │  HITL gate: Dennis confirms engagement before spawning workflow
     ▼
[4] WORKFLOW_SPAWNED   ←  kanban tickets created, supabase workspace flagged,
     │   tier-2 duckdb initialized, audit baseline locked
     ▼
[5] WORK_IN_PROGRESS
     │  agency worker picks tickets, updates status,
     │  optional status page updates visible to client
     ▼
[6] DELIVERABLES_READY
     │  HITL gate: Dennis reviews before billing remainder
     ▼
[7] FINAL_PAYMENT_PAID   ←  Stripe second charge ($remaining) on Dennis approval
     │
     ▼
[8] DELIVERED   ←  Vercel production deploy fires (HITL gate),
     │   client gets final URL + handoff email,
     │   tier-3 supabase marked RELEASED
     ▼
[9] RETAINER (optional, future v2)
```

## 6. Functional requirements

### 6.1 Client report skill (replaces one-off `seo-audit-report` invocation)

A new skill `seo-client-report` that, given a slug + workspace, generates:

- `CLIENT-SCORE-<slug>-<date>.md` (client-facing)
- `CLIENT-SCORE-<slug>-<date>.html` (styled, scannable, includes "Accept & Pay" CTA)
- `<slug>-cover-letter.md` (email body)
- Stripe Checkout session URL (pre-populated with deposit amount)
- Vercel preview URL (per-client route on `klicksmartai.com/client/<slug>/`)

Inputs: `audit_date`, `score_overall`, `score_tier`, `engagement_quote.total_usd`, `client.contact_email`, `client.domain`.

### 6.2 Stripe deposit billing

- 50% deposit at acceptance, 50% on Dennis approval at completion.
- Use **Stripe Checkout (hosted)** — no PCI scope, no custom card forms.
- Webhook listens for `checkout.session.completed` → updates engagement row.
- Webhook URL: `https://<railway>/webhooks/stripe` (signature verified).
- Idempotency: webhook events de-duplicated by `event.id`.
- Refund logic: if HITL gate rejects after payment, full refund fires automatically (no manual intervention).

### 6.3 Agency workflow automation

On `DEPOSIT_PAID` + HITL approval:

- Create kanban tickets in client workspace (Phase 1 / Phase 2 / Phase 3 / Track & Measure).
- Insert/refresh `client_workspace` row in Supabase with `state='work_in_progress'`.
- Lock audit baseline in tier-2 duckdb (immutable copy tagged `accepted-<date>`).
- Spawn a Notion linear / GitHub issue per ticket (configurable per client).

### 6.4 Railway backend (shared multi-tenant)

- **One** Railway service (`klicksmartai-pipeline`).
- Multi-tenant via `client_slug` in URL + middleware.
- Endpoints:
  - `POST /engagements` — create engagement (HITL)
  - `GET  /engagements/:slug` — fetch state + score
  - `POST /webhooks/stripe` — payment events
  - `POST /webhooks/vercel` — deploy events
  - `GET  /client/:slug` — render the client portal (HTML)
- Storage: Supabase (Tier 3) for state + audit data; tier-2 duckdb not exposed to Railway (stays local).
- Secrets: `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `SUPABASE_SERVICE_ROLE_KEY`, `VERCEL_TOKEN`.

### 6.5 Vercel deploy (per-client URL)

- On `DELIVERED` + HITL approval: trigger Vercel deploy via MCP.
- Target: `klicksmartai.com/client/<slug>/` (subpath) OR `<slug>.klicksmartai.com` (subdomain — owner choice).
- Build: static Next.js site with data pulled from Railway `/client/:slug`.
- No build secrets needed beyond `RAILWAY_API_URL`.

## 7. Non-functional requirements

| req | description |
|---|---|
| **Latency** | page first-paint <2s on 3G; Stripe checkout redirect <1s |
| **Reliability** | Stripe webhook MUST be retried (idempotency keys); Supabase row updates atomic |
| **Security** | All Stripe endpoints verify signature; no secrets in client code; Supabase RLS enabled on engagement tables; client portal read-only |
| **HITL** | Every external side-effect (charge, deploy, workflow spawn) gated on explicit owner approval — no autonomous billing, no autonomous deploy |
| **Audit** | Every state transition logged to `audit_log` table + mnemosyne canonical fact store |
| **Cost** | Railway free/developer tier + Stripe 2.9% + 30¢/txn; target <$15/mo infra at 1 engagement/mo |
| **Reusability** | Skill produces report from any slug with workspace metadata; no per-client hard-coding |

## 8. Tech stack

| layer | tool |
|---|---|
| Skill authoring | Hermes Agent (`skill_manage` + `~/.hermes/skills/productivity/seo-client-report/`) |
| Report generation | Jinja2 templates + Python (`scripts/build_report.py`) |
| Backend | Node.js + Express on Railway (TypeScript) |
| DB | Supabase (Tier 3, project `amgknqnhiscryvcfeoyj`) |
| Payments | Stripe Checkout (hosted) |
| Frontend (client portal) | Next.js + Tailwind, deployed on Vercel |
| Email | Resend OR Gmail API (existing config) |
| Workflow trigger | Hermes kanban MCP (existing) + Notion linear (existing) |

## 9. Build phases (suggested 4-week sprint)

| week | deliverable |
|---|---|
| W1 | `seo-client-report` skill (md + html output, no payments yet). Generates CLIENT-SCORE + cover letter + portal URL. **Smoke-test against existing gpc + veritas data.** |
| W2 | Railway backend scaffold (Express + Supabase client + `/engagements` + `/client/:slug` endpoints). Deployed to Railway staging. **No Stripe yet.** |
| W3 | Stripe Checkout integration + webhooks + idempotency. Test mode. **HITL-gated charges.** |
| W4 | Vercel deploy automation + end-to-end test with one synthetic engagement (gpc or veritas). **HITL-gated deploys.** |

Each week ends with a smoke test + owner demo.

## 10. Open questions / risks

| # | question | resolution path |
|---|---|---|
| R1 | **No `STRIPE_SECRET_KEY` yet** | build scaffolding now, plug in when available; test mode key from Stripe dashboard is fine for dev |
| R2 | **No `RAILWAY_TOKEN` yet** | same — scaffold locally; deploy later |
| R3 | **Multi-tenant security** | Supabase RLS policies must scope engagement reads by `client_slug`; client never sees other clients' data |
| R4 | **Refund logic** | if Dennis rejects post-payment, full refund auto-fires — but does Stripe allow refund-without-customer-action? Yes, via API |
| R5 | **Custom domain per client** | v1 uses `klicksmartai.com/client/<slug>/`; custom domain (e.g. `veritas-seo.klicksmartai.com`) is a v2 feature |
| R6 | **Stripe Connect / payouts** | not in v1; if KlickSmartAI ever sub-contracts work, revisit |
| R7 | **Client portal UX** | v1 = single-page report + Accept button; v2 = full dashboard with progress, files, messages |

## 11. Success criteria

- ✅ `seo-client-report` skill generates CLIENT-SCORE + portal URL for any slug in <30s
- ✅ Test-mode Stripe deposit captured end-to-end against a synthetic client
- ✅ Railway service running, `/client/:slug` renders real engagement data
- ✅ Vercel production deploy fires on Dennis approval, returns 200 on the public URL
- ✅ One real engagement (gpc OR veritas) fully processed through the pipeline (audit → accept → deposit → workflow → deliver → final payment → URL)
- ✅ Smoke test 16/16 green across all 8 pipeline states
- ✅ HITL gates verified — no autonomous charge, no autonomous deploy

## 12. Out of scope (explicit)

- Client portal messaging / chat
- File upload / S3 / asset hosting
- Contract / e-signature
- Time tracking / agency internal hour logging
- Multi-currency (USD only in v1)
- International tax (Stripe Tax handled by Stripe dashboard manually)
- Client-side analytics dashboard (out — Tier 3 Supabase is the data layer; Frappe / dashboards read it)

---

**next step:** Dennis reviews this PRD → either approves & schedules W1 build, or amends scope.

**file path:** `~/wiki/processes/seo-client-acceptance-deploy-prd.md`
**status:** DRAFT
**linked PRDs:** `seo-client-onboarding-sprint.md`, `seo-organic-growth-playbook.md`, `frappe-workspace-preliminary-plan.md` (Tier 4 context)
