# E6 — Product security leadership (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Risk exception accepted without owner and review date |
| Failure | Fail closed: Schema of an exception; refuse incomplete |

Lab tests: `test_property.py` under `labs/E6/e6-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Risk exception accepted without owner and review date`
- `--impl fixed`: **pass**

exception needs owner, review date, a11y flag.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Procurement questionnaire vs this record.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
