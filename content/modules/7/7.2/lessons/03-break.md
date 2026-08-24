# 7.2 — Object, property, and function security (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
**Forbidden outcome:** Member resolves secret_internal

**Authorized scope:** `labs/7.2/7.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable field.py allows member internal.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: resolve('member','secret_internal') True.

## Vulnerable fixture (local)

```python
def resolve(role, field):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Serializer dumps the ORM object. |
| Impact | Internal secret or PII extra. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/7.2/7.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Bulk update; search highlighting leaking snippets.

## Non-goals

No live-target instructions. Synthetic data only.
