# 2.4 — State, time, concurrency, and distributed failure (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
share_note keyed by idempotency_key; share_count stays 1.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
"""Fixed: same idempotency key does not duplicate the share side effect."""

_SHARES: list[str] = []
_SEEN: set[str] = set()


def reset() -> None:
    _SHARES.clear()
    _SEEN.clear()


def share_count() -> int:
    return len(_SHARES)


def share_note(note_id: str, idempotency_key: str | None = None) -> None:
    if idempotency_key:
        if idempotency_key in _SEEN:
            return
        _SEEN.add(idempotency_key)
    _SHARES.append(note_id)
```

## Why this restores the cell

Persist key → share id; second POST returns the first.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

FastAPI does not dedupe POSTs. HTTP 201 twice is still two rows.

Keys that expire too fast replay as new shares.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

## Residual risk

Lost first response still needs a read-your-write path.
