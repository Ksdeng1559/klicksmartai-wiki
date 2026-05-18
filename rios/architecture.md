# RIOS Architecture

## System Flow

```text
External Intelligence Sources
        ↓
Hermes Signal Intelligence Layer
        ↓
GitHub Wiki / Obsidian Knowledge Layer
        ↓
Graphify + Pinecone Semantic Memory
        ↓
DuckDB Local Analytics
        ↓
MotherDuck Cloud Persistence
        ↓
Claude / GPT / Gemini Reasoning Layer
        ↓
SendGrid + Vidyard + Unipile Execution Layer
        ↓
Learning Layer
```

## External Intelligence Sources

- people
- organizations
- counties
- tribes
- government agencies
- investors
- projects
- policies
- funding opportunities
- news
- LinkedIn activity
- email activity
- meeting notes
- research reports
- SBIR solicitations
- SAM.gov
- Grants.gov

## Graph Intelligence Layer

Entities:

- Person
- Organization
- Project
- Community
- Funding Source
- Opportunity
- Signal
- Meeting
- Policy
- County
- Tribe
- Investor
- Agency

Relationships:

- knows
- works_with
- funds
- introduced
- advises
- partners_with
- belongs_to
- influences
- supports
- owns
- manages
- applies_to

## Learning Layer

RIOS updates:

- relationship score
- engagement activity
- meeting outcomes
- signal effectiveness
- response patterns
- opportunity outcomes
- agent effectiveness
- next-best-action performance
