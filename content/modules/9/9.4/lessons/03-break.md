# 9.4 — Automated analysis and tool orchestration (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
**Forbidden outcome:** Unmapped HIGH finding allows ship

**Authorized scope:** `labs/9.4/9.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable sast.py ships anyway.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: ship_ok([HIGH], {}) True.

## Vulnerable fixture (local)

```python
def ship_ok(findings, mappings):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Scanner output not joined to 9.1. |
| Impact | Unknown HIGH in prod. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/9.4/9.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

SCA CVE vs actually called function.

## Non-goals

No live-target instructions. Synthetic data only.
