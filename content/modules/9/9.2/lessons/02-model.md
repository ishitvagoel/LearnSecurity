# 9.2 — Secure code review (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | reviewer, author |
| Objects | eval(user) |
| Actions | review_ok |
| Channels | PR |
| TCB | Human + checklist tied to 1.1 cells. |
| Untrusted | Green CI, pretty formatting |
| State / time | One PR. |
| 1.1 cell | Integrity of the change. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| reviewer | eval(user) | approve | deny |
| reviewer | bound SQL | approve | maybe |
| bot | comment | approve | never-alone |
| author | self-merge | prod | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/9.2/9.2-lab` file `review.py`.

## Transfer

Terraform, GitHub Actions yaml.

## Residual risk

Unknown unknowns — 9.3 tests.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
