# 9.2 — Secure code review

Pass A specification. Lesson prose lives in `lessons/`. No weaponized eval exploits in learner pages.

## Identity

- **id:** 9.2
- **slug:** secure-code-review
- **title:** Secure code review
- **phase / track / difficulty:** 9 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 6.1 interpreter confusion; 9.1 coverage predicate.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 9

## Objective hierarchy

1. Produce a **review predicate** so `eval` on user input is not approved.
2. Name attacker capabilities (plausible-looking diff; generated code) and trust assumptions (local `review_ok(diff)`).
3. Transfer: Terraform, GitHub Actions yaml, clinic eval in a report template — without treating LGTM as review.

## Prerequisite concepts

6.1 data vs interpreter grammar; ASVS `v5.0.0-1.3.2` (avoid eval); OWASP Code Review Guide v2 (2017) as **guidance**; NIST SSDF 1.1 PW.7 / RV.1; SSDF 1.2 IPD **draft**; 9.4 bots as aid not oracle.

## Misconceptions

- Tests mean review is optional.
- Formatters catch security.
- AI review replaces 9.2.
- LGTM after reading the README is complete mediation.
- A substring denylist is a complete review oracle.

## Concept map

Coverage (9.1) → human review of interpreters/authority/state (this module) → tests (9.3) → bots (9.4) → generated-code residual (E1).

## Invariant prompts

- What must remain true for `review_ok("x = eval(user)")`?
- What fails if the reviewer only confirmed the UI still looks right?

## Threat-model prompts

- What can go wrong when visual plausibility is the review?
- What residual remains if the lab denylist misses `exec(`?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/9.2/9.2-lab`. Forbidden: eval on user input approved in review. The substring check is a **lab stand-in**, not a complete oracle.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-1.3.2` avoid eval / dynamic code execution. `v5.0.0-15.1.5` documenting dangerous functionality is **Level 3, labeled advanced**.
- OWASP Code Review Guide v2 (2017): **seminal guidance** for how to look (data flow, authority, interpreters), not a control catalogue.
- NIST SSDF 1.1 (final) PW.7 (review/analyze human-readable code), RV.1. SSDF 1.2 IPD is **draft**.

## Review triggers

LGTM on eval(user); README-only review; ignoring framework-generated SQL; no authority question.

## Time budget and SecureCollab

Evidence: structured review of the seeded diff. Feeds Gate 9 (not-attempted).

## Operational considerations

`review_block_eval`. Residual: unknown unknowns — 9.3 tests; substring stand-in.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: visual-plausibility vs data-flow; eval stand-in labeled; SSDF PW.7 |
