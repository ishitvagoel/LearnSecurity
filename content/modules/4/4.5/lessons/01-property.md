# 4.5 — OAuth, OIDC, and delegated authorization (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”

## Property (start here)

A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen token minted for another API; confused deputy client.
- **Trust:** Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.
**Mechanism (not the property):** Authlib defaults may verify signature only if you configure poorly.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 4.5 |
|---|---|
| Root cause | Signature verified without audience. |
| Preconditions | accept_token ignores aud. |
| Impact (1.1 cell) | Authenticity of the audience binding. — Other-api token spends SecureCollab API. |
| Prevention | Exact aud match (or constrained list). |
| Detection | Reject metric by aud. |
| Recovery | Revoke client; rotate keys. |

## Framework defaults vs application guarantees

Authlib defaults may verify signature only if you configure poorly.

## Mechanism limits and bypasses

Correct aud still needs 1.2 on the note.

Empty aud; array aud tricks; alg=none (do not teach as a payload — reject unknown alg).

## Residual risk

Full OAuth (PKCE, state, nonce, sender-constraining) not in this micro-fixture.

## Practice

Sequence: authz-code + PKCE vs this lab’s single aud check — name what is missing.

Run `labs/4.5/4.5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.

Clinic: wrong-aud FHIR token.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
