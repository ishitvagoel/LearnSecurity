# E6 — Product security leadership (Review)

**Kind:** code-review
**Loop step:** Review
**Standards:** Risk ownership; WCAG 2.2 on any human control named in the exception.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. Leadership is accountable residual, not a slide.

## Attacker capabilities and trust assumptions

Executive who wants the date. Trust: local exception dict.

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

Exceptions that rely on a human process must remain operable and understandable (WCAG 2.2).

## Practice

Run `labs/E6/e6-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
