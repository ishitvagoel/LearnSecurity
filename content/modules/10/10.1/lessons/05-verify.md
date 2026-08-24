# 10.1 — Secure software lifecycle and security culture (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Merge without a threat-model identifier |
| Failure | Fail closed: Require tm id; triggers on identity, data, mobile… |

Lab tests: `test_property.py` under `labs/10.1/10.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Merge without a threat-model identifier`
- `--impl fixed`: **pass**

missing tm-id cannot merge.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Exception path (E6).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
