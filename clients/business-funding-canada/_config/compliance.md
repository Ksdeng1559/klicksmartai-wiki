---
type: Compliance
title: "Business Funding Canada — Compliance"
status: active
generated: 2026-10-02
verified: 2026-10-02
jurisdiction: Canada (BC primary; AB, ON, others as §3.2)
---

# Compliance

> **Read before drafting any client-facing copy.** BFC is a **pay-per-lead generator** for Canadian SMB business funding — NOT a lender, broker, or mortgage broker. This workspace captures SMB-owner funding inquiries and resells them to funders / brokers / lenders (the "buyers"). Compliance overlay reflects that.

## 1. Federal — PIPEDA

The Personal Information Protection and Electronic Documents Act governs collection, use, and disclosure of personal information in commercial activities.

- **SMB-owner PII collected:** name, contact, business financials, personal guarantee info, identity.
- **Rule:** No real SMB-owner PII lands in `drafts/`, `projects/`, or `deliverables/`. Use synthetic placeholders.
- **Lead-transfer disclosure:** Every lead transferred to a buyer is a PIPEDA-controlled disclosure. **Express consent from the SMB owner is required** before any PII leaves BFC. Consent language must be specific to the buyer (or to "a network of approved funders / brokers").
- **Source:** https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/

## 2. Federal — CASL (Canada's Anti-Spam Legislation)

Applies to all commercial email + SMS to Canadian recipients.

- **Express consent** required before sending marketing email/SMS — to lead sources AND to any lead-buyer outreach.
- **Unsubscribe** must be one-click + honored within 10 business days.
- **Identification:** every email identifies BFC + physical address.
- **Source:** https://www.fightspam.gc.ca/

## 3. Provincial regulators — limited reach for SMB lending AND lead generation

Unlike mortgage brokerage, **most alternative SMB financing is not provincially regulated** in Canada. And **lead generation itself is generally unregulated** at the provincial level in most provinces (with evolving case law and some provincial statutes catching up).

### 3.1 BC — BCFSA
- BC Financial Services Authority. **Mortgage brokers only.** Out of scope for BFC.
- Source: https://www.bcfsa.ca/

### 3.2 Alberta — RECA
- Real Estate Council of Alberta. **Mortgage brokers only.** Out of scope for BFC.
- Source: https://www.reca.ca/

### 3.3 Ontario — FSRA
- Financial Services Regulatory Authority of Ontario. **Mortgage brokers only.** Out of scope for BFC.
- Source: https://www.fsrao.ca/

### 3.4 Quebec — OACIQ
- _Organisme d'autoréglementation du courtage immobilier du Québec_. **Mortgage brokers only.** Out of scope for BFC.
- Source: https://www.oaciq.com/

**Operational implication:** BFC's compliance overlay is **PIPEDA + CASL + per-buyer contracts + per-province any lead-gen rules**. Provincial mortgage-broker regulators do NOT apply. Don't invoke BCFSA / RECA / FSRA on BFC copy.

## 4. BFC-specific language — what NOT to say

Because BFC is **not** the lender, the following are non-expermissible in any BFC copy (landing page, ad, content, email, lead-magnet):

- [x] **No rate quote** — BFC does not set rates. (If comparative rate content is needed, label as "indicative — your funder will quote.")
- [x] **No "guaranteed approval"** — BFC does not approve.
- [x] **No "lender" or "broker" self-description** — BFC is a **lead-generation service**. Use "connects you with funders", "matches you with approved partners", or "we generate your funding request and send it to qualified funders."
- [x] **No "act now" / urgency** framing on financial products.
- [x] **No direct solicitation of credit applications** in language that implies BFC will fund. The lead is the product, not the credit decision.

**Permissible language:**
- "Get matched with funders for your business funding needs"
- "Submit your funding request in 2 minutes"
- "We connect Canadian SMBs with funders / brokers who specialize in [vertical]"
- "Our network of approved funders will contact you with offers"

## 5. Lead form compliance — required fields & disclosures

Every lead capture form (BFC landing pages, content CTAs, paid acquisition landing pages) must include:

- **Express consent checkbox:** "I agree to be contacted by [Business Funding Canada name] and its network of approved funders / brokers about my funding request. I understand my information will be transferred to those partners per the [Privacy Policy]."
- **Identification:** BFC's legal name + physical address in the consent block.
- **CASL compliance:** if the form is also subscribing the user to marketing email/SMS, separate checkbox required.
- **PIPEDA-compliant privacy policy** linked from every form page.
- **Right to withdraw consent** statement.

## 6. Lead-buyer compliance (separate layer)

When BFC transfers a lead to a buyer:

- **Buyer must agree** under contract to PIPEDA-compliant handling of the PII BFC transfers.
- **Buyer must agree** under contract not to resell the lead to a third party without BFC's consent.
- **Buyer must agree** under contract to honor the SMB owner's withdrawal-of-consent request within 10 business days.
- **BFC must track** which buyer received which lead (audit trail) — for PIPEDA accountability.
- **Lead-buyer contracts** live in `_config/lead-buyers/` (when present).

## 7. Borrower / SMB data handling

- **Never** copy real SMB owner names, real financials, real customer data into drafts.
- If a research artifact needs a real-world example, use synthetic placeholders + cite the public source.
- Audit log: every place SMB owner data appears in `research/` should be reviewed for synthetic-vs-real status.

## 8. Approved-for-external-use claims

Per OKF §9 + the CBS citation discipline: every load-bearing claim in client-facing artifacts carries `{source, owner, retrieved_at, effective_date, status: Draft|Corroborated|Verified|Counsel Approved, approved_for_external_use, expires_or_reverify_on}`. Only `Verified` and `Counsel Approved` claims may be quoted externally without further review.

## 9. When in doubt

Pause. Escalate to Dennis. Do not invent lead-pricing claims, buyer claims, or regulatory language.