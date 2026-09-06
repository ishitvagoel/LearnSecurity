# 7.2 — Object, property, and function security

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 7.2
- **slug:** object-property-and-function-security
- **title:** Object, property, and function security
- **phase / track / difficulty:** 7 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 4.4 object×tenant; 7.1 extra-key *writes*.
- **routeTags:** complete, web-api
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **role × field matrix** plus deny tests so a member cannot resolve `secret_internal`.
2. Name attacker capabilities (member using GraphQL fields or REST `?fields=`) and trust assumptions (local `resolve(role, field)`).
3. Transfer: clinic member cannot resolve SSN; bulk update; search snippets — without treating UUID obscurity as a grant.

## Prerequisite concepts

4.4 grant is object-and-tenant keyed; 7.1 extra keys on *write*; 1.2 cells; identifiers locate.

## Misconceptions

- Object-level authz implies field-level.
- Private JSON keys are hidden.
- GraphQL resolvers inherit REST policy magically.
- A UUID is a capability.

## Concept map

Object×tenant (4.4) → field read grain (this module) → extra-key writes (7.1) → worker dumps (7.4).

## Invariant prompts

- What must remain true if GET `/notes/{id}` succeeds for a member?
- What fails if the UI hides `secret_internal` but the serializer still dumps it?

## Threat-model prompts

- What can go wrong when `to_dict()` dumps the ORM object?
- What residual remains after a role change if serializers are cached (`v5.0.0-8.3.2`)?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/7.2/7.2-lab`. Forbidden: member resolves `secret_internal`. No live GraphQL attacks.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.3` (field-level / BOPLA, Level 2); `v5.0.0-8.2.1` (function-level); `v5.0.0-8.2.2` (object-level / BOLA — already 4.4, restated so grains stay distinct); `v5.0.0-8.3.2` immediate application of authorization changes is **Level 3, labeled advanced**.
- OWASP API Security Top 10:2023 API1/API3/API5 as **awareness after** the cause (also 4.4).

## Review triggers

New serializer, GraphQL field, CSV, search snippet; role change.

## Time budget and SecureCollab

Evidence: role×field matrix, mutation tests. Feeds Gate 7 / M2 (milestone stays not-attempted).

## Operational considerations

`field_denied` without the secret value. Service/admin reads are audited.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: role×field mental models; ASVS v5.0.0-8.2.3; L3 8.3.2 labeled advanced |
