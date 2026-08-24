# 2.3 — Browser security model (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Token-binding / anomaly (later); XSS reports. |
| Signal (no bodies) | Set-Cookie without HttpOnly in staging scans. |
| Revoke / recover | Revoke session (4.3); rotate. |
| Residual | Browser extensions; physical access. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/2.3/2.3-browser-policy`.

## Transfer

React Native WebView cookie bridge.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
