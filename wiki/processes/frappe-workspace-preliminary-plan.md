# Plan: Frappe CRM as Workspace Layer for KlickSmartAI Client Deliverables

**Status:** Preliminary draft for review
**Author:** Hermes (CoS)
**Date:** 2026-08-28
**Related context:** `processes/lead-sniperai-cli-os.md` (Tier-4 designation), `clients/veritas-developments/drafts/website/v2-plan-brief-2026-08-28.md` (Evermont `Capital Mandate` DocType)

---

## 1. Why Frappe, and what role it plays

Per the existing `lead-sniperai-cli-os.md` SOP, our data architecture is 4 tiers:

```
Tier 1: SOURCE       CSV / Apollo / Tavily / Apify / Deepline / Manual
   │
   ▼
Tier 2: LOCAL        DuckDB + adapter layer (gitignored)
   │
   ▼ PASS-graded
Tier 3: SUPABASE     yolqrstktoqlszybwymw.supabase.co (canonical schema)
   │
   ▼
Tier 4: FRAPPE CRM   Customer 360 / action surface  ◀─ THIS PLAN
```

**Boundary rule (existing):** Tier 3 is read-only for downstream consumers; Tier 4 mirrors Tier 3 but never writes back.

**The current gap:** Tiers 1–3 are about *intelligence* (leads, signals, opportunities). They do **not** model:
- Client workspaces (which wiki clients/ are, today)
- Per-client deliverables (drafts → projects → deliverables)
- Per-client pipeline (Veritas investor materials, GPC SEO audits, Spectra county research)
- Human action items, owner accountability, approval audit trail

**Frappe fills that gap.** It becomes the **Customer 360 / Action Surface** — humans (Dennis, David, Daniel, future consultants) do outreach, approvals, and follow-ups in Frappe; intelligence (leads, signals) stays in Tiers 1–3.

---

## 2. What goes in Frappe vs. what stays where

| Layer | Owned by | Why |
|---|---|---|
| **Leads, signals, opportunities** | Supabase (Tier 3) | Schema-source-of-truth, multi-tenant, migration-tracked |
| **Source-of-truth docs, drafts, code** | GitHub wiki (`~/wiki`) | Version-controlled, reviewable, public to client when shared |
| **Approval workflow, task state, audit** | Frappe (Tier 4) | Workflow engine, assignment, comments, attachments |
| **Contact 360, deal pipeline, activity log** | Frappe (Tier 4) | Native CRM affordances |
| **Kanban state (today)** | `~/.hermes/kanban.db` | Hermes-internal worker dispatch |
| **Eventually:** Kanban state | Frappe Custom DocType (mirror) | One kanban to rule them all |

The **wiki stays the document substrate**. Frappe becomes the **work substrate**.

---

## 3. Proposed DocTypes

Frappe ships with `Customer`, `Contact`, `Lead`, `Opportunity`, `Task`, `Project`, `ToDo`. We'll mostly **use stock + 6 custom DocTypes** rather than rebuild.

### 3.1 Stock DocTypes (configured, not coded)

| DocType | Config | Notes |
|---|---|---|
| **Customer** | One record per `clients/<slug>/` (linked to `Client Workspace` custom DT) | Maps directly to our 10 wiki clients |
| **Contact** | One per stakeholder (David, Daniel, Dennis, future consultants) | |
| **Lead** | Inbound prospect per client (from Tier-3 Supabase `leads`) | Mirrored from Tier 3 via scheduled job |
| **Opportunity** | One per engagement or pipeline item | Maps to `projects/<slug>/<engagement>/` |
| **ToDo / Task** | Owner-assigned action items | Replaces our ad-hoc `VALIDATION_QUEUE.md` rows |
| **Project** | Roll-up under Customer for grouping deliverables | |
| **Event** | Calendar/follow-up cadence | Mirrors `relationships/current.md` |

### 3.2 Custom DocTypes (the workspace layer)

```
Client Workspace
├── name: slug (e.g. "veritas-developments")
├── customer: link → Customer (the wiki client's CRM-side record)
├── tier_3_supabase_project_id: data (e.g. Supabase project uuid)
├── canonical_workspace_path: data (e.g. /home/denni/wiki/clients/veritas-developments)
├── identity: long text (parsed from CLAUDE.md / IDENTITY.md, kept fresh)
├── last_synced_at: datetime
└── sync_state: select (idle | syncing | error)

Deliverable
├── workspace: link → Client Workspace
├── title: data
├── lane: select [drafts, review, approved, delivered]
├── subcategory: data (seo, outreach, deck, …)
├── source_file_path: data (wiki-relative path)
├── tier_3_supabase_id: data (cross-tier key, nullable)
├── kanban_task_id: data (mirrored Hermes kanban t_xxx, nullable)
├── idempotency_key: data (slug:lane:relpath — same as seed-kanban-from-clients.py)
├── status: select (auto-derived from lane)
├── created_at, updated_at: datetime
└── events: table → Deliverable Event

Deliverable Event
├── deliverable: link → Deliverable
├── kind: select (created, promoted_to_review, approved, revised, killed, delivered, commented)
├── actor: link → User
├── payload: long text (JSON of the change)
└── created_at: datetime

Approval Request                          ◀─ replaces VALIDATION_QUEUE.md
├── deliverable: link → Deliverable
├── requested_by: link → User
├── verdict: select (pending | approved | revise | killed)
├── reviewer: link → User
├── rationale: text
├── proposed_changes: long text
└── closed_at: datetime

Investor Mandate                          ◀─ Veritas Evermont requirement
├── workspace: link → Client Workspace
├── mandate_type: select (capital_raise, partnership, co_sponsor)
├── target_size_usd: currency
├── geography: data
├── target_profiles: long text
├── linked_deliverables: table → Deliverable
└── status: select (draft, in_review, issued, closed)
```

That's **6 custom DocTypes**, well under the maintenance burden of building a custom CRM.

---

## 4. Sync architecture

```
wiki/CLAUDE.md  ──┐
wiki/IDENTITY.md ──┤── (sync-clients-to-frappe.py, daily)
                  ├──► Frappe Customer + Client Workspace
Supabase leads   ──────► Frappe Lead + Contact 360
wiki/drafts/     ──┐
wiki/projects/   ──┤── (seed-deliverables-from-clients.py, on-demand)
wiki/deliverables──┘     │
                         ├──► Frappe Deliverable (per file)
                         └──► Hermes kanban.db (existing seeder)
```

### Two sync scripts to build:

**`sync-clients-to-frappe.py`**
- Scans `clients/<slug>/` for `CLAUDE.md`/`IDENTITY.md`
- Upserts `Customer` + `Client Workspace` records
- Idempotent on slug
- Daily cron

**`sync-deliverables-to-frappe.py`**
- Scans each client's `drafts/`, `projects/`, `deliverables/`
- Upserts `Deliverable` records keyed by `idempotency_key = {slug}:{lane}:{relpath}`
- Creates `Approval Request` records for items in `drafts/<subdir>/` with `VALIDATION_QUEUE.md` rows marked `pending`
- Writes `Deliverable Event` rows for state changes (diff vs. last sync)
- Reuses the same idempotency key as `seed-kanban-from-clients.py` — so **Hermes Kanban, Frappe Deliverables, and wiki folders all share one cross-system identity**

### One bidirectional link to build:

**Webhook: Frappe → Hermes chat**
- When `Approval Request.verdict = approved` fires, send a Telegram/Slack notification
- When `Deliverable.status` transitions, log to `task_events` in kanban.db
- This is the **HITL gate made visible** — Dennis's approval is now a Frappe action that propagates everywhere

### What we explicitly do NOT build (yet):

- **Replace Hermes Kanban with Frappe Kanban.** Hermes kanban.db is the worker dispatch substrate; Frappe is the human substrate. Mirror, don't migrate.
- **Migrate wiki docs into Frappe.** Frappe holds *references* (path, hash, last-edit) to wiki files, not their content.
- **Replace Supabase with Frappe for Tier 3.** Tier 3 is intelligence; Tier 4 is action. The boundary rule from `lead-sniperai-cli-os.md` stands.

---

## 5. Where to host Frappe

Three options:

| Option | Pros | Cons | Cost |
|---|---|---|---|
| **A. Frappe Cloud** | Zero ops, official, auto-upgrade | Vendor lock, vendor pricing | ~$25/user/mo |
| **B. Self-host via Docker on our WSL** | Full control, mirrors our existing Docker pattern (GPC OpenSEO) | We own uptime, backups, upgrades | Server cost (already have host) |
| **C. Self-host on a Hetzner/Contabo VPS** | Public URL, available to David/Daniel | New attack surface, new credentials to manage | ~$5-15/mo |

**Recommendation: B (self-host Docker on WSL).** Why:
- We already run OpenSEO (`127.0.0.1:3005`) and CCR (`127.0.0.1:3456`) on WSL — same ops pattern
- Frappe needs MariaDB + Redis + Node + Python — Docker Compose handles all of it
- Public access later via `local-backend-public-tunnel` (cloudflared) — proven pattern, no new ops surface
- Cost: $0 (use existing WSL host)

Phase 2: cloudflared tunnel so David/Daniel can access.

---

## 6. Phased rollout

### Phase 0 — Decision (today, ~30 min)
- [ ] Review this plan
- [ ] Decide on hosting (B recommended)
- [ ] Confirm scope: clients + deliverables + approvals + (optional) investor mandates for Veritas

### Phase 1 — Stand up Frappe locally (~2-3 hours)
- [ ] `docker compose up -d` Frappe + MariaDB + Redis via official `frappe_docker` stack
- [ ] Create site `workspace.localhost`
- [ ] Create 6 custom DocTypes above
- [ ] Seed 10 `Customer` + 10 `Client Workspace` records by hand for testing
- [ ] Verify dashboard renders + web form works
- **Gate:** Frappe loads in browser at `http://127.0.0.1:8000`

### Phase 2 — Sync clients + deliverables (~3-4 hours)
- [ ] Build `sync-clients-to-frappe.py` (pulls from `clients/<slug>/CLAUDE.md`)
- [ ] Build `sync-deliverables-to-frappe.py` (pulls from `drafts/`, `projects/`, `deliverables/`)
- [ ] Run once: confirm Veritas shows 8/11/8/7 deliverables
- [ ] Wire idempotency key shared with `seed-kanban-from-clients.py`
- **Gate:** Re-running sync is a no-op; new files appear; deleted files marked

### Phase 3 — Approval workflow (~3-4 hours)
- [ ] Migrate `VALIDATION_QUEUE.md` rows into `Approval Request` records
- [ ] Add Frappe workflow: `pending → approved | revise | killed`
- [ ] Add webhook from Frappe → Telegram on verdict change
- [ ] Test: create a draft in `clients/<slug>/drafts/`, run sync, see it as Approval Request in Frappe, approve it in Frappe, see Telegram notification
- **Gate:** HITL approval loop works end-to-end without touching chat

### Phase 4 — Public access (~2-3 hours)
- [ ] Add cloudflared tunnel to Frappe port 8000
- [ ] Create Frappe users for David, Daniel
- [ ] Permission rules: each user sees their assigned clients only
- **Gate:** David opens Frappe from his laptop, sees Veritas

### Phase 5 — Optional: Veritas investor mandates (~4-6 hours)
- [ ] Build `Investor Mandate` UI + workflow
- [ ] Add cross-link from `Deliverable` (decks, memos) to `Investor Mandate`
- [ ] Veritas-side validation with David
- **Gate:** Evermont raise workflow runs end-to-end in Frappe

**Total estimate: 14-20 hours of build work, across ~5 days.**

---

## 7. Risks & open questions

| Risk | Mitigation |
|---|---|
| Frappe Docker is heavy (~4 GB image, slow first build) | Use the official `frappe_docker` images; pre-pull; document in skill |
| Frappe has a steep learning curve (Python + JS + Jinja + DocType meta) | Phase 1 includes a 1-hour "Frappe in 60 min" walkthrough; reference existing wiki process docs |
| Frappe workflow engine is opinionated — may not match our 4-lane (drafts/review/approved/delivered) model | Keep Hermes Kanban as substrate; Frappe mirrors, not replaces |
| Tier-3 read-only rule could break if Frappe wants to write back | Reaffirm rule in `processes/lead-sniperai-cli-os.md`; add a "Tier 4 → Tier 3" block in the boundary diagram |
| David/Daniel learning curve on yet another tool | Frappe's stock UI is familiar (looks like any CRM); training budget = 30 min walkthrough |
| Self-hosted Frappe means we own backups | Phase 1 includes nightly `mariadb-dump` + S3 archive |
| WSL Frappe performance under WSL2 | If sluggish, move to bare-metal Linux; don't virtualize twice |

**Open questions for you:**
1. Hosting: A/B/C? (B recommended)
2. Scope: just clients + deliverables + approvals, or also investor mandates in Phase 1?
3. Users in Phase 4: just David/Daniel, or also any clients themselves (read-only portal)?
4. Backup target: do we have an S3 / B2 / similar already configured? (I don't see one in `~/.hermes/config.yaml`)
5. Should I draft this as a separate wiki page (`processes/frappe-workspace.md`) or extend `processes/lead-sniperai-cli-os.md`?

---

## 8. What I'll do once you approve

1. Save this plan to `~/wiki/processes/frappe-workspace.md` (or wherever you say)
2. Update memory: "Frappe CRM = Tier-4 workspace substrate, Docker self-host, 6 custom DocTypes planned"
3. Add a skill: `~/.hermes/skills/devops/frappe-docker-wsl` (mirror of `openseo-deploy` pattern)
4. Begin Phase 1 once you say **proceed to build**

---

**Bottom line:** Frappe is the right tool because we already designated it Tier 4. The risk isn't the technology — it's the scope creep. Phases 1–3 give us a working workspace layer in ~10 hours; Phase 5 is optional Veritas-specific add-on.
