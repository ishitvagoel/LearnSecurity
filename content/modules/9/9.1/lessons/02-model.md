# 9.1 — Verification requirements and traceability (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | reviewer, CI, requirement AUTHZ-1 |
| Objects | status cell, test that asserts isolation |
| Actions | covered |
| Channels | assurance matrix |
| TCB | Link to a failing-on-vulnerable test. |
| Untrusted | Colour in Jira |
| State / time | Release day. |
| 1.1 cell | Integrity of the assurance case. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| AUTHZ-1 | isolation test | cover | allow |
| AUTHZ-1 | status done | cover | deny |
| AUTHZ-1 | HTTP 200 test | cover | deny |
| exception | unmapped | ship | E6 |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/9.1/9.1-lab` file `trace.py`.

## Transfer

MASVS STORAGE for 8.2.

## Residual risk

Unmapped Level 3 risks.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
