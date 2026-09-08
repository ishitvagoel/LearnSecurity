# Lab 4.1 — leftover session after delete

**Module:** `4.1`
**Authorized scope:** this directory only. Local course fixture. No live IdPs.
**Invariant:** After `delete_user("alice")`, `session_valid("alice")` is false. Lifecycle is complete mediation over time.
**Root cause class:** trust / time (authentication artifact outlived the subject)
**Non-goals:** live SSO, real cookies, real HR data.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/4.1/4.1-lab`, then run `git restore --source=HEAD -- labs/4.1/4.1-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`delete_user` adds the user to `DELETED` but leaves `SESSIONS["alice"]` true. `session_valid` still returns that session. Forbidden outcome: deleted user's leftover session still authenticates.

## Structural fix

Pop the session in `delete_user` and treat `DELETED` as deny in `session_valid`. Honest session still works before delete.

## Verify

```
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

From repo root:

```
python3 -m pytest labs/4.1/4.1-lab/tests --impl vulnerable
python3 -m pytest labs/4.1/4.1-lab/tests --impl fixed
```

The first command must fail. The second must pass.

## Operate

Signal: `session_after_delete` with user id; never a note body. Mass revoke; rotate if JWTs self-verify.

## Transfer

Clinic departing clinician. Prompt only; do not leave this directory.
