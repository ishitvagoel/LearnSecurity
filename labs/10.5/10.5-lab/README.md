# Lab 10.5 — a green SIEM is not recovery

**Module:** `10.5`
**Authorized scope:** this directory only. Local course fixture. No live incident systems or third-party SIEMs.
**Invariant:** `close_incident({"recovery": "todo", "logs": "ok"})` is false. Logs must not contain `note_body`. Honest recovery+safe logs may close.
**Root cause class:** close on detection quality
**Non-goals:** PagerDuty as recovery; claiming Gate 10 or M4.

The `recovery` field is a **teaching stand-in** for restore-test evidence. `note_body` in logs is the 3.1/5.1/8.5 spiral: observability must not become a second note store.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/10.5/10.5-lab`, then run `git restore --source=HEAD -- labs/10.5/10.5-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`close_incident` always returns true. Forbidden outcomes: incident closed without recovery evidence; note body in logs.

## Structural fix

Require `recovery == "done"` and `'note_body' not in logs`.

## Verify

```
python3 -m pytest labs/10.5/10.5-lab/tests --impl vulnerable
python3 -m pytest labs/10.5/10.5-lab/tests --impl fixed
```

The first command must fail the forbidden tests. The second must pass. Honest recovery+safe logs may pass on both.

## Operate

Signal: `incident_closed_without_recovery`. Do not log note bodies or session tokens. Do not claim Gate 10 or M4.

## Transfer

Clinic: close ticket when SIEM is green. Ransomware restore vs note-level integrity. Prompt only.
