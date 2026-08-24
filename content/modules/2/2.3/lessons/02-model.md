# 2.3 — Browser security model (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Page script, browser cookie jar, attacker XSS |
| Objects | sc_session cookie |
| Actions | js_read_session, document.cookie |
| Channels | DOM, Cookie header |
| TCB | Browser cookie jar + server Set-Cookie flags. |
| Untrusted | Any JavaScript bundle, including yours after XSS. |
| State / time | Cookie lifetime vs XSS window. |
| 1.1 cell | Session confidentiality against script (not against the network — that’s TLS). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| page script | HttpOnly cookie | read | deny |
| browser | Cookie header | send-to-origin | allow |
| XSS | session | steal-via-js | deny-if-HttpOnly |
| network attacker | cookie | read-on-wire | TLS-not-this-lab |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/2.3/2.3-browser-policy` file `cookies.py`.

## Transfer

React Native WebView cookie bridge.

## Residual risk

Browser extensions; physical access.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
