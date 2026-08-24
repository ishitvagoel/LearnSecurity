# 10.1 — Secure software lifecycle and security culture (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
**Mechanism (not the property):** CODEOWNERS is not a threat model.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 10.1 |
|---|---|
| Root cause | Security as a later phase. |
| Preconditions | merge_ok({}) True. |
| Impact (1.1 cell) | Integrity of process evidence. — Surfaces without 3.2. |
| Prevention | Require tm id; triggers on identity, data, mobile… |
| Detection | merge_blocked_no_tm. |
| Recovery | Open TM, then merge. |

## Framework defaults vs application guarantees

CODEOWNERS is not a threat model.

## Mechanism limits and bypasses

A stale tm-id rubber stamp — 3.2 age.

Hotfix path without after-the-fact TM (must still record).

## Residual risk

Metrics vanity — count TMs with tests, not posters.

## Practice

Write the merge checklist line.

Run `labs/10.1/10.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Exception path (E6).

Clinic: “HIPAA training complete” as merge.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Merge and checklist UIs must be accessible to the actual reviewers you have.
