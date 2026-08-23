# 10.5 — Logging, detection, incident response, recovery, and maintenance (Review)

**Kind:** code-review
**Loop step:** Review
**Standards:** NIST CSF 2.0 Recover (final) as outcome label; not a playbook menu.

## Property (start here)

An incident cannot close until recovery is marked done and logs do not contain note bodies.

## Attacker capabilities and trust assumptions

On-call theater. Trust: local incident dict.

## This step

Review the diff as a SecureCollab PR. Reject client trust, interpreter concatenation, Report-Only as enforcement, and closing findings without retest. Keys stay out of lessons.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong mechanism relative to the property, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, authorization, accountability, privacy, availability, or safety).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

The lab mechanism is a teaching stand-in. FastAPI, Next.js, Android APIs, and scanners are not this invariant.

## Residual risk

Incident comms and account recovery after compromise must be usable (WCAG 2.2).

## Practice

Run `labs/10.5/10.5-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
