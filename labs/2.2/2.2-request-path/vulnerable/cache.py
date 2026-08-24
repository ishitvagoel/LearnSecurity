"""Vulnerable: cache key is URL only; tenant is not part of the key."""

from __future__ import annotations

_CACHE: dict[str, str] = {}


def cache_put(path: str, tenant: str, body: str) -> None:
    _CACHE[path] = body


def cache_get(path: str, tenant: str) -> str | None:
    return _CACHE.get(path)


def reset() -> None:
    _CACHE.clear()
