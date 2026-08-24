# 9.5 — Authorized assessment, reporting, and remediation (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
retest None => cannot close.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def close_finding(f):
    return f.get('retest') == 'pass'
```

## Why this restores the cell

Require retest of the same cell.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Jira Done is not retest.

CVSS 9.8 vs business priority — you still judge.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

KEV vs internal-only.

## Residual risk

Unknown variants — hunt (same root cause).
