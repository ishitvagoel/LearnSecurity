# E3 — Payments, financial, health, and other high-assurance systems (1 Property)

**Kind:** concept-model
**Loop step:** 1 Property
**Standards:** Idempotency as integrity of money movement; do not invent a payment standard pin.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater.

## Attacker capabilities and trust assumptions

Retried capture. Trust: local set. No real card data.

## This step

Start from this system's testable sentence, not a topic title. A mechanism (TLS, MASVS control, scanner, CSP) is not the invariant.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong mechanism relative to the property, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, authorization, accountability, privacy, availability, or safety).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

The lab mechanism is a teaching stand-in. FastAPI, Next.js, Android APIs, and scanners are not this invariant.

## Residual risk

If the primary control is bypassed, detection and recovery still apply; do not claim checkbox completeness.

## Practice

Run `labs/E3/e3-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
