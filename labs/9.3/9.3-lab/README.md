# Lab 9.3 — HTTP 200-only is not a security test

**Module:** `9.3`
**Authorized scope:** this directory only. Local course fixture. No live apps or public fuzzing.
**Invariant:** `{status_asserted: True}` is not a security test. Honest rows that name `forbidden_outcome` (and may also assert status) may count.
**Root cause class:** happy path as assurance
**Non-goals:** WSTG cookbooks as the definition of shape; claiming Gate 9.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/9.3/9.3-lab`, then run `git restore --source=HEAD -- labs/9.3/9.3-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`is_security_test` is true when `status_asserted` is set. Forbidden outcome: HTTP 200-only test counted as a security test.

## Structural fix

Require `forbidden_outcome`. Status alone is a product test.

## Verify

```
python3 -m pytest labs/9.3/9.3-lab/tests --impl vulnerable
python3 -m pytest labs/9.3/9.3-lab/tests --impl fixed
```

The first command must fail on the 200-only row. The second must pass. Honest `{forbidden_outcome: True, status_asserted: True}` may pass on both.

## Operate

Signal: `security_suite_missing_isolation`. Do not log bodies. Do not claim Gate 9.

## Transfer

Clinic `test_get_patient_200`. Prompt only.
