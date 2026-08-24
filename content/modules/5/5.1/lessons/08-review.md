# 5.1 — Data lifecycle and privacy engineering (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
Review `labs/5.1/5.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/5.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): delete_account only NOTES.pop
- Seeded smell (label it yourself): Analytics “immutable for ML” without exception record
- Seeded smell (label it yourself): No test body_retained after delete
- Seeded smell (label it yourself): Privacy policy PDF as the control

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Encryption makes retention OK
- Privacy equals confidentiality
- GDPR text in footer is the invariant

## Practice

Write three review notes. Do not open the keys file.

## Transfer

CSV export to a partner; clinic-booking card PHI.

## HITL / WCAG 2.2

Delete-account journey must be completable with keyboard and clear status (WCAG 3.3.x). An unreachable delete is a privacy incident (1.4).
