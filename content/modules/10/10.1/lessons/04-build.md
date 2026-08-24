# 10.1 — Secure software lifecycle and security culture (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
{} => merge_ok False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def merge_ok(pr):
    return bool(pr.get('threat_model'))
```

## Why this restores the cell

Require tm id; triggers on identity, data, mobile…

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

CODEOWNERS is not a threat model.

A stale tm-id rubber stamp — 3.2 age.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Exception path (E6).

## Residual risk

Metrics vanity — count TMs with tests, not posters.
