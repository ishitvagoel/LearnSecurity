# 10.1 — Secure software lifecycle and security culture (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
**Forbidden outcome:** Merge without a threat-model identifier

**Authorized scope:** `labs/10.1/10.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable sdl.py merges without TM.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: merge_ok({}) True.

## Vulnerable fixture (local)

```python
def merge_ok(pr):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Security as a later phase. |
| Impact | Surfaces without 3.2. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/10.1/10.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Exception path (E6).

## Non-goals

No live-target instructions. Synthetic data only.
