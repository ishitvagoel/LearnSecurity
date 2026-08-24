# 10.1 — Secure software lifecycle and security culture (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
Review `labs/10.1/10.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/10.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): merge_ok True without tm
- Seeded smell (label it yourself): Security champion optional forever
- Seeded smell (label it yourself): Vanity vuln-count KPI
- Seeded smell (label it yourself): No change-trigger matrix

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- SAMM score is product security
- Culture cannot be tested
- SSDLC is a waterfall gate at the end

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Exception path (E6).

## HITL / WCAG 2.2

Merge and checklist UIs must be accessible to the actual reviewers you have.
