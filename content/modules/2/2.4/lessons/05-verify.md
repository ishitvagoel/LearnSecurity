# 2.4 — State, time, concurrency, and distributed failure (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Retry creates a second share grant |
| Failure | Fail closed: Persist key → share id; second POST returns the first |

Lab tests: `test_idempotency.py` under `labs/2.4/2.4-state-time`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Retry creates a second share grant`
- `--impl fixed`: **pass**

two calls with k1 => count 1.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
