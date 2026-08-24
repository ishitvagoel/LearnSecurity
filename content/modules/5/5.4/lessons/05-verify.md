# 5.4 — Secure communication and channel binding (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Client X-Forwarded-Proto treated as TLS |
| Failure | Fail closed: Ignore client proto unless the immediate peer is a trusted proxy with a bound identity |

Lab tests: `test_property.py` under `labs/5.4/5.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Client X-Forwarded-Proto treated as TLS`
- `--impl fixed`: **pass**

mismatch is not TLS.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

mTLS service identity vs this header.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
