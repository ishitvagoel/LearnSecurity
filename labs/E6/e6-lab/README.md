# Lab E6 — an exception without owner and review is not accepted

**Module:** `E6`
**Authorized scope:** this directory only. Local course fixture. No live PSIRT.
**Invariant:** `accept_exception({"owner": "", "review_by": None})` is false. A complete record may be accepted.
**Root cause class:** oral acceptance treated as a register row
**Non-goals:** SAMM score as the exception; CISA pledge as Gate 7; live disclosure.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/E6/e6-lab`, then run `git restore --source=HEAD -- labs/E6/e6-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`accept_exception` always returns true. Forbidden outcome: incomplete exception accepted.

## Structural fix

Require `owner`, `review_by`, and `wcag_checked`.

## Verify

```
python3 -m pytest labs/E6/e6-lab/tests --impl vulnerable
python3 -m pytest labs/E6/e6-lab/tests --impl fixed
```

The first command must fail `test_exception_needs_owner_review_and_wcag`. The second must pass. Honest complete exceptions may pass on both.

## Operate

Signal: `exception_incomplete_denied`. Do not log residual-risk narratives that contain secrets.

## Transfer

Clinic “HIPAA exception.” Procurement questionnaire vs this record. Prompt only.
