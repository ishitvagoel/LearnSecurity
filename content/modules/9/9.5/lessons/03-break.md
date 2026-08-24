# 9.5 — Authorized assessment, reporting, and remediation (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
**Forbidden outcome:** Finding closed without retest

**Authorized scope:** `labs/9.5/9.5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable pentest.py closes anyway.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: close_finding({retest: None}) True.

## Vulnerable fixture (local)

```python
def close_finding(f):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Closure on intent. |
| Impact | Vulnerable still there; false residual. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/9.5/9.5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

KEV vs internal-only.

## Non-goals

No live-target instructions. Synthetic data only.
