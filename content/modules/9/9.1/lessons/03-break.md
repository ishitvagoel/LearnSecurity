# 9.1 — Verification requirements and traceability (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
**Forbidden outcome:** Status-only row counted as AUTHZ-1 coverage

**Authorized scope:** `labs/9.1/9.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable trace.py treats status as coverage.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: covered True when asserts_isolation False.

## Vulnerable fixture (local)

```python
def covered(req_id, tests):
    return any(t.get('req') == req_id for t in tests)
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Status without evidence. |
| Impact | Ship 1.2 holes with a green gate. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/9.1/9.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

MASVS STORAGE for 8.2.

## Non-goals

No live-target instructions. Synthetic data only.
