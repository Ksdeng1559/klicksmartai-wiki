# BOSS SIP — Financial Services Onboarding

## What the SIP Is

The Subscriber Injection Profile (SIP) is a structured persona layer that lives between the Intelligence Engine (L3) and the Execution Engine (L4). Every agent reads it before generating any output. It ensures the client's voice — not a generic sales template — flows through every message.

Think of it as the client fingerprint. Once loaded, the system speaks that client's language automatically.

---

## Onboarding Sequence

```
New Client Signs
      ↓
1. Vertical Detection
   → mortgage / insurance / wealth
      ↓
2. Context Directory Created
   /context/{vertical}/
      ↓
3. SIP Intake (Discovery Call)
   → ICP, pain vocabulary, tone rules, compliance mode
      ↓
4. Offer Map Populated
   5 offers minimum, each with signal triggers + hook templates
      ↓
5. Signal Patterns Configured
   hot / warm / cold signals for their specific vertical
      ↓
6. Conversation States Set
   5 states with entry conditions + message templates
      ↓
7. Validation
   3 test leads run through SIP layer — manually review before live
      ↓
8. Client Goes Live
```

---

## SIP Intake — Live Discovery Fields

Collect these during the onboarding discovery call.

### 1. Vertical
```
[ ] Mortgage  [ ] Insurance  [ ] Wealth
```
Confirm one primary vertical. Mixed verticals use the dominant revenue stream.

### 2. Compliance Mode
```
[ ] FINRA (US brokers)
[ ] IIROC (Canadian advisors)
[ ] state-level / provincial
[ ] other: ___
```
Determines language boundaries in every message.

### 3. ICP — Target Client Profile
| Field | Question |
|-------|----------|
| Title | Who do they call on? (e.g., "financial advisors with AUM $10M+") |
| Industry | What does their day-to-day look like? |
| Geography | Any geographic constraints? |
| Signal type | What life events trigger the conversation? |

### 4. Pain Vocabulary
What words does the client use when describing the problem they can't solve?
- Example (insurance): "estate planning gaps", "casualty exposure", "over-leveraged portfolio"
- Example (wealth): "retirement income ladder", "sequence of returns risk", "tax leakage"
- Example (mortgage): "cash damming", "rate lock regret", "portfolio dilution"

### 5. Tone Rules
```
[ ] Formal — institutional, compliance-first
[ ] Professional — direct, no fluff
[ ] Conversational — approachable but credible
[ ] Ultra-casual — matching their LinkedIn voice
```
Defaults to Professional if not specified.

### 6. Offer Map — Minimum 5 Offers
For each offer:
- `offer_name` — internal name (e.g., "Portfolio Stress Test")
- `signal_triggers[]` — what signals activate this offer
- `pain_match` — which pain hypothesis it addresses
- `hook_template` — pre-written opener template
- `cta_template` — booking or reply CTA
- `compliance_notes` — language to avoid for this offer

### 7. Signal Patterns — Per State
```
HOT:     [list signals that indicate urgent need]
WARM:    [list signals that indicate qualified interest]
COLD:    [list signals that indicate early-stage awareness]
```
These override the default vertical patterns if client-specific.

### 8. Conversation State Preferences
Confirm the 5-state model works for their funnel. Adjust entry/exit conditions per state if needed.

---

## Files Delivered After Onboarding

Each client's context directory is self-contained:

```
/context/{vertical}/{client-slug}/
  ├── ICP.json              ← their specific ICP
  ├── SIP.json              ← persona + tone + compliance
  ├── offer_map.json        ← their 5+ offers
  ├── signal_patterns.json ← hot/warm/cold by vertical
  └── conversation_states.json ← 5 states + transition logic
```

Directory lives in Supabase Storage under the client's isolated project.

---

## Validation Before Go-Live

Take 3 real leads (from their existing pipeline or LinkedIn) and run them through the SIP layer manually:

1. Lead data enters Intelligence Builder
2. SIP Injection Agent rewrites payload through vertical lens
3. Output drafted — message generated
4. Dennis or client reviews manually

**Pass criteria:** Message sounds like it came from their internal team, not a vendor.

**Fail signals:** Generic language, wrong compliance tone, offer mismatch, off-target ICP.

If it fails → iterate SIP tone rules and pain vocabulary until it passes.

---

## Post-Go-Live

Once live, the Cross-Client Intelligence Layer runs on the 1st of each month (requires 2+ clients in same vertical). DenchRefeed the global patterns back into each client's SIP context on each monthly cycle.

New verticals (e.g., M&A advisory, estate planning) require only a new context directory + 5 JSON files. Zero system changes.

---

## Source Docs
- `[[boss-raas]]` — BOSS v3 Revenue Conversion Machine
- `[[klick2client-os]]` — Klick2Client OS v1.0 (delivery framework)
- raw/reference/BOSS-SIP-Implementation-Plan-v1.docx