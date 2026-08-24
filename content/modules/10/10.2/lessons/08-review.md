# 10.2 — Source control, CI/CD, dependencies, and software supply chain (Review)

**Kind:** code-review
**Loop step:** Review
**Standards:** SSDF; lockfiles are mechanisms.

## Property (start here)

Install must fail when the lockfile hash does not match the fetched artifact. CI green is not integrity of dependencies.

## Attacker capabilities and trust assumptions

Substituted package. Trust: local hash compare. No real npm/pypi fetch.

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

If the primary control is bypassed, detection and recovery still apply; do not claim checkbox completeness.

## Practice

Run `labs/10.2/10.2-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
