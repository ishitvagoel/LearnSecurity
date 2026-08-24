# 6.3 — Cross-site and cross-context attacks (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | victim browser, evil.example, app |
| Objects | share POST, Origin, CSRF token |
| Actions | allow_share |
| Channels | cookie + cross-site POST |
| TCB | Server check of Origin/Fetch Metadata and/or anti-CSRF token bound to session. |
| Untrusted | Cookie presence, Referer alone |
| State / time | User still logged in while visiting evil. |
| 1.1 cell | Integrity of share grants (3.4/1.2) against the browser’s confused-deputy. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| app origin | POST share | with token | allow |
| evil origin | POST share | cookie only | deny |
| evil origin | GET share | mutate | deny |
| bearer API | POST | no cookie | different-model |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.3/6.3-lab` file `csrf.py`.

## Transfer

postMessage, clickjacking, CORS * with credentials.

## Residual risk

User clicking “share” on a lookalike UI — 4.2 phishing.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
