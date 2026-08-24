# 6.5 — Server-side requests and protocol parsing (7 Generalize)

**Kind:** transfer-challenge
**Loop step:** 7 Generalize
**Standards:** ASVS 5.0.0 V10 SSRF (chapter-level).

## Property (start here)

Server-side fetch allowlists lab.securecollab.test only. Link-local metadata IPs are out of scope.

## Attacker capabilities and trust assumptions

Member who pastes a URL for a preview. Trust: URL parser, no real HTTP.

## This step

Keep the property; change one channel (worker, WebView, CSV, CI). Do not answer with a Top 10 name. Label drafts draft.

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

Run `labs/6.5/6.5-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
