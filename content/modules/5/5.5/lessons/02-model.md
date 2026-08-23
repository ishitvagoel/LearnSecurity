# 5.5 — Database and persistence security (2 Model)

**Kind:** design-exercise
**Loop step:** 2 Model
**Standards:** ASVS 5.0.0 V13/V5 (chapter-level). Teach bind variables, not payload catalogs.

## Property (start here)

Note fetch is parameterized: user input is not concatenated into a query string. Local model only — no live DB attacks.

## Attacker capabilities and trust assumptions

Caller who supplies note_id. Trust: in-process list.

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

Run `labs/5.5/5.5-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
