# SpectraHoldings Wiki Schema

## Purpose

This schema governs how knowledge is stored, updated, validated, and used by AI agents supporting Spectra Holdings Group.

The wiki exists to produce standardized, repeatable, and decision-ready financial intelligence for capital formation, project execution, and enterprise-level decision making.

## Operating Standard

Every output must follow:

```text
INPUT -> MODEL -> VALIDATION -> DECISION -> OUTPUT
```

No output is complete unless it supports one of five decisions:

- Proceed
- Pause
- Restructure
- Reject
- Request more data

## Naming Rules

- Use lowercase file names.
- Use hyphens instead of spaces.
- Use clear names that agents can retrieve.
- Every page must include YAML frontmatter.
- Every page should link to at least two related pages using wikilinks.
- Every material update must be recorded in `log.md`.
- Every new page must be added to `index.md`.
