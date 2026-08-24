# 4.5 — OAuth, OIDC, and delegated authorization (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | client, resource server, other-api |
| Objects | JWT aud, expected audience |
| Actions | accept_token |
| Channels | Authorization header |
| TCB | RS checks aud (and later iss, exp, signature). |
| Untrusted | Client-supplied token blob |
| State / time | Long-lived tokens after client deprovision (4.1). |
| 1.1 cell | Authenticity of the audience binding. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| client | aud=securecollab-api | call API | allow-if-valid |
| client | aud=other-api | call API | deny |
| browser | id_token | call API | deny |
| mobile | custom-scheme token | store | 8.3 residual |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/4.5/4.5-lab` file `jwt_aud.py`.

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

## Residual risk

Full OAuth (PKCE, state, nonce, sender-constraining) not in this micro-fixture.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
