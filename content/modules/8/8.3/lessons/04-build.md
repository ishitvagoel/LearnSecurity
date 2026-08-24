# 8.3 — Network, deep links, WebViews, IPC (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
as=admin leaves current_user alice.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
SESSION={'user':'alice'}
def reset():
    SESSION['user']='alice'
def open_link(query):
    return None
def current_user():
    return SESSION['user']
```

## Why this restores the cell

Do not take identity from links; validate App Link certs; WebView allow-list.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

exported=true defaults on old Android.

Verified App Links still pass query strings.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

OAuth redirect to app (4.5).

## Residual risk

User installs attacker app — OS model.
