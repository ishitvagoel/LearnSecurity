# 9.4 — Automated analysis and tool orchestration (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
**Mechanism (not the property):** GitHub code scanning default is not your policy.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 9.4 |
|---|---|
| Root cause | Scanner output not joined to 9.1. |
| Preconditions | ship_ok([HIGH], {}) True. |
| Impact (1.1 cell) | Integrity of release decision. — Unknown HIGH in prod. |
| Prevention | Block unmapped HIGH; allow mapped+accepted with E6. |
| Detection | unmapped_high count. |
| Recovery | Map or fix; do not suppress silently. |

## Framework defaults vs application guarantees

GitHub code scanning default is not your policy.

## Mechanism limits and bypasses

False positives exist — mapping is how you record that.

Severity downgrade without evidence.

## Residual risk

Blind spots (authz logic) — 9.2/9.3.

## Practice

Triage one HIGH: reachability, map, or exception.

Run `labs/9.4/9.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

SCA CVE vs actually called function.

Clinic: 50 unmapped HIGHs.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Triage UI must be usable; otherwise people mass-suppress.
