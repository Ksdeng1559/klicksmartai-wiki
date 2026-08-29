# Agent × DuckDB Workspace Protocol

**Audience:** any AI agent (Claude Code, ChatGPT, Hermes, future tools) that needs to read or write KlickSmartAI client workspace data.

**Status:** Phase A complete (schema + 1 client seeded); Phase B in progress (this doc).

---

## Why this exists

KlickSmartAI client workspaces (Veritas, OpenSEO, GPC, etc.) live in **DuckDB files** at:

```
~/wiki/clients/<client-slug>/.local_tier/clients/<client-slug>.duckdb
```

Each file is the **canonical source of truth** for that engagement. Markdown deliverables, rendered HTML, scores, decisions, contacts, conversations, and audit events all live in the same file. The markdown files in `projects/website/` and HTML in `projects-preview/` are **derived** — they're regenerated from the DB.

This protocol makes the workspace **read-write for multiple agents** without conflict or silent overwrites.

---

## Quick start (read-only mode)

```python
import duckdb
DB = "/home/denni/wiki/clients/veritas-developments/.local_tier/clients/veritas-developments.duckdb"
con = duckdb.connect(DB, read_only=True)

# 1. What's ready to send to the client right now?
con.execute("SELECT * FROM v_client_ready").fetchall()

# 2. What's blocking forward motion?
con.execute("SELECT * FROM v_pending_decisions").fetchall()

# 3. What just happened (last 30 days)?
con.execute("SELECT * FROM v_recent_activity").fetchall()

# 4. Read a specific deliverable's markdown body (LLM-readable)
md = con.execute(
    "SELECT body_md FROM client_deliverables WHERE deliverable_id = ?",
    ['client-score-2026-08-28']
).fetchone()[0]

# 5. Read the DB-README (self-describing workspace)
readme = con.execute(
    "SELECT meta_value FROM client_workspace_meta WHERE meta_key = 'db_readme'"
).fetchone()[0]
print(readme)
```

That's it. No Hermes-specific tools, no custom clients. Plain SQL.

---

## Schema (11 tables + 3 views)

### Core identity
- **`clients`** — 1 row per workspace. `client_slug`, `client_display`, `domain`, `client_status`, `industry`, `geography`, `primary_contacts`.

### Deliverables (the workspace)
- **`client_deliverables`** — every audit, cover memo, score, quote. Has `body_md` (LLM-readable) and `body_html` (browser/agent-readable) side-by-side. Status: `draft` → `released` → `sent` → `archived`. Tracks `created_by` + `released_by` for multi-agent attribution.
- **`client_deliverable_sections`** — per-section breakdown. Useful when you only need a specific part (e.g., "show me the ROI section").

### Decisions
- **`client_decisions`** — pending + resolved decisions. Each row has `options` (JSON), `context_md`, `impact_if_unresolved`. View `v_pending_decisions` sorts by priority.

### People + conversations
- **`client_contacts`** — David, Daniel, etc. Has `decision_authority` (`final`/`consult`/`none`) so you know who actually signs off.
- **`client_conversations`** — per-deliverable chat history. **Append-only** — never edit past rows. Each message has `agent` (`dennis`/`hermes`/`claude-code`/`chatgpt`) so attribution is built-in.

### Reference data
- **`client_artifacts`** — images, citations, screenshots, external URLs.
- **`client_audit_log`** — append-only event timeline. **THE history table** — survives deletions elsewhere.
- **`client_workspace_meta`** — key/value config, including the DB-README itself.

### Scoring (Veritas is the pilot)
- **`client_scores`** — composite score + 4 dimensions + ROI numbers.
- **`client_score_keyword_tiers`** — per-tier keyword universe.
- **`client_score_history`** — time-series across audit cycles.

### Views
- **`v_client_ready`** — released deliverables + score.
- **`v_pending_decisions`** — open + pending-client decisions sorted by priority.
- **`v_recent_activity`** — last 30 days of audit events.

---

## Write protocol

**Append-only tables** (never UPDATE/DELETE):
- `client_audit_log`
- `client_conversations`

**Mutable tables** (UPDATE allowed but always log it):
- `client_deliverables` — only the owner (`dennis`) promotes draft → released.
- `client_decisions` — update `decision_status`, `chosen_option`, `resolved_at`, `resolved_by` when decided.
- `client_contacts` — update `response_state`, `last_contact_at` after outreach.

**Replace-only tables** (INSERT OR REPLACE):
- `clients` — single-row identity.
- `client_workspace_meta` — KV config.

### Before ANY write, append an audit event

```python
import duckdb, uuid
from datetime import datetime

con = duckdb.connect(DB)  # not read_only
event_id = f"evt-{uuid.uuid4().hex[:12]}"
agent = "claude-code"  # whoever you are
con.execute("""
    INSERT INTO client_audit_log
        (event_id, client_slug, event_type, event_target_type, event_target_id, agent, summary, created_at)
    VALUES (?, 'veritas-developments', ?, ?, ?, ?, ?, ?)
""", [event_id, event_type, target_type, target_id, agent, summary, datetime.utcnow()])
con.commit()
```

---

## Concurrency rules

**Local file locks** — DuckDB uses a single-writer model. Two agents writing at the same time will corrupt the file.

**Recommended pattern:**
1. Agent opens connection, writes within a transaction, commits, closes.
2. Don't hold the connection open across long thinking pauses.
3. If you must write, do it fast: INSERT + COMMIT + CLOSE.

**Read-only mode** is safest for non-owner agents:

```python
con = duckdb.connect(DB, read_only=True)
```

Read-only connections don't take the writer lock.

---

## Migration paths

| Target | When | How |
|---|---|---|
| **MotherDuck** | when multi-user cloud access is needed | `INSTALL motherduck; ATTACH 'md:veritas_workspace'; COPY FROM DATABASE veritas_workspace TO veritas_workspace;` — schema unchanged. |
| **Supabase** | only tables needing Postgres features (conversations, contacts) | `INSTALL postgres; ATTACH 'postgresql://user:pass@db.supabase.co:5432/postgres'; CREATE TABLE supabase.conversations AS SELECT * FROM client_conversations;` |
| **JSONL export** | for ChatGPT file upload | `COPY (SELECT body_md FROM client_deliverables WHERE status='released') TO '/tmp/veritas.jsonl';` |

---

## When to use this workspace

✅ Use the workspace when the user asks about:
- "What's ready to send to the client?"
- "What's blocking?"
- "Show me the audit" / "Show me the score" / "Show me the cover memo"
- "What did we decide on the Reg-D question?"
- "What's David and Daniel's status?"
- "What happened on 2026-08-28?"
- "Generate a quote for this engagement"

❌ Don't use the workspace for:
- Tax/accounting data (not stored here)
- Time tracking or invoicing (separate systems)
- Secrets / credentials (never store in DB)

---

## Phase history

| Phase | Status | What |
|---|---|---|
| A — Schema + Veritas seed | ✅ done (2026-08-28) | 8 new tables, 3 views, 1 client seeded with 3 RELEASED deliverables, 2 contacts, 2 decisions, 10 audit events. |
| B — Agent read API | ✅ done (2026-08-28) | DB-README embedded inside workspace; this protocol doc written. |
| C — Local concurrency hardening | ⏳ planned | WAL mode + connection-per-writer pattern doc + tests. |
| D — MotherDuck migration | ⏳ planned | When cloud access is needed. |
| E — Multi-client seeding | ⏳ planned | OpenSEO, GPC Development, etc. Same schema, different `.duckdb` files. |

---

## Worked example: a new agent joins

A new agent has never seen this workspace before. They want to figure out what's going on with Veritas.

```python
import duckdb
DB = "/home/denni/wiki/clients/veritas-developments/.local_tier/clients/veritas-developments.duckdb"
con = duckdb.connect(DB, read_only=True)

# Step 1: read the embedded README
readme = con.execute("SELECT meta_value FROM client_workspace_meta WHERE meta_key='db_readme'").fetchone()[0]
print(readme)

# Step 2: discover what's in the workspace
tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main' ORDER BY table_name").fetchall()
for (t,) in tables:
    count = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t:40}  {count} rows")

# Step 3: read the v_client_ready view (the canonical "what's ready" answer)
ready = con.execute("SELECT deliverable_id, kind, score_overall, year1_roi_pct FROM v_client_ready").fetchall()
for r in ready:
    print(f"  ready: {r[0]} ({r[1]}) score={r[2]}/100, Y1 ROI {r[3]}%")

# Step 4: read the v_pending_decisions view (the canonical "what's blocking" answer)
pending = con.execute("SELECT decision_id, decision_priority, owner, decision_label FROM v_pending_decisions").fetchall()
for r in pending:
    print(f"  pending: {r[1]} {r[0]} (owner: {r[2]}) — {r[3]}")
```

In ~10 lines of Python, a brand-new agent has full workspace context. **No Hermes-specific tools, no prior conversation, no schema knowledge required.**

That's the protocol. Keep it that simple.
