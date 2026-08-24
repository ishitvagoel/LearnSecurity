# 10.5 — Logging, detection, incident response, recovery, maintenance (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
recovery todo => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def close_incident(inc):
    logs = inc.get('logs', '')
    return inc.get('recovery') == 'done' and 'note_body' not in logs
```

## Why this restores the cell

Require recovery evidence (restore test, revoke list).

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

PagerDuty is not recovery.

Observability pipeline as exfil (3.1).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Ransomware restore vs note-level integrity.

## Residual risk

Some incidents never get perfect forensic certainty — say so.
