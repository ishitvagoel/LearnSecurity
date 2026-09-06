# Lab 3.4 — product cap on the write path

**Module:** `3.4`
**Authorized scope:** this directory only. Local course fixture. No public APIs.
**Invariant:** A note share grant cannot be applied enough times to exceed the product cap of 5. Abuse is a logic invariant. HTML `max` is not enforcement.
**Root cause class:** trust (policy only in the UI)
**Non-goals:** live tenants, real member emails, weaponized bots.

## Reset

`add_share` tests call `reset()` via conftest. Re-run pytest. Optional: `git checkout -- labs/3.4/3.4-lab` if you edited fixtures.

## Vulnerable behavior (local only)

`add_share` always increments. Eight calls yield `last == 8`. Forbidden outcome: share grants exceed the product cap of 5.

## Structural fix

If `_n >= 5`, return `_n` without incrementing. Five honest shares still succeed. The sixth does not increment.

## Verify

```
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

From repo root:

```
python3 -m pytest labs/3.4/3.4-lab/tests --impl vulnerable
python3 -m pytest labs/3.4/3.4-lab/tests --impl fixed
```

The first command must fail. The second must pass.

## Operate

CI/signal: `share_cap_denied` with note id and count; never a note body. Trim extras if they landed. Announce “share limit reached” (WCAG 4.1.3) without treating that as the cap.

## Transfer

Clinic max 3 guardians; invite one-use (6.6); export quota (6.7). Prompt only; do not leave this directory.
