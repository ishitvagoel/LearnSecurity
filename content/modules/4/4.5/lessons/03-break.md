# 4.5 — OAuth, OIDC, and delegated authorization (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
**Forbidden outcome:** JWT with wrong audience accepted as a SecureCollab session

**Authorized scope:** `labs/4.5/4.5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable jwt_aud.py accepts any aud.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: accept_token ignores aud.

## Vulnerable fixture (local)

```python
def accept_token(claims: dict, expected_aud: str) -> bool:
    return "sub" in claims
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Signature verified without audience. |
| Impact | Other-api token spends SecureCollab API. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/4.5/4.5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

## Non-goals

No live-target instructions. Synthetic data only.
