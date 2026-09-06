# SecureCollab Phase 1 — delegated access and audience

Design stub for Module 4.5. Not a production authorization server.

## Freeze

- Local `accept_token(claims, expected_aud)`. Synthetic `aud` strings `securecollab-api` and `other-api`.
- No live OAuth, no JWKS fetch, no real redirect.

## Audience is a name

A bearer JWT with `aud=other-api` must not spend `securecollab-api`. Signature (named residual) without audience is confused-deputy fuel. OAuth 2.1 is an Internet-Draft. RFC 9700 (BCP 240), RFC 10017 (browser apps, BCP 212, August 2026), and RFC 8252 (native apps) are the final protocol pins. PKCE, `state`, `nonce`, and sender-constraining (`v5.0.0-10.3.5` Level 3) are named holes.

## Tests

`accept_token({sub, aud: other-api}, securecollab-api)` is false. Missing `aud` is false. Expected `aud` is true. 1.2 on the note is still required after a valid audience.
