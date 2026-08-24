# 8.4 — Build, distribution, attestation, and resilience (3 Break)

**Kind:** mechanism-lab
**Loop step:** 3 Break
**Standards:** MASVS 2.1 resilience; attestation vendor docs are mechanisms.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present.

## Attacker capabilities and trust assumptions

Sideloaded debug APK. Trust: server sees build_type. Local only.

## This step

The authorized break is the local vulnerable/ fixture. No live targets, no weaponized copy-paste exploits, no public CDN to attack.

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

Run `labs/8.4/8.4-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
