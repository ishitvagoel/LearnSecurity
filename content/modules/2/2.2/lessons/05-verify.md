# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Shared cache returns tenant A's body to tenant B |
| Failure | Fail closed: Key = (tenant_id, route, representation) |

Lab tests: `test_cache_key.py` under `labs/2.2/2.2-request-path`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Shared cache returns tenant A's body to tenant B`
- `--impl fixed`: **pass**

tA hit works; tB get is None.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Authenticated RSS or export CSV via CDN.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
