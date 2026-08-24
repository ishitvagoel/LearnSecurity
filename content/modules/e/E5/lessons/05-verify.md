# E5 — Large-scale authorization and multi-tenant SaaS (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | JSON body switches the bound tenant |
| Failure | Fail closed: Ignore body tenant; bind from session; RLS extra |

Lab tests: `test_property.py` under `labs/E5/e5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `JSON body switches the bound tenant`
- `--impl fixed`: **pass**

body cannot switch tenant.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Zanzibar tuple vs this binding.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
