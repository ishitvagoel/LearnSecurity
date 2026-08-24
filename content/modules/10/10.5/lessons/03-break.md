# 10.5 — Logging, detection, incident response, recovery, maintenance (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
**Forbidden outcome:** Incident closed without recovery evidence

**Authorized scope:** `labs/10.5/10.5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable ir.py closes anyway.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: close_incident({recovery:'todo', logs:'ok'}) True.

## Vulnerable fixture (local)

```python
def close_incident(inc):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Close on detection quality. |
| Impact | System still broken or attacker still in. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/10.5/10.5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Ransomware restore vs note-level integrity.

## Non-goals

No live-target instructions. Synthetic data only.
