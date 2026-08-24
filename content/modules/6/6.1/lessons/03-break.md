# 6.1 — Interpreter confusion and injection (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
**Forbidden outcome:** User-controlled name executed via a shell string

**Authorized scope:** `labs/6.1/6.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable argv.py uses sh -c concat.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: returns ['sh','-c','ls '+name].

## Vulnerable fixture (local)

```python
def argv_for_list(name):
    return ['sh', '-c', 'ls ' + name]
def uses_shell(name):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Concatenating untrusted data into a shell grammar. |
| Impact | OS interpreter runs attacker grammar (lab asserts structure only). |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.1/6.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Jinja, SQL, mail headers.

## Non-goals

No live-target instructions. Synthetic data only.
