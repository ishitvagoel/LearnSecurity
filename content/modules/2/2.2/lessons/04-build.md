# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
cache_get requires same tenant as cache_put.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
"""Fixed: cache key includes the bound tenant (not Host/X-Forwarded-* from the client)."""

from __future__ import annotations

_CACHE: dict[tuple[str, str], str] = {}


def cache_put(path: str, tenant: str, body: str) -> None:
    _CACHE[(path, tenant)] = body


def cache_get(path: str, tenant: str) -> str | None:
    return _CACHE.get((path, tenant))


def reset() -> None:
    _CACHE.clear()
```

## Why this restores the cell

Key = (tenant_id, route, representation). Default private for notes.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Next.js fetch cache and FastAPI HTTPException defaults do not encode tenant.

Cache-Control: private still fails if your CDN is configured to cache anyway.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Authenticated RSS or export CSV via CDN.

## Residual risk

Operational error at the CDN remains; monitor.
