# 9.3 — Security-focused tests (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
**Mechanism (not the property):** pytest-cov 90% is not 1.2.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 9.3 |
|---|---|
| Root cause | Happy path as assurance. |
| Preconditions | is_security_test({status_asserted: True}) True. |
| Impact (1.1 cell) | Integrity of evidence. — 4.4 holes with green CI. |
| Prevention | Require forbidden-outcome asserts. |
| Detection | lint tests for security suite membership. |
| Recovery | Add negative tests. |

## Framework defaults vs application guarantees

pytest-cov 90% is not 1.2.

## Mechanism limits and bypasses

Property tests still need oracles.

Renaming test_security_*.

## Residual risk

Exploratory testing (9.5).

## Practice

Write one forbidden-outcome test name for this module’s neighbors.

Run `labs/9.3/9.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Fuzzing without an oracle.

Clinic: test_get_patient_200.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
