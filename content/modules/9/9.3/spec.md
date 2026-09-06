# 9.3 — Security-focused tests

Pass A specification. Lesson prose lives in `lessons/`. This module owns test *shape*, not the ASVS catalogue of *what* to test.

## Identity

- **id:** 9.3
- **slug:** security-focused-tests
- **title:** Security-focused tests
- **phase / track / difficulty:** 9 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.2 / 4.4 isolation tests; 9.1 coverage predicate; 9.2 review.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 9

## Objective hierarchy

1. Produce a **security-test predicate** so HTTP 200-only is not counted as a security test.
2. Name attacker capabilities (happy-path suite; lint membership) and trust assumptions (local `is_security_test(t)`).
3. Transfer: clinic `test_get_patient_200`; fuzzing without an oracle — without treating pytest-cov as 1.2.

## Prerequisite concepts

9.1 coverage needs a real isolation assert; this module defines that assert’s *shape*. ASVS 5.0.0, WSTG 4.2, and MASTG 2.0.0 are catalogues of *what* to test. NIST SSDF 1.1 PW.8; SSDF 1.2 IPD **draft**. Residual exploratory testing is 9.5.

## Misconceptions

- Coverage percentage is security.
- Fuzzing finds all authz bugs.
- Snapshot tests are isolation tests.
- WSTG checklist membership is a passing security test.
- HTTP 200 is evidence of 1.2.

## Concept map

Coverage predicate (9.1) → review (9.2) → forbidden-outcome tests (this module) → tools (9.4) → exploratory (9.5).

## Invariant prompts

- What must remain true for `is_security_test({status_asserted: True})`?
- What fails if fuzzing has no oracle?

## Threat-model prompts

- What can go wrong when the suite only asserts 200?
- What residual remains after a well-shaped isolation test?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/9.3/9.3-lab`. Forbidden: HTTP 200-only test counted as a security test.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): catalogue of *what* (AUTHZ-1 maps to `v5.0.0-8.2.1` / `8.2.2`). This module owns *shape*. `v5.0.0-15.4.1` concurrency/TOCTOU tests are **Level 3, labeled advanced** — still need a forbidden outcome, not “the fuzzer ran.”
- OWASP WSTG 4.2 (final): catalogue of web tests. WSTG 5.0 is **in development / draft** if cited.
- OWASP MASTG 2.0.0 (final): mobile catalogue.
- NIST SSDF 1.1 PW.8 (final). SSDF 1.2 IPD is **draft**.

## Review triggers

assert status_code==200 only; empty security suite; chaos without authz; fuzzing without an oracle.

## Time budget and SecureCollab

Evidence: layered security test portfolio with at least one forbidden-outcome test. Feeds Gate 9 (not-attempted).

## Operational considerations

`security_suite_missing_isolation`. Exploratory testing remains 9.5.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: forbidden-outcome shape; WSTG 4.2 as catalogue; L3 15.4.1 labeled advanced |
