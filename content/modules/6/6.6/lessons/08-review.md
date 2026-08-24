# 6.6 — Workflow, race, and exceptional-condition failures (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
Review `labs/6.6/6.6-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.6.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): accept always True
- Seeded smell (label it yourself): No unique constraint
- Seeded smell (label it yourself): Fail-open on DB error
- Seeded smell (label it yourself): Token in query logs (4.3)

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- 400 errors are fail-safe
- Email links are authenticators of the recipient
- Races are only performance

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

## HITL / WCAG 2.2

Invite errors (“link already used”) must be announced accessibly so people do not retry into a support backdoor.
