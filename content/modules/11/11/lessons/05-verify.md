# 11 — Capstone: SecureCollab integration (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.

## Property (start here)

After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.

## Attacker capabilities and trust assumptions

- **Attacker:** Former collaborator with a cached id; delayed worker (7.4).
- **Trust:** Local share map.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Revoked share still reads the note |
| Failure | Fail closed: Complete mediation on read; invalidate caches; wipe mobile |

Lab tests: `test_property.py` under `labs/11/11-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Revoked share still reads the note`
- `--impl fixed`: **pass**

revoked share cannot read.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Clinic: revoke a guardian.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
