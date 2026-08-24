# 3.2 — Threat modeling (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Green scanner produces an empty SecureCollab threat model |
| Failure | Fail closed: Seed mandatory threats; scanner findings are extra, not the set |

Lab tests: `test_property.py` under `labs/3.2/3.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Green scanner produces an empty SecureCollab threat model`
- `--impl fixed`: **pass**

green scan still lists cross-tenant-read.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Add webhooks (7.3): which new threats?

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
