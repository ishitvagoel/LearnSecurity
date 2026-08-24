# 5.3 — Key and secret lifecycle (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
auth(hardcoded, current=rotated) False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def auth(presented, current=None):
    return bool(current) and presented == current
```

## Why this restores the cell

Generate unique secrets; rotate; refuse known defaults; never commit.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

pydantic Settings reading .env does not rotate anything.

Vault without rotation policy is a new hard-to-scan dump.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.

## Residual risk

PQC migration is a plan, not this test.
