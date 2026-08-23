# 8.3 — Network, deep links, WebViews, and inter-app communication (Review)

**Kind:** code-review
**Loop step:** Review
**Standards:** MASVS 2.1 platform interaction; 2.3/6.3 web origins are a different channel.

## Property (start here)

A deep link query as= must not switch the signed-in principal. Exported activities are an attack surface; the session is the identity.

## Attacker capabilities and trust assumptions

Another app sending securecollab://notes?as=admin. Trust: local session dict. No real IPC.

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

Run `labs/8.3/8.3-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
