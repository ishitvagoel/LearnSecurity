# E6 — Product security leadership (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | exception_missing_owner. |
| Signal (no bodies) | exception_incomplete_denied. |
| Revoke / recover | Expire; fix or re-accept with fields. |
| Residual | Some risk always remains — that’s the point of an honest register. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/E6/e6-lab`.

## Transfer

Procurement questionnaire vs this record.

## Usability

The exception must record whether the residual includes an inaccessible control (1.4). Leadership owns that users cannot complete recovery.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
