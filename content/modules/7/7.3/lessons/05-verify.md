# 7.3 — Webhooks, callbacks, and third-party APIs (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Unsigned webhook body accepted |
| Failure | Fail closed: Verify MAC; bind to secret per provider; timestamp |

Lab tests: `test_property.py` under `labs/7.3/7.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Unsigned webhook body accepted`
- `--impl fixed`: **pass**

missing signature rejected.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Signed redirects; outbound webhook SSRF (6.5).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
