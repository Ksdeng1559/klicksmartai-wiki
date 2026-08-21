# IDC Recruitment Hypotheses A/B/C — HUBERT-X Experimentation Framework

**Date:** May 6, 2026  
**Status:** HITL DRAFT — Awaiting Owner Approval  
**Project:** IDC Recruitment Agent (HUBERT-X)  
**Skill Reference:** `idc-recruitment-agent-core`

---

## Overview

HUBERT-X is a **Recruitment Experimentation Engine** — not a simple recruiter, but a multi-agent triangulation system that discovers the most effective cognitive trigger to move elite Life Insurance advisors from their current firms to Insurance Direct Canada (IDC).

This document formalizes the three core A/B hypotheses that the Narrative Architect (Strategist) agent will assign to each qualified lead based on their Pedigree Score and Sovereign Gap analysis.

---

## The Three Value Propositions

### VP-A: Infrastructure ("Your current firm is a bottleneck to your scale.")

**Target Profile:** Advisors whose production is constrained by outdated tools, manual processes, or lack of HNW-specific infrastructure at their current carrier/brokerage.

**Core Message Frame:**
> "You've maxed out what your current platform can support. The ceiling isn't your talent — it's their systems."

**Evidence Anchors (IDC's advantage):**
- IDC offers specialized HNW tools and platforms that most brokerages lack
- Streamlined underwriting, carrier access, and case management

**Sovereign Gap Examples:**
| Competitor Type | Sovereign Gap |
|:---|:---|
| Traditional career agency | Limited carrier selection, outdated CRM |
| Captive insurer | Single-product constraint, no cross-selling freedom |
| Small independent brokerage | Manual admin overhead, no compliance/tech stack |

**Hypothesis:** Advisors producing $500K+ GDC annually are actively looking for infrastructure that removes friction. If IDC can demonstrate a quantifiable productivity gain (e.g., "3 more hours/week on revenue-generating activity"), this hook outperforms comp discussions.

---

### VP-B: Client Value ("Your HNW clients deserve the specialized tools IDC provides.")

**Target Profile:** Advisors with established HNW/Affluent books who pride themselves on client service quality and may be dissatisfied with the service limitations of their current firm.

**Core Message Frame:**
> "Your clients' needs have outgrown what your current carrier offers. You know it — and they're starting to notice."

**Evidence Anchors (IDC's advantage):**
- IDC's direct-to-consumer model + digital tools
- Canada's pioneer in direct insurance distribution
- Specialized life, critical illness, and health insurance products

**Sovereign Gap Examples:**
| Competitor Type | Sovereign Gap |
|:---|:---|
| Bank-owned brokerage | Product-push quotas over client-needs analysis |
| Generalist P&C brokerage | Life insurance is an afterthought, not the focus |
| Regional agency | Limited estate planning / advanced case design support |

**Hypothesis:** Advisors who define themselves by client outcomes are more motivated by the ability to serve better than by earning more. This hook opens conversations that comp discussions cannot.

---

### VP-C: Economics ("You are under-earning based on your production volume.")

**Target Profile:** High-volume producers (especially those coming from career agency or captive models) where the compensation structure clearly caps their upside relative to production.

**Core Message Frame:**
> "Based on your production volume, our model shows a 20-40% comp gap between what you're earning and what you should be earning."

**Evidence Anchors (IDC's advantage):**
- IDC's commission structure vs. career agency grids
- Ownership/equity model for top producers
- No captive product constraints limiting revenue streams

**Sovereign Gap Examples:**
| Competitor Type | Sovereign Gap |
|:---|:---|
| Career agency (NYL/NML/Guardian) | 50%+ grid haircut on first-year commissions |
| MGA aggregator | Fee compression, no renewal/equity upside |
| Captive insurer | Single-product, no cross-sell revenue |

**Hypothesis:** After 5-7 years in the business, production-focused advisors become acutely aware of comp structure limitations. A data-backed comp comparison is the most direct path to a conversation — but it MUST be paired with at least one non-comp value anchor (VP-A or VP-B) to avoid "mercenary" framing.

---

## Assignment Logic (The Strategist Agent)

| Lead Profile | Primary VP | Secondary VP | Rationale |
|:---|:---|:---|:---|
| Career agency veteran (7+ yrs, $500K+ GDC) | VP-C → VP-A | Infrastructure + comp | "You've proven it; now stop giving away half your production." |
| HNW specialist (CLU/CFP, $1M+ book) | VP-B → VP-C | Client value + comp | "Your clients deserve better; you deserve the upside." |
| High-growth producer (3-5 yrs, fast ramp) | VP-A → VP-C | Infrastructure + comp | "You're scaling fast — don't let your platform slow you down." |
| P&C-heavy broker adding life | VP-A → VP-B | Infrastructure + client | "Life insurance shouldn't be an afterthought — here's the stack." |

---

## Experimentation Protocol

1. **Assignment:** The Strategist assigns a primary VP to each lead based on Pedigree Score and profile signals.
2. **Rotation:** After every 10 leads, review VP success rates. Shift to the highest-converting VP.
3. **Challenger Protocol:** When one VP consistently outperforms, create a variation (same frame, different language or channel) to raise the ceiling.
4. **Anti-Pattern Detection:** If a VP shows <5% response rate across 20+ attempts, retire it and test a new hypothesis.

---

## Verification Checklist

- [ ] All three VPs have distinct, non-overlapping messaging frames
- [ ] Each VP has at least 3 concrete Sovereign Gap examples
- [ ] Assignment logic is clear and executable by an agent
- [ ] Success metrics (response rate → meeting booked → advisor signed) are defined

---

## Next Steps

1. **Approve this framework** → proceed to A/B Tracking Sheet initialization
2. **Build the 3 agent personas** (Hunter, Strategist, Diplomat) with production prompts
3. **Ingest Batch 1 of 10 leads** → Run POC
