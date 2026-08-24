# E3 — Payments and other high-assurance systems (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Health record append-only audit.

**Product sketch:** Simulated copay.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Stripe idempotency is not your local ledger unless you use it.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/E3/e3-lab` stays the only running system you may break.
