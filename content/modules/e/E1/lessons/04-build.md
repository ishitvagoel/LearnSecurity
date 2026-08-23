# E1 — AI, LLM, and agentic application security (4 Build)

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** Elective E1; treat vendor AI-security features as mechanisms. Draft eval methods stay draft if cited.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. OWASP LLM lists are awareness, not this syllabus.

## Attacker capabilities and trust assumptions

Prompt that asks the model to call exec_sql. Trust: local tool router. No live model vendor.

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

If the primary control is bypassed, detection and recovery still apply; do not claim checkbox completeness.

## Practice

Run `labs/E1/e1-lab` (`--impl vulnerable` then `fixed`). Map the failing test to this property.

## Transfer

Change one channel (worker, mobile, CSV, CI). Do not define security as a Top 10 item.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence.
