# A token for another API, or a missing audience, must fail

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“OpenID Connect is configured” is not this topic’s evidence. “The JWT verifies” is a tool observation. The check is: `accept_token({"sub": "alice", "aud": "other-api"}, "securecollab-api")` is false. That observation must be **false** on the broken files (returns true) and **true** on the repaired files.

## Picture: other-api and missing aud must fail

Asserting a library called `verify` can still hide that a wrong-audience token still counts as a session.

```mermaid
flowchart LR
  V["broken files"] --> F["Must fail: other-api and missing aud"]
  X["repaired files"] --> P["Must pass the same denies"]
```

| Mode | Must show for this topic |
|---|---|
| Normal | expected `aud` is true (may pass on both) |
| Wrong input / abuse | `aud=other-api` and missing `aud` are false; broken files must fail |
| Not claimed | PKCE; JWKS; DPoP; who-is-allowed on notes |

The checks are in `labs/4.5/4.5-lab/tests/test_property.py`. `test_wrong_audience_is_rejected` is there so a wrong-audience token accepted as a session still fails.

```text
python3 -m pytest labs/4.5/4.5-lab/tests --impl vulnerable
python3 -m pytest labs/4.5/4.5-lab/tests --impl fixed
```

A token whose `aud` is this API may pass on both sides. You still have to deny `other-api` and a missing audience. If the broken files do not fail other-api, the lab is miswired — fix the wiring, not the check. A setup error is not proof the rule holds.

## What the tests do not prove

- PKCE / `state` / `nonce`
- Backend-for-frontend token confinement
- Sender-constrained tokens (advanced)
- Note authorization (who-is-allowed)
- Native redirect safety (claimed HTTPS, not a custom scheme)

## Practice

Do not treat a grep for `verify` in an Authlib call as the check. Compare `aud`.

## Use it somewhere new

Clinic FHIR. Asserting HTTP 200 is not audience evidence. Do not run a test that hits a live identity provider.

## What this page is not doing

Do not add a live token. Do not paste JWTs into tickets. Answer keys are not on this site.
