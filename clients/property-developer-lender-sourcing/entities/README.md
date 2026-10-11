# Entities

One record per developer / sponsor / institutional contact. Schema:

```markdown
---
entity_type: developer | sponsor | contact | advisor
name: Full legal name
slug: kebab-case
created: YYYY-MM-DD
status: draft | approved | archived
---

# Entity Name

## Identity
- Legal name, jurisdiction of formation, EIN (if available)
- Principal(s) with contact info
- Website

## Track record
- Completed projects
- Pipeline
- AUM / capital deployed

## Capital relationships
- Existing debt providers
- Existing equity partners
- Existing referral channels (law firm, CPA, wealth manager)

## Compliance
- Securities registration status
- State MLO licenses held
- Broker-dealer affiliations
- Reg D filings

## Notes
- Working hypothesis + open questions
- Warm-intro paths
```

## Placeholder

- `_template-entity.md` — empty template (see below)

## When to create

- New developer signs engagement letter
- New advisor / contact becomes a referral channel
- New institutional relationship gets a record
