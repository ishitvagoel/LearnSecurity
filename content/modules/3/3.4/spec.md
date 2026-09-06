# 3.4 — Business logic and abuse-resistant design

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 3.4
- **slug:** business-logic-and-abuse-resistant-design
- **title:** Business logic and abuse-resistant design
- **phase / track / difficulty:** 3 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–3.3 authored.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 3

## Objective hierarchy

1. Produce a **misuse-case set, workflow state machine, and abuse-control plan** for SecureCollab Phase 1 share grants (cap 5).
2. Name attacker capabilities (scripted loop; disabled UI max; parallel sixth) and trust assumptions (HTML is not the TCB).
3. Transfer: clinic max 3 guardians; optionally invite tokens (6.6) and export quotas (6.7).

## Prerequisite concepts

1.2 share grants; 2.4 retries vs this module’s *count* cap; 3.2 named threats; 6.7 rate limits later.

## Misconceptions

- Business logic is not security.
- Rate limits replace product caps.
- CWE-799 or API4/API6 is the requirement.
- HTML `max=5` is enforcement.

## Concept map

Authority (1.2) → time/retry (2.4) → this module’s product cap → 6.6/6.7 related quotas.

## Invariant prompts

- What must remain true if the client disables `max`?
- What fails if `/import` skips the cap?

## Threat-model prompts

- What can go wrong if eight POSTs hit `/share`?
- What residual remains if support may override?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/3.4/3.4-lab`. Forbidden: eight `add_share` calls yield count > 5. No live APIs.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-2.1.3`, `v5.0.0-2.2.2`, `v5.0.0-2.3.2`, `v5.0.0-2.3.4`; `v5.0.0-2.3.5` **Level 3, labeled advanced**.
- OWASP API Security Top 10:2023 API4/API6 **awareness** only.
- WCAG 2.2 (final) 4.1.3 for the denial message.

## Review triggers

New share/import/GraphQL path; support override; cap change; superseding ASVS V2.

## Time budget and SecureCollab

Evidence: misuse cases, state machine, abuse-control plan. Blueprint §9.1.

## Operational considerations

`share_cap_denied`; trim extras; WCAG announcement is not the cap. Teams >5 need an owned exception (E6).

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: write-path cap vs UI max; API4/API6 labeled awareness |
