# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
**Mechanism (not the property):** Next.js fetch cache and FastAPI HTTPException defaults do not encode tenant.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 2.2 |
|---|---|
| Root cause | Key omitted the subject’s tenant; shared store. |
| Preconditions | Shared cache; path-only key; tA populated the entry. |
| Impact (1.1 cell) | Confidentiality via shared mechanism (Saltzer least common mechanism). — Cross-tenant read without guessing ids. |
| Prevention | Key = (tenant_id, route, representation). Default private for notes. |
| Detection | Cache-hit with mismatched tenant id in logs (no body). |
| Recovery | Purge the prefix; treat as 1.1 incident if bodies escaped. |

## Framework defaults vs application guarantees

Next.js fetch cache and FastAPI HTTPException defaults do not encode tenant.

## Mechanism limits and bypasses

Cache-Control: private still fails if your CDN is configured to cache anyway.

Normalized URLs, HTTP/2 push, stale-while-revalidate serving tA to tB.

## Residual risk

Operational error at the CDN remains; monitor.

## Practice

Write the key tuple for /notes/n1. Run the lab.

Run `labs/2.2/2.2-request-path` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Authenticated RSS or export CSV via CDN.

Clinic: cached /patients/me.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
