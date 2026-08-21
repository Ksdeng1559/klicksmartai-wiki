# Division-Based Agent Architecture
**Status:** Reference Framework
**Reference:** Adapted from `agency-agents` philosophy

## Core Philosophy
Shift from a **Generalist Agent** (one agent doing everything) to a **Division-Based Pipeline** (a sequence of specialized experts). This increases output quality by ensuring each step of the process is handled by an agent optimized for that specific cognitive task.

## The Division Pipeline (Example: Outbound OS)

| Stage | Division/Agent | Primary Responsibility | Key Input | Key Output |
| :--- | :--- | :--- | :--- | :--- |
| **1. Intelligence** | **Wealth Scout / Lead Gen** | Signal detection & data harvesting. | Target Vertical/Keywords | Enriched Lead List + "Wealth Signals" |
| **2. Strategy** | **Persona Architect** | Analyzing lead psychology and mapping triggers. | Enriched Lead Data | Narrative Angle + Psychological Hook |
| **3. Execution** | **Copywriter** | Drafting high-conversion, tone-specific prose. | Narrative Angle + Framework | Draft Message |
| **4. Quality** | **QA Auditor** | Vibe-check, fact-verification, and spam-trigger removal. | Draft Message | Approved Output |

## Design Principles for New Divisions
When creating new agent divisions, follow these constraints:
1. **Atomic Responsibility:** One agent = one specific outcome.
2. **Hand-off Protocol:** Define exactly what the next agent needs to receive (e.g., JSON schema) to begin work.
3. **Context Isolation:** Agents only receive the data relevant to their stage, preventing "context drift" or noise.

## Potential Variations & Applications
- **Content Engine:** Researcher $\rightarrow$ Outliner $\rightarrow$ Writer $\rightarrow$ Editor $\rightarrow$ Distributor.
- **Recruitment (Hubert-X):** Sourcing $\rightarrow$ Screening $\rightarrow$ Outreach $\rightarrow$ Scheduling.
- **Client Onboarding:** Audit $\rightarrow$ Strategy $\rightarrow$ Roadmap $\rightarrow$ Implementation.
