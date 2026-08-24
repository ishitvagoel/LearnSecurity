# 9.3 — Security-focused tests (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
status-only is not a security test.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def is_security_test(t):
    return bool(t.get('forbidden_outcome'))
```

## Why this restores the cell

Require forbidden-outcome asserts.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

pytest-cov 90% is not 1.2.

Property tests still need oracles.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Fuzzing without an oracle.

## Residual risk

Exploratory testing (9.5).
