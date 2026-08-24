# 11 — Capstone: SecureCollab integration (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.

## Property (start here)

After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.

## Attacker capabilities and trust assumptions

- **Attacker:** Former collaborator with a cached id; delayed worker (7.4).
- **Trust:** Local share map.
**Forbidden outcome:** Revoked share still reads the note

**Authorized scope:** `labs/11/11-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable capstone.py still reads.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: read after revoke still body.

## Vulnerable fixture (local)

```python
NOTES={'n1': {'tenant': 'A', 'body': 'secret'}}
GRANTS={('n1', 'B')}
def reset():
    GRANTS.clear(); GRANTS.add(('n1', 'B'))
def revoke(nid, tenant):
    pass
def read(nid, tenant):
    n = NOTES[nid]
    return n['body']
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Grant not consulted after revoke. |
| Impact | Ex-collaborator confidentiality fail. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/11/11-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Clinic: revoke a guardian.

## Non-goals

No live-target instructions. Synthetic data only.
