# 3.2 — Threat modeling (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
**Forbidden outcome:** Green scanner produces an empty SecureCollab threat model

**Authorized scope:** `labs/3.2/3.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable model.py returns [] when scan is green.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: scan_green=True; model copies it.

## Vulnerable fixture (local)

```python
def threats_from_scan(scanner_green: bool) -> list[str]:
    return [] if scanner_green else ["generic"]
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Tool output substituted for thinking. |
| Impact | No test for 1.2; residual unowned. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/3.2/3.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Add webhooks (7.3): which new threats?

## Non-goals

No live-target instructions. Synthetic data only.
