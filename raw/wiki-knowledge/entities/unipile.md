# Unipile

**What it is:** Unified Communication API — single integration for messaging, email, and calendar across LinkedIn, Gmail, WhatsApp, Instagram, Telegram, Outlook, Google Calendar
**URL:** https://www.unipile.com/

## What It Does

**Three core API surfaces:**
- **Messaging API** — LinkedIn, WhatsApp, Instagram, Telegram (send, receive, reply)
- **Email API** — Gmail, Outlook (send, receive, automate workflows)
- **Calendar API** — Google Calendar (sync, schedule, events)

**Platform capabilities:**
- Data Enrichment — retrieve LinkedIn profile data + company details
- Outreach Sequences — multi-step follow-ups across Email, Messaging, Calendar
- Unified Inbox — real-time sync across all channels in one view
- REST API with real-time webhooks
- Auth on behalf of users

**Target markets (from site):** ATS Software, CRM Software, Outreach Software, AI Agent Publishers

## Key Features

| Feature | What It Means |
|---------|---------------|
| Single API | One integration = all major communication platforms |
| LinkedIn API | Send/retrieve messages, enrich profiles, connection requests |
| Data Enrichment | Pull contact + company data from LinkedIn at scale |
| Outreach Sequences | Multi-channel drip campaigns with follow-up timing |
| Unified Inbox | All conversations in one place, real-time sync |
| 7-Day Free Trial | Self-serve access before buying |

## KlickSmartAI Use Case

**Highest fit for WWR (WealthWireRadar):**
- LinkedIn outreach to HNW advisors at scale (manual connection requests → automated follow-up sequence)
- Enrich advisor profiles automatically (name, company, title, industry)
- Unified inbox for all subscriber interactions
- Multi-channel sequences: LinkedIn DM → Gmail follow-up → Calendar invite

**Potential stack combination:**
- Drop Cowboy (ringless voicemail) + Unipile (LinkedIn/Gmail/WhatsApp outreach) + Hermes (orchestration layer)
- Full cold outreach system for financial advisors without a manual SDR team

**For GPC / client websites:** Could power a unified "contact us" inbox across LinkedIn + email + WhatsApp for client-facing communication.

## Pricing
| Tier | Price |
|------|-------|
| Per account/month | €5 ($5.50 USD) |
| Minimum | €49/month ($55) — up to 10 accounts |
| 11–50 accounts | €5/account/month |

Pricing is per linked account (e.g., 3 Gmail + 2 LinkedIn + 6 WhatsApp = 11 accounts = €55/month). No per-request overage. Cancel anytime. 7-day free trial.

## Gmail API Specifics

| Feature | Detail |
|---------|--------|
| Delivery success rate | 99.5% |
| SPF/DKIM/DMARC | Not required — bypassed via Unipile |
| Email operations | Send, reply, list, delete, move, folders |
| Tracking | Open + click tracking |
| Webhooks | New email, open, click events |
| Auth | OAuth or credential-based (white label option) |

## Notes
- 3,000+ SaaS platforms already use it
- "AI Agent Publishers" specifically called out as target market — aligns with KlickSmartAI's autonomous agent operating model
- LinkedIn is the primary channel for B2B advisor outreach