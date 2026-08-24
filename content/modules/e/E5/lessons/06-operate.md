# E5 — Large-scale authorization and multi-tenant SaaS (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | body_tenant_ignored mismatch logs. |
| Signal (no bodies) | body_tenant_mismatch. |
| Revoke / recover | Audit B’s data for A’s actions. |
| Residual | Honest super-admin — E6 + 3.3. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/E5/e5-lab`.

## Transfer

Zanzibar tuple vs this binding.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
