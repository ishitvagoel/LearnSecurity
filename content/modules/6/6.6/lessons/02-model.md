# 6.6 — Workflow, race, and exceptional-condition failures (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | invitee, attacker with token copy |
| Objects | token t1, membership |
| Actions | accept |
| Channels | email link, API |
| TCB | Atomic consume of token. |
| Untrusted | Email channel, retries |
| State / time | Two accepts 1ms apart. |
| 1.1 cell | Integrity of membership workflow. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| invitee | fresh t1 | accept | allow |
| anyone | used t1 | accept | deny |
| attacker | stolen t1 unused | accept | residual-email |
| system | expired t1 | accept | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.6/6.6-lab` file `invite.py`.

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

## Residual risk

Email is a phishable channel (4.2).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
