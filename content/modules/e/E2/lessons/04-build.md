# E2 — Advanced browser and edge security (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
Report-Only => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def isolation_enforced(headers):
    return 'Content-Security-Policy' in headers
```

## Why this restores the cell

Detect enforcing header; don’t claim isolation otherwise.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Helmet defaults may be report-only in some templates.

CSP does not replace encoding (6.2) or CSRF (6.3).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Trusted Types, COOP/COEP.

## Residual risk

XS-Leaks — named as elective depth.
