# 6.1 — Interpreter confusion and injection (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
**Mechanism (not the property):** subprocess defaults are easy to misuse; FastAPI has no opinion.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.1 |
|---|---|
| Root cause | Concatenating untrusted data into a shell grammar. |
| Preconditions | returns ['sh','-c','ls '+name]. |
| Impact (1.1 cell) | Integrity of the OS interpreter boundary. — OS interpreter runs attacker grammar (lab asserts structure only). |
| Prevention | argv list; no shell; validate allow-listed names. |
| Detection | Unexpected child processes. |
| Recovery | Kill; rotate host if it left the lab (it must not). |

## Framework defaults vs application guarantees

subprocess defaults are easy to misuse; FastAPI has no opinion.

## Mechanism limits and bypasses

Rejecting ; | still fails on IFS and encoding (2.1).

Another interpreter: SQL, template, LDAP — same *shape*.

## Residual risk

Needed shell for a plugin — isolate that binary.

## Practice

Map data flow into each interpreter on the export path.

Run `labs/6.1/6.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Jinja, SQL, mail headers.

Clinic export-to-CSV filename.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
