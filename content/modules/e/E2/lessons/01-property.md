# E2 — Advanced browser and edge security (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
**Mechanism (not the property):** Helmet defaults may be report-only in some templates.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For E2 |
|---|---|
| Root cause | Report-Only mistaken for on. |
| Preconditions | Report-Only header => enforced True. |
| Impact (1.1 cell) | Integrity of the browser policy mechanism (2.3 layered with 6.2). — XSS still runs; dashboard looks green. |
| Prevention | Detect enforcing header; don’t claim isolation otherwise. |
| Detection | csp_mode metric. |
| Recovery | Flip to enforcing after fix 6.2. |

## Framework defaults vs application guarantees

Helmet defaults may be report-only in some templates.

## Mechanism limits and bypasses

CSP does not replace encoding (6.2) or CSRF (6.3).

JSONP, trusted-types not deployed, edge cache stripping headers (2.2).

## Residual risk

XS-Leaks — named as elective depth.

## Practice

Classify each header as enforce vs signal.

Run `labs/E2/e2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Trusted Types, COOP/COEP.

Clinic: Report-Only as “HIPAA header.”

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
