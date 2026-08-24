# 8.3 — Network, deep links, WebViews, IPC (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
**Forbidden outcome:** Deep link as= switches the signed-in user

**Authorized scope:** `labs/8.3/8.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable link.py switches user.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: open_link({as:admin}) sets admin.

## Vulnerable fixture (local)

```python
SESSION={'user':'alice'}
def reset():
    SESSION['user']='alice'
def open_link(query):
    if 'as' in query:
        SESSION['user']=query['as']
def current_user():
    return SESSION['user']
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Identity taken from the link. |
| Impact | Local privilege / account switch. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/8.3/8.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

OAuth redirect to app (4.5).

## Non-goals

No live-target instructions. Synthetic data only.
