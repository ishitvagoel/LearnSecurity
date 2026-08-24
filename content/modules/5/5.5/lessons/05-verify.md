# 5.5 — Database and persistence security (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Query built by concatenating untrusted strings into SQL |
| Failure | Fail closed: Parameters; identifier allow-lists for ORDER BY |

Lab tests: `test_property.py` under `labs/5.5/5.5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Query built by concatenating untrusted strings into SQL`
- `--impl fixed`: **pass**

is_bound true; concat fails the test.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

NoSQL operators, GraphQL args (7.1).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
