# 4.4 — Authorization and tenant isolation (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Grant on n1 authorizes n2 |
| Failure | Fail closed: Grant keyed by note id; deny default |

Lab tests: `test_property.py` under `labs/4.4/4.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Grant on n1 authorizes n2`
- `--impl fixed`: **pass**

n1 maybe true; n2 false.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Property-level: bob can read title but not body (7.2).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
