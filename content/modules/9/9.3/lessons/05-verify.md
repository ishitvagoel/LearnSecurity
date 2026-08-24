# 9.3 — Security-focused tests (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | HTTP 200-only test counted as a security test |
| Failure | Fail closed: Require forbidden-outcome asserts |

Lab tests: `test_property.py` under `labs/9.3/9.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `HTTP 200-only test counted as a security test`
- `--impl fixed`: **pass**

status_asserted only => False.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Fuzzing without an oracle.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
