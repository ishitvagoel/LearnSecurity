# A broken no-op revoke must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Until you can fail it, it is still a slogan

“Capstone scanner green” is not evidence. “DELETE returned 200” is a tool observation. The check is: B after revoke is None, A after revoke still reads, B before revoke still reads. The B-after-revoke observation must be **false** on the broken files (returns the body) and **true** on the repaired files. Do not hit live tenants.

## Picture: a broken no-op revoke must fail the check

A check that only counts passing tests can still look green while B after revoke still reads. The broken files have to fail that case. The repaired files have to pass it.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: B after revoke]
  X["repaired files --impl fixed"] --> P[Must pass: deny]
```

If both pass, the test is not looking at B after revoke. If both fail, the fix is not structural or the check is wrong.

## Four modes, even for a share dict

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | B after revoke → None; broken files must fail |
| Normal | A after revoke → body (may pass on both) |
| Normal | B before revoke → body (may pass on both) |
| Not claimed | live clinic; an assurance gate; worker or cache wipe |

The file is `labs/11/11-lab/tests/test_property.py`. The test `test_revoked_share_cannot_read` exists so no-op `revoke` cannot count as a pass. `conftest.py` calls `reset()` so grant state does not leak.

Honest owner-after-revoke and share-before-revoke may pass on both implementations. That does not excuse the B-after-revoke deny test. If the broken files do not fail `test_revoked_share_cannot_read`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/11/11-lab/tests --impl vulnerable
python3 -m pytest labs/11/11-lab/tests --impl fixed
```

A test that only greps `revoke` in a README without calling `read("n1", "B")` after `revoke("n1", "B")` is not this topic’s evidence. This practice never opens a live host.

## What the tests do not prove

- Worker leftover session is gone
- Phone cache is wiped
- Copies already sent are gone
- Access-rights change in the same session without signing in again
- An assurance gate complete

Record those as leftover or later topics, not as silent passes.

## Practice

Run both this session from the lab directory if needed:

```text
python3 -m pytest labs/11/11-lab/tests --impl vulnerable
python3 -m pytest labs/11/11-lab/tests --impl fixed
```

Paste nothing from answer keys. Write fail/pass into your notes next to the B-after-revoke row. Reject a “test” that only greps `revoke` in a README without calling `read("n1", "B")` after `revoke("n1", "B")`.

## Use it somewhere new

A clinic example: a test that only asserts “revoke returned 200” is not this topic. A live clinic system is out of scope.

## What this page is not doing

Do not treat a live tenant screenshot as proof. Do not log note bodies. Answer keys are not on this site. This page does not mark you as finished.
