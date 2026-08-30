# Callable Playbook Pattern — SOPs as Functions

> **Upstream clarification (OKF v0.2).** OKF does not have a dedicated "Playbook" section — `Playbook` appears in §4.1 as an example type. The formal upstream machinery for **callable contracts with parameters/executor/attester** is `type: Attested Computation` (§10). KlickSmartAI uses `type: Playbook` for human-executed SOPs (sales cadences, outreach sequences, validation routines) and reserves `type: Attested Computation` for values that must be reproducibly computed by a script. This doc covers both shapes; for the Attested Computation contract fields (`runtime`, `parameters`, `executor`, `attester`, `receipt`), defer to OKF v0.2 §10.

This document is the KlickSmartAI profile of OKF Playbook + Attested Computation patterns for company SOPs and runnable procedures.

## When to use Playbook vs Attested Computation

| Use `type: Playbook` when... | Use `type: Attested Computation` when... |
|---|---|
| Humans execute the steps (sales call, manual review, manual outreach) | A script / function produces a value the consumer must trust |
| Verification = human signed off on the SOP being correct | Verification = a deterministic attester script inspects a runtime receipt |
| The "output" is a decision or action, not a number | The "output" is a number, table, file, or other reproducible artifact |
| Example: `sop/cdfi-7-touch-outreach.md` (Veritas CDFI sales cadence) | Example: `computations/revenue.md` (finance FY revenue computation, per upstream §10 example) |

Both share the parameters/executor/attester shape; the difference is whether `runtime` is a human or a script.

## Minimum frontmatter

```yaml
---
okf_version: "0.2"
type: Playbook
title: <Human-readable name>
description: <one-sentence purpose>
status: stable
generated:
  by: human:<author>
  at: <ISO 8601 with offset>
verified:
  - by: human:<reviewer>
    at: <ISO 8601 with offset>
    evidence: <free-text citation, e.g. "Slack #sop-review 2026-08-29, signed off by Dennis">
parameters:
  - name: <param1>
    type: string | number | enum | boolean | object
    required: true | false
    default: <...>
    description: <one-sentence>
  - name: <param2>
    type: enum
    required: false
    default: <value>
    description: <one-sentence>
    enum: [val1, val2, val3]
executor:
  resource: <relative path to playbook body, or external URL>
  receipt: <expected receipt schema, see below>
attester:
  resource: <relative path to verification logic or test, or external URL>
sources:
  - id: <slug>
    resource: <url|path>
    title: <human-readable>
    author: <human:<name> or process:<id>>
---
```

## The 5 mandatory blocks

### 1. `parameters[]`

An ordered list of typed inputs the LLM must gather before invoking. Each entry has:
- `name` (camelCase or kebab-case — pick one and stick to it)
- `type` (OKF §6: `string` | `number` | `enum` | `boolean` | `object`)
- `required` (true | false)
- `default` (optional — applied if param omitted)
- `description` (one sentence)
- `enum` (when type=enum, list valid values)

**Convention:** name parameters by what they ARE, not what they're FOR. Example: `audience_id`, not `the_audience_we_want_to_target`.

### 2. `executor.resource`

Where the actual procedure lives. Two flavors:

**Internal (most common):** a relative path from the bundle root to a step-by-step markdown file.
```yaml
executor:
  resource: /sop/cdfi-7-touch-outreach-body.md
  receipt: cdfi-7-touch-outreach-receipt.md
```

**External:** a URL to a process or external doc.
```yaml
executor:
  resource: https://docs.internal.company.com/sop/cdfi-7-touch
  receipt: pdf-summary
```

The body file follows the executor content convention (see below).

### 3. `executor.receipt`

The expected output schema. Two forms:

**Markdown file:** name of a file in the same directory that documents the receipt shape.
```yaml
executor:
  resource: /sop/cdfi-7-touch-outreach-body.md
  receipt: cdfi-7-touch-outreach-receipt.md
```

**Schema name:** a free-text label for an inline schema.
```yaml
executor:
  resource: /sop/cdfi-7-touch-outreach-body.md
  receipt: "7-step outreach completion record: { step1_at: ISO 8601, ..., step7_at: ISO 8601, outcome: enum[meeting_booked|no_response|replied_only|opted_out] }"
```

### 4. `attester.resource`

Where the verification logic lives. Can be:
- A test script (Python / bash)
- A checklist markdown file
- A URL to an external verification service

```yaml
attester:
  resource: /sop/cdfi-7-touch-outreach-attester.md
```

The attester's job: confirm the executor's receipt actually satisfies the playbook's intent. Example: for a 7-touch outreach, the attester confirms each step's `at` timestamp is within the SOP's cadence window.

### 5. `verified[]`

Human review record. Required for `status: stable`. Must include at least one `human:` actor for trust tier to be Human-reviewed.

```yaml
verified:
  - by: human:dennis
    at: 2026-08-29T14:30:00-07:00
    evidence: "Verified against Veritas Reg D 506(b) compliance overlay"
  - by: human:david_poole
    at: 2026-08-29T15:00:00-07:00
    evidence: "Approved for CDFI relationship context"
```

## Executor body content convention

When `executor.resource` points to a markdown file, that file follows this structure:

```markdown
# <Playbook title> — Procedure

## Parameters (echoed from frontmatter)
- `<name>` (<type>, <required>): <description>
- ...

## Pre-conditions
- <what must be true before running>

## Steps
1. <step 1>
2. <step 2>
...

## Receipt (echoed from frontmatter)
<expected output shape>

## Failure modes
- <what could go wrong> → <how to handle>

## Examples
### Example 1: <scenario>
<walkthrough with actual values>
```

The body is documentation humans (and LLMs) read. The frontmatter is what LLMs parse programmatically.

## Worked example: cdfi-7-touch-outreach.md

This is the canonical example in the Veritas workspace (`/home/denni/wiki/clients/veritas-developments/sop/cdfi-7-touch-outreach.md`).

**Frontmatter:**

```yaml
---
okf_version: "0.2"
type: Playbook
title: CDFI 7-Touch Outreach (Faith-Framed)
description: 7-touch cadence for introducing Veritas to CDFIs and Christian foundations.
status: stable
generated:
  by: human:dennis
  at: 2026-08-29T11:00:00-07:00
verified:
  - by: human:dennis
    at: 2026-08-29T11:00:00-07:00
    evidence: "Initial authoring + compliance overlay against Reg D 506(b)"
  - by: human:david_poole
    at: 2026-08-29T14:00:00-07:00
    evidence: "Approved for CDFI relationship context"
parameters:
  - name: cdfi_name
    type: string
    required: true
    description: "Full legal name of the CDFI or Christian foundation"
  - name: contact_name
    type: string
    required: true
    description: "Primary contact at the CDFI"
  - name: asset_class
    type: enum
    required: false
    default: "manufactured-housing"
    description: "Asset class for the outreach"
    enum: ["manufactured-housing", "mixed-use", "multi-family"]
  - name: tier
    type: enum
    required: false
    default: "warm"
    description: "Outreach tier (warm intro vs cold)"
    enum: ["warm", "cold"]
executor:
  resource: /sop/cdfi-7-touch-outreach-body.md
  receipt: cdfi-7-touch-outreach-receipt.md
attester:
  resource: /sop/cdfi-7-touch-outreach-attester.md
sources:
  - id: veritas-compliance
    resource: /_config/compliance.md
    title: "Veritas Compliance Overlay"
    author: human:dennis
---
```

**How an LLM consumes this:**

1. Reads `type: Playbook` → knows this is callable, not just a doc.
2. Parses `parameters[]` → knows it needs `cdfi_name` + `contact_name`, can prompt the user for them.
3. If `asset_class` and `tier` are missing, applies defaults.
4. Follows `executor.resource` → opens `/sop/cdfi-7-touch-outreach-body.md`.
5. Walks the 7 steps, produces output matching `executor.receipt` schema.
6. Verifies output via `attester.resource` → opens `/sop/cdfi-7-touch-outreach-attester.md`.
7. Records receipt in the bundle's `log.md` for auditability.

**No human in the loop needed for invocation** — the `verified[]` block in the frontmatter is the standing human approval. The attester + executor ensure correctness.

## Authoring checklist

When creating or upgrading a SOP to callable Playbook:

- [ ] `type: Playbook` (not `Reference`)
- [ ] `status: stable` (after human review)
- [ ] `parameters[]` is complete and typed
- [ ] `executor.resource` exists and is reachable
- [ ] `executor.receipt` is documented (markdown file or inline schema)
- [ ] `attester.resource` exists and is reachable
- [ ] `verified[]` has at least one `human:` entry
- [ ] `generated.by` is `human:<author>` (not `agent:<skill-name>` unless the agent truly wrote it)
- [ ] `sources[]` cites the bundle's compliance overlay and any upstream procedures
- [ ] Body file (if separate) follows the executor content convention

## When NOT to use Playbook

- **Single-step procedures** (e.g. "send a Slack reminder every Friday") → plain `Reference` doc is fine; the ceremony of a callable function is overkill.
- **Procedures still in flux** → use `status: draft` first; promote to `stable` + Playbook only after the procedure has been run 3+ times.
- **Procedures with no clear receipt** → if you can't define a receipt schema, the procedure is too vague to be callable; write it as a reference doc and revisit.

## Bundle-level impact

A bundle with multiple `type: Playbook` files becomes a **portable procedural library** — any LLM that ingests the bundle can call any of the SOPs as a function. This is the highest-value OKF pattern for KlickSmartAI client workspaces because:

1. Dennis's writing style, compliance overlays, and CDFI relationship patterns become reusable functions any agent can call.
2. New agents (or LLMs from other vendors) can run the same SOPs without re-onboarding.
3. The `verified[]` block is the standing compliance sign-off — no need to re-validate per execution.
