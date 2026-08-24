# 7.1 — API contracts, protocols, and inventory (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | member, admin flag |
| Objects | display_name, is_admin |
| Actions | apply |
| Channels | JSON PATCH/PUT |
| TCB | Allow-listed writable fields server-side. |
| Untrusted | JSON keys, GraphQL mutations, protobuf unexpected fields |
| State / time | One PATCH; also undocumented /v0 leftover (inventory). |
| 1.1 cell | Authorization of properties. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| member | display_name | PATCH | allow |
| member | is_admin | PATCH | deny |
| admin | is_admin | PATCH | allow-audited |
| ghost /v0 | any | call | deny-or-inventory |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/7.1/7.1-lab` file `patch.py`.

## Transfer

GraphQL mutation arguments; gRPC unknown fields.

## Residual risk

Honest display_name XSS (6.2) is another cell.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
