# E5 — Large-scale authorization and multi-tenant SaaS (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
Review `labs/E5/e5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/E5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): tenant from body
- Seeded smell (label it yourself): RLS session var from JSON
- Seeded smell (label it yourself): Cache key without tenant (2.2)
- Seeded smell (label it yourself): Support impersonation silent

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- RLS replaces app mediation
- Subdomain is unforgeable tenant
- Scale means we switch to IAM instead of 1.2

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Zanzibar tuple vs this binding.
