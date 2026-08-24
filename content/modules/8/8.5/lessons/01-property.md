# 8.5 — Mobile verification and privacy (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
**Mechanism (not the property):** Firebase Crashlytics “automatic” will ship whatever you log.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 8.5 |
|---|---|
| Root cause | Exception message includes the body. |
| Preconditions | secret in str(report). |
| Impact (1.1 cell) | Privacy/confidentiality of bodies in telemetry. — Bodies at a vendor; maybe public if misbucketed. |
| Prevention | Do not put bodies in exceptions; SDK filters; permission minimization. |
| Detection | CI grep crash fixtures; vendor DLP. |
| Recovery | Purge vendor; notify if needed. |

## Framework defaults vs application guarantees

Firebase Crashlytics “automatic” will ship whatever you log.

## Mechanism limits and bypasses

Play Data safety form is disclosure, not redaction.

Screenshots in bug reports; ANR traces.

## Residual risk

Vendor as processor — contract + 5.1.

## Practice

MASVS-PRIVACY traceability for this one cell.

Run `labs/8.5/8.5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Web Sentry (10.5) same cell.

Clinic crash with patient name.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

In-app “send feedback” must not require attaching a screenshot of PHI to proceed.
