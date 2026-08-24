# 4.5 — OAuth, OIDC, and delegated authorization (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

**Product sketch:** Clinic: wrong-aud FHIR token.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Authlib defaults may verify signature only if you configure poorly.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/4.5/4.5-lab` stays the only running system you may break.
