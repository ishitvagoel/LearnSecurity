# 7.4 — Queues, workers, events, and service identity (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | alice session, export-service |
| Objects | export job |
| Actions | exporter |
| Channels | queue payload |
| TCB | Service credential distinct from user sessions. |
| Untrusted | Job JSON, user ids inside jobs |
| State / time | Job delayed 6h after user deletion (4.1). |
| 1.1 cell | Authorization of the worker plane. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| user session | export job | run | deny-as-identity |
| service | export job | run | allow-least-priv |
| deleted user | old job | run | deny-4.1 |
| tB job | tA worker ctx | run | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/7.4/7.4-lab` file `worker.py`.

## Transfer

Outbox pattern; event schemas.

## Residual risk

Broker ACLs — 10.3.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
