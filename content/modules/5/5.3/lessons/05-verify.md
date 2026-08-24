# 5.3 — Key and secret lifecycle (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Hardcoded default API key still authenticates after rotation |
| Failure | Fail closed: Generate unique secrets; rotate; refuse known defaults; never commit |

Lab tests: `test_property.py` under `labs/5.3/5.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Hardcoded default API key still authenticates after rotation`
- `--impl fixed`: **pass**

hardcoded fails; current succeeds if you add that test.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
