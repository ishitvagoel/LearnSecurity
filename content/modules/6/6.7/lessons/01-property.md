# 6.7 — Resource abuse, automation, and availability (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
**Mechanism (not the property):** nginx rate limit without identity is shared-fate.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.7 |
|---|---|
| Root cause | No resource account. |
| Preconditions | allow(4) True. |
| Impact (1.1 cell) | Availability and cost; secondary confidentiality via extra copies. — Cost/DoS; extra CSV copies of bodies. |
| Prevention | Quota + authz + maybe queue. |
| Detection | export_denied_quota. |
| Recovery | Disable token; bill anomaly. |

## Framework defaults vs application guarantees

nginx rate limit without identity is shared-fate.

## Mechanism limits and bypasses

Per-IP limits punish NAT; need per-subject.

New accounts; GraphQL aliases (7.1).

## Residual risk

Legitimate burst — owned exception.

## Practice

Budget: CPU, bytes, paid API calls.

Run `labs/6.7/6.7-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Notification fan-out; search complexity.

Clinic bulk-export patients.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Quota errors must be readable; do not trap keyboard users in a spinner that retries (amplifying load).
