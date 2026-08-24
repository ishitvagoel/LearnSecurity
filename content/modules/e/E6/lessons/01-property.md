# E6 — Product security leadership (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
**Mechanism (not the property):** Jira “risk” issue type without dates.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For E6 |
|---|---|
| Root cause | Oral acceptance. |
| Preconditions | accept_exception({owner:'', review_by:None}) True. |
| Impact (1.1 cell) | Accountability of residual risk (1.1 + 1.4). — Unowned holes; inaccessible recovery (1.4) forever. |
| Prevention | Schema of an exception; refuse incomplete. |
| Detection | exception_missing_owner. |
| Recovery | Expire; fix or re-accept with fields. |

## Framework defaults vs application guarantees

Jira “risk” issue type without dates.

## Mechanism limits and bypasses

A perfect register that nobody reads.

Rename to “tech debt.”

## Residual risk

Some risk always remains — that’s the point of an honest register.

## Practice

Write one exception that would pass the lab.

Run `labs/E6/e6-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Procurement questionnaire vs this record.

Clinic: “HIPAA exception.”

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

The exception must record whether the residual includes an inaccessible control (1.4). Leadership owns that users cannot complete recovery.
