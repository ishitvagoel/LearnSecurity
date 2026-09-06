# 0.2 — Diagnostic and adaptive bridge

Pass A specification. Lesson prose lives in `lessons/`. A placement quiz of 100 does not skip 1.2 or Gate 1. NICE language may skip tooling gaps, never invariants. Do not mark Gate 0 complete from a quiz.

## Identity

- **id:** 0.2
- **slug:** diagnostic-and-adaptive-bridge
- **title:** Diagnostic and adaptive bridge
- **phase / track / difficulty:** 0 / bridge / foundation
- **estimatedMinutes:** 240
- **prerequisites:** 0.1 orientation; diagnostics never skip 1.2 or Gate 1.
- **routeTags:** complete, web-api, bridge
- **releaseMilestone:** none
- **masteryGate:** 0

## Objective hierarchy

1. Produce a **skip predicate** so `quiz_score_grants_phase1_skip(100)` is false.
2. Name attacker capabilities (hurried learner; hiring manager with a badge) and trust assumptions (local diagnostic repo is honest; quiz items are not production secrets).
3. Transfer: clinic onboarding quiz; vendor cert used to skip a threat-model review.

## Prerequisite concepts

0.1 scope. This module places learners into **tooling** bridges (Git/SQL/HTTP) without minting 1.2 cells.

## Misconceptions

- Placement is a security clearance.
- Fast learners skip invariants.
- Tool fluency is threat modeling.
- LMS percentage is ASVS.

## Concept map

Score-as-capability (break) → skip only tooling units (this module) → 1.2/1.3/1.4 still required. Residual: memorizing answers without running the lab.

## Invariant prompts

- What must remain true for a 100% quiz?
- What fails if Gate 1 is back-dated?

## Threat-model prompts

- What can a 100% quiz fail to prove about tenant isolation?
- What Git/SQL/HTTP gaps still need a bridge?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/0.2/0.2-bridge`. Forbidden: quiz score used as authorization to skip 1.2 / Gate 1.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST SP 800-181r1 NICE Framework (final): Secure Systems Development competencies as **informative** role language. Components v2.2.0 (2026-04-28) are living data, not Gate 1.
- NIST CSF 2.0 GV: outcome labels, not a skip.
- WCAG 2.2 1.4.1: diagnostic UI must not be color-only “green = skip Phase 1.”

## Review triggers

Score grants Phase 1 skip; badge as Gate 1; 1.4 hidden by adaptive path.

## Time budget and SecureCollab

Bridge. Python skip predicate stand-in only.

## Operational considerations

`phase1_skip_denied`. Audit skipped-module lists. Do not back-date Gate 1.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: quiz score is not a 1.2 cell |
