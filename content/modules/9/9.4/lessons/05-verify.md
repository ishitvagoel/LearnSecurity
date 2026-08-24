# 9.4 — Automated analysis and tool orchestration (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Unmapped HIGH finding allows ship |
| Failure | Fail closed: Block unmapped HIGH; allow mapped+accepted with E6 |

Lab tests: `test_property.py` under `labs/9.4/9.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Unmapped HIGH finding allows ship`
- `--impl fixed`: **pass**

unmapped HIGH blocks.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

SCA CVE vs actually called function.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
