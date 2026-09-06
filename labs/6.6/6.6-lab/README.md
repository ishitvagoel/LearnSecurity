# Lab 6.6 — an invite token is a one-shot consume

**Module:** `6.6`
**Authorized scope:** this directory only. Local course fixture. No live mail.
**Invariant:** `accept('t1')` is true once; the second call is false.
**Root cause class:** token never marked used
**Non-goals:** threaded race harnesses, live invite links.

## Reset

Re-run pytest (`conftest` calls `reset()`). Optional: `git checkout -- labs/6.6/6.6-lab`.

## Vulnerable behavior (local only)

`accept` always returns true. Forbidden outcome: invite token accepted twice.

## Structural fix

Record the token as used when the first accept succeeds. Distinct tokens remain independent.

## Verify

```
python3 -m pytest labs/6.6/6.6-lab/tests --impl vulnerable
python3 -m pytest labs/6.6/6.6-lab/tests --impl fixed
```

The first command must fail on second-accept. The second must pass. First accept of `t1` may pass on both.

## Operate

Signal: `invite_replay_denied`. Do not log tokens.

## Transfer

Clinic invite-guardian token. Prompt only.
