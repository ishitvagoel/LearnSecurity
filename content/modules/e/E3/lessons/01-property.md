# E3 — Payments and other high-assurance systems (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
**Mechanism (not the property):** Stripe idempotency is not your local ledger unless you use it.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For E3 |
|---|---|
| Root cause | Non-idempotent side effect (2.4). |
| Preconditions | two capture(k1) => count 2. |
| Impact (1.1 cell) | Integrity of money-like state. — Double charge (simulated). |
| Prevention | Idempotency key as primary key of capture. |
| Detection | charge_count vs unique keys. |
| Recovery | Credit the extra (runbook); still fail the test first. |

## Framework defaults vs application guarantees

Stripe idempotency is not your local ledger unless you use it.

## Mechanism limits and bypasses

PCI SAQ is not this cell.

New key each retry (client).

## Residual risk

Webhook vs capture race (7.3+2.4).

## Practice

Map 2.4, 7.3, 5.1 (no PAN stored).

Run `labs/E3/e3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Health record append-only audit.

Simulated copay.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Payment confirmations must be accessible; trapped users retry (this bug).
