# 6.7 — Resource abuse, automation, and availability (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
allow(4) False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def allow(n_calls):
    return n_calls <= 3
```

## Why this restores the cell

Quota + authz + maybe queue.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

nginx rate limit without identity is shared-fate.

Per-IP limits punish NAT; need per-subject.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Notification fan-out; search complexity.

## Residual risk

Legitimate burst — owned exception.
