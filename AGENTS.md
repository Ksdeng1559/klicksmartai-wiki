# Agent guidance — hermes-wiki

This wiki is the Hermes Agent knowledge base. Read SCHEMA.md before ingest.

**Two wikis, two purposes:**
- ~/wiki = KlickSmartAI client/operations wiki (Spectra, Dare2Dream, GTM, etc.)
- ~/hermes-wiki (this) = Hermes codebase + operator runbook + Dennis's env patterns

Do not duplicate content from ~/wiki here, and do not put Hermes-internals
into ~/wiki. They serve different masters.

**Source order:** Hermes source → installed skills → session history → memory → external docs.

**Confidence rule:** mark `confidence: low` for single-source claims; only
`high` when well-supported across multiple sources. Lint will surface
`confidence: low` pages for review.

**Provenance:** append `^[raw/articles/source.md]` to paragraphs on pages
synthesizing 3+ sources so claims trace back.

**Cross-reference every page** to at least 2 others via `[[wikilinks]]`.