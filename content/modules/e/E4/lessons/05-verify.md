# E4 — Memory safety and native-code boundaries (5 Verify)

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** Memory-safety as an integrity/availability property at the FFI boundary.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. This models a length mismatch — it is not a weaponized native exploit.

## Attacker capabilities and trust assumptions

Caller supplying a long src. Trust: local bytes. No live memory corruption.

## This step

pytest --impl vulnerable must fail; --impl fixed must pass. A test that only checks HTTP 200 is not a security test.

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

Run `labs/E4/e4-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
