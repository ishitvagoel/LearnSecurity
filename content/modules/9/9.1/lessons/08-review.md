# 9.1 — Verification requirements and traceability (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
Review `labs/9.1/9.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/9.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): status-only coverage
- Seeded smell (label it yourself): ASVS copied wholesale
- Seeded smell (label it yourself): No isolation assert
- Seeded smell (label it yourself): Exceptions without expiry

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- ASVS certification exists as a sticker
- Number of tests is coverage
- Green build is Gate 9

## Practice

Write three review notes. Do not open the keys file.

## Transfer

MASVS STORAGE for 8.2.
