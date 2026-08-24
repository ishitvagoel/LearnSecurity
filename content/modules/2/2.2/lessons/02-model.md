# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | tA member, tB member, cache node |
| Objects | Note body, cache key, Authorization, Host |
| Actions | cache_put, cache_get |
| Channels | TLS, HTTP, CDN POP |
| TCB | Origin cache-key policy (tenant + path + auth). |
| Untrusted | URL path alone, “Vary: Accept-Encoding” only, client-supplied X-Tenant |
| State / time | Cached 60s after tA’s GET — tB’s GET in that window. |
| 1.1 cell | Confidentiality via shared mechanism (Saltzer least common mechanism). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| tA | /notes/n1 | GET-hit | own-body |
| tB | /notes/n1 | GET | miss-or-own |
| anon | /notes/n1 | GET | deny |
| ops | cache | purge-prefix | allow |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/2.2/2.2-request-path` file `cache.py`.

## Transfer

Authenticated RSS or export CSV via CDN.

## Residual risk

Operational error at the CDN remains; monitor.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
