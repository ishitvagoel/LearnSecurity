# 6.4 — Files, paths, uploads, archives, XML, deserialization (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Resolved path escapes the lab root |
| Failure | Fail closed: Join + canonicalize + prefix; random stored names; never execute uploads |

Lab tests: `test_property.py` under `labs/6.4/6.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Resolved path escapes the lab root`
- `--impl fixed`: **pass**

.. does not escape.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

XML entity expansion; pickle; YAML load.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
