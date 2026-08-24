# 7.3 — Webhooks, callbacks, and third-party APIs (6 Operate)

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** ASVS V10; 5.4 channel ≠ authenticity.

## Property (start here)

Webhook bodies without a valid lab HMAC are rejected. TLS to the peer is not authenticity of this callback.

## Attacker capabilities and trust assumptions

Caller who can POST /webhook. Trust: local compare.

## This step

Detect without logging note bodies or tokens. Recover fail-safe (revoke, rotate, quarantine). If a human must act, the path must be usable (WCAG 2.2).

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

Run `labs/7.3/7.3-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
