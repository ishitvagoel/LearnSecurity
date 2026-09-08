# Lab 8.5 — a crash report must not include the note body

**Module:** `8.5`
**Authorized scope:** this directory only. Local course fixture. No live Crashlytics, Play Console, or public apps.
**Invariant:** `'secret' not in str(crash_report('secret'))`. Honest crashes may still include a stack key.
**Root cause class:** report builder copies the note body into telemetry
**Non-goals:** vendor DLP cookbooks, live reverse engineering, real PII.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/8.5/8.5-lab`, then run `git restore --source=HEAD -- labs/8.5/8.5-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`crash_report` returns `{'stack': 'npe', 'note': note_body}`. Forbidden outcome: crash JSON contains the note body.

## Structural fix

Return `'note': '[redacted]'` (lab stand-in). Do not copy `note_body` into the payload.

## Verify

```
python3 -m pytest labs/8.5/8.5-lab/tests --impl vulnerable
python3 -m pytest labs/8.5/8.5-lab/tests --impl fixed
```

The first command must fail on the body-present test. The second must pass. Honest stack-present may pass on both.

## Operate

Signal: `crash_body_redacted`. Do not log note bodies or vendor payloads.

## Transfer

Clinic crash with a synthetic patient name. Prompt only.
