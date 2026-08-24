# 4.5 — OAuth, OIDC, and delegated authorization (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Reject metric by aud. |
| Signal (no bodies) | jwt_aud_mismatch; client_revoked. |
| Revoke / recover | Revoke client; rotate keys. |
| Residual | Full OAuth (PKCE, state, nonce, sender-constraining) not in this micro-fixture. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/4.5/4.5-lab`.

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
