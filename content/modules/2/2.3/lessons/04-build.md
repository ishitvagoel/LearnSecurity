# 2.3 — Browser security model (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
js_read_session returns None when httponly True.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
"""Fixed: HttpOnly session is not readable to script; XSS is not 'solved' — this is one cell."""


def js_read_session(cookies: dict) -> str | None:
    session = cookies.get("sc_session")
    if not session:
        return None
    if session.get("httponly"):
        return None
    return session["value"]
```

## Why this restores the cell

HttpOnly; Secure; careful SameSite — still not XSS-proof.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Next.js “cookies() are httpOnly by default” is not true for every cookie you set manually.

HttpOnly does not stop network theft, CSRF (6.3), or native apps reading the store.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

React Native WebView cookie bridge.

## Residual risk

Browser extensions; physical access.
