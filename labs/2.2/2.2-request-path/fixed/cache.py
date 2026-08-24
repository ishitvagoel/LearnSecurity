"""Fixed: cache key includes the bound tenant (not Host/X-Forwarded-* from the client)."""

from __future__ import annotations

_CACHE: dict[tuple[str, str], str] = {}


def cache_put(path: str, tenant: str, body: str) -> None:
    _CACHE[(path, tenant)] = body


def cache_get(path: str, tenant: str) -> str | None:
    return _CACHE.get((path, tenant))


def reset() -> None:
    _CACHE.clear()
