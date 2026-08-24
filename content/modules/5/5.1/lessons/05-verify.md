# 5.1 — Data lifecycle and privacy engineering (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Analytics copy still holds note body after account deletion |
| Failure | Fail closed: Inventory copies; delete or unlink bodies in each |

Lab tests: `test_property.py` under `labs/5.1/5.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Analytics copy still holds note body after account deletion`
- `--impl fixed`: **pass**

after delete body_retained is None.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

CSV export to a partner; clinic-booking card PHI.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
