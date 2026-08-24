# 9.2 — Secure code review (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | review_bot as aid not oracle (9.4). |
| Signal (no bodies) | review_block_eval. |
| Revoke / recover | Revert. |
| Residual | Unknown unknowns — 9.3 tests. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/9.2/9.2-lab`.

## Transfer

Terraform, GitHub Actions yaml.

## Usability

Review UI must be keyboard accessible; otherwise people rubber-stamp from a phone.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
