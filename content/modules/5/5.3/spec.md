# 5.3 — Key and secret lifecycle

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 5.3
- **slug:** key-and-secret-lifecycle
- **title:** Key and secret lifecycle
- **phase / track / difficulty:** 5 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.2 authored. Application secrets ≠ user passwords (4.2).
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 5

## Objective hierarchy

1. Produce a **secret inventory, rotation exercise, and compromise runbook** (hardcoded default dies after rotate).
2. Name attacker capabilities (repo clone; old image) and trust assumptions (Vault sticker is not rotation).
3. Transfer: clinic gist-leaked API key; envelope DEK vs KEK sketch.

## Prerequisite concepts

5.2 AEAD needs keys; 4.1 leftover artifacts; 7.4 worker defaults later.

## Misconceptions

- gitignore means it was never leaked.
- KMS equals rotated.
- Passwords and API keys are the same lifecycle.

## Concept map

AEAD (5.2) → this module’s current secret → 7.4 / 8.4 extra copies.

## Invariant prompts

- What must remain true of `sk-lab-hardcoded` after rotation?
- What fails if `current` is missing?

## Threat-model prompts

- What can go wrong with a default in source?
- What residual remains in images and logs?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/5.3/5.3-lab`. Forbidden: hardcoded default still authenticates after rotation. Disposable lab string only.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-13.3.1`, `v5.0.0-13.2.3`, `v5.0.0-11.1.1`; `v5.0.0-13.3.4` and `v5.0.0-13.3.3` **Level 3, labeled advanced**.

## Review triggers

New secret class, worker, or mobile embed; superseding ASVS.

## Time budget and SecureCollab

Evidence: inventory, rotation exercise, compromise runbook. Feeds Gate 5.

## Operational considerations

`default_secret_used`; never log the value.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: secret-outlives-rotation mental models; ASVS v5.0.0-13.2.3; L3 rotate/HSM labeled advanced |
