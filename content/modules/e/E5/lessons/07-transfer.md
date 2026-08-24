# E5 — Large-scale authorization and multi-tenant SaaS (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Zanzibar tuple vs this binding.

**Product sketch:** Clinic group practice switching org_id in JSON.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Postgres RLS with a SET tenant from the body is this bug.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/E5/e5-lab` stays the only running system you may break.
