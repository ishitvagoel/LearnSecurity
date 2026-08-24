# 6.3 — Cross-site and cross-context attacks (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Cross-origin state-changing POST authorized by cookie alone |
| Failure | Fail closed: Reject foreign Origin; require token for cookie sessions |

Lab tests: `test_property.py` under `labs/6.3/6.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Cross-origin state-changing POST authorized by cookie alone`
- `--impl fixed`: **pass**

foreign POST denied.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

postMessage, clickjacking, CORS * with credentials.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
