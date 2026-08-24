# E5 — Large-scale authorization and multi-tenant SaaS (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | session A, body B |
| Objects | tenant id |
| Actions | tenant_for |
| Channels | JSON, header, subdomain |
| TCB | Bound tenant from session/host. |
| Untrusted | body.tenant, X-Tenant |
| State / time | One request; also analytics warehouse (5.1, 3.3). |
| 1.1 cell | Authorization of the tenant context. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| session A | body B | tenant | A |
| session A | no body | tenant | A |
| RLS | SET from body | run | deny |
| lake | export | tenant | bind |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/E5/e5-lab` file `rls.py`.

## Transfer

Zanzibar tuple vs this binding.

## Residual risk

Honest super-admin — E6 + 3.3.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
