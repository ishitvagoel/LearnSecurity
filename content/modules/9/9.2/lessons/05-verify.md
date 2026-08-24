# 9.2 — Secure code review (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | eval on user input approved in review |
| Failure | Fail closed: Reject eval-on-user; look at data flow, authz, state, config |

Lab tests: `test_property.py` under `labs/9.2/9.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `eval on user input approved in review`
- `--impl fixed`: **pass**

eval on user rejected.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Terraform, GitHub Actions yaml.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
