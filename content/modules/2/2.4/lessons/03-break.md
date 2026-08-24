# 2.4 — State, time, concurrency, and distributed failure (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
**Forbidden outcome:** Retry creates a second share grant

**Authorized scope:** `labs/2.4/2.4-state-time` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable share.py increments on every call.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Timeout; client retries same key; handler inserts again.

## Vulnerable fixture (local)

```python
"""Vulnerable: every share_note call performs the side effect (retry duplicates)."""

_SHARES: list[str] = []


def reset() -> None:
    _SHARES.clear()


def share_count() -> int:
    return len(_SHARES)


def share_note(note_id: str, idempotency_key: str | None = None) -> None:
    _SHARES.append(note_id)
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Non-idempotent side effect + retry = extra grant. |
| Impact | Extra principal on the note (1.2 cell changes). |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/2.4/2.4-state-time/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

## Non-goals

No live-target instructions. Synthetic data only.
