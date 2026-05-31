# RIOS Architecture

## System Flow

```text
Mission Control
        ↓
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
        ↓
(Self-Correction Loop ← feeds back to Mission Control)
```

## Mission Control

RIOS's opportunity engine + GTM autopilot. Scans the full graph continuously for pattern matches across entities, signals, relationships, and historical outcomes — then generates and executes actionable strategies that feed back into the system.

**Inputs:** Graph topology, signal history, battlecard triggers, SIP routing outcomes, learning layer feedback, ClientFlow intake patterns, MIX pipeline velocity, `/goal` north star document.

**Outputs:**
- Opportunity entities (scored, ranked, SIP-vertical-tagged)
- Battlecard generation triggers
- Advisor routing recommendations
- SIP vertical reassignments
- Anomaly alerts (unusual signal clusters, cold leads, stalled pipelines)
- **GTM strategy execution** — automated playbooks run against opportunities

**Pattern types scanned:**
- Co-occurrence: multiple signals pointing to same entity cluster
- Temporal: signal velocity changes (new surge vs. gradual decline)
- Relational: new cross-entity connections that bypass normal routing
- Behavioral: intake-to-close patterns from ClientFlow/MIX history
- Anomaly: leads/deals that break expected SIP routing or velocity norms

---

### GTM Autopilot

Mission Control executes GTM Engineer strategies on autopilot — pulling from the GTM Engineering Resources stack and running structured plays against scored opportunities.

**GTM Stack wired in:**
- **Signal detection** → Apify (news + event crawlers), Explorium signal engine
- **Enrichment** → EnrichLayer (per-profile), Apollo (lead lists), Clay (AI workflows)
- **Outbound execution** → Klick2Client OS (LinkedIn + Email lifecycle), Instantly (email warmup + sending)
- **Workflow orchestration** → Claude Code + AgentSource (replaces n8n + Zapier — 5→2 failure points)
- **Research layer** → Bright Data (bulk company research), Apify (CSE crawlers)

**Plays executed on autopilot:**
- Omnichannel orchestration (email + LinkedIn + intent data)
- AI-driven hyper-personalization (per-opportunity battlecard → personalized outreach)
- Account-based marketing with intent data (target org clusters)
- Referral-first GTM (partner cultivation cycles with CRM follow-up)
- First-party data strategy (post-HPPA compliance)
- 360-day parallel track sequencing (inbound + outbound + partner simultaneously)

**Trigger logic:** Opportunity score ≥70 → GTM autopilot activates → play selected by SIP vertical + pattern type → execution via Klick2Client OS → outcome fed to learning layer.

---

### Self-Correction Loop

Mission Control continuously measures its own performance against `/goal` — the strategic north star document. Every execution cycle closes the loop.

```
/goal (north star)
    ↓
Mission Control generates + executes opportunity
    ↓
Execution via GTM stack (Klick2Client OS, Instantly, Apify, etc.)
    ↓
Learning Layer records outcome (won/lost/stale/anomaly)
    ↓
Self-correction: compare outcome vs. /goal targets
    ↓
Mission Control adjusts:
  - Pattern weighting (which pattern types convert)
  - GTM play selection (which plays work for which verticals)
  - Score thresholds (calibrate qualification_score cutoff)
  - SIP routing rules (reassign verticals based on outcome data)
  - Opportunity confidence bias (raise/lower confidence based on hit rate)
    ↓
/goal updated (if objective changed) or pattern model retrained
```

**Self-correction triggers:**
- Pattern hit rate drops below threshold → recalibrate pattern weights
- GTM play conversion below `/goal` KPI → switch play type or vertical routing
- Qualification score accuracy degrades → retrain ClientFlow scoring model
- Pipeline velocity stalls → alert + recommend advisor reassignment
- `/goal` objective changed → full strategy re-alignment, regenerate all open opportunities

**`/goal` document** (`wiki/goal.md`) — the living strategic document Mission Control reads as its north star. Defines: current OKRs, target verticals, pipeline revenue targets, win rate goals, conversion benchmarks, active GTM plays, and suppression rules. Must be updated by the operator when strategy shifts.

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
- **ClientFlow intake** — qualification scores, routing decisions, lead profiles, practice areas
- **MIX Dashboard** — pipeline value, deal status, activity feed, KPI trends, agent capacity

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
- Lead *(ClientFlow intake — qualified prospect with score + routing decision)*
- Advisor *(assigned to lead, tracks capacity + load)*
- IntakeSession *(90-second qualification session — outputs battlecard trigger)*
- Subscriber *(MIX pipeline — open deal with status, assignee, priority)*

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
- assigned_to *(advisor → lead)*
- intake_of *(lead → intake_session)*
- qualified_from *(lead → intake_session)*

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
- **ClientFlow qualification accuracy** — score vs. actual conversion rate
- **MIX pipeline velocity** — time from intake to closed deal
- **SIP vertical routing accuracy** — mortgage/insurance/wealth assignment correctness
- **Offer engine performance** — offer selection vs. meeting-booked rate
- **Mission Control pattern hit rate** — opportunities generated vs. opportunities that converted
- **`/goal` alignment score** — how close actual outcomes track against north star OKRs (revenue, win rate, conversion benchmarks)
