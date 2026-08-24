# E3 — Payments and other high-assurance systems (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
Review `labs/E3/e3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/E3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): double capture increments twice
- Seeded smell (label it yourself): PAN in logs
- Seeded smell (label it yourself): PCI checkbox as the test
- Seeded smell (label it yourself): No idempotency key

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- PCI means the app is safe
- We don’t store cards so no money bugs
- Webhooks are eventually consistent so double charge is OK

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Health record append-only audit.

## HITL / WCAG 2.2

Payment confirmations must be accessible; trapped users retry (this bug).
