# 3.2 — Threat modeling (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
**Mechanism (not the property):** STRIDE stickers on a DFD are not a model without invalidation conditions.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 3.2 |
|---|---|
| Root cause | Tool output substituted for thinking. |
| Preconditions | scan_green=True; model copies it. |
| Impact (1.1 cell) | Integrity of the *assurance story* — missing threats are untested 1.1 cells. — No test for 1.2; residual unowned. |
| Prevention | Seed mandatory threats; scanner findings are extra, not the set. |
| Detection | CI fails if required threat ids missing. |
| Recovery | Add the threat, tests, owner; do not back-date. |

## Framework defaults vs application guarantees

STRIDE stickers on a DFD are not a model without invalidation conditions.

## Mechanism limits and bypasses

LINDDUN is valuable for 5.1; it still won’t list IDOR for you automatically.

Moving threats to “accepted” without residual.

## Residual risk

Unknown unknowns — review triggers exist for that.

## Practice

List three threats that remain if every CVE is patched.

Run `labs/3.2/3.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Add webhooks (7.3): which new threats?

Clinic SMS reminders.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
