# Lab 0.2 — a quiz score is not a 1.2 cell

**Module:** `0.2`
**Authorized scope:** this directory only. Local course fixture.
**Invariant:** `quiz_score_grants_phase1_skip(100)` is false. A low score also does not skip.
**Root cause class:** a number treated as a capability
**Non-goals:** NICE work-role fluency as Gate 1; LMS percentage as ASVS.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/0.2/0.2-bridge`, then run `git restore --source=HEAD -- labs/0.2/0.2-bridge` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

Score ≥ 80 grants a Phase 1 skip. Forbidden outcome: quiz score used as authorization to skip 1.2 / Gate 1.

## Structural fix

Diagnostics never grant 1.2 cells or skip Gate 1 evidence. Tooling-bridge skips stay a separate decision.

## Verify

```
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
python3 -m pytest labs/0.2/0.2-bridge/tests --impl fixed
```

The first command must fail `test_high_quiz_score_is_not_authorization`. The second must pass. Honest low-score tests may pass on both.

## Operate

Signal: `phase1_skip_denied`. Audit skipped-module lists. Do not back-date Gate 1.

## Transfer

Vendor cert used to skip a threat-model review. Clinic onboarding quiz. Prompt only.
