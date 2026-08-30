-- ============================================================================
-- Veritas Client Workspace — Phase A schema v1.2.0
-- MotherDuck-compatible, multi-agent readable
-- Existing 3 tables (client_scores, client_score_keyword_tiers,
-- client_score_history) are PRESERVED unchanged.
--
-- Changelog:
-- v1.1.0 (2026-08-28) - added owner_contact_id FK to client_decisions
--                       (replaces ambiguous first-name owner column for JOINs)
-- v1.2.0 (2026-08-28) - added wiki_path + wiki_published_at to
--                       client_deliverables so workspace tracks its own
--                       publication state (no duplicate publishes,
--                       last-known-publish timestamp)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- Table 1: clients
-- One row per client workspace. Workspace IS the DB — this row IS the
-- identity record. agents read this first to know who they're serving.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS clients (
    client_slug         TEXT PRIMARY KEY,           -- 'veritas-developments'
    client_display      TEXT NOT NULL,              -- 'Veritas Development Group LLC'
    domain              TEXT,                       -- 'veritasdevelopmentgroupllc.com'
    domain_alt          TEXT,                       -- 'veritas-developments.com' (parked)
    client_status       TEXT NOT NULL,              -- 'active' | 'paused' | 'archived'
    client_tier         TEXT,                       -- 'pilot' | 'standard' | 'strategic'
    industry            TEXT,                       -- 'commercial-construction'
    geography           TEXT,                       -- 'kc-metro' | 'kc-mo' | 'national'
    primary_contacts    TEXT,                       -- JSON array: [{name,role,email,phone}]
    created_by          TEXT NOT NULL,              -- 'dennis' (the founder, not an agent)
    created_at          TIMESTAMP NOT NULL,
    onboarded_at        TIMESTAMP,
    notes               TEXT
);

-- ----------------------------------------------------------------------------
-- Table 2: client_deliverables
-- The canonical workspace. Every deliverable = one row. Markdown + HTML both
-- stored so any LLM can read body_md and any browser/agent can read body_html.
-- path_md / path_html keep IDE/external-edit affordances.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_deliverables (
    deliverable_id      TEXT PRIMARY KEY,           -- 'audit-v4-2026-08-28'
    client_slug         TEXT NOT NULL,              -- FK -> clients
    kind                TEXT NOT NULL,              -- 'audit' | 'cover-memo' | 'client-score' | 'quote' | 'proposal' | 'one-pager'
    title               TEXT NOT NULL,
    status              TEXT NOT NULL,              -- 'draft' | 'released' | 'sent' | 'archived'
    version             INTEGER NOT NULL DEFAULT 1,
    body_md             TEXT NOT NULL,              -- canonical markdown (LLM-readable)
    body_html           TEXT NOT NULL,              -- rendered HTML (browser/agent-readable)
    path_md             TEXT,                       -- ~/wiki/clients/.../foo.md (optional external editor path)
    path_html           TEXT,                       -- projects-preview/foo.html
    word_count          INTEGER,
    parent_deliverable_id TEXT,                     -- e.g. cover memo's parent = audit v4
    tags                TEXT,                       -- JSON array: ['kc-area','roi','foundation-gap']
    audience            TEXT,                       -- 'client' | 'internal' | 'mixed'
    created_by          TEXT NOT NULL,              -- 'hermes' | 'claude-code' | 'chatgpt' | 'dennis'
    created_at          TIMESTAMP NOT NULL,
    updated_by          TEXT,
    updated_at          TIMESTAMP,
    released_by         TEXT,
    released_at         TIMESTAMP,
    wiki_path           TEXT,                       -- 'entities/veritas-developments.md' (set when published to wiki)
    wiki_published_at   TIMESTAMP,                   -- when this deliverable last went live in the wiki
    notes               TEXT
);

CREATE INDEX IF NOT EXISTS idx_deliverables_client_status
    ON client_deliverables (client_slug, status);

CREATE INDEX IF NOT EXISTS idx_deliverables_kind
    ON client_deliverables (client_slug, kind);

-- ----------------------------------------------------------------------------
-- Table 3: client_deliverable_sections
-- Sections within a deliverable, queryable individually. Built so a new agent
-- can ask "what's the ROI section say?" without scanning the whole body.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_deliverable_sections (
    section_id          TEXT PRIMARY KEY,
    deliverable_id      TEXT NOT NULL,              -- FK -> client_deliverables
    client_slug         TEXT NOT NULL,
    section_order       INTEGER NOT NULL,
    section_heading     TEXT NOT NULL,              -- '## 4-dimension scoring'
    section_anchor      TEXT,                       -- 'scoring-rubric' (URL-safe)
    section_body_md     TEXT NOT NULL,
    word_count          INTEGER,
    created_by          TEXT NOT NULL,
    created_at          TIMESTAMP NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_sections_deliverable
    ON client_deliverable_sections (deliverable_id, section_order);

-- ----------------------------------------------------------------------------
-- Table 4: client_decisions
-- Every decision point the client needs to make — single source of truth,
-- queryable for "what's blocking?" without parsing markdown.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_decisions (
    decision_id         TEXT PRIMARY KEY,           -- 'veritas-c3-regd-adjacency'
    client_slug         TEXT NOT NULL,
    decision_label      TEXT NOT NULL,              -- 'C3: Reg-D adjacency on financing guide'
    decision_category   TEXT NOT NULL,              -- 'compliance' | 'positioning' | 'scope' | 'budget' | 'timeline'
    decision_status     TEXT NOT NULL,              -- 'open' | 'pending-client' | 'resolved' | 'deferred' | 'cancelled'
    decision_priority   TEXT NOT NULL,              -- 'P1' | 'P2' | 'P3'
    related_deliverable_id TEXT,
    raised_by           TEXT NOT NULL,              -- 'hermes' | 'claude-code' | 'dennis' | 'chatgpt'
    raised_at           TIMESTAMP NOT NULL,
    owner               TEXT,                       -- human label: 'David' | 'Daniel' | 'Dennis'
    owner_contact_id    TEXT,                       -- FK -> client_contacts.contact_id (preferred for JOINs)
    options             TEXT,                       -- JSON array of {label, description, tradeoffs}
    chosen_option       TEXT,
    resolved_at         TIMESTAMP,
    resolved_by         TEXT,
    context_md          TEXT,                       -- why this decision exists
    impact_if_unresolved TEXT
);

CREATE INDEX IF NOT EXISTS idx_decisions_client_status
    ON client_decisions (client_slug, decision_status);

CREATE INDEX IF NOT EXISTS idx_decisions_priority
    ON client_decisions (client_slug, decision_priority, decision_status);

-- ----------------------------------------------------------------------------
-- Table 5: client_conversations
-- Per-deliverable chat history. Any agent appends. Append-only — never edit.
-- Each row = one message in one conversation thread.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_conversations (
    message_id          TEXT PRIMARY KEY,
    client_slug         TEXT NOT NULL,
    thread_id           TEXT NOT NULL,              -- groups messages into one conversation
    related_deliverable_id TEXT,
    role                TEXT NOT NULL,              -- 'user' | 'assistant' | 'system' | 'tool'
    agent               TEXT NOT NULL,              -- 'dennis' | 'hermes' | 'claude-code' | 'chatgpt'
    body_md             TEXT NOT NULL,
    in_reply_to         TEXT,                       -- FK -> message_id (for threading)
    created_at          TIMESTAMP NOT NULL,
    metadata_json       TEXT                        -- model, tokens, etc.
);

CREATE INDEX IF NOT EXISTS idx_conversations_thread
    ON client_conversations (thread_id, created_at);

CREATE INDEX IF NOT EXISTS idx_conversations_client
    ON client_conversations (client_slug, created_at);

-- ----------------------------------------------------------------------------
-- Table 6: client_artifacts
-- Image refs, citation links, external file paths, screenshots. Lets the
-- workspace carry visual + bibliographic context alongside the text.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_artifacts (
    artifact_id         TEXT PRIMARY KEY,
    client_slug         TEXT NOT NULL,
    related_deliverable_id TEXT,
    artifact_kind       TEXT NOT NULL,              -- 'image' | 'citation' | 'screenshot' | 'pdf' | 'external-url' | 'data-table'
    artifact_label      TEXT NOT NULL,
    artifact_uri        TEXT NOT NULL,              -- file://, https://, or relative path
    artifact_caption    TEXT,
    artifact_metadata_json TEXT,
    created_by          TEXT NOT NULL,
    created_at          TIMESTAMP NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_artifacts_client
    ON client_artifacts (client_slug, artifact_kind);

-- ----------------------------------------------------------------------------
-- Table 7: client_audit_log
-- Append-only event log. Every agent's contribution traceable. The TRUE
-- history table — survives deletions in deliverables.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_audit_log (
    event_id            TEXT PRIMARY KEY,
    client_slug         TEXT NOT NULL,
    event_type          TEXT NOT NULL,              -- 'created' | 'updated' | 'released' | 'sent' | 'archived' | 'decision-raised' | 'decision-resolved' | 'note'
    event_target_type   TEXT,                       -- 'deliverable' | 'decision' | 'contact' | 'client'
    event_target_id     TEXT,
    agent               TEXT NOT NULL,              -- 'dennis' | 'hermes' | 'claude-code' | 'chatgpt'
    summary             TEXT NOT NULL,
    detail_md           TEXT,
    related_artifact_ids TEXT,                      -- JSON array
    created_at          TIMESTAMP NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_audit_client_time
    ON client_audit_log (client_slug, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_audit_target
    ON client_audit_log (event_target_type, event_target_id);

-- ----------------------------------------------------------------------------
-- Table 8: client_contacts
-- People involved with the client. David, Daniel, future team members.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client_contacts (
    contact_id          TEXT PRIMARY KEY,           -- 'david-poole'
    client_slug         TEXT NOT NULL,
    contact_name        TEXT NOT NULL,
    contact_role        TEXT,                       -- 'CEO' | 'CFO' | 'Managing Partner' | 'VP Engineering'
    contact_email       TEXT,
    contact_phone       TEXT,
    contact_linkedin    TEXT,
    contact_status      TEXT NOT NULL,              -- 'primary' | 'secondary' | 'prospect' | 'inactive'
    decision_authority  TEXT,                       -- 'final' | 'consult' | 'none' (for approval flows)
    response_state      TEXT,                       -- 'awaiting-reply' | 'engaged' | 'declined' | 'no-reply'
    last_contact_at     TIMESTAMP,
    notes               TEXT,
    created_by          TEXT NOT NULL,
    created_at          TIMESTAMP NOT NULL,
    updated_at          TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_contacts_client
    ON client_contacts (client_slug, contact_status);

-- ----------------------------------------------------------------------------
-- View 1: v_client_ready
-- "What's ready to send to the client right now?" — single SQL any agent runs.
-- Cross-joins deliverables with their parent score (if any), deduplicated.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_client_ready AS
SELECT DISTINCT
    d.deliverable_id,
    d.client_slug,
    d.kind,
    d.title,
    d.status,
    d.version,
    s.score_overall,
    s.score_tier,
    s.year1_roi_pct,
    s.year2_roi_pct,
    s.breakeven_month,
    d.released_at,
    d.released_by,
    d.word_count,
    d.path_md,
    d.path_html
FROM client_deliverables d
LEFT JOIN client_scores s
    ON s.client_slug = d.client_slug
WHERE d.status = 'released'
  AND d.audience IN ('client', 'mixed');

-- ----------------------------------------------------------------------------
-- View 2: v_pending_decisions
-- "What's blocking forward motion?" — open + pending-client decisions.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_pending_decisions AS
SELECT
    decision_id,
    client_slug,
    decision_label,
    decision_category,
    decision_status,
    decision_priority,
    related_deliverable_id,
    owner,
    raised_at,
    impact_if_unresolved,
    context_md
FROM client_decisions
WHERE decision_status IN ('open', 'pending-client')
ORDER BY
    CASE decision_priority WHEN 'P1' THEN 1 WHEN 'P2' THEN 2 ELSE 3 END,
    raised_at;

-- ----------------------------------------------------------------------------
-- View 3: v_recent_activity
-- Last 30 days of audit events. agents use this to see what's been done.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_recent_activity AS
SELECT
    event_id,
    client_slug,
    event_type,
    event_target_type,
    event_target_id,
    agent,
    summary,
    created_at
FROM client_audit_log
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '30 days'
ORDER BY created_at DESC;
