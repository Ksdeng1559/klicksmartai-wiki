-- ============================================================================
-- Migration: v1.1.0 -> v1.2.0
-- Date: 2026-08-28
-- Author: Hermes
-- Apply with: python3 ../../../../../tmp/migrate_v120.py
--             (or run ALTER TABLE statements directly)
-- ============================================================================
--
-- Purpose: Add wiki_path + wiki_published_at to client_deliverables so the
-- workspace tracks its own publication state. Prevents duplicate publishes,
-- records last-known-publish timestamp, and gives every agent a single SQL
-- to ask "is this RELEASED deliverable also published to wiki?"
--
-- Idempotency: Safe to re-run. ALTER TABLE ADD COLUMN will fail in DuckDB
-- if the column already exists — wrap in a check or use a Python migration
-- script that DESCRIBEs first.

ALTER TABLE client_deliverables ADD COLUMN wiki_path TEXT;
ALTER TABLE client_deliverables ADD COLUMN wiki_published_at TIMESTAMP;

-- Update schema_version row (do this from Python; SQL below is reference):
--   UPDATE client_workspace_meta
--   SET meta_value = '1.2.0', updated_at = CURRENT_TIMESTAMP
--   WHERE meta_key = 'schema_version';

-- Append migration event (do this from Python; SQL below is reference):
--   INSERT INTO client_audit_log
--     (event_id, client_slug, event_type, event_target_type, event_target_id,
--      agent, summary, created_at)
--   VALUES
--     ('migration-v1.2.0-<utc-timestamp>', 'veritas-developments',
--      'schema-migrated', 'schema', 'v1.2.0', 'hermes',
--      'v1.1.0 -> v1.2.0: added wiki_path + wiki_published_at columns',
--      CURRENT_TIMESTAMP);

-- Backfill existing RELEASED deliverables (run from Python; example SQL):
--   UPDATE client_deliverables
--   SET wiki_path = 'entities/veritas-developments.md',
--       wiki_published_at = '2026-08-28T19:00:00Z'
--   WHERE status = 'released' AND wiki_path IS NULL;

-- ============================================================================
-- ROLLBACK (not auto-applied; only if needed):
--   ALTER TABLE client_deliverables DROP COLUMN wiki_published_at;
--   ALTER TABLE client_deliverables DROP COLUMN wiki_path;
--   UPDATE client_workspace_meta SET meta_value = '1.1.0' WHERE meta_key = 'schema_version';
-- ============================================================================
