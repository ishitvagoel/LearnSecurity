# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Cache-hit with mismatched tenant id in logs (no body). |
| Signal (no bodies) | cdn_hit_tenant_mismatch; purge playbook. |
| Revoke / recover | Purge the prefix; treat as 1.1 incident if bodies escaped. |
| Residual | Operational error at the CDN remains; monitor. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/2.2/2.2-request-path`.

## Transfer

Authenticated RSS or export CSV via CDN.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
