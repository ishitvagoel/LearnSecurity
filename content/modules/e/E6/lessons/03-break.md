# E6 — Product security leadership (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
**Forbidden outcome:** Risk exception accepted without owner and review date

**Authorized scope:** `labs/E6/e6-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable risk.py accepts empty exception.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: accept_exception({owner:'', review_by:None}) True.

## Vulnerable fixture (local)

```python
def accept_exception(exc):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Oral acceptance. |
| Impact | Unowned holes; inaccessible recovery (1.4) forever. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/E6/e6-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Procurement questionnaire vs this record.

## Non-goals

No live-target instructions. Synthetic data only.
