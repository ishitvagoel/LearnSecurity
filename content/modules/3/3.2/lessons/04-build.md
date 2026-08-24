# 3.2 — Threat modeling (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
threats_from_scan always includes cross-tenant-read.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
ALWAYS = ["cross-tenant-read", "hostile-browser", "stolen-worker"]

def threats_from_scan(scanner_green: bool) -> list[str]:
    return list(ALWAYS)
```

## Why this restores the cell

Seed mandatory threats; scanner findings are extra, not the set.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

STRIDE stickers on a DFD are not a model without invalidation conditions.

LINDDUN is valuable for 5.1; it still won’t list IDOR for you automatically.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Add webhooks (7.3): which new threats?

## Residual risk

Unknown unknowns — review triggers exist for that.
