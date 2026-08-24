# 9.5 — Authorized assessment, reporting, and remediation (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
Review `labs/9.5/9.5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/9.5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): close without retest
- Seeded smell (label it yourself): CVSS as the only priority
- Seeded smell (label it yourself): Live-target language
- Seeded smell (label it yourself): No variant search

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Pentest replaces SSDLC
- Critical CVSS must be first always
- Retest is the same as the original exploit blog

## Practice

Write three review notes. Do not open the keys file.

## Transfer

KEV vs internal-only.

## HITL / WCAG 2.2

Reports used by engineers must be readable (structure, not color-only severity).
