# 8.5 — Mobile verification and privacy (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | crash SDK, developer |
| Objects | stack trace, note body |
| Actions | crash_report |
| Channels | HTTPS to vendor, logcat |
| TCB | Redaction before send. |
| Untrusted | Third-party SDK, verbose logging |
| State / time | Crash at view-note. |
| 1.1 cell | Privacy/confidentiality of bodies in telemetry. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| SDK | body | send | deny |
| SDK | stack | send | allow |
| logcat | body | print | deny |
| vendor | retention | 5.1 | contract |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/8.5/8.5-lab` file `crash.py`.

## Transfer

Web Sentry (10.5) same cell.

## Residual risk

Vendor as processor — contract + 5.1.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
