# A broken no-op revoke must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

A green capstone scanner does not consult the grant on the next read. HTTP 200 on DELETE is a status. After revoke, B has to read None, A has to still read, and B before revoke has to still read. On the broken files B-after-revoke still returns the body. On the repaired files it does not. Do not hit live tenants.

## Picture: a broken no-op revoke must fail the check

A passing-test tally can still hide that B after revoke still reads.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: B after revoke]
  X["repaired files --impl fixed"] --> P[Must pass: deny]
```

If both pass, you are not looking at B after revoke.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | B after revoke → None; broken files must fail |
| Normal | A after revoke → body (may pass on both) |
| Normal | B before revoke → body (may pass on both) |
| Not claimed | live clinic; an assurance gate; worker or cache wipe |

The test `test_revoked_share_cannot_read` is there so no-op `revoke` still fails. `conftest.py` calls `reset()` so grant state does not leak.

The owner after revoke, and B before revoke, may pass on both sides. You still have to deny B after revoke. If the broken files do not fail `test_revoked_share_cannot_read`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/11/11-lab/tests --impl vulnerable
python3 -m pytest labs/11/11-lab/tests --impl fixed
```

A `revoke` heading in a README is not `read("n1", "B")` after `revoke("n1", "B")`. This practice never opens a live host.

## What the tests do not prove

- Worker leftover session is gone
- Phone cache is wiped
- Copies already sent are gone
- Access-rights change in the same session without signing in again
- This page does not finish the capstone check-in

## Practice

Do not treat a grep for `revoke` in a README as the check. Call `read("n1", "B")` after `revoke("n1", "B")`.

## Use it somewhere new

Asserting “revoke returned 200” is not this check. Do not use a live clinic system.

## What this page is not doing

Do not treat a live tenant screenshot as proof. Do not log note bodies. Answer keys are not on this site. This page does not mark you as finished.
