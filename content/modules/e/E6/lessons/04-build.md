# E6 — Product security leadership (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
empty owner/date => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def accept_exception(exc):
    return bool(exc.get('owner') and exc.get('review_by') and exc.get('wcag_checked'))
```

## Why this restores the cell

Schema of an exception; refuse incomplete.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Jira “risk” issue type without dates.

A perfect register that nobody reads.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Procurement questionnaire vs this record.

## Residual risk

Some risk always remains — that’s the point of an honest register.
