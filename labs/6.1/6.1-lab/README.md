# Lab 6.1 — export name is data, not shell grammar

**Module:** `6.1`
**Authorized scope:** this directory only. Local course fixture. No live OS commands.
**Invariant:** `argv_for_list` returns a program-plus-args list. It must not invoke a shell.
**Root cause class:** data mixed into shell grammar
**Non-goals:** live command execution, metacharacter cookbooks, argument-injection payloads.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/6.1/6.1-lab`, then run `git restore --source=HEAD -- labs/6.1/6.1-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`argv_for_list` returns `sh -c` with a concatenated name. Forbidden outcome: user-controlled name executed via a shell string. Tests check argv **shape** only.

## Structural fix

Return `['ls', '--', name]`. `uses_shell` is false. `--` is the extra slot that names argument injection as a residual, not an executed case.

## Verify

```
python3 -m pytest labs/6.1/6.1-lab/tests --impl vulnerable
python3 -m pytest labs/6.1/6.1-lab/tests --impl fixed
```

The first command must fail on the shell-argv tests. The second must pass.

## Operate

Signal: `child_process_anomaly`. Do not log PHI filenames.

## Transfer

Clinic export-to-CSV filename. Prompt only.
