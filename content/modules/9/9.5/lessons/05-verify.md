# 9.5 — Authorized assessment, reporting, and remediation (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Finding closed without retest |
| Failure | Fail closed: Require retest of the same cell |

Lab tests: `test_property.py` under `labs/9.5/9.5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Finding closed without retest`
- `--impl fixed`: **pass**

no retest => False.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

KEV vs internal-only.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
