# 4.1 — Identity lifecycle (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
**Forbidden outcome:** Deleted user's leftover session still authenticates

**Authorized scope:** `labs/4.1/4.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable lifecycle.py leaves session live.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: delete_user removes profile only.

## Vulnerable fixture (local)

```python
SESSIONS = {"alice": True}
DELETED = set()

def reset():
    SESSIONS.clear(); SESSIONS["alice"] = True
    DELETED.clear()

def delete_user(user: str) -> None:
    DELETED.add(user)

def session_valid(user: str) -> bool:
    return bool(SESSIONS.get(user))
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Authentication artifact outlived the subject. |
| Impact | Ex-employee or attacker with the cookie still reads tenant notes. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/4.1/4.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Contractor access end-date; support impersonation tickets.

## Non-goals

No live-target instructions. Synthetic data only.
