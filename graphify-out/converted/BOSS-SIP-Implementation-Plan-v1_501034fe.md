<!-- converted from BOSS-SIP-Implementation-Plan-v1.docx -->

BOSS SIP
Subscriber Injection Profile + Vertical Engine
Implementation Plan  ·  v1.0  ·  March 2026



◆  SECTION 1 — WHAT THE SUBSCRIBER INJECTION PROFILE IS  ◆

# 1. The Subscriber Injection Profile (SIP)
The SIP is a structured persona injection layer that every agent reads before generating any output. Without it, all agents speak in the same generic voice regardless of whether they are reaching out to an insurance broker about estate planning or a mortgage professional about cash damming. With SIP, each vertical has its own brain — its own language, its own pain vocabulary, its own compliance boundaries, and its own offer framing.


## 1.1  SIP Structure — Full Schema


## 1.2  SIP as a Layer in the v3 Architecture
The SIP inserts between the Intelligence Layer (L3) and the Execution Engine (L4). After the Intelligence Builder generates the intent/pain/hook/offer payload, the SIP Injection Agent reads the vertical context and rewrites the payload through the vertical lens — applying the correct tone, language rules, compliance mode, and offer framing before the message is drafted.



◆  SECTION 2 — THREE VERTICAL ENGINES  ◆

# 2. Splitting Into Three Vertical Engines
The financial services vertical contains three fundamentally different businesses that share geography and regulation but diverge on signals, offers, tone, and compliance risk. Running them as one generic 'Financial Services' engine causes messaging conflicts, offer confusion, and lower conversion. BOSS v4 separates them into three autonomous engines, each with its own context directory.

## 2.1  Context Directory Structure

/context/
├── mortgage/
│   ├── ICP.json
│   ├── SIP.json
│   ├── offer_map.json
│   ├── signal_patterns.json
│   └── conversation_states.json
├── insurance/
│   ├── ICP.json
│   ├── SIP.json
│   ├── offer_map.json
│   ├── signal_patterns.json
│   └── conversation_states.json
└── wealth/
├── ICP.json
├── SIP.json
├── offer_map.json
├── signal_patterns.json
└── conversation_states.json

Each context directory is completely self-contained. Adding a fourth vertical (HVAC, M&A, Healthcare) requires creating a new directory and populating five JSON files — zero system changes required.

## 2.2  Vertical Engine Specifications





◆  SECTION 3 — COMPLETE SIP FILES PER VERTICAL  ◆

# 3. SIP Files — Production-Ready JSON
These are the exact JSON files to create in each vertical context directory. Copy directly — replace client-specific values as noted.

### 3.1  /context/mortgage/SIP.json


### 3.2  /context/insurance/SIP.json


### 3.3  /context/wealth/SIP.json



◆  SECTION 4 — DYNAMIC OFFER ENGINE  ◆

# 4. Dynamic Offer Engine
In BOSS v3, offer assignment was a static lookup: signal_type → offer_name. The Dynamic Offer Engine upgrades this to a function of five inputs. The correct offer is no longer predetermined — it is calculated at the moment of intelligence generation based on everything known about the lead.


## 4.1  Dynamic Offer Decision Matrix


## 4.2  Offer Engine Agent Prompt Structure
The Dynamic Offer Engine runs as part of the Intelligence Builder agent. After generating intent and pain hypothesis, it reads the offer decision matrix from offer_map.json and selects the best fit offer using this structured reasoning prompt:

SYSTEM: You are the BOSS Dynamic Offer Engine for the {vertical} vertical.
Read the SIP at /context/{vertical}/SIP.json.
Read the offer_map at /context/{vertical}/offer_map.json.

INPUT:
signal_type:         {signal_type}
pain_hypothesis:     {pain}
conversation_state:  {state}
prior_offers_shown:  {client_history.offers_shown}
lead_score:          {score}

TASK: Select the single best offer from offer_map.json that:
1. Maps to the signal_type and pain_hypothesis
2. Matches the conversation_state (new leads get awareness offers,
engaged leads get action offers)
3. Has NOT been shown to this contact before (check prior_offers_shown)
4. Complies with SIP.compliance_mode language rules

OUTPUT: { offer_name, offer_hook, offer_cta, compliance_notes }


◆  SECTION 5 — CONVERSATION STATE MACHINE  ◆

# 5. Replacing Campaigns with a State Machine
BOSS v3 ran email sequences as campaigns: Email 1 → Email 2 → Email 3 on a fixed schedule. The problem is that a lead who replies after Email 1 still receives Email 2 as if they never engaged. The Conversation State Machine replaces this with context-aware sequencing — the message sent is determined by the lead's current state, not the calendar day.

## 5.1  The Five Conversation States


## 5.2  State Transition Logic
State transitions are triggered by observable events — not by time elapsed. The Reply Classifier and Engagement Monitor feed events to the State Machine Agent, which updates conversation_state in the contacts table.



◆  SECTION 6 — CROSS-CLIENT INTELLIGENCE LAYER  ◆

# 6. Global Intelligence — Data Network Effects
The most powerful upgrade in this architecture is one most systems never build: cross-client learning. In BOSS v3, each client's outcomes improved their own scoring model. In BOSS v4, anonymized pattern intelligence is shared across clients in the same vertical — creating a data network effect where every new client makes the system smarter for all clients.


## 6.1  Cross-Client Intelligence Architecture


## 6.2  Global Intelligence Update Cycle
The Cross-Client Intelligence Layer runs monthly — not weekly. Weekly cycles are too noisy for cross-client pattern extraction. Monthly cycles give enough data volume per client to produce statistically meaningful patterns.

- 1st of each month: DuckDB cross-client analytics query runs across all active clients per vertical
- Query extracts: signal_type + outcome + hook_category + offer_name — NO PII, no contact data
- Patterns with statistical significance (n ≥ 50 events, p < 0.05) written to global JSON files
- Global JSON files version-bumped — all new clients onboard with latest global context
- Existing clients' next Sunday recalibration incorporates global patterns as a prior — their own client data remains the primary weight


◆  SECTION 7 — IMPLEMENTATION PLAN  ◆

# 7. SIP Implementation Roadmap
The SIP and vertical engine upgrade is additive — it does not break the v3 architecture. Each phase can be deployed independently. Start with the highest-revenue vertical first (determined by which client you close first).


- Create /context/mortgage/, /context/insurance/, /context/wealth/ directories in Supabase Storage
- Populate ICP.json per vertical (adapt from existing generic ICP.json in v3)
- Write all three SIP.json files from Section 3 of this document
- Build offer_map.json per vertical — minimum 5 offers per vertical, each with: offer_name, signal_triggers[], pain_match, hook_template, cta_template, compliance_notes
- Build signal_patterns.json per vertical — hot/warm/cold signal lists from Section 2.2
- Build conversation_states.json per vertical — 5 states with entry conditions, messaging templates, and transition logic
- Validation: run a test lead through each vertical context manually — does the output sound like a specialist? If not, refine the SIP tone and language_rules.


- Build SIP Injection Agent (Sonnet model — this is where margin is made)
- Agent reads: Intelligence Builder output + SIP.json for detected vertical + conversation_state
- Agent rewrites: hook, pain framing, offer selection, CTA through SIP language_rules filter
- Agent outputs: SIP-compliant payload with compliance_notes field populated
- Test with 3 leads per vertical — review output manually before activating in pipeline
- Add vertical detection to Signal Qualifier: classify each signal as mortgage/insurance/wealth based on company type + contact title
- Route each lead to the correct context directory based on vertical classification


- Add conversation_state column to Supabase contacts table (NEW_LEAD default)
- Build State Machine Agent (Haiku — simple state transition logic)
- Upgrade Reply Classifier to output conversation_state transition alongside classification
- Update Smartlead campaign structure: replace 4 fixed sequences with state-based templates
- Each Smartlead campaign now has 5 message templates (one per state) instead of a linear sequence
- Test: route 10 real replies through State Machine — verify correct state transitions
- Activate Engagement Monitor: track email opens (2+) and LinkedIn profile views as ENGAGED triggers


- Build Dynamic Offer Engine as a sub-function inside Intelligence Builder
- Implement the offer selection prompt from Section 4.2 per vertical
- Add prior_offers_shown[] field to contacts table — track what has been shown to each contact
- Test offer selection across 20 leads spanning all three verticals and all 5 conversation states
- Validate: no lead should receive the same offer twice · no offer should violate SIP language_rules
- Activate globally after validation — this replaces the static signal_to_offer mapping in v3


- Requires minimum 2 active clients per vertical AND 30+ days of outcome data before first run
- Build Cross-Client Analytics Query in DuckDB — extracts anonymized patterns (no PII)
- Build Global Pattern Writer: writes extracted patterns to global JSON files in /context/[vertical]/
- Set monthly trigger: 1st of each month, 2am — low traffic, no interference with daily agents
- Build New Client Onboarding Protocol: new clients receive global JSON files as starting context
- Activate when: 3+ insurance clients, 3+ mortgage clients, or 2+ wealth clients are active



◆  SECTION 8 — NEW AGENTS ADDED BY SIP UPGRADE  ◆

# 8. New Agent Registry — SIP Layer


BOSS — Subscriber Injection Profile + Vertical Engine Implementation Plan
v1.0  ·  March 2026  ·  Companion to BOSS v3 Revenue Conversion Machine + BOSS MVP Control Document v3.0
CONFIDENTIAL — KlickSmart AI Internal Use Only
| THE STRATEGIC UPGRADE
BOSS v3 built a Revenue Conversion Machine that speaks to Financial Services generically. This document defines the upgrade that makes the system speak with specialized authority — as an Insurance advisor brain, a Mortgage strategist brain, and an Investment planner brain. The Subscriber Injection Profile (SIP) is the persona layer that controls voice, offer framing, compliance boundaries, and conversation style per vertical. Combined with three separate vertical workflow engines, this transforms BOSS from a tool into a programmable revenue workforce.
Outcome: AI Revenue Employees by Industry — the Agent-as-a-Service moat. |
| --- |
| WITHOUT SIP vs WITH SIP
Without SIP: 'Hi [Name], I noticed you're hiring and wanted to reach out about our lead generation system...' — this is the same email every competitor sends. The prospect reads it as spam.
With SIP (Insurance): 'Hi [Name], saw you're adding capacity — most protection advisors at this stage find that insurability windows close faster than their pipeline fills. Here's what we built...' — the prospect reads this as a specialist who understands their world.
The SIP is what makes the system feel like an AI employee with domain expertise, not a generic chatbot with a mail merge. |
| --- |
| SIP Schema — All Fields
{
  "profile_name":      "Insurance Advisor — Protection First",
  "vertical":          "insurance",
  "tone":              "advisory, risk-aware, compliance-safe",
  "authority_position": "Risk mitigation specialist",
  "primary_offer":     "Insurability Optimization Engine",
  "pain_bias": [
    "future uninsurability",
    "health deterioration risk",
    "family protection gaps",
    "estate planning vacuum"
  ],
  "language_rules": {
    "avoid":  ["guarantee", "high returns", "best investment", "will perform"],
    "prefer": ["protect", "qualify", "secure", "lock in", "preserve", "hedge"]
  },
  "cta_style":         "low-pressure, education-first, risk-framed",
  "compliance_mode":   "strict",
  "jurisdiction": {
    "country":  "Canada",
    "province": "BC",
    "rules":    ["CASL", "OSFI", "FSRA", "IIROC"]
  },
  "conversation_state_map": "insurance_states.json",
  "offer_map_path":    "/context/insurance/offer_map.json",
  "signal_map_path":   "/context/insurance/signal_patterns.json",
  "icp_path":          "/context/insurance/ICP.json"
} |
| --- |
| v3 Flow (Before SIP) | v4 Flow (With SIP) |
| --- | --- |
| Intelligence Builder → raw payload | Intelligence Builder → raw payload → SIP Injection Agent → vertical-toned payload |
| Generic hook: 'Saw you're hiring...' | Insurance hook: 'Saw you're adding a protection specialist — most advisors find insurability windows close before new capacity fills the pipeline...' |
| Generic offer: 'Lead Enrichment Engine' | Insurance offer: 'Insurability Optimization Engine — we identify clients whose window is closing before they know it' |
| One compliance mode for all messages | Per-vertical compliance: Insurance=STRICT, Mortgage=MODERATE, Wealth=STRICT |
| Static offer assignment from offer_map.json | Dynamic Offer Engine: f(signal + pain + vertical + SIP + conversation_state + history) |
| A  Mortgage Engine |
| --- |
| SIGNALS
• Rate drop announcements (BoC decisions)
• New MLS listings spike in target market
• Refi application volume increase signals
• Mortgage broker posting about equity extraction
• Client approaching renewal date (12-month window)
• Competitor broker office closure nearby

OFFERS
• Refinance Optimization Audit
• Cash Damming Implementation Guide
• Equity Extraction Roadmap
• Database Reactivation — Pre-Renewal Campaign
• Smith Manoeuvre Awareness Campaign

TONE: Financial optimization, opportunity-driven, urgency-aware
COMPLIANCE MODE: MODERATE — avoid rate guarantees, approval promises |
| B  Insurance Engine |
| --- |
| SIGNALS
• Aging demographics in target postal codes
• New advisor hiring (capacity expansion signal)
• Business sale / ownership transition signals
• Health-related life event (marriage, child, diagnosis)
• Estate planning content engagement
• Policy lapse / competitor exit signals

OFFERS
• Insurability Optimization Engine
• Insurability Window Audit
• Family Protection Gap Analysis
• Estate Planning Accelerator
• Business Owner Protection Package
• Living Benefits Awareness Campaign

TONE: Protection-first, risk-aware, education-led, empathy-driven
COMPLIANCE MODE: STRICT — OSFI/FSRA language rules strictly enforced |
| C  Wealth / Investment Engine |
| --- |
| SIGNALS
• Business sale / liquidity event signals
• Executive compensation disclosure (public filings)
• High-income role at target company (hiring signal)
• Company IPO or funding round detected
• Inherited wealth indicators (estate filing, obituary)
• Portfolio consolidation / advisor change signals

OFFERS
• Portfolio Structuring Review
• Tax Efficiency Acceleration
• Wealth Transfer Framework
• Corporate Investment Strategy
• Business Exit Optimization
• Philanthropic Planning Introduction

TONE: Strategic, long-term thinking, high-trust, peer-level
COMPLIANCE MODE: STRICT — IIROC/OSC rules apply, zero speculative claims |
| Mortgage SIP
{
  "profile_name":      "Mortgage Strategist — Wealth Optimizer",
  "vertical":          "mortgage",
  "tone":              "financial optimization, opportunity-urgency, advisor-peer",
  "authority_position": "Mortgage strategy and equity optimization specialist",
  "primary_offer":     "Refinance Optimization Audit",
  "pain_bias": [
    "leaving equity locked in property",
    "missing the rate window",
    "database going cold between renewals",
    "losing clients to digital lenders"
  ],
  "language_rules": {
    "avoid":  ["guaranteed approval", "best rate available", "will save you"],
    "prefer": ["optimize", "unlock", "leverage", "position", "accelerate", "map"]
  },
  "cta_style":         "value-first, map-the-opportunity, 12-minute conversation",
  "compliance_mode":   "moderate",
  "jurisdiction": {"country":"Canada","rules":["CASL","FSRA","CMHC guidelines"]},
  "conversation_state_map": "/context/mortgage/conversation_states.json"
} |
| --- |
| Insurance SIP
{
  "profile_name":      "Insurance Advisor — Protection First",
  "vertical":          "insurance",
  "tone":              "advisory, risk-aware, compliance-safe, empathetic",
  "authority_position": "Risk mitigation and protection planning specialist",
  "primary_offer":     "Insurability Optimization Engine",
  "pain_bias": [
    "future uninsurability due to health changes",
    "family protection gaps going unaddressed",
    "estate planning vacuum in HNW households",
    "business continuity risk without key-person coverage"
  ],
  "language_rules": {
    "avoid":  ["guarantee", "high returns", "investment growth", "will perform", "earn"],
    "prefer": ["protect", "secure", "lock in", "qualify while", "preserve", "hedge", "cover"]
  },
  "cta_style":         "low-pressure, education-first, risk-framed, no urgency manipulation",
  "compliance_mode":   "strict",
  "jurisdiction": {"country":"Canada","rules":["CASL","OSFI","FSRA","IIROC"]},
  "conversation_state_map": "/context/insurance/conversation_states.json"
} |
| --- |
| Wealth / Investment SIP
{
  "profile_name":      "Wealth Advisor — Strategic Capital Deployment",
  "vertical":          "wealth",
  "tone":              "strategic, peer-level, long-horizon, high-trust",
  "authority_position": "Wealth structuring and capital efficiency specialist",
  "primary_offer":     "Portfolio Structuring Review",
  "pain_bias": [
    "tax drag eroding compounding returns",
    "wealth transfer complexity at exit",
    "capital sitting idle post-liquidity event",
    "portfolio consolidation opportunity unmapped"
  ],
  "language_rules": {
    "avoid":  ["guaranteed returns", "outperform the market", "risk-free", "double your money"],
    "prefer": ["structure", "allocate", "optimize", "transfer efficiently", "deploy", "compound"]
  },
  "cta_style":         "peer-to-peer, intellectual curiosity, no pressure, long-game framing",
  "compliance_mode":   "strict",
  "jurisdiction": {"country":"Canada","rules":["CASL","IIROC","OSC","NI 31-103"]},
  "conversation_state_map": "/context/wealth/conversation_states.json"
} |
| --- |
| THE OFFER SELECTION FORMULA
Offer = f(signal_type + pain_hypothesis + vertical + SIP.primary_offer + conversation_state + client_history) |
| --- |
| Signal Type | Vertical | Conversation State | Pain Hypothesis | → Recommended Offer |
| --- | --- | --- | --- | --- |
| hiring_advisor | Insurance | NEW_LEAD | Capacity expanding but pipeline not ready | Insurability Window Audit — 'before new clients fill the book' |
| rate_drop | Mortgage | NEW_LEAD | Clients locked in above-market rates | Refinance Optimization Audit — 'map the savings window' |
| rate_drop | Mortgage | ENGAGED | Already aware — looking for execution help | Cash Damming Implementation — move from awareness to action |
| business_sale | Wealth | NEW_LEAD | Capital about to be released — no deployment plan | Portfolio Structuring Review — 'what happens the day the deal closes' |
| business_sale | Insurance | NEW_LEAD | Key-person coverage expiring at sale | Living Benefits + Estate Planning — 'the coverage gap no one mentions at closing' |
| hiring_advisor | Wealth | CURIOUS | Scaling firm — need HNW client acquisition | Database Reactivation — 'your existing book has dormant wealth events' |
| competitor_exit | Mortgage | NEW_LEAD | Orphaned clients in the market | Database Reactivation Campaign — 'advisors in your area just went dark' |
| renewal_window | Mortgage | NURTURE | 12-month renewal approaching | Pre-Renewal Campaign — 'position before the banks do' |
| STATE | ENTRY TRIGGER | MESSAGING STRATEGY | TONE | OFFER TIER |
| --- | --- | --- | --- | --- |
| NEW LEAD | Lead enters from waterfall — no prior contact | Signal-based opener → pattern break → micro value → soft CTA | Warm, curious, peer-level | Awareness offer (audit, guide, framework) |
| ENGAGED | Opened 2+ emails OR clicked link OR viewed LinkedIn profile | Deepen insight — reference prior engagement signal | Informed, substantive | Action offer (implementation, session, demo) |
| CURIOUS | Replied with a question OR requested more info | Answer question directly → bridge to offer → book conversation | Expert, unhurried | Consultation offer (strategy call, mapping session) |
| OBJECTION | Replied with price / timing / competitor / trust objection | Acknowledge → reframe → reduce friction → re-offer | Empathetic, patient | Modified offer (lower commitment, proof-first) |
| READY | Expressed interest in booking OR asked about availability | Remove all friction immediately — single CTA to calendar | Efficient, direct | Booking — no more selling needed |
| From State | Event | → New State | Agent Action |
| --- | --- | --- | --- |
| NEW LEAD | Email opened 2+ times (no reply) | ENGAGED | Switch to ENGAGED messaging template — reference that they've seen this before |
| NEW LEAD | LinkedIn profile viewed after DM sent | ENGAGED | LinkedIn follow-up DM acknowledging the view — 'noticed you checked us out...' |
| NEW LEAD / ENGAGED | Reply received — contains question | CURIOUS | Route to Reply Handler — answer question directly, bridge to offer |
| NEW LEAD / ENGAGED | Reply received — objection detected | OBJECTION | Route to Objection Handler — classify objection type, apply SIP language rules |
| CURIOUS / OBJECTION | Reply signals positive intent | READY | Meeting Booker activated — single calendar link, zero friction |
| ANY STATE | Unsubscribe keyword detected | REMOVED | Permanent suppression — no re-entry possible |
| ANY STATE | No engagement for 30 days | NURTURE | Move to monthly nurture sequence — low frequency, high value content only |
| NURTURE | New buying signal detected | NEW LEAD | Re-enter waterfall at Stage 1 with updated signal context |
| HOW NETWORK EFFECTS COMPOUND
Client A (Insurance, BC) discovers that 'hiring_advisor' signals convert at 34% when the hook references 'insurability window closing'. This pattern is anonymized and written to the global signal_patterns.json for the insurance vertical.
Client B (Insurance, Ontario) is onboarded two months later. Their system starts with the pattern library already trained on Client A's outcomes — they reach peak performance in Week 2 instead of Week 8.
After 10 insurance clients: the pattern library has 100,000+ outcome data points. The system's prediction accuracy for insurance leads is an order of magnitude better than any single-client model. This is the moat. |
| --- |
| Data Type | Per-Client (Private) | Cross-Client (Anonymized) | Stored In |
| --- | --- | --- | --- |
| Contact records | Full PII — name, email, company, all interactions | Never shared | Supabase per-client |
| Signal patterns | Client-specific signal config | Signal_type + conversion_rate + hook_category (no contact data) | Global signal_patterns.json per vertical |
| Scoring weights | Client-specific weights based on their ICP | Aggregate weight distribution across vertical (what dimensions matter most) | Global scoring_weights_baseline.json per vertical |
| Hook performance | Client-specific hook → reply_rate data | Hook category + reply_rate quartile (anonymized) | Global hook_library.json per vertical |
| Offer conversion | Client-specific offer → meeting_rate | Offer_name + signal_type + conversion_rate (no client ID) | Global offer_performance.json per vertical |
| Objection patterns | Client-specific objections received | Objection_type + frequency + successful_response_pattern | Global objection_playbook.json per vertical |
| I1 | Context Directory Build (Days 1–3)
Create /context/ directory structure · Populate all 15 JSON files · Validate schema |
| --- | --- |
| I2 | SIP Injection Agent (Days 4–7)
Build the new L3.5 agent · Test per vertical · Integrate into v3 pipeline |
| --- | --- |
| I3 | Conversation State Machine (Days 8–14)
Replace campaign-based sequences · Build State Machine Agent · Activate reply routing |
| --- | --- |
| I4 | Dynamic Offer Engine (Days 15–21)
Replace static offer lookup · Build offer selection logic · Activate per vertical |
| --- | --- |
| I5 | Cross-Client Intelligence (Month 2+)
Anonymized pattern extraction · Global JSON update cycle · New client fast-start |
| --- | --- |
| PRIORITY ORDER SUMMARY
1. Build context directories + all 15 JSON files (Days 1–3) — zero code, pure configuration
2. Build SIP Injection Agent (Days 4–7) — one new agent, inserts between L3 and L4
3. Add conversation_state to contacts table + State Machine Agent (Days 8–14)
4. Build Dynamic Offer Engine (Days 15–21) — replaces static lookup
5. Cross-Client Intelligence (Month 2+) — activates when data volume is sufficient
Total time to fully operational SIP system: 21 days of focused build work |
| --- |
| Agent | Layer | Model | When It Runs | Input | Output |
| --- | --- | --- | --- | --- | --- |
| Vertical Classifier | L2 exit | Haiku | After Signal Qualifier PASS | Signal + company type + contact title | vertical: mortgage|insurance|wealth → routes to correct /context/ directory |
| SIP Injection Agent | L3.5 (NEW) | Sonnet | After Intelligence Builder | Raw payload + SIP.json + conversation_state | SIP-compliant payload: hook rewritten, offer reframed, compliance notes added |
| State Machine Agent | L4 entry | Haiku | On every reply + on engagement events | Reply classification + engagement events + current state | New conversation_state → updates contacts table → routes to correct message template |
| Engagement Monitor | L4 | Haiku | Realtime on email open/click events | Email open event + open count for this contact | Triggers state transition NEW_LEAD → ENGAGED when threshold met |
| Dynamic Offer Engine | L3.5 sub-function | Sonnet | Inside Intelligence Builder + SIP Agent | Signal + pain + state + prior_offers + offer_map.json | Selected offer name + hook + CTA + compliance notes |
| Cross-Client Analyzer | L5 global | DuckDB + Haiku | Monthly — 1st of month 2am | All outcome data across vertical — anonymized | Updated global signal_patterns + hook_library + offer_performance JSON files |
| New Client Bootstrapper | L5 setup | Haiku | On new client onboarding | Global JSON files for detected vertical | Client context directory pre-populated with global patterns as starting point |
| Compliance Mode Enforcer | L6 upgraded | Haiku | Before every send — now vertical-aware | Message draft + SIP.compliance_mode + jurisdiction.rules | CLEARED (compliant) or REWRITE (non-compliant with specific rule violation cited) |