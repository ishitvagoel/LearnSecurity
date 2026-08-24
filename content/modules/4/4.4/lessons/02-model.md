# 4.4 — Authorization and tenant isolation (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | bob with n1 grant, alice owner |
| Objects | n1, n2, grant row |
| Actions | can_read |
| Channels | GET /notes/{id} |
| TCB | Lookup (subject, object) not (subject, any object). |
| Untrusted | Client-supplied note_id, “I’m a collaborator” boolean |
| State / time | Grant revoked on n1 (11, 2.4) must not linger on n1 either. |
| 1.1 cell | Authorization (1.1/1.2). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| bob | n1 | read | allow-if-granted |
| bob | n2 | read | deny |
| alice | n2 | read | allow-owner |
| anon | n1 | read | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/4.4/4.4-lab` file `grant.py`.

## Transfer

Property-level: bob can read title but not body (7.2).

## Residual risk

Honest grant on n1 still reveals n1 — that’s the product.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
