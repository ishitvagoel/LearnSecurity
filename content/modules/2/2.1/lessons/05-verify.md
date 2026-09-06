# 2.1-LO-05 — Evidence is a failing test, then a passing pair

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-2.2.1`; RFC 8259 JSON (STD 90, final).

## An invariant that cannot fail a test is still a slogan

Happy-path HTTP 200 is not this module’s evidence (see 9.3). The oracle is the local pair against a named forbidden outcome.

## Mental model: fail-on-vulnerable, pass-on-fixed

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F[Must fail duplicate-key assertion]
  X["--impl fixed"] --> P[Must pass both CLEAN and AMBIGUOUS]
  F --> E[Evidence the property was false]
  P --> E2[Evidence the predicate is now true]
```

| Case | Must show |
|---|---|
| Normal | CLEAN unique-key JSON is accepted with `acl_tenant == stored_tenant == tA` |
| Negative / abuse | AMBIGUOUS duplicate keys: rejected **or** both tenants identical |
| Failure default | Uncertainty does not persist a body under a guessed tenant |

Lab tests: `test_unambiguous_json_is_accepted` and `test_duplicate_tenant_keys_are_one_meaning` in `labs/2.1/2.1-parser-boundaries/tests/test_parser.py`.

```text
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl vulnerable
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl fixed
```

Map each test to a matrix cell from LO-02. Do not paste keys.

## What the tests do not prove

- PostgreSQL `jsonb` agreement
- GraphQL variable parsing
- Unicode identifier spoofing
- Authorization for an honest unique-key object (that is 1.2)

Record those as residuals or later modules, not as silent passes.

## Practice

Execute both implementations this session. If vulnerable does not fail, the lab is miswired—fix the wiring, not the assertion.

## Transfer

GraphQL and REST both ingest the same note. A test that only asserts status 200 on `/graphql` is not parser-agreement evidence.
