# 2.3 — Browser security model (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
**Forbidden outcome:** Script reads the HttpOnly session cookie

**Authorized scope:** `labs/2.3/2.3-browser-policy` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable cookies.py exposes session to script.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Cookie without HttpOnly; script runs.

## Vulnerable fixture (local)

```python
"""Vulnerable: session cookie is readable to script in the origin (no HttpOnly)."""


def js_read_session(cookies: dict) -> str | None:
    session = cookies.get("sc_session")
    if not session:
        return None
    return session["value"]
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Session presented to the script interpreter. |
| Impact | Session theft then 1.2 as the thief. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/2.3/2.3-browser-policy/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

React Native WebView cookie bridge.

## Non-goals

No live-target instructions. Synthetic data only.
