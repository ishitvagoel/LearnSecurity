# E2 — Advanced browser and edge security

Pass A specification. Lesson prose lives in `lessons/`. Content-Security-Policy-Report-Only is not enforcement. Do not mark Gate 7 complete.

## Identity

- **id:** E2
- **slug:** advanced-browser-and-edge-security
- **title:** Advanced browser and edge security
- **phase / track / difficulty:** 7 / elective / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Opens after Phase 7; 2.3 cookies; 6.2 encoding; 2.2 edge.
- **routeTags:** complete, elective
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce an **enforcement predicate** so Report-Only does not make `isolation_enforced` true.
2. Name attacker capabilities (XSS that Report-Only would only log) and trust assumptions (local header dict).
3. Transfer: clinic Report-Only as “HIPAA header”; Trusted Types / COOP — without treating CSP3 as encoding.

## Prerequisite concepts

6.2 encoding first; 2.3 HttpOnly is a different cell; 2.2 cache may strip headers.

## Misconceptions

- Report-Only is isolation.
- Helmet defaults are the application guarantee.
- CSP replaces encoding or CSRF.

## Concept map

Report-Only counted as on (break) → require enforcing header (this module) → encoding (6.2) → Trusted Types draft layer. Residual: XS-Leaks; edge cache stripping.

## Invariant prompts

- What must remain true for a Report-Only header?
- What fails if the dashboard is green but the browser never blocked a script?

## Threat-model prompts

- What can XSS do when CSP is Report-Only?
- What residual remains if CSP is enforcing but encoding is skipped?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/E2/e2-lab`. Forbidden: Report-Only treated as isolation. No live XSS.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-3.4.3` CSP as a **layer** (Level 2); `v5.0.0-3.4.7` CSP reporting is **Level 3, labeled advanced** — reporting is not enforcement.
- W3C CSP3: **Working Draft** (pin `w3c-csp3`). Trusted Types: **Working Draft**.
- RFC 10017 OAuth browser: related architecture, not this header cell.

## Review triggers

Report-Only counted as on; JSONP leftover; Trusted Types not deployed; edge cache stripping CSP.

## Time budget and SecureCollab

Elective depth on 2.3/6.2. Not a core gate.

## Operational considerations

`csp_report_only_not_enforced`. Flip to enforcing after 6.2.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: Report-Only is not enforcement; CSP3 labeled draft |
