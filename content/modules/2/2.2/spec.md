# 2.2 — DNS, transport, HTTP, TLS, proxies, CDNs, and caches

Pass A specification only.

## Identity

- **id:** 2.2
- **slug:** dns-transport-http-tls-proxies-cdns-caches
- **title:** DNS, transport, HTTP, TLS, proxies, CDNs, and caches
- **phase / track / difficulty:** 2 / core / foundation
- **estimatedMinutes:** 300
- **prerequisites:** 2.1 Pass A (parsers); 1.3 boundaries
- **routeTags:** complete, accelerated, web-api
- **releaseMilestone:** M0
- **masteryGate:** 2

## Objective hierarchy

1. Trace a request **end to end** (browser → DNS → TLS → edge/CDN → app → DB) and mark where identity, scheme, host, headers, body, and **cache keys** can be transformed or trusted incorrectly.
2. State TLS 1.3 **deployment responsibilities** (certificate/hostname validation, versions, forwarding of client identity) without treating “HTTPS on” as the property.
3. Transfer: add a CDN or reverse proxy and list which 1.3 boundaries and cache-key assumptions change.

## Misconceptions

- TLS termination means the app can trust `X-Forwarded-*` and `Host`.
- CDN cache is a performance-only concern.
- RFC 9846 is a checkbox (“TLS 1.3 enabled”).

## Concept map

DNS/name → TCP/TLS (RFC 9846) → HTTP hops → cache key → origin app. Each hop may rewrite trust.

## Invariant prompts

- Who authenticated the name, and to which hop?
- What is the cache key, and can an attacker poison it?
- After TLS is terminated, what identity is still bound to the request?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 2.2-LO-01 | concept-model | Hops, Host, forwarded identity, cache keys | 1 Property |
| 2.2-LO-02 | design-exercise | Request-path diagram for local SecureCollab + edge | 2 Model |
| 2.2-LO-03 | mechanism-lab | Local proxy that rewrites Host or cache key | 3 Break |
| 2.2-LO-04 | design-exercise | Hardened local edge config: what the origin still must verify | 4 Build |
| 2.2-LO-05 | verification-lab | Tests that origin rejects unauthenticated forwarded identity | 5 Verify |
| 2.2-LO-06 | operations-exercise | Cert failure / expiry drill notes | 6 Operate |
| 2.2-LO-07 | transfer-challenge | Add CDN: new cache-key and Host trust | 7 Generalize |
| 2.2-LO-08 | code-review | Seeded app that trusts X-Forwarded-For for authz | 5 Verify |

## Lab briefs

**Lab `2.2-request-path`:** local reverse proxy/fixture only. Forbidden: attacking real CDNs or third-party sites.

## Assessment blueprint

Explain hops; design path diagram; break local rewrite; verify origin checks; operate cert failure; communicate residual after TLS termination.

## Standards references

ASVS 5.0.0 V4/V12/V13 `final`. RFC 9846 TLS 1.3 `final` (July 2026).

## Review triggers

New edge, CDN, HTTP/2-3, or mTLS.

## Time budget

~300 min. Core of M0 observable skeleton.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
