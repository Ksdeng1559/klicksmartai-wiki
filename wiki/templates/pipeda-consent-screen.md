---
title: PIPEDA Consent Screen Template — KlickSmartAI OS
description: Standard onboarding consent screen for financial advisor OS deployments. Compliant with PIPEDA s.6-7 requirements for contact graph data processing.
audience: Canadian financial advisors, wealth managers, mortgage brokers, estate planners
compliance: PIPEDA (GAP-19 alignment), SOC 2 Type II, air-gapped optional
---

# PIPEDA Consent Screen Template
## KlickSmartAI OS — Financial Services Onboarding

**Version:** 1.0  
**Date:** 2026-04-18  
**Purpose:** Standalone consent screen for contact graph import. Used at OS onboarding alongside or after general Terms of Service. Must appear **before** any contact data is requested or imported.  

---

## Design principles

1. **Separate from T&Cs** — consent for contact graph import must not be bundled into a general terms checkbox. It requires its own explicit opt-in.
2. **Plain language** — no legalese. Every sentence answers "what does this mean for me?"
3. **Purpose-stated** — explicitly name the purpose: "to find warm introduction paths within your professional network."
4. **Data minimisation visible** — show exactly what is and is not imported.
5. **Withdrawable** — advisor can revoke consent at any time via Settings → Privacy.

---

## Page layout

**Title (H1):**  
`Connect Your Professional Network`

**Subtitle:**  
`This helps [Advisor OS] find warm introduction paths — it only touches the data you choose.`

---

## Section 1 — What this does

> When you import your LinkedIn connections or contact list, [Platform] builds a private relationship map that helps identify which contacts are best positioned to introduce you to qualified prospects. **No one else can see your network. Your data is never shared or cross-matched with other users.**

---

## Section 2 — What data is imported (and what is not)

| ✓ Imported | ✗ Never imported |
|-----------|-----------------|
| Name | Email addresses |
| Job title | Phone numbers |
| Company name | LinkedIn private messages |
| LinkedIn profile URL | Full LinkedIn connection list (read-only URL reference only) |
| Most recent interaction date | |
| Connection degree (1st, 2nd, 3rd) | |

---

## Section 3 — How your data is protected

**Your data never leaves your server.**  
If your firm uses the air-gapped deployment option, all relationship data stays inside your network infrastructure at all times.

**Isolation by design.**  
Every advisor account is in a separate tenant. Your contact graph is visible only to you and your authorised team members.

**You own it. You can delete it.**  
Revoke consent at any time in Settings → Privacy, and all contact graph data is deleted within **30 days.**

**Transparency.**  
Every query against your relationship graph is logged with timestamp and user ID. Audit logs available on request.

**If a breach occurs, we notify you immediately.**  
Reportable breach events trigger an alert within 24 hours, along with a complete incident report.

---

## Section 4 — Compliance certifications

- SOC 2 Type II certified
- PIPEDA-compliant data processing
- Air-gapped deployment available (zero internet dependency for contact data)
- GDPR-aligned architecture (applies if you have EU clients)

---

## Section 5 — Consent statement

> I understand that [Platform] will import and process my contact network data — limited to names, titles, companies, and public-facing LinkedIn profile URLs — to generate warm introduction path recommendations within my account only.
>
> I understand I can revoke this consent at any time and request deletion of my contact graph data.
>
> I have read and understand the [Privacy Policy →] and this consent form.

---

## Section 6 — Consent checkbox (REQUIRED)

```
☐  I consent to having my professional contact network imported and processed 
    as described above. I understand I can withdraw this consent at any time.
```

**Checkbox label:**  
`"Yes, help me find warm introduction paths"`  
(or similar plain-language affirmative action label)

---

## Section 7 — Legal footer

> This consent form is provided in accordance with **PIPEDA sections 6 and 7** (consent and purpose limitations) and **PIPEDA section 28** (retention and access rights). By checking the box above, you confirm you are authorised to share the contact data within your organisation. If you are uncertain, consult your compliance team or legal counsel before proceeding.
>
> For questions: **privacy@[yourplatform.com]**  
> Privacy Policy: **[URL]**  
> Data Deletion Request: **[Settings → Privacy or URL]**

---

## Implementation checklist

- [ ] Separate page from T&Cs — not bundled into a general terms checkbox
- [ ] Appears before any contact import API is called
- [ ] Consent event logged: `{timestamp, user_id, consent_version, action: "granted"|"revoked"}`
- [ ] `rm_nodes` schema: name, title, company, LinkedIn URL, interaction_recency only — no email, no phone
- [ ] Data deletion endpoint tested: `DELETE /advisor/{id}/contact-graph`
- [ ] Consent revocation path: Settings → Privacy → "Revoke contact graph consent"
- [ ] Audit log query available for advisor: "Show my data access history"
- [ ] Privacy policy updated to reference relationship graph processing
- [ ] Legal counsel reviewed for firm's specific PIPEDA obligations

---

## Source

- WWR v2.0 PRD §0C — GAP-19 PIPEDA compliance requirements  
- PIPEDA SC 2000, c. 5 — sections 6 (consent), 7 (purpose limitation), 28 (retention/access)
- OS Deployment: Klick2Client OS + KlickSmartAI OS

---

## Notes

**Why no email/phone in `rm_nodes`:**  
PIPEDA's highest-sensitivity bucket is contact information that enables direct outreach. By excluding email addresses and phone numbers from the relationship graph entirely, the OS stays outside the most regulated data category while still powering the pathfinding algorithm via degree-of-separation scoring.

**Scope: BC, Ontario, Alberta (PIPEDA). Quebec (QPAMP) and mortgage brokers (OSMV) are out of scope for this template — separate addenda required before deployment in those jurisdictions.**

**For mortgage brokers (OSMV regulated):** The Office des services aux entreprises et aux professionnels financiers (OSMV) in Quebec has specific record-keeping requirements. Firms with Quebec-based clients or employees should add a QPAMP addendum to this consent screen.

> **Note: Quebec and OSMV-regulated mortgage brokers are out of scope for this deployment.**