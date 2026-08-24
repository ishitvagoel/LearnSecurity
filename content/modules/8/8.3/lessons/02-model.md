# 8.3 — Network, deep links, WebViews, IPC (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | alice session, attacker app |
| Objects | as query, current_user |
| Actions | open_link |
| Channels | Intent, App Link, custom scheme |
| TCB | Ignore identity params; use session. |
| Untrusted | All extras, URLs, WebView JS bridges |
| State / time | Cold start via link. |
| 1.1 cell | Authenticity of the principal. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| attacker app | as=admin | identity | deny |
| alice session | open note link | nav | allow-if-1.2 |
| WebView | js bridge | call | allow-list |
| custom scheme | token | 4.5 | deny-leak |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/8.3/8.3-lab` file `link.py`.

## Transfer

OAuth redirect to app (4.5).

## Residual risk

User installs attacker app — OS model.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
