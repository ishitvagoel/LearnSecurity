# 6.1 — Interpreter confusion and injection (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | User-controlled name executed via a shell string |
| Failure | Fail closed: argv list; no shell; validate allow-listed names |

Lab tests: `test_property.py` under `labs/6.1/6.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `User-controlled name executed via a shell string`
- `--impl fixed`: **pass**

not sh -c; uses_shell false.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Jinja, SQL, mail headers.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
