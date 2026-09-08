# Lab 9.5 — a PDF is not a retest

**Module:** `9.5`
**Authorized scope:** this directory only. Local course fixture. No live-target pentests, no public or third-party systems.
**Invariant:** `close_finding({"retest": None})` is false. Honest `{retest: "pass"}` may close.
**Root cause class:** closure on intent
**Non-goals:** live WSTG campaigns; claiming Gate 9.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/9.5/9.5-lab`, then run `git restore --source=HEAD -- labs/9.5/9.5-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`close_finding` always returns true. Forbidden outcome: finding closed without retest.

## Structural fix

Require `retest == "pass"`.

## Verify

```
python3 -m pytest labs/9.5/9.5-lab/tests --impl vulnerable
python3 -m pytest labs/9.5/9.5-lab/tests --impl fixed
```

The first command must fail on `retest None`. The second must pass. Honest `retest pass` may pass on both.

## Operate

Signal: `finding_closed_without_retest`. Do not log bodies. Do not claim Gate 9.

## Transfer

Clinic pentest PDF shelf. Prompt only.
