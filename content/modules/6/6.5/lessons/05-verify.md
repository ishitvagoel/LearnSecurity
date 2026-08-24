# 6.5 — Server-side requests and protocol parsing (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Server-side fetch to link-local metadata is allowed |
| Failure | Fail closed: Allow-list; parse then pin; block link-local, loopback, metadata; no open redirects |

Lab tests: `test_property.py` under `labs/6.5/6.5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Server-side fetch to link-local metadata is allowed`
- `--impl fixed`: **pass**

169.254 denied; lab host ok.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Webhook delivery (7.3) is egress too.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
