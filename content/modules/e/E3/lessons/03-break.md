# E3 — Payments and other high-assurance systems (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
**Forbidden outcome:** Duplicate capture double-charges the lab ledger

**Authorized scope:** `labs/E3/e3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable pay.py double-charges.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: two capture(k1) => count 2.

## Vulnerable fixture (local)

```python
CHARGES=[]
def reset():
    CHARGES.clear()
def capture(key):
    CHARGES.append(key)
    return True
def charge_count():
    return len(CHARGES)
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Non-idempotent side effect (2.4). |
| Impact | Double charge (simulated). |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/E3/e3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Health record append-only audit.

## Non-goals

No live-target instructions. Synthetic data only.
