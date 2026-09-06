# 6.3 — Cross-site and cross-context attacks

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.3
- **slug:** cross-site-and-cross-context-attacks
- **title:** Cross-site and cross-context attacks
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 2.3 cookie jar; 4.3 session channel; 4.4 grants.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce a **cross-origin policy matrix** plus share-POST tests for SecureCollab.
2. Name attacker capabilities (foreign origin with the victim’s cookie) and trust assumptions (origin × token).
3. Transfer: clinic “share with partner” POST; postMessage/clickjacking/CORS as named residuals.

## Prerequisite concepts

2.3 ambient cookies; 4.4 share is a grant; SameSite is a helper not complete; Bearer is a different deputy.

## Misconceptions

- SameSite is CSRF done.
- JSON APIs cannot CSRF.
- CORS is CSRF defense.

## Concept map

Cookie session (2.3) → this module’s site-bound intent → CORS/postMessage/clickjacking named residuals → 6.5 open redirect.

## Invariant prompts

- What must remain true if a foreign origin POSTs share with the victim cookie and no token?
- What fails if GET still mutates share?

## Threat-model prompts

- What can go wrong when cookies travel without site-bound intent?
- What residual remains if origin and token are checked but a subframe or postMessage path is not?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.3/6.3-lab`. Forbidden: cookie-only share POST from a foreign origin. No live third-party sites.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-3.5.1`, `v5.0.0-3.5.3`, `v5.0.0-3.3.2`; `v5.0.0-3.5.8` **Level 3, labeled advanced**.
- SameSite and Fetch Metadata as *helpers*, not the property.

## Review triggers

New share method, cookie SameSite change, CORS credentialed route, or postMessage listener.

## Time budget and SecureCollab

Evidence: origin × token matrix, deny tests, named residuals. Feeds Gate 6.

## Operational considerations

`foreign_origin_post_denied`. Revoke surprise shares. Lookalike UI is 4.2.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: cookie-without-intent mental models; ASVS v5.0.0-3.5.1; L3 3.5.8 labeled advanced |
