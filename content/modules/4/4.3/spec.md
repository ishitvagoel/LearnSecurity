# 4.3 — Sessions, cookies, and tokens

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 4.3
- **slug:** sessions-cookies-and-tokens
- **title:** Sessions, cookies, and tokens
- **phase / track / difficulty:** 4 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–4.2 authored.
- **routeTags:** complete, web-api
- **releaseMilestone:** M1
- **masteryGate:** 4

## Objective hierarchy

1. Produce a **session protocol/state diagram and theft/replay tests** for SecureCollab Phase 1 (no query-string tokens).
2. Name attacker capabilities (Referer, access logs, screenshots) and trust assumptions (TLS does not hide query from logs).
3. Transfer: clinic appointment deep link; magic-link email (6.6).

## Prerequisite concepts

2.3 cookie jar vs script; 2.2 hop vs log; 3.1 query-string logs; 4.2 session mint.

## Misconceptions

- Query strings are fine over TLS.
- JWT means secure.
- HttpOnly is the same as “not in the URL.”

## Concept map

Authn (4.2) → this module’s channel → 4.4 authorization using the session → 4.5 OAuth tokens.

## Invariant prompts

- What must remain true if a URL is pasted into chat?
- What fails if uvicorn logs the query?

## Threat-model prompts

- What can go wrong with `?access_token=`?
- What residual remains for one-time magic links?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/4.3/4.3-lab`. Forbidden: session from query-string token. No live CDNs.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-14.2.1`, `v5.0.0-3.4.5`, `v5.0.0-3.3.4`.

## Review triggers

New OAuth flow; magic-link; log drain; superseding ASVS V14.

## Time budget and SecureCollab

Evidence: session protocol diagram, theft/replay tests. Feeds M1.

## Operational considerations

`query_token_rejected`; log-redact; revoke leaked tokens.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: URL-as-postcard models; ASVS 14.2.1 |
