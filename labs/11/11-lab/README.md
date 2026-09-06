# Lab 11 — revoke is not an event, it is mediation

**Module:** `11`
**Authorized scope:** this directory only. Local course fixture. No live tenants, clinics, or third-party notes apps.
**Invariant:** after `revoke("n1", "B")`, `read("n1", "B")` is `None`. Owner `A` may still read. Share may read before revoke.
**Root cause class:** grant not consulted after revoke
**Non-goals:** a green scanner as the 13 artifacts; claiming Gate 11 or M5.

The in-memory `GRANTS` set is a **teaching stand-in** for 1.2 complete mediation over time (2.4 / 4.1 / 4.4). It is not SecureCollab production authorization.

## Reset

Re-run pytest. Optional: `git checkout -- labs/11/11-lab`.

## Vulnerable behavior (local only)

`revoke` is a no-op and `read` returns the body. Forbidden outcome: revoked share still reads the note.

## Structural fix

Consult owner-or-grant on every `read`. `revoke` removes the grant.

## Verify

```
python3 -m pytest labs/11/11-lab/tests --impl vulnerable
python3 -m pytest labs/11/11-lab/tests --impl fixed
```

The first command must fail the revoke test. The second must pass. Honest owner-after-revoke and share-before-revoke may pass on both.

## Operate

Signal: `revoked_share_read_denied`. Do not log note bodies. Do not claim Gate 11 or M5.

## Transfer

Clinic: revoke a guardian. Prompt only.
