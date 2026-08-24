# 7.1 — API contracts, protocols, and inventory (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | rejected_field metric. |
| Signal (no bodies) | unknown_field_rejected; shadow_endpoint_scan. |
| Revoke / recover | Demote; audit. |
| Residual | Honest display_name XSS (6.2) is another cell. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/7.1/7.1-lab`.

## Transfer

GraphQL mutation arguments; gRPC unknown fields.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
