# 10.5 — Logging, detection, incident response, recovery, maintenance (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
**Mechanism (not the property):** PagerDuty is not recovery.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 10.5 |
|---|---|
| Root cause | Close on detection quality. |
| Preconditions | close_incident({recovery:'todo', logs:'ok'}) True. |
| Impact (1.1 cell) | Resilience — recover is part of the 1.1 cell when prevention failed. — System still broken or attacker still in. |
| Prevention | Require recovery evidence (restore test, revoke list). |
| Detection | closed_without_recovery. |
| Recovery | This *is* the step — restore drill. |

## Framework defaults vs application guarantees

PagerDuty is not recovery.

## Mechanism limits and bypasses

Observability pipeline as exfil (3.1).

Mark recovery N/A without E6.

## Residual risk

Some incidents never get perfect forensic certainty — say so.

## Practice

Tabletop: stolen session (4.3) — detect, revoke, recover.

Run `labs/10.5/10.5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Ransomware restore vs note-level integrity.

Clinic: close ticket when SIEM is green.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

IR runbooks and status pages must be usable under stress (keyboard, language, not color-only severity).
