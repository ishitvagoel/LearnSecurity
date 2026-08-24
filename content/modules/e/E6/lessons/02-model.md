# E6 — Product security leadership (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | VP eng, security, users who need a11y |
| Objects | exception record |
| Actions | accept_exception |
| Channels | risk register |
| TCB | Required fields + expiry. |
| Untrusted | Slide deck, chat thumbs-up |
| State / time | Until review_by. |
| 1.1 cell | Accountability of residual risk (1.1 + 1.4). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| VP | complete record | accept | allow |
| VP | empty owner | accept | deny |
| expired | past review_by | still-open | deny-or-revisit |
| a11y residual | flag | record | required |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/E6/e6-lab` file `risk.py`.

## Transfer

Procurement questionnaire vs this record.

## Residual risk

Some risk always remains — that’s the point of an honest register.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
