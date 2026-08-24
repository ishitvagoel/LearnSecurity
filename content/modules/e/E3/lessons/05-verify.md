# E3 — Payments and other high-assurance systems (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Duplicate capture double-charges the lab ledger |
| Failure | Fail closed: Idempotency key as primary key of capture |

Lab tests: `test_property.py` under `labs/E3/e3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Duplicate capture double-charges the lab ledger`
- `--impl fixed`: **pass**

duplicate capture does not double charge.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Health record append-only audit.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
