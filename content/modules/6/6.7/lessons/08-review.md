# 6.7 — Resource abuse, automation, and availability (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
Review `labs/6.7/6.7-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.7.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): No cap
- Seeded smell (label it yourself): Limit only in frontend
- Seeded smell (label it yourself): Global IP limit
- Seeded smell (label it yourself): No test fourth denied

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Availability is ops not appsec
- Captcha replaces quotas
- Autoscaling is the control

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Notification fan-out; search complexity.

## HITL / WCAG 2.2

Quota errors must be readable; do not trap keyboard users in a spinner that retries (amplifying load).
