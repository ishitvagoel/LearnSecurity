# 9.4 — Automated analysis and tool orchestration (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
unmapped HIGH => ship_ok False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def ship_ok(findings, mappings):
    return all(f['id'] in mappings for f in findings if f.get('sev') == 'HIGH')
```

## Why this restores the cell

Block unmapped HIGH; allow mapped+accepted with E6.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

GitHub code scanning default is not your policy.

False positives exist — mapping is how you record that.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

SCA CVE vs actually called function.

## Residual risk

Blind spots (authz logic) — 9.2/9.3.
