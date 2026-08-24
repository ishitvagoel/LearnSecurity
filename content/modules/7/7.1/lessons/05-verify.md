# 7.1 — API contracts, protocols, and inventory (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Client PATCH sets is_admin |
| Failure | Fail closed: Explicit writable set; ignore/reject unknown privileged fields |

Lab tests: `test_property.py` under `labs/7.1/7.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Client PATCH sets is_admin`
- `--impl fixed`: **pass**

PATCH is_admin does not stick.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

GraphQL mutation arguments; gRPC unknown fields.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
