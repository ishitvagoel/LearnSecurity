# 6.6 — Workflow, race, and exceptional-condition failures (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
**Forbidden outcome:** Invite token accepted twice

**Authorized scope:** `labs/6.6/6.6-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable invite.py allows replay.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: second accept True.

## Vulnerable fixture (local)

```python
_used=False
def reset():
    global _used
    _used=False
def accept(token):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Non-atomic check-then-set; token not marked used. |
| Impact | Extra member or replay after revoke. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.6/6.6-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

## Non-goals

No live-target instructions. Synthetic data only.
