# 5.4 — Secure communication and channel binding

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 5.4
- **slug:** secure-communication-and-channel-binding
- **title:** Secure communication and channel binding
- **phase / track / difficulty:** 5 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 2.2 hop model; 5.3 secrets. MASVS-NETWORK waits for 8.x.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 5

## Objective hierarchy

1. Produce a **trust-chain / hop diagram and TLS tests** (socket scheme, not client Forwarded-Proto).
2. Name attacker capabilities (cleartext client forging the header) and trust assumptions (bound proxy vs header name).
3. Transfer: clinic SPA https URL vs http API socket; mTLS vs this header.

## Prerequisite concepts

2.2 hops; 4.3 cookie flags; 5.2 at-rest is a different cell.

## Misconceptions

- HTTPS URL in the client proves TLS.
- Forwarded headers are for security.
- Pinning is always required.

## Concept map

Hop model (2.2) → this module’s socket scheme → 8.x pinning trade-off.

## Invariant prompts

- What must remain true if the client sends `X-Forwarded-Proto: https` on `http`?
- What fails if `--proxy-headers` trusts `*`?

## Threat-model prompts

- What can go wrong for cookie Secure flags and HSTS?
- What residual remains at TLS termination?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/5.4/5.4-lab`. Forbidden: client Forwarded-Proto counted as TLS. No live load balancers.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- IETF RFC 9846 TLS 1.3 (final).
- OWASP ASVS 5.0.0 (final): `v5.0.0-12.2.1`, `v5.0.0-12.1.1`, `v5.0.0-12.3.2`; `v5.0.0-12.1.4` and `v5.0.0-12.1.5` **Level 3, labeled advanced**.

## Review triggers

New proxy hop, mTLS, or pinning policy; superseding TLS RFC.

## Time budget and SecureCollab

Evidence: hop diagram, TLS tests, certificate-failure drill (named). Feeds Gate 5.

## Operational considerations

`header_https_socket_http`; revoke cleartext cookies; never log cookies.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: hop-vs-claim mental models; RFC 9846; ASVS v5.0.0-12.2.1; L3 OCSP/ECH labeled advanced |
