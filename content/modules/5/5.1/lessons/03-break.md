# 5.1 — Data lifecycle and privacy engineering (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
**Forbidden outcome:** Analytics copy still holds note body after account deletion

**Authorized scope:** `labs/5.1/5.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable lifecycle.py leaves analytics body.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: delete_account pops NOTES only.

## Vulnerable fixture (local)

```python
NOTES={'alice':'secret'}
ANALYTICS={'alice':'secret'}
def reset():
    NOTES.clear(); NOTES['alice']='secret'
    ANALYTICS.clear(); ANALYTICS['alice']='secret'
def delete_account(user):
    NOTES.pop(user, None)
def body_retained(user):
    return ANALYTICS.get(user)
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Secondary copy not in the deletion graph. |
| Impact | Bodies persist after the person left. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/5.1/5.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

CSV export to a partner; clinic-booking card PHI.

## Non-goals

No live-target instructions. Synthetic data only.
