# 6.7 — Resource abuse, automation, and availability (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Unbounded exports (4th allowed in the lab window) |
| Failure | Fail closed: Quota + authz + maybe queue |

Lab tests: `test_property.py` under `labs/6.7/6.7-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Unbounded exports (4th allowed in the lab window)`
- `--impl fixed`: **pass**

fourth export denied.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Notification fan-out; search complexity.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
