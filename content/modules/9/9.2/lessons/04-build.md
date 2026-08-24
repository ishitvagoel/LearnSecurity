# 9.2 — Secure code review (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
eval(user) => review_ok False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def review_ok(diff):
    return 'eval(' not in diff
```

## Why this restores the cell

Reject eval-on-user; look at data flow, authz, state, config.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

GitHub “rulesets” do not read eval.

Review misses generated code (E1).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Terraform, GitHub Actions yaml.

## Residual risk

Unknown unknowns — 9.3 tests.
