# E3 — Payments and other high-assurance systems (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
two capture(k1) => count 1.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
SEEN=set(); CHARGES=[]
def reset():
    SEEN.clear(); CHARGES.clear()
def capture(key):
    if key in SEEN:
        return False
    SEEN.add(key)
    CHARGES.append(key)
    return True
def charge_count():
    return len(CHARGES)
```

## Why this restores the cell

Idempotency key as primary key of capture.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Stripe idempotency is not your local ledger unless you use it.

PCI SAQ is not this cell.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Health record append-only audit.

## Residual risk

Webhook vs capture race (7.3+2.4).
