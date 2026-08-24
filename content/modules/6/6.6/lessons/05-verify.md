# 6.6 — Workflow, race, and exceptional-condition failures (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Invite token accepted twice |
| Failure | Fail closed: Single-use in a transaction; expire; bind to recipient |

Lab tests: `test_property.py` under `labs/6.6/6.6-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Invite token accepted twice`
- `--impl fixed`: **pass**

t1 then t1 => False.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
