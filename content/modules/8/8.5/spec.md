# 8.5 — Mobile verification and privacy

Pass A specification. Lesson prose lives in `lessons/`. No Crashlytics payload dumps or live-store attacks.

## Identity

- **id:** 8.5
- **slug:** mobile-verification-and-privacy
- **title:** Mobile verification and privacy
- **phase / track / difficulty:** 8 / mobile / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 8.1–8.4; 3.1 log bodies; 5.1 extra copies.
- **routeTags:** complete, mobile
- **releaseMilestone:** M3
- **masteryGate:** 8

## Objective hierarchy

1. Produce a **crash-report redaction** plus deny tests so a note body never appears in telemetry JSON.
2. Name attacker capabilities (crash-platform operator; logcat reader; tracker SDK) and trust assumptions (local `crash_report(body)`).
3. Transfer: clinic crash with a synthetic patient name; web Sentry (10.5) — without treating Play Data safety as redaction.

## Prerequisite concepts

3.1 protection-level logging (`v5.0.0-16.2.5`); 5.1 extra copies / processors; 8.1 hostile APK; MASVS-PRIVACY 2.1.0; MAS Testing Profiles live in MASTG, not MASVS L1/L2/R.

## Misconceptions

- Store privacy labels are controls.
- Debug logs stay on device.
- MASTG is a scanner.
- Play Data safety redacts crash bodies.
- MASVS “L1/L2/R” are current verification levels.

## Concept map

Telemetry is a 3.1 / 5.1 sink (this module) → MASVS-PRIVACY traceability (9.1) → web crash sinks (10.5) → vendor as processor (5.1).

## Invariant prompts

- What must remain true for `crash_report("secret")`?
- What fails if the Play Data safety form is the only control?

## Threat-model prompts

- What can go wrong when an exception message includes the note body?
- What residual remains if the vendor is an honest processor?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/8.5/8.5-lab`. Forbidden: crash JSON contains the note body. No live Crashlytics, Play Console, or public apps.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP MASVS 2.1.0 (final): `MASVS-PRIVACY-1` (minimize access); `MASVS-PRIVACY-2` (prevent identification); `MASVS-PRIVACY-3` (transparency — Play Data safety is disclosure, not redaction); `MASVS-PRIVACY-4` (user control). No MASVS L1/L2/R.
- OWASP MASTG 2.0.0 (final, June 2026): MASVS → MASWE → MASTG tests. A spreadsheet row without a test is 9.1.
- OWASP ASVS 5.0.0 (final): `v5.0.0-16.2.5` logging by protection level (spiral from 3.1); `v5.0.0-16.5.4` last-resort error handlers is **Level 3, labeled advanced**.
- OWASP Mobile Top 10:2024: awareness after the cause, not the syllabus.
- NIST Privacy Framework 1.0 (final) for privacy outcomes; Privacy Framework 1.1 remains **draft**.

## Review triggers

Crash SDK logs bodies; leftover READ_LOGS; tracker SDK without a processor review; MASVS row without a test.

## Time budget and SecureCollab

Evidence: mobile verification report + one redacted-crash test. Feeds Gate 8 / M3 (not-attempted).

## Operational considerations

`crash_body_redacted`. Purge vendor copies. Vendor remains a 5.1 processor.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: telemetry-is-a-sink mental models; MASVS-PRIVACY-1–4; ASVS v5.0.0-16.2.5 |
