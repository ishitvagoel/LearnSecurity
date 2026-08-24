# 3.4 — Business logic and abuse-resistant design (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
**Mechanism (not the property):** HTML max=5 is not enforcement.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 3.4 |
|---|---|
| Root cause | Policy only in the UI. |
| Preconditions | add_share without cap. |
| Impact (1.1 cell) | Integrity of the share policy; availability of the owner’s threat model (too many readers). — Unbounded readers; 1.2 matrix explodes. |
| Prevention | Check count in the write path; reject 6th. |
| Detection | share_cap_denied metric; anomaly on one note. |
| Recovery | Trim extra grants; notify owner. |

## Framework defaults vs application guarantees

HTML max=5 is not enforcement.

## Mechanism limits and bypasses

Cap on /share but not on /import or GraphQL.

Parallel requests before commit (needs transaction/lock — 2.4).

## Residual risk

Legitimate teams >5 need an owned exception (E6).

## Practice

State machine: shares=0..5; 6th denied.

Run `labs/3.4/3.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Invite tokens (6.6) and export quotas (6.7).

Clinic: max 3 guardians per child.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Error “share limit reached” must be programmatically announced (WCAG 4.1.3), not only a red border.
