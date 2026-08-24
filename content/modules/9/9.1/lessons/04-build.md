# 9.1 — Verification requirements and traceability (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
status-only row is not coverage.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def covered(req_id, tests):
    return any(t.get('req') == req_id and t.get('asserts_isolation') for t in tests)
```

## Why this restores the cell

Coverage predicate requires the isolation assert.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

ASVS PDF is not your matrix.

Level 2 tailored — say what you dropped (E6).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

MASVS STORAGE for 8.2.

## Residual risk

Unmapped Level 3 risks.
