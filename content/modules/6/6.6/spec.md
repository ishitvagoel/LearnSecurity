# 6.6 — Workflow, race, and exceptional-condition failures

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.6
- **slug:** workflow-race-and-exceptional-condition-failures
- **title:** Workflow, race, and exceptional-condition failures
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 2.4 idempotency; 4.3 token-in-URL.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce a **single-use invite** state machine plus consume tests.
2. Name attacker capabilities (two tabs; copied token) and trust assumptions (local `accept()` consume).
3. Transfer: clinic invite-guardian; password reset; 7.4 jobs.

## Prerequisite concepts

2.4 retry vs second grant; 4.3 query-string tokens; 4.2 phishable email.

## Misconceptions

- HTTP 400 is fail-safe.
- Email links authenticate the recipient.
- Races are only performance.

## Concept map

Idempotent share (2.4) → consume-once invite (this module) → fail-open errors (V16) → workers (7.4).

## Invariant prompts

- What must remain true if `accept` runs twice?
- What fails if the used flag is checked then set without a lock?

## Threat-model prompts

- What can go wrong when check-then-set is not atomic?
- What residual remains if consume is correct but email is still a postcard (4.3 / 4.2)?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.6/6.6-lab`. Forbidden: invite token accepted twice. Local set, not a live race harness.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-2.3.4`, `v5.0.0-2.3.3`, `v5.0.0-16.5.3`; `v5.0.0-16.5.4` **Level 3, labeled advanced**.
- OWASP Top 10:2025 A10 as **awareness after** the cause.

## Review triggers

New invite, reset, or retry path; fail-open on store errors.

## Time budget and SecureCollab

Evidence: consume-once tests, fail-closed note, named TOCTOU residual. Feeds Gate 6.

## Operational considerations

`invite_replay_denied`. Email is phishable (4.2). Do not log tokens (4.3).

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: consume-once mental models; ASVS v5.0.0-2.3.4; L3 16.5.4 labeled advanced |
