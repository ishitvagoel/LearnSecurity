# 3.3 — Secure architecture patterns (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
**Forbidden outcome:** App DB role can SELECT another tenant's rows

**Authorized scope:** `labs/3.3/3.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable roles.py allows app to read tA as tB.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: app role can_select other tenant.

## Vulnerable fixture (local)

```python
def can_select(role: str, tenant: str, note_tenant: str) -> bool:
    return role == "app"
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | One omnipotent DB user shared by app and migrate. |
| Impact | Forgot WHERE becomes a breach. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/3.3/3.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Serverless function with a shared “admin” connection string.

## Non-goals

No live-target instructions. Synthetic data only.
