# 7.2 — Object, property, and function security (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Member resolves secret_internal |
| Failure | Fail closed: Allow-list fields by role; never bind authz to the id format |

Lab tests: `test_property.py` under `labs/7.2/7.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Member resolves secret_internal`
- `--impl fixed`: **pass**

member cannot resolve secret_internal.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Bulk update; search highlighting leaking snippets.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
