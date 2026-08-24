# 9.4 — Automated analysis and tool orchestration (2 Model)

**Kind:** design-exercise
**Loop step:** 2 Model
**Standards:** ASVS + tool results as inputs; not compliance theater.

## Property (start here)

A HIGH scanner finding without a mapped SecureCollab requirement cannot pass the lab gate. Tools do not prove invariants.

## Attacker capabilities and trust assumptions

Team that clicks dismiss. Trust: local findings list.

## This step

Name principals, objects, and channels. Open design: the client, APK, or prompt is hostile. Secrecy of the check is not the property.

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

Run `labs/9.4/9.4-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
