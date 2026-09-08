# Lab 6.7 — export has a resource account

**Module:** `6.7`
**Authorized scope:** this directory only. Local course fixture. No public load tests.
**Invariant:** `allow(4)` is false. `allow(3)` may be true.
**Root cause class:** no resource account
**Non-goals:** live RPS against public hosts, CAPTCHA cookbooks.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/6.7/6.7-lab`, then run `git restore --source=HEAD -- labs/6.7/6.7-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`allow` always returns true. Forbidden outcome: fourth export allowed.

## Structural fix

`allow(n)` is `n <= 3` on the export action.

## Verify

```
python3 -m pytest labs/6.7/6.7-lab/tests --impl vulnerable
python3 -m pytest labs/6.7/6.7-lab/tests --impl fixed
```

The first command must fail on `allow(4)`. The second must pass. Honest `allow(3)` may pass on both.

## Operate

Signal: `quota_denied`. Do not log CSV bodies.

## Transfer

Clinic bulk-export. Prompt only.
