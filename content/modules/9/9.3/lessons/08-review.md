# Review status-only is_security_test like a pull request

**Kind:** code-review
**Loop step:** Review

Intended findings live only in the answer-key folder — not here. Do not open that file until your review has been evaluated.

## What you are reviewing

A colleague ships the notes app’s security-suite gate. Review `labs/9.3/9.3-lab/vulnerable/` as that change. Your job is not to count suspicious lines. Reconstruct whether `{status_asserted: True}` still counts as a security test, compare that with the rule, and write changes a developer can verify.

Start at `is_security_test` and the 200-only row, not at a scanner color or a coverage screenshot. The check you already ran (`test_http_200_only_is_not_a_security_test`) is the rule test. A comment “will add isolation later” is not.

## Picture: assert r.status_code==200 only

Start with this seeded smell: **`assert r.status_code==200` only**. Label it rule, tool, or false comfort before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|200-only counted as security| Property["Rule - good if tested"]
  Q -->|line coverage| Mechanism[Tool - coverage]
  Q -->|testing-guide tick| False[False comfort]
```

Start from what must stay true (200-only is not a security test). Everything that is not a named what must not happen at that call is a candidate happy-path path. A coverage screenshot without that check is the same problem, not a different kind of finding.

Fuzz with no named bad result is leftover 9.5. Field grain is 7.2. Do not skip `test_http_200_only_is_not_a_security_test`. Do not claim a later gate. Do not treat coverage percent as the isolation check.

## Seeded smells (label them yourself)

- `assert r.status_code==200` only
- No cross-company test
- Security suite empty
- Chaos / fuzz with no who-is-allowed named bad result

Also reject: live targets; closing findings without re-running `test_http_200_only_is_not_a_security_test`; keys in learner notes; claiming a later gate; treating coverage percent as the isolation check.

## Common mix-ups

- Coverage is security
- Fuzzing finds all who-is-allowed bugs
- Snapshot tests are isolation tests
- A draft testing guide is the current pin
- A later gate follows from a green suite

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false comfort, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_http_200_only_is_not_a_security_test`. Do not open the keys file.

## Use it somewhere new

Clinic change that “added test_get_patient_200 as the security test” is an incomplete review of whether 200-only still counts as security. Name the independent falsehood that would still keep 200-only from counting as security.

## Can people still use it

A failing security test must say what must not happen in the assertion message, not only “assert False.”

## What this page is not doing

Do not merge by adding a comment “will add isolation later.” That comment is leftover without an owner. Do not fuzz a public host to prove the finding.
