# Lab: 1.2-authority-matrix

**Module:** `1.2`  
**Authorized scope:** local course fixture (this directory only). No public or third-party targets.  
**Invariant:** A logged-in SecureCollab member of tenant B cannot read tenant A’s note body via `read_note`.  
**Root cause class:** authority (ambient `current_user` without object check)  
**Non-goals:** live systems, real PII, weaponized HTTP payloads.

## Reset

Restore `vulnerable/` and `fixed/` from git. Synthetic tenants `tA`/`tB` only.

## Vulnerable behavior (local only)

`vulnerable/notes.py` treats **authentication** as **authorization**: any known user who supplies note id `n1` receives tenant A’s body. That is a complete-mediation miss on the object.

Forbidden outcome: `read_note("bob", "n1")` returns tenant A’s note.

## Structural fix

`fixed/notes.py` mediates **subject, object, action**: same-tenant membership is required; missing notes deny (fail-safe). A denylist of “bob” would not restore the invariant when a third tenant appears.

## Verify

From this lab directory:

```bash
python3 -m pytest tests/test_mediation.py --impl vulnerable   # must FAIL on cross-tenant read
python3 -m pytest tests/test_mediation.py --impl fixed        # must PASS
```

Happy path: alice reads n1. Negative: bob cannot read n1. Unknown note and unknown user deny.

## Operate

Log denied cross-tenant reads (subject, object, action) without logging note bodies. Revoke stolen sessions. Recovery is out of scope until 1.4.

## Transfer

Add a **worker** principal that exports notes. Redraw the matrix: the worker must not inherit alice’s ambient process user as permission on n2.
