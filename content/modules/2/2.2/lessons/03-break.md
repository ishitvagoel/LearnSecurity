# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
**Forbidden outcome:** Shared cache returns tenant A's body to tenant B

**Authorized scope:** `labs/2.2/2.2-request-path` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable cache.py keys only on path.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Shared cache; path-only key; tA populated the entry.

## Vulnerable fixture (local)

```python
"""Vulnerable: cache key is URL only; tenant is not part of the key."""

from __future__ import annotations

_CACHE: dict[str, str] = {}


def cache_put(path: str, tenant: str, body: str) -> None:
    _CACHE[path] = body


def cache_get(path: str, tenant: str) -> str | None:
    return _CACHE.get(path)


def reset() -> None:
    _CACHE.clear()
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Key omitted the subject’s tenant; shared store. |
| Impact | Cross-tenant read without guessing ids. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/2.2/2.2-request-path/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Authenticated RSS or export CSV via CDN.

## Non-goals

No live-target instructions. Synthetic data only.
