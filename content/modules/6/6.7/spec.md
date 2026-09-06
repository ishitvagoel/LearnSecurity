# 6.7 — Resource abuse, automation, and availability

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.7
- **slug:** resource-abuse-automation-and-availability
- **title:** Resource abuse, automation, and availability
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 3.4 product cap; 5.1 extra copies.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce a **per-subject export quota** plus deny tests.
2. Name attacker capabilities (scripted member) and trust assumptions (local `allow(n)`).
3. Transfer: clinic bulk-export; notification fan-out; search complexity (7.1).

## Prerequisite concepts

3.4 write-path cap vs UI max; 5.1 extra copies; nginx IP limit is shared-fate.

## Misconceptions

- Availability is ops, not appsec.
- CAPTCHA replaces quotas.
- Autoscaling is the control.

## Concept map

Product cap (3.4) → resource account (this module) → GraphQL complexity (7.1) → cost alerts.

## Invariant prompts

- What must remain true on the fourth export in the window?
- What fails if the limit lives only in the SPA?

## Threat-model prompts

- What can go wrong when exports have no resource account?
- What residual remains if per-IP limits punish NAT while a stolen session still exports?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.7/6.7-lab`. Forbidden: fourth export allowed. No live load tests against public hosts.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-2.4.1`, `v5.0.0-2.1.3`, `v5.0.0-2.3.2`; `v5.0.0-2.4.2` **Level 3, labeled advanced**.
- OWASP API Security Top 10:2023 API4/API6 as **awareness after** the cause (also 3.4).

## Review triggers

New export, notify fan-out, or search; frontend-only limiter.

## Time budget and SecureCollab

Evidence: quota tests, per-subject vs per-IP note, cost signal. Feeds Gate 6.

## Operational considerations

`quota_denied`; `cost_alert`. Legitimate burst is an owned exception. Readable quota errors (WCAG).

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: resource-account mental models; ASVS v5.0.0-2.4.1; L3 2.4.2 labeled advanced |
