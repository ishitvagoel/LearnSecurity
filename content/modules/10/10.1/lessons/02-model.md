# 10.1 — Secure software lifecycle and security culture (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | author, reviewer |
| Objects | PR, tm-id |
| Actions | merge_ok |
| Channels | GitHub |
| TCB | Required field + human 9.2. |
| Untrusted | “tiny change” label |
| State / time | Every merge. |
| 1.1 cell | Integrity of process evidence. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| PR | tm-id+tests | merge | allow |
| PR | no tm | merge | deny |
| hotfix | no tm | merge | deny-or-timeboxed-E6 |
| poster | wall | merge | irrelevant |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/10.1/10.1-lab` file `sdl.py`.

## Transfer

Exception path (E6).

## Residual risk

Metrics vanity — count TMs with tests, not posters.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
