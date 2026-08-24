# 8.2 — Local data, keys, biometrics, offline state, and leakage surfaces (5 Verify)

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** MASVS 2.1 storage; ASVS V6 at rest is a different cell — name which store you mean.

## Property (start here)

An offline-cached note body must not sit as plaintext on the lab disk map. Encoding or a world-readable prefs file is not confidentiality.

## Attacker capabilities and trust assumptions

Backup/ADB-style reader of the local store. Trust: process that can read DISK. No real device.

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

Run `labs/8.2/8.2-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
