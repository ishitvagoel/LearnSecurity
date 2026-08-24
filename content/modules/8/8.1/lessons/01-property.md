# 8.1 — Hostile-client and mobile platform model (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
**Mechanism (not the property):** Play Integrity is a signal, not 1.2.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 8.1 |
|---|---|
| Root cause | Policy evaluated on the attacker’s CPU. |
| Preconditions | allow_export({integrity:ok}, 'fail') True. |
| Impact (1.1 cell) | Authorization — server decides. — Export without server authority. |
| Prevention | Ignore client integrity for authorization; server attest/session 1.2. |
| Detection | client_claim_ignored; attest_fail. |
| Recovery | Revoke app tokens. |

## Framework defaults vs application guarantees

Play Integrity is a signal, not 1.2.

## Mechanism limits and bypasses

Attestation raises cost, does not establish trust of the client binary.

Old app version; emulator farms.

## Residual risk

Honest users on rooted devices — product policy.

## Practice

Responsibility matrix: client vs server for each 1.1 cell.

Run `labs/8.1/8.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Feature flags in the APK; premium=true.

Clinic Android: client says hipaaMode=true.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
