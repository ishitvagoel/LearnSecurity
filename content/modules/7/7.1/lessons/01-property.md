# 7.1 — API contracts, protocols, and inventory (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
**Mechanism (not the property):** Pydantic extra=allow is this bug. FastAPI will happily take extra if your model does.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 7.1 |
|---|---|
| Root cause | Binder maps any key onto the entity. |
| Preconditions | apply(..., {is_admin: True}) succeeds. |
| Impact (1.1 cell) | Authorization of properties. — Privilege lift. |
| Prevention | Explicit writable set; ignore/reject unknown privileged fields. |
| Detection | rejected_field metric. |
| Recovery | Demote; audit. |

## Framework defaults vs application guarantees

Pydantic extra=allow is this bug. FastAPI will happily take extra if your model does.

## Mechanism limits and bypasses

Allow-list must track every protocol (REST, GraphQL, gRPC).

CSV import; admin BFF; 7.4 job payload.

## Residual risk

Honest display_name XSS (6.2) is another cell.

## Practice

Inventory endpoints; mark each field writable by which role.

Run `labs/7.1/7.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

GraphQL mutation arguments; gRPC unknown fields.

Clinic: PATCH patient {is_staff:true}.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
