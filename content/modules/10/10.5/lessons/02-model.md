# 10.5 — Logging, detection, incident response, recovery, maintenance (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | IR lead, engineer |
| Objects | incident ticket |
| Actions | close_incident |
| Channels | tracker, backups |
| TCB | Checklist: contain, revoke, retest, recover, learn. |
| Untrusted | “logs=ok” as enough |
| State / time | After contain. |
| 1.1 cell | Resilience — recover is part of the 1.1 cell when prevention failed. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| incident | restore+revoke | close | allow |
| incident | recovery todo | close | deny |
| logs | bodies | store | deny-3.1 |
| EOL | unpatched | run | deny-or-E6 |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/10.5/10.5-lab` file `ir.py`.

## Transfer

Ransomware restore vs note-level integrity.

## Residual risk

Some incidents never get perfect forensic certainty — say so.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
