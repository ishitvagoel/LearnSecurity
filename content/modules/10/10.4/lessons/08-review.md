# 10.4 — Deployment and configuration hardening (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
Review `labs/10.4/10.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/10.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): boot_ok prod debug True
- Seeded smell (label it yourself): Admin on 0.0.0.0
- Seeded smell (label it yourself): Migration fail-open
- Seeded smell (label it yourself): No rollback drill

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- IaC means hardened
- Canary equals secure config
- Feature flags are not TCB

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Feature flag that disables authz.
