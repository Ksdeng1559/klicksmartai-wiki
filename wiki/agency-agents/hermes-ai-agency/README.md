# Hermes AI Agency — Vault

This folder is the agency knowledge base. It is designed to be ingested by any AI agent (Hermes, Claude Code, Codex, etc.) without custom tooling.

## How to read this vault

1. **`AGENTS.md`** — operating rules, escalation list, continuity policy. Read first.
2. **`DASHBOARD.md`** — live status: what services are live, what's running, what's blocked.
3. **`KANBAN.md`** — active work, owners, due dates, artifact links.
4. **`REGISTRY.md`** — index of departments and AI employees with links to their profiles and SOUL.md files.
5. **`DECISIONS.md`** — dated log of CEO decisions.
6. **`NOTES.md`** — chief-of-staff running notes (working memory).
7. **Department profiles** in `departments/<name>/PROFILE.md` and `SOUL.md`.
8. **Employee profiles** in `employees/<name>/SOUL.md`.
9. **Service offers** in `service-offers/<offer>/`.
10. **Marketing, sales, delivery** in their respective folders.

## Conventions

- Files are markdown, Obsidian-readable.
- SOUL.md files describe an AI employee's voice, scope, and constraints.
- Decision entries are append-only and dated (ISO 8601).
- Customer PII does NOT live in the vault — it lives in the CRM/transactional layer.
- API keys do NOT live in the vault — they live in `~/.hermes/profiles/<profile>/.env`.

## Out of scope (here)

- Customer PII (deal-specific data, owner contact details beyond publicly-published business info)
- Pricing templates awaiting CEO sign-off (those live in `service-offers/<offer>/PRICING.md` once approved)
- Outreach copy awaiting CEO sign-off (those live in `sales/outreach-sequences.md` once approved)

## Updated 2026-06-30

- **Canonical codebase:** Lead Sniper 3.0 at `C:\Users\denni\AI-Applications\LeadSniper-3.0\` (from `github.com/Ksdeng1559/LeadSniper-3.0`)
- **Supabase backend:** project `yolqrstktoqlszybwymw` (live, 375 leads, 71 battle_cards)
- **Audit capability:** 6-signal outdated detection verified end-to-end (8-site batch, 43% hit rate)
- **Active playbook:** `okf/leadsniperai/playbooks/phase-2-continuous-discovery.md` (proposed, awaiting CEO approval)
