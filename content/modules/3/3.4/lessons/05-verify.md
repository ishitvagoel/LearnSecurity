# 3.4 — Business logic and abuse-resistant design (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Share grants exceed the product cap of 5 |
| Failure | Fail closed: Check count in the write path; reject 6th |

Lab tests: `test_property.py` under `labs/3.4/3.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Share grants exceed the product cap of 5`
- `--impl fixed`: **pass**

eighth add leaves last <= 5.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Invite tokens (6.6) and export quotas (6.7).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
