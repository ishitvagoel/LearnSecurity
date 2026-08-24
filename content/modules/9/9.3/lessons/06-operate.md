# 9.3 — Security-focused tests (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | lint tests for security suite membership. |
| Signal (no bodies) | security_suite_missing_isolation. |
| Revoke / recover | Add negative tests. |
| Residual | Exploratory testing (9.5). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/9.3/9.3-lab`.

## Transfer

Fuzzing without an oracle.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
