# 2.3 — Browser security model (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
**Mechanism (not the property):** Next.js “cookies() are httpOnly by default” is not true for every cookie you set manually.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 2.3 |
|---|---|
| Root cause | Session presented to the script interpreter. |
| Preconditions | Cookie without HttpOnly; script runs. |
| Impact (1.1 cell) | Session confidentiality against script (not against the network — that’s TLS). — Session theft then 1.2 as the thief. |
| Prevention | HttpOnly; Secure; careful SameSite — still not XSS-proof. |
| Detection | Token-binding / anomaly (later); XSS reports. |
| Recovery | Revoke session (4.3); rotate. |

## Framework defaults vs application guarantees

Next.js “cookies() are httpOnly by default” is not true for every cookie you set manually.

## Mechanism limits and bypasses

HttpOnly does not stop network theft, CSRF (6.3), or native apps reading the store.

XSS in a sibling cookie that is not HttpOnly; MITM without Secure.

## Residual risk

Browser extensions; physical access.

## Practice

Name three things HttpOnly does *not* prove. Run the lab.

Run `labs/2.3/2.3-browser-policy` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

React Native WebView cookie bridge.

Clinic patient portal session cookie.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
