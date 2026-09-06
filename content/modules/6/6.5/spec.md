# 6.5 — Server-side requests and protocol parsing

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.5
- **slug:** server-side-requests-and-protocol-parsing
- **title:** Server-side requests and protocol parsing
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 2.1 URL parsers; 6.1 interpreter shape; 6.4 paths.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce an **egress allow-list** plus URL tests for SecureCollab unfurl.
2. Name attacker capabilities (user-supplied preview URL) and trust assumptions (local `allowed()`, no live metadata fetch).
3. Transfer: clinic “fetch PDF from URL”; webhooks (7.3).

## Prerequisite concepts

2.1 URL is a structure; 6.4 path object; 2.2 hop vs cache key.

## Misconceptions

- HTTPS URLs cannot SSRF.
- Private-IP denylists are complete.
- Open redirect is just UX.

## Concept map

URL as structure (2.1) → server fetch (this module) → open redirect / desync named residuals → webhooks (7.3).

## Invariant prompts

- What must remain true if the preview URL is link-local?
- What fails if you only check `https://` as a string prefix?

## Threat-model prompts

- What can go wrong when the server fetches attacker-chosen authority?
- What residual remains if the host allow-list is correct but redirects or DNS rebinding are not?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.5/6.5-lab`. Forbidden: allow link-local metadata. Tests call `allowed()` only. No live cloud metadata, no public fetches.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-1.3.6`, `v5.0.0-13.2.4`, `v5.0.0-3.7.2`; `v5.0.0-3.7.3` **Level 3, labeled advanced**.
- OWASP API Security Top 10:2023 API7 as **awareness after** the cause.

## Review triggers

New unfurl, webhook, or redirect; parser change; dedicated egress proxy.

## Time budget and SecureCollab

Evidence: allow-list, deny tests, named redirect/DNS residuals. Feeds Gate 6.

## Operational considerations

`egress_denied`. Never rotate a real instance role in this course. Dedicated egress proxy for customer URLs.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: URL-as-authority mental models; ASVS v5.0.0-1.3.6; L3 3.7.3 labeled advanced |
