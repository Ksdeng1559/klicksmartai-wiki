# Spectraholdings Wiki Schema

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

## Standard Frontmatter

```yaml
---
title:
created:
updated:
type:
status:
confidence:

tags: []

sources: []

relationships:
  - related_to:
  - depends_on:
  - supports:

contradictions: []

decision_impact: []
---
```

## Page Types

Allowed page types:

- entity
- concept
- agent
- workflow
- prompt
- summary
- decision
- validation
- comparison
- query
- raw-index

## Core Tags

### Organization

- spectra
- subsidiary
- partner
- municipality
- investor
- nonprofit
- landowner

### Finance

- mcf
- capital-stack
- cdfi
- municipal-bond
- donor-advised-fund
- opportunity-zone
- qof
- grant
- debt
- equity

### Real Estate

- housing
- land
- development
- entitlement
- zoning
- construction
- asset-management

### Market

- county
- census
- affordability
- migration
- wages
- housing-demand
- disaster-risk

### Operations

- vertical-integration
- manufacturing
- supply-chain
- anchor-hub
- concrete
- fabrication
- energy-tech

### Outputs

- investor-brief
- county-brief
- landowner-brief
- pro-forma
- feasibility
- decision-brief

## Decision Standard

No output is complete unless it answers:

1. Should we proceed?
2. What are the risks?
3. What improves the deal?
4. What breaks the deal?
5. What data is missing?

## Confidence Scoring

Use:

- `0.90-1.00` = highly sourced / validated
- `0.75-0.89` = strong but needs review
- `0.50-0.74` = directional only
- below `0.50` = do not use for investor materials

## Contradiction Handling

When new information conflicts with existing content:

1. Do not overwrite silently.
2. Record the contradiction in frontmatter.
3. Add both claims with source/date.
4. Flag for review in `validations/`.
5. Update `log.md`.

## Knowledge Graph Relationships

Allowed relationship types:

- related_to
- depends_on
- supports
- funds
- validates
- contradicts
- supersedes
- requires
- impacts
- part_of
- produces
- owned_by
