# 9.2 — Secure code review (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
**Forbidden outcome:** eval on user input approved in review

**Authorized scope:** `labs/9.2/9.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable review.py approves eval.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: review_ok('x=eval(user)') True.

## Vulnerable fixture (local)

```python
def review_ok(diff):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Visual plausibility. |
| Impact | Interpreter confusion shipped (6.1). |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/9.2/9.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Terraform, GitHub Actions yaml.

## Non-goals

No live-target instructions. Synthetic data only.
