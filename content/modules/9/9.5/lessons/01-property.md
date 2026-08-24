# 9.5 — Authorized assessment, reporting, and remediation (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
**Mechanism (not the property):** Jira Done is not retest.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 9.5 |
|---|---|
| Root cause | Closure on intent. |
| Preconditions | close_finding({retest: None}) True. |
| Impact (1.1 cell) | Integrity of the fix loop. — Vulnerable still there; false residual. |
| Prevention | Require retest of the same cell. |
| Detection | closed_without_retest metric. |
| Recovery | Reopen. |

## Framework defaults vs application guarantees

Jira Done is not retest.

## Mechanism limits and bypasses

CVSS 9.8 vs business priority — you still judge.

Retest different endpoint.

## Residual risk

Unknown variants — hunt (same root cause).

## Practice

Write a three-line report: cause, impact, retest cmd.

Run `labs/9.5/9.5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

KEV vs internal-only.

Clinic pentest PDF shelf.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Reports used by engineers must be readable (structure, not color-only severity).
