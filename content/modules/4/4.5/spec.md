# 4.5 — OAuth, OpenID Connect, browser apps, and native apps

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 4.5
- **slug:** oauth-openid-connect-browser-apps-and-native-apps
- **title:** OAuth, OpenID Connect, browser apps, and native apps
- **phase / track / difficulty:** 4 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–4.4 authored. 4.3 refused JWT-as-architecture; this module adds audience.
- **routeTags:** complete, web-api
- **releaseMilestone:** M1
- **masteryGate:** 4

## Objective hierarchy

1. Produce **protocol sequence diagrams and redirect/audience tests** for SecureCollab Phase 1 (code+PKCE named; lab executes `aud`).
2. Name attacker capabilities (wrong-audience bearer; confused deputy; custom-scheme intercept) and trust assumptions (signature without `aud` is not enough).
3. Transfer: clinic wrong-aud FHIR token; RFC 8252 native redirect vs BFF/SPA.

## Prerequisite concepts

4.3 token channel; 4.4 object grants after a valid audience; 4.1 leftover tokens; 8.3 native redirects later.

## Misconceptions

- OIDC login replaces your matrix.
- JWT means OAuth is done.
- Mobile custom scheme is a safe redirect.

## Concept map

Session channel (4.3) → this module’s audience and client shape → 4.4 on the note → 8.3 native redirects.

## Invariant prompts

- What must remain true if a token minted for another API is presented?
- What fails if only the signature is checked?

## Threat-model prompts

- What can go wrong with SPA token storage vs BFF (`v5.0.0-10.1.1`)?
- What residual remains without PKCE, mix-up defenses, or sender-constraining?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/4.5/4.5-lab`. Forbidden: JWT with wrong or missing audience accepted as a SecureCollab session. No live IdPs. OAuth 2.1 labeled draft.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- IETF RFC 9700 / BCP 240 (final) OAuth 2.0 security.
- IETF RFC 10017 / BCP 212 (final, August 2026) browser-based apps.
- IETF RFC 8252 (final) native apps.
- OWASP ASVS 5.0.0 (final): `v5.0.0-10.3.1`, `v5.0.0-10.1.1`, `v5.0.0-10.2.1`, `v5.0.0-10.5.4`; `v5.0.0-10.3.5` **Level 3, labeled advanced**.
- OAuth 2.1 **Internet-Draft**.

## Review triggers

New client type, redirect URI, token format, or superseding RFC/ASVS.

## Time budget and SecureCollab

Evidence: sequence diagrams and malicious-client/redirect tests. Lab freeze is audience. Feeds M1 / Gate 4.

## Operational considerations

`jwt_aud_mismatch`; revoke client; never log raw tokens.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: audience-is-a-name mental models; RFC 9700 / 10017 / 8252; ASVS v5.0.0-10.3.1; 10.3.5 labeled Level 3 advanced; OAuth 2.1 draft |
