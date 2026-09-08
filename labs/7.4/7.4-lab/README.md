# Lab 7.4 — leftover user session is not worker identity

**Module:** `7.4`
**Authorized scope:** this directory only. Local course fixture. No live brokers.
**Invariant:** `exporter({"user_session": "alice", "service": None})` is `None`. Honest `service=worker-sc` may succeed.
**Root cause class:** ambient user context in a system worker
**Non-goals:** live Redis/RabbitMQ, zero-trust product cookbooks.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/7.4/7.4-lab`, then run `git restore --source=HEAD -- labs/7.4/7.4-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`exporter` returns `user_session` if present. Forbidden outcome: exporting under alice’s session.

## Structural fix

Return `"worker-sc"` only when `service == "worker-sc"`. Leftover sessions are ignored.

## Verify

```
python3 -m pytest labs/7.4/7.4-lab/tests --impl vulnerable
python3 -m pytest labs/7.4/7.4-lab/tests --impl fixed
```

The first command must fail on leftover `user_session`. The second must pass. Honest `worker-sc` may pass on both.

## Operate

Signal: `worker_identity_wrong`. Do not log session cookies.

## Transfer

Clinic batch-export worker. Prompt only.
