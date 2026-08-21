# RIOS — Relationship Intelligence Operating System

RIOS is the relationship and opportunity intelligence layer inside the KlickSmartAI Knowledge Wiki ecosystem.

## Purpose

RIOS turns signals, relationships, funding opportunities, and institutional knowledge into actionable business development intelligence.

Traditional CRM systems answer:

```text
What stage is this contact in?
```

RIOS answers:

```text
Why should we engage now?
What opportunity exists?
Who knows whom?
What funding aligns?
What problem matters most?
What action should occur next?
```

## Operating Loop

```text
Signal
→ Context
→ Relationship Intelligence
→ Opportunity
→ Action
→ Learning Loop
```

## Core Objects

- Organization
- Person
- Relationship
- Signal
- Opportunity
- Battlecard
- Meeting
- Policy
- Funding Source
- Lead *(ClientFlow intake)*
- Advisor
- IntakeSession
- Subscriber *(MIX pipeline)*

## Stack

| Layer | Tool / System | Function |
|-------|---------------|----------|
| Signal monitoring | Hermes | Scheduled research and change detection |
| Knowledge source | GitHub Wiki / Obsidian | Source of truth |
| Graph memory | Graphify | Entity and relationship mapping |
| Semantic memory | Pinecone | Vector search and retrieval |
| Local analytics | DuckDB | Fast local scoring and staging |
| Cloud storage | MotherDuck | Shared opportunity graph and historical records |
| Reasoning | Claude / GPT / Gemini | Battlecards, briefs, scoring, proposals |
| Outreach | SendGrid | Email delivery and tracking |
| Video | Vidyard | Personalized executive engagement |
| Relationship capture | Unipile | LinkedIn/email sync and conversation history |

## Key Questions

1. Who should we contact?
2. Why now?
3. What problem do they have?
4. What opportunity exists?
5. What funding aligns?
6. Who knows them?
7. Who can provide a warm introduction?
8. What action should happen next?
9. What should the outreach say?
10. What did we learn from the last interaction?
