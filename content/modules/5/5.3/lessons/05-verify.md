# 5.3 — Key and secret lifecycle (5 Verify)

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** ASVS 5.0.0 V13 secrets (chapter-level).

## Property (start here)

A disposable lab API key must not be a hardcoded default that always authenticates. Rotation means the old value fails.

## Attacker capabilities and trust assumptions

Repo clone containing the default. Trust: local string compare.

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

Run `labs/5.3/5.3-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
