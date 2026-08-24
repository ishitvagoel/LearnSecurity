# 4.5 — OAuth, OIDC, and delegated authorization (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
Review `labs/4.5/4.5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/4.5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): verify signature, skip aud
- Seeded smell (label it yourself): ID token used as API access token
- Seeded smell (label it yourself): Implicit flow in SPA README
- Seeded smell (label it yourself): No test other-api aud

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- OIDC login replaces your matrix
- JWT means OAuth is done
- Mobile custom scheme is a safe redirect

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.
