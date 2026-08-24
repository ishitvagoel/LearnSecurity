# 10.5 — Logging, detection, incident response, recovery, maintenance (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | closed_without_recovery. |
| Signal (no bodies) | incident_closed_without_recovery denied. |
| Revoke / recover | This *is* the step — restore drill. |
| Residual | Some incidents never get perfect forensic certainty — say so. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/10.5/10.5-lab`.

## Transfer

Ransomware restore vs note-level integrity.

## Usability

IR runbooks and status pages must be usable under stress (keyboard, language, not color-only severity).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
