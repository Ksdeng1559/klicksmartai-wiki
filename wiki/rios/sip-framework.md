# Subscriber Injection Profile (SIP) Framework
## Financial Professionals — Mortgage Brokers, Financial Planners, Insurance Agents

> **Document Origin:** BOSS SIP Implementation Plan v1.0 · March 2026  
> **Source:** `raw/reference/BOSS-SIP-Implementation-Plan-v1.docx`  
> **Status:** Filed · Active  
> **Companion:** `rios/architecture.md` (RIOS v4.9)  
> **KlickSmart AI · CONFIDENTIAL — Internal Use Only**

---

## What the SIP Is

The SIP is a structured persona injection layer that every agent reads before generating any output. Without it, all agents speak in the same generic voice — identical whether reaching out to a mortgage broker about equity extraction or an insurance advisor about estate planning. With SIP, each vertical has its own brain: its own language, pain vocabulary, compliance boundaries, and offer framing.

**Without SIP vs WITH SIP (Insurance example):**
```
WITHOUT: "Hi [Name], I noticed you're hiring and wanted to reach out about our 
          lead generation system..." — reads as spam.

WITH SIP: "Hi [Name], saw you're adding capacity — most protection advisors at 
          this stage find insurability windows close faster than their pipeline 
          fills. Here's what we built..." — reads as specialist expertise.
```

**Without SIP vs WITH SIP (Mortgage example):**
```
WITHOUT: "Hi [Name], I saw your recent post about market activity..." — generic.

WITH SIP: "Hi [Name], caught your post on the refi surge — the equity extraction 
          window is narrowing for clients locked above 4.5%. We've mapped a 
          cash damming playbook for brokers in your position..." — reads as peer.
```

---

## Three Vertical Engines

The financial services vertical contains three fundamentally different businesses sharing geography and regulation but diverging on signals, offers, tone, and compliance risk.

| Vertical | Profile | Tone | Compliance |
|----------|---------|------|-----------|
| **Mortgage** | Mortgage Strategist — Wealth Optimizer | Financial optimization, opportunity-urgency, advisor-peer | MODERATE |
| **Insurance** | Insurance Advisor — Protection First | Advisory, risk-aware, compliance-safe, empathetic | STRICT |
| **Wealth** | Wealth Advisor — Strategic Capital Deployment | Strategic, peer-level, long-horizon, high-trust | STRICT |

---

## Directory Structure

```
/context/
├── mortgage/
│   ├── SIP.json              ← Mortgage vertical persona
│   ├── ICP.json              ← Ideal Client Profile
│   ├── offer_map.json        ← Signal → Offer decision matrix
│   ├── signal_patterns.json  ← Hot/warm/cold signals
│   └── conversation_states.json  ← State machine definitions
├── insurance/
│   ├── SIP.json              ← Insurance vertical persona
│   ├── ICP.json
│   ├── offer_map.json
│   ├── signal_patterns.json
│   └── conversation_states.json
└── wealth/
    ├── SIP.json              ← Wealth vertical persona
    ├── ICP.json
    ├── offer_map.json
    ├── signal_patterns.json
    └── conversation_states.json
```

Adding a fourth vertical requires creating a new directory and populating five JSON files — **zero system changes required**.

---

## SIP Schema — All Fields

```json
{
  "profile_name": "Vertical-specific profile name",
  "vertical": "mortgage|insurance|wealth",
  "tone": "Comma-separated tone descriptors",
  "authority_position": "How the system positions itself",
  "primary_offer": "Lead offer for this vertical",
  "pain_bias": [
    "Primary pain point 1",
    "Primary pain point 2",
    "Primary pain point 3",
    "Primary pain point 4"
  ],
  "language_rules": {
    "avoid": ["phrase1", "phrase2"],
    "prefer": ["phrase1", "phrase2"]
  },
  "cta_style": "Low-pressure, education-first, etc.",
  "compliance_mode": "strict|moderate|minimal",
  "jurisdiction": {
    "country": "Canada",
    "rules": ["CASL", "FSRA", "CMHC guidelines"]
  },
  "conversation_state_map": "/context/[vertical]/conversation_states.json"
}
```

---

## Conversation State Machine

| State | Entry Trigger | Tone | Offer Tier |
|-------|-------------|------|------------|
| **NEW_LEAD** | Signal detected, no prior contact | Warm, curious, peer-level | Awareness (audit, guide, framework) |
| **ENGAGED** | Opened 2+ emails OR clicked link OR viewed LinkedIn | Informed, substantive | Action (implementation, session, demo) |
| **CURIOUS** | Replied with question OR requested more info | Expert, unhurried | Consultation (strategy call, mapping session) |
| **OBJECTION** | Replied with price/timing/competitor/trust objection | Empathetic, patient | Modified offer (lower commitment, proof-first) |
| **READY** | Expressed interest in booking OR asked about availability | Efficient, direct | Booking — single CTA, no more selling |
| **NURTURE** | No engagement for 30 days | Value-first, low frequency | Monthly content, re-entry trigger |
| **REMOVED** | Unsubscribe keyword detected | N/A | Permanent suppression — no re-entry |

---

## Dynamic Offer Engine

Offer is calculated, not assigned:

```
Offer = f(signal_type + pain_hypothesis + vertical + SIP.primary_offer + conversation_state + client_history)
```

| Signal Type | Vertical | State | Pain Hypothesis | Recommended Offer |
|-------------|----------|-------|-----------------|-------------------|
| `rate_drop` | mortgage | NEW_LEAD | Clients locked above market | Refinance Optimization Audit |
| `rate_drop` | mortgage | ENGAGED | Aware but need execution help | Cash Damming Implementation |
| `hiring_advisor` | insurance | NEW_LEAD | Pipeline not ready for new capacity | Insurability Window Audit |
| `business_sale` | wealth | NEW_LEAD | Capital releasing — no deployment plan | Portfolio Structuring Review |
| `competitor_exit` | mortgage | NEW_LEAD | Orphaned clients in the market | Database Reactivation Campaign |
| `renewal_window` | mortgage | NURTURE | 12-month renewal approaching | Pre-Renewal Campaign |

---

## Compliance Mode by Vertical

| Vertical | Mode | Key Rules |
|----------|------|-----------|
| **Mortgage** | MODERATE | Avoid rate guarantees, approval promises, "best rate" claims |
| **Insurance** | STRICT | OSFI/FSRA language strictly enforced; no "guarantee", "will perform", "earn" |
| **Wealth** | STRICT | IIROC/OSC rules apply; zero speculative claims, no "risk-free", "double your money" |

---

## SIP in the RIOS Architecture

The SIP inserts between the Intelligence Layer (L3) and the Execution Engine (L4):

```
v3 Flow (Before SIP):
Intelligence Builder → raw payload → Generic hook drafted

v4 Flow (With SIP):
Intelligence Builder → raw payload → SIP Injection Agent → vertical-toned payload → Compliance Mode Enforcer → CLEARED message
```

Each vertical's SIP is loaded at L3.5 before any message is drafted. The Compliance Mode Enforcer (L6) validates output against jurisdiction rules before sending.

---

## Quick Reference — Language Rules

**MORTGAGE:**
- **Avoid:** "guaranteed approval", "best rate available", "will save you"
- **Prefer:** "optimize", "unlock", "leverage", "position", "accelerate", "map"

**INSURANCE:**
- **Avoid:** "guarantee", "high returns", "investment growth", "will perform", "earn"
- **Prefer:** "protect", "secure", "lock in", "qualify while", "preserve", "hedge", "cover"

**WEALTH:**
- **Avoid:** "guaranteed returns", "outperform the market", "risk-free", "double your money"
- **Prefer:** "structure", "allocate", "optimize", "transfer efficiently", "deploy", "compound"

---

## ICP Refinement Data Points

The SIP document provides the following ICP refinement inputs:

**Mortgage ICP signals:**
- Rate drop announcements (BoC decisions)
- New MLS listings spike in target market
- Refi application volume increase
- Client approaching renewal date (12-month window)
- Competitor broker office closure nearby
- Mortgage broker posting about equity extraction

**Insurance ICP signals:**
- Aging demographics in target postal codes
- New advisor hiring (capacity expansion)
- Business sale / ownership transition
- Health-related life event (marriage, child, diagnosis)
- Estate planning content engagement
- Policy lapse / competitor exit

**Wealth ICP signals:**
- Business sale / liquidity event signals
- Executive compensation disclosure (public filings)
- High-income role at target company
- Company IPO or funding round detected
- Inherited wealth indicators (estate filing, obituary)
- Portfolio consolidation / advisor change signals

---

## Cross-Client Intelligence (Network Effects)

The most powerful moat: anonymized pattern intelligence shared across clients in the same vertical.

```
Client A (Insurance, BC) discovers 'hiring_advisor' signals convert at 34% 
when hook references 'insurability window closing'.

Pattern anonymized → written to global signal_patterns.json (insurance vertical)

Client B (Insurance, Ontario) onboarded 2 months later → starts with pattern 
library already trained on Client A's outcomes → reaches peak performance 
in Week 2 instead of Week 8.

After 10 insurance clients: 100,000+ outcome data points. Prediction accuracy 
an order of magnitude better than any single-client model.
```

Cross-client data types (anonymized, no PII):
- Signal patterns → `global signal_patterns.json`
- Hook performance → `global hook_library.json`
- Offer conversion → `global offer_performance.json`
- Objection patterns → `global objection_playbook.json`
- Scoring weights → `global scoring_weights_baseline.json`

---

## Implementation Roadmap

| Phase | Days | Task |
|-------|------|------|
| I1 | 1–3 | Build context directories + all 15 JSON files |
| I2 | 4–7 | Build SIP Injection Agent (L3.5, Sonnet) |
| I3 | 8–14 | Build Conversation State Machine + State Machine Agent |
| I4 | 15–21 | Build Dynamic Offer Engine |
| I5 | Month 2+ | Activate Cross-Client Intelligence (min 2 clients per vertical) |

**Total: 21 days to fully operational SIP system.**

---

## New Agents Added by SIP Upgrade

| Agent | Layer | Model | Input | Output |
|-------|-------|-------|-------|--------|
| Vertical Classifier | L2 exit | Haiku | Signal + company type | Routes to correct `/context/` directory |
| SIP Injection Agent | L3.5 (NEW) | Sonnet | Raw payload + SIP.json + state | SIP-compliant payload + compliance_notes |
| State Machine Agent | L4 entry | Haiku | Reply classification + engagement events | New conversation_state → routes to correct template |
| Engagement Monitor | L4 | Haiku | Email open count threshold | Triggers NEW_LEAD → ENGAGED transition |
| Dynamic Offer Engine | L3.5 sub | Sonnet | Signal + pain + state + prior_offers + SIP | Selected offer + hook + CTA + compliance notes |
| Cross-Client Analyzer | L5 global | DuckDB + Haiku | All outcome data (anonymized) | Updated global JSON files |
| New Client Bootstrapper | L5 setup | Haiku | New client onboarding detected | Pre-populated context with global patterns |
| Compliance Mode Enforcer | L6 | Haiku | Message draft + SIP.compliance_mode | CLEARED or REWRITE with specific rule cited |

---

## Companion Documents

- `rios/architecture.md` — RIOS v4.9 full architecture (agents, layers, data model)
- `raw/reference/BOSS-SIP-Implementation-Plan-v1.docx` — Source document (original)
- `raw/reference/boss-raas-v3.md` — BOSS v3 Revenue Conversion Machine
- `clients/` — Client-specific ICP files per vertical (to be generated)