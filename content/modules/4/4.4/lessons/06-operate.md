# 4.4 — Authorization and tenant isolation (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Deny logs (1.2 operate). |
| Signal (no bodies) | authz_deny{object}; grant_table_drift. |
| Revoke / recover | Revoke; audit bob’s reads. |
| Residual | Honest grant on n1 still reveals n1 — that’s the product. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/4.4/4.4-lab`.

## Transfer

Property-level: bob can read title but not body (7.2).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
