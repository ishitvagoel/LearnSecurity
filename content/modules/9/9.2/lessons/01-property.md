# 9.2 — Secure code review (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
**Mechanism (not the property):** GitHub “rulesets” do not read eval.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 9.2 |
|---|---|
| Root cause | Visual plausibility. |
| Preconditions | review_ok('x=eval(user)') True. |
| Impact (1.1 cell) | Integrity of the change. — Interpreter confusion shipped (6.1). |
| Prevention | Reject eval-on-user; look at data flow, authz, state, config. |
| Detection | review_bot as aid not oracle (9.4). |
| Recovery | Revert. |

## Framework defaults vs application guarantees

GitHub “rulesets” do not read eval.

## Mechanism limits and bypasses

Review misses generated code (E1).

eval hidden in helper; framework magic.

## Residual risk

Unknown unknowns — 9.3 tests.

## Practice

Review the lab vulnerable file as a PR.

Run `labs/9.2/9.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Terraform, GitHub Actions yaml.

Clinic: eval in a report template.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Review UI must be keyboard accessible; otherwise people rubber-stamp from a phone.
