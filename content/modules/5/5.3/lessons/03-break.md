# 5.3 — Key and secret lifecycle (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
**Forbidden outcome:** Hardcoded default API key still authenticates after rotation

**Authorized scope:** `labs/5.3/5.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable secrets.py still honors the default.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: auth(hardcoded) True while current is rotated-now.

## Vulnerable fixture (local)

```python
DEFAULT='sk-lab-hardcoded'
def auth(presented, current=None):
    return presented == DEFAULT or presented == current
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Default credential never invalidated. |
| Impact | Silent backdoor equal to production admin if copied. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/5.3/5.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.

## Non-goals

No live-target instructions. Synthetic data only.
