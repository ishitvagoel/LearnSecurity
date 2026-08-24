# E2 — Advanced browser and edge security (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Report-Only CSP counted as isolation enforcement |
| Failure | Fail closed: Detect enforcing header; don’t claim isolation otherwise |

Lab tests: `test_property.py` under `labs/E2/e2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Report-Only CSP counted as isolation enforcement`
- `--impl fixed`: **pass**

report-only is not enforcement.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Trusted Types, COOP/COEP.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
