# 7.2 — Object, property, and function security (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
**Mechanism (not the property):** SQLAlchemy to_dict() is not a policy.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 7.2 |
|---|---|
| Root cause | Serializer dumps the ORM object. |
| Preconditions | resolve('member','secret_internal') True. |
| Impact (1.1 cell) | Authorization at property grain. — Internal secret or PII extra. |
| Prevention | Allow-list fields by role; never bind authz to the id format. |
| Detection | field_denied. |
| Recovery | Rotate the secret; audit. |

## Framework defaults vs application guarantees

SQLAlchemy to_dict() is not a policy.

## Mechanism limits and bypasses

Hiding fields in UI only.

CSV export; 7.4; debug toolbar.

## Residual risk

Admin sees secret_internal — audited.

## Practice

Table: role × field.

Run `labs/7.2/7.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Bulk update; search highlighting leaking snippets.

Clinic: member cannot resolve ssn.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
