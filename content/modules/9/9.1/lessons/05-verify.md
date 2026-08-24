# 9.1 — Verification requirements and traceability (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Status-only row counted as AUTHZ-1 coverage |
| Failure | Fail closed: Coverage predicate requires the isolation assert |

Lab tests: `test_property.py` under `labs/9.1/9.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Status-only row counted as AUTHZ-1 coverage`
- `--impl fixed`: **pass**

asserts_isolation False => not covered.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

MASVS STORAGE for 8.2.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
