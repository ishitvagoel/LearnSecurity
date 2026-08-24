# 10.5 — Logging, detection, incident response, recovery, maintenance (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Incident closed without recovery evidence |
| Failure | Fail closed: Require recovery evidence (restore test, revoke list) |

Lab tests: `test_property.py` under `labs/10.5/10.5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Incident closed without recovery evidence`
- `--impl fixed`: **pass**

cannot close without recovery.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Ransomware restore vs note-level integrity.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
