# Lab 4.5

**Authorized scope:** this directory only.
**Invariant:** An access token is accepted only if **aud** is this API. A token minted for another audience is not a SecureCollab session. OAuth 2.1 remains an **Internet-Draft** — label it.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: any token with sub is accepted regardless of aud. OAuth 2.1 is draft.
