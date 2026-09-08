# Lab 9.2 — eval on user input must not be approved

**Module:** `9.2`
**Authorized scope:** this directory only. Local course fixture. No live GitHub orgs, no weaponized eval.
**Invariant:** `review_ok("x = eval(user)")` is false. Honest diffs without eval may pass.
**Root cause class:** visual plausibility / always-approve
**Non-goals:** complete review oracle, live exploits. The substring check is a **lab stand-in**.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/9.2/9.2-lab`, then run `git restore --source=HEAD -- labs/9.2/9.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`review_ok` always returns true. Forbidden outcome: eval on user input approved in review.

## Structural fix

Return false when `'eval('` is in the diff. Name the residual: this is not a complete oracle.

## Verify

```
python3 -m pytest labs/9.2/9.2-lab/tests --impl vulnerable
python3 -m pytest labs/9.2/9.2-lab/tests --impl fixed
```

The first command must fail on eval approval. The second must pass. Honest diffs without eval may pass on both.

## Operate

Signal: `review_block_eval`. Do not log payloads.

## Transfer

Clinic eval in a report template. Prompt only.
