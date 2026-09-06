# Lab 4.5 — wrong-audience JWT is not a SecureCollab session

**Module:** `4.5`
**Authorized scope:** this directory only. Local course fixture. No live IdPs.
**Invariant:** `accept_token` is true only when `aud` matches `securecollab-api`. A token minted for `other-api` is not a session. OAuth 2.1 remains an **Internet-Draft**.
**Root cause class:** trust / interpreter (signature-or-sub without audience)
**Non-goals:** live OAuth, real JWKS, weaponized alg=none walkthroughs.

## Reset

Re-run pytest. Optional: `git checkout -- labs/4.5/4.5-lab`.

## Vulnerable behavior (local only)

`accept_token` returns true if `sub` is present. It ignores `aud`. Forbidden outcome: JWT with wrong (or missing) audience accepted as a SecureCollab session.

## Structural fix

Require `aud` to equal the expected resource-server name (string or list membership). Missing `aud` is deny. This is not PKCE, nonce, or DPoP.

## Verify

From repo root:

```
python3 -m pytest labs/4.5/4.5-lab/tests --impl vulnerable
python3 -m pytest labs/4.5/4.5-lab/tests --impl fixed
```

The first command must fail on the deny tests. The second must pass. The honest expected-aud test may pass on both.

## Operate

Signal: `jwt_aud_mismatch` with expected aud and token id (or hash), never the raw token or a note body. Revoke the client; rotate keys if tokens self-verify.

## Transfer

Clinic: wrong-aud FHIR token. RFC 8252 native redirect. Prompt only; do not leave this directory.
