# RIOS Battlecard Schema

A battlecard is the core actionable intelligence output of RIOS.

It answers:

```text
Why this person?
Why this organization?
Why now?
What should we say?
What should happen next?
```

## Battlecard JSON Schema

```json
{
  "battlecard_id": "",
  "created_at": "",
  "target_person": {
    "name": "",
    "title": "",
    "organization": "",
    "email": "",
    "linkedin": ""
  },
  "target_organization": {
    "name": "",
    "type": "",
    "location": "",
    "website": ""
  },
  "why_now": "",
  "opportunity_summary": "",
  "relationship_context": {
    "known_connections": [],
    "warm_intro_paths": [],
    "relationship_strength": 0,
    "confidence": 0
  },
  "funding_context": {
    "programs": [],
    "agency_alignment": [],
    "grant_or_sbir_fit": "",
    "deadline_notes": ""
  },
  "recommended_message": {
    "email_subject": "",
    "email_body": "",
    "video_briefing_angle": "",
    "linkedin_note": ""
  },
  "next_best_action": "",
  "risks_and_assumptions": [],
  "source_links": [],
  "score": {
    "opportunity_score": 0,
    "relationship_score": 0,
    "urgency_score": 0,
    "overall_priority": 0
  }
}
```

## Required Narrative Sections

Each battlecard should include:

- why now
- likely priorities
- relationship map
- funding opportunities
- opportunity summary
- recommended outreach
- next-best actions
- risks and assumptions
- suggested follow-up sequence

## Execution Path

```text
Battlecard
→ SendGrid email
→ Vidyard video briefing
→ Unipile relationship capture
→ RIOS learning update
```
