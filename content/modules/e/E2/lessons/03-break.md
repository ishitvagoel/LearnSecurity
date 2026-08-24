# E2 — Advanced browser and edge security (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
**Forbidden outcome:** Report-Only CSP counted as isolation enforcement

**Authorized scope:** `labs/E2/e2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable csp.py treats Report-Only as enforcement.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Report-Only header => enforced True.

## Vulnerable fixture (local)

```python
def isolation_enforced(headers):
    return 'Content-Security-Policy-Report-Only' in headers or 'Content-Security-Policy' in headers
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Report-Only mistaken for on. |
| Impact | XSS still runs; dashboard looks green. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/E2/e2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Trusted Types, COOP/COEP.

## Non-goals

No live-target instructions. Synthetic data only.
