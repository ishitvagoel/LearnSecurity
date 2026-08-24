# 10.4 — Deployment and configuration hardening (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Production process boots with debug enabled |
| Failure | Fail closed: Refuse boot; config review; no debug routes registered |

Lab tests: `test_property.py` under `labs/10.4/10.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Production process boots with debug enabled`
- `--impl fixed`: **pass**

prod debug must not boot.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Feature flag that disables authz.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
