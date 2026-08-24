# 9.3 — Security-focused tests (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | CI, author |
| Objects | status_asserted-only test |
| Actions | is_security_test |
| Channels | pytest |
| TCB | Assert on deny/isolation/encoding… |
| Untrusted | Coverage % |
| State / time | PR build. |
| 1.1 cell | Integrity of evidence. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| test | HTTP 200 | security? | no |
| test | bob cannot read n1 | security? | yes |
| test | fuzz 5xx | security? | maybe-availability |
| test | mutation of grant | security? | yes |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/9.3/9.3-lab` file `stest.py`.

## Transfer

Fuzzing without an oracle.

## Residual risk

Exploratory testing (9.5).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
