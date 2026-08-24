# 9.1 — Verification requirements and traceability (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
**Mechanism (not the property):** ASVS PDF is not your matrix.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 9.1 |
|---|---|
| Root cause | Status without evidence. |
| Preconditions | covered True when asserts_isolation False. |
| Impact (1.1 cell) | Integrity of the assurance case. — Ship 1.2 holes with a green gate. |
| Prevention | Coverage predicate requires the isolation assert. |
| Detection | CI: every L2 req maps a test id. |
| Recovery | Add tests; do not backfill “done.” |

## Framework defaults vs application guarantees

ASVS PDF is not your matrix.

## Mechanism limits and bypasses

Level 2 tailored — say what you dropped (E6).

Test named test_authz that asserts 200.

## Residual risk

Unmapped Level 3 risks.

## Practice

One chain for AUTHZ-1.

Run `labs/9.1/9.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

MASVS STORAGE for 8.2.

Clinic: HIPAA “done” column.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
