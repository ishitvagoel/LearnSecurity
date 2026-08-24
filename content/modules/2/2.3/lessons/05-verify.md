# 2.3 — Browser security model (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Script reads the HttpOnly session cookie |
| Failure | Fail closed: HttpOnly; Secure; careful SameSite — still not XSS-proof |

Lab tests: `test_httponly.py` under `labs/2.3/2.3-browser-policy`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Script reads the HttpOnly session cookie`
- `--impl fixed`: **pass**

HttpOnly session not script-readable.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

React Native WebView cookie bridge.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
