# 4.4 — Authorization and tenant isolation (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
**Mechanism (not the property):** Depends(get_user) is not Depends(can_read_note).

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 4.4 |
|---|---|
| Root cause | Collection-level “has any grant” flag. |
| Preconditions | can_read(bob, n2) true because bob has n1. |
| Impact (1.1 cell) | Authorization (1.1/1.2). — Unauthorized read of n2 body. |
| Prevention | Grant keyed by note id; deny default. |
| Detection | Deny logs (1.2 operate). |
| Recovery | Revoke; audit bob’s reads. |

## Framework defaults vs application guarantees

Depends(get_user) is not Depends(can_read_note).

## Mechanism limits and bypasses

UUID obscurity is not a grant.

GraphQL node(id); export zip; search index (2.2).

## Residual risk

Honest grant on n1 still reveals n1 — that’s the product.

## Practice

Four cells: bob×{n1,n2} × read.

Run `labs/4.4/4.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Property-level: bob can read title but not body (7.2).

Clinic: grant on appointment A ≠ chart B.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
