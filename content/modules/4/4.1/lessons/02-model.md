# 4.1 — Identity lifecycle (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | deleted user, leftover session, admin |
| Objects | session token, notes |
| Actions | delete_user, session_valid, read |
| Channels | cookie, worker job |
| TCB | Session store checks user state on every use. |
| Untrusted | JWT still-signed after deletion (4.3/4.5) |
| State / time | T+0 delete; T+1h replay cookie. |
| 1.1 cell | Authorization over time (1.2 + 2.4). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| alice live | n1 | read | allow |
| alice deleted+cookie | n1 | read | deny |
| admin | alice | delete | allow-audited |
| worker | alice jobs | run | deny-after-delete |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/4.1/4.1-lab` file `lifecycle.py`.

## Transfer

Contractor access end-date; support impersonation tickets.

## Residual risk

Backups still contain the user row — 5.1.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
