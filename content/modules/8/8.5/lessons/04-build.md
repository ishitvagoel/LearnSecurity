# 8.5 — Mobile verification and privacy (4 Build)

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** MASVS 2.1 privacy; NIST Privacy Framework 1.0 (final).

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a policy PDF.

## Attacker capabilities and trust assumptions

Crash reporter / support inbox. Trust: local dict. No real PII.

## This step

Restore the invariant with the smallest structural control in fixed/. Framework defaults are not this guarantee. Name remaining bypasses.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong mechanism relative to the property, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, authorization, accountability, privacy, availability, or safety).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

The lab mechanism is a teaching stand-in. FastAPI, Next.js, Android APIs, and scanners are not this invariant.

## Residual risk

Crash-upload consent and support emails must be understandable (WCAG 2.2).

## Practice

Run `labs/8.5/8.5-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
