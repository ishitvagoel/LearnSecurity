# 4.5 — OAuth, OIDC, and delegated authorization (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
aud must equal expected.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def accept_token(claims: dict, expected_aud: str) -> bool:
    aud = claims.get("aud")
    if isinstance(aud, list):
        return expected_aud in aud
    return aud == expected_aud
```

## Why this restores the cell

Exact aud match (or constrained list).

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Authlib defaults may verify signature only if you configure poorly.

Correct aud still needs 1.2 on the note.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

## Residual risk

Full OAuth (PKCE, state, nonce, sender-constraining) not in this micro-fixture.
