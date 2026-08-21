# Insurance Direct Canada — AI Recruitment Agent

## Overview
A Hermes-powered 24/7 recruitment portal / receptionist for Insurance Direct Canada. Receives resumes, scores candidates against a defined rubric, delivers a company video to qualified applicants, and follows up to schedule interviews with founders or HR.

## Architecture

```
Candidate (WhatsApp/Discord/Telegram via Native Hermes)
    └── Hermes Agent (24/7 portal/receptionist: Gemma 4 Vision)
            ├── Receive & parse resume
            │       ├── First name, last name, email
            │       └── Resume format: TBD (PDF upload / paste text / LinkedIn link)
            ├── Cross-platform deduplication check
            │       └── Candidate_UUID system
            ├── External scoring system
            │       └── IDC Rubric + Gemma 4 Vision analysis
            ├── Qualified candidate?
            │       ├── YES → Send company video (3–10 min)
            │       │           └── Follow-up: "Did you watch it? Interested in scheduling?"
            │       └── NO  → Reject / waitlist / flag
            └── Interview scheduling
                    └── Founders / HR
                    └── Mechanism: TBD (Calendly / Google Calendar / HR notification)
```

## Platform
- **Primary:** WhatsApp via native Hermes connection
- **Secondary:** Discord for admin/community, Telegram for testing
- **Bot name:** TBD (@InsuranceDirectCanadaBot via BotFather)

## Candidate Data Points
- First name
- Last name
- Email address
- Resume (file or text)

## Scoring System
- **Rubric:** IDC 6-category weighted rubric
- **External scoring engine:** Gemma 4 Vision (multimodal analysis)
- **Cross-platform deduplication:** Candidate_UUID system

## Video
- Provided by Insurance Direct Canada
- Length: 3–10 minutes
- Delivered to qualified candidates only
- Follow-up confirms candidate watched it before scheduling

## Open Questions
1. Resume format — PDF upload/preferred (native platform file upload)
2. WhatsApp first (primary), then Discord (admin), Telegram (testing)
3. Full scoring rubric — IDC 6-category weighted (Sales 35%, Fit 25%, Insurance Fit 15%, Experience 13%, [...])
4. Bot destination — native Hermes connections, no dedicated bot needed
5. Interview scheduling mechanism — TBD (Calendly / Google Calendar / HR notification) - post-qualification
6. Unqualified candidate handling — Reject / waitlist based on Gemma 4 Vision scores

## Status
🟢 Ready — Direct-to-Hermes architecture defined: Native WhatsApp/Discord/Telegram connections, Gemma 4 Vision scoring, Candidate_UUID system

## Related
- [[client-acquisition-roadmap]] — Sabrina's 0→5 customer framework
- [[value-first-bd-playbook]] — outreach and follow-up cadence patterns
- [[pipeda-consent-screen]] — PIPEDA-compliant data collection (BC/ON/AB scope)
