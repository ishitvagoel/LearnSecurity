# E2 — Advanced browser and edge security (6 Operate)

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** CSP3 WD (**draft**); Trusted Types WD (**draft**). 2.3 browser cells still apply.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. CSP3 remains a Working Draft — label it draft.

## Attacker capabilities and trust assumptions

Injected active content in the model. Trust: local header dict. No live XSS campaign.

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

Run `labs/E2/e2-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
