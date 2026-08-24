# E5 — Large-scale authorization and multi-tenant SaaS (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
**Mechanism (not the property):** Postgres RLS with a SET tenant from the body is this bug.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For E5 |
|---|---|
| Root cause | Client-chosen tenant. |
| Preconditions | tenant_for({A},{B}) == B. |
| Impact (1.1 cell) | Authorization of the tenant context. — Cross-tenant read/write at scale. |
| Prevention | Ignore body tenant; bind from session; RLS extra. |
| Detection | body_tenant_ignored mismatch logs. |
| Recovery | Audit B’s data for A’s actions. |

## Framework defaults vs application guarantees

Postgres RLS with a SET tenant from the body is this bug.

## Mechanism limits and bypasses

Search indexes, caches (2.2), data lakes — every copy.

Support impersonation without audit (E6).

## Residual risk

Honest super-admin — E6 + 3.3.

## Practice

List every place tenant is read from.

Run `labs/E5/e5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Zanzibar tuple vs this binding.

Clinic group practice switching org_id in JSON.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
