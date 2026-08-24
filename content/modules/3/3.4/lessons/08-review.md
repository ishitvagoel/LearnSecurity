# 3.4 — Business logic and abuse-resistant design (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
Review `labs/3.4/3.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/3.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): Cap in React only
- Seeded smell (label it yourself): No transaction around count+insert
- Seeded smell (label it yourself): Test loops 8 times and expects success
- Seeded smell (label it yourself): Support tool bypasses cap without audit

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Business logic is not security
- Rate limits replace product caps
- CWE-799 is the requirement

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Invite tokens (6.6) and export quotas (6.7).

## HITL / WCAG 2.2

Error “share limit reached” must be programmatically announced (WCAG 4.1.3), not only a red border.
