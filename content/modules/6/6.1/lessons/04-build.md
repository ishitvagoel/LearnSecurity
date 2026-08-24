# 6.1 — Interpreter confusion and injection (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
argv is ['ls', name] or reject; uses_shell False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def argv_for_list(name):
    if any(c in name for c in ' 	;|&$`'):
        raise ValueError('rejected')
    return ['ls', name]
def uses_shell(name):
    return False
```

## Why this restores the cell

argv list; no shell; validate allow-listed names.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

subprocess defaults are easy to misuse; FastAPI has no opinion.

Rejecting ; | still fails on IFS and encoding (2.1).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Jinja, SQL, mail headers.

## Residual risk

Needed shell for a plugin — isolate that binary.
