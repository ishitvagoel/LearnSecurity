# 11 — Capstone: SecureCollab integration (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.

## Property (start here)

After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.

## Attacker capabilities and trust assumptions

- **Attacker:** Former collaborator with a cached id; delayed worker (7.4).
- **Trust:** Local share map.
revoke then read is None.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
NOTES={'n1': {'tenant': 'A', 'body': 'secret'}}
GRANTS={('n1', 'B')}
def reset():
    GRANTS.clear(); GRANTS.add(('n1', 'B'))
def revoke(nid, tenant):
    GRANTS.discard((nid, tenant))
def read(nid, tenant):
    n = NOTES[nid]
    if tenant == n['tenant'] or (nid, tenant) in GRANTS:
        return n['body']
    return None
```

## Why this restores the cell

Complete mediation on read; invalidate caches; wipe mobile.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

A green capstone scanner is not the 13 artifacts.

Email already received the body — residual 5.1.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Clinic: revoke a guardian.

## Residual risk

Honest copies already made — policy + detect.
