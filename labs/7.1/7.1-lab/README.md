# Lab 7.1 — extra keys are not writable fields

**Module:** `7.1`
**Authorized scope:** this directory only. Local course fixture. No public API attacks.
**Invariant:** `apply(user, {"is_admin": true})` leaves `is_admin` false. Honest `display_name` may change.
**Root cause class:** binder maps any key onto the entity
**Non-goals:** live targets, OpenAPI cookbooks as the control.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/7.1/7.1-lab`, then run `git restore --source=HEAD -- labs/7.1/7.1-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`apply` copies every key from `body` onto `user`. Forbidden outcome: PATCH sets `is_admin`.

## Structural fix

Copy only keys in `ALLOWED = {"display_name"}`. Extra keys are skipped.

## Verify

```
python3 -m pytest labs/7.1/7.1-lab/tests --impl vulnerable
python3 -m pytest labs/7.1/7.1-lab/tests --impl fixed
```

The first command must fail on `is_admin`. The second must pass. Honest `display_name` may pass on both.

## Operate

Signal: `unknown_field_rejected`. Do not log the PATCH body.

## Transfer

Clinic PATCH `is_staff`. Prompt only.
