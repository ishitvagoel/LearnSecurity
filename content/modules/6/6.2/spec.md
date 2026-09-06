# 6.2 — Browser injection and active content

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.2
- **slug:** browser-injection-and-active-content
- **title:** Browser injection and active content
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 2.1 parsers; 2.3 cookie jar; 6.1 interpreter shape.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce a **context-encoding map** plus HTML-text tests for SecureCollab note titles.
2. Name attacker capabilities (collaborator-edited title) and trust assumptions (HTML text context in this lab).
3. Transfer: clinic nickname; markdown-to-HTML as a second parser (2.1).

## Prerequisite concepts

6.1 data vs grammar; 2.3 HttpOnly is not XSS defense; CSP3/Trusted Types are layered and **draft**.

## Misconceptions

- CSP replaces encoding.
- React JSX is a guarantee for `dangerouslySetInnerHTML`.
- Markdown is inert HTML.

## Concept map

Interpreter shape (6.1) → HTML text context (this module) → CSP/Trusted Types as extra (draft) → E2 for report-only vs enforce.

## Invariant prompts

- What must remain true if a title contains `<`?
- What fails if you encode HTML text but concatenate into a JavaScript string?

## Threat-model prompts

- What can go wrong when HTML grammar mixes with data?
- What residual remains if encoding is correct for text but wrong for attributes or URLs?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.2/6.2-lab`. Forbidden: unencoded markup in HTML text. Teaching encode; not an exploit kit. Tame marker: `<` must become `&lt;`.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-1.2.1`, `v5.0.0-3.4.3`; `v5.0.0-3.4.7` **Level 3, labeled advanced**.
- W3C CSP3 and Trusted Types: **draft**.
- CWE-79 as awareness after the cause.

## Review triggers

New HTML template, markdown pipeline, or CSP mode change; CSP3 becoming a Recommendation.

## Time budget and SecureCollab

Evidence: context map, encode test, named CSP draft residual. Feeds Gate 6.

## Operational considerations

`stored_field_review`; CSP reports are not enforcement. Do not log title bodies if they are PHI.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: HTML-grammar and context mental models; ASVS v5.0.0-1.2.1; CSP3 draft; L3 3.4.7 labeled advanced |
