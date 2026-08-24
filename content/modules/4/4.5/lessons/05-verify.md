# 4.5 — OAuth, OIDC, and delegated authorization (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | JWT with wrong audience accepted as a SecureCollab session |
| Failure | Fail closed: Exact aud match (or constrained list) |

Lab tests: `test_property.py` under `labs/4.5/4.5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `JWT with wrong audience accepted as a SecureCollab session`
- `--impl fixed`: **pass**

wrong aud false; expected aud true.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
