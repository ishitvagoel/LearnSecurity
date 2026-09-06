# Fail on the broken files, then pass on the repaired ones

**Kind:** verification-lab
**Loop step:** 5 Verify

## If you cannot test it, it is still a slogan

“We put max on the select” is not this topic’s evidence. “The filter has an awareness-list rule” is a tool observation. The check is: after eight `add_share()` calls, `last <= 5`. That observation must be **false** on the broken files and **true** on the repaired files.

## Picture: last greater than 5 must fail

A test that only asserts a max attribute exists can pass while eight calls still leave count 8. This check asks whether a sixth grant still counts as a passing control. Broken must fail that question. Repaired must pass it.

```mermaid
flowchart LR
  V["broken files"] --> F["Must fail: last greater than 5"]
  X["repaired files"] --> P["Must pass: last 5 and sixth no increment"]
```

| Mode | Must show for this topic |
|---|---|
| Normal | Five honest shares still land (`test_five_shares_are_allowed`) |
| Wrong input / abuse | Eight `add_share` calls leave `last <= 5`; broken files must fail |
| Sixth | Does not increment past 5 |
| Not claimed | Production locks; GraphQL; rate limits; awareness-list compliance |

Lab tests in `labs/3.4/3.4-lab/tests/test_property.py`. `test_share_cap_is_enforced` is a **what-must-not-happen** test: a sixth grant is not allowed to count as a passing control.

```text
python3 -m pytest labs/3.4/3.4-lab/tests --impl vulnerable
python3 -m pytest labs/3.4/3.4-lab/tests --impl fixed
```

Map each test to the state-machine row you wrote. If the broken files do not fail the eight-call assertion, the lab is miswired — fix the wiring, not the check. An environment error is not security evidence.

## What the tests do not prove

- Two parallel sixths (needs a real lock)
- Import/GraphQL paths
- Rate limits
- Support override audit (advanced)
- That the accessible status message exists (leftover)

Record those as leftover or later topics, not as silent passes.

## Practice

Run both this session. Write the fail/pass pair next to the matrix row. Reject a “test” that only greps `max={5}` in JSX without calling `add_share` eight times.

## Use it somewhere new

Clinic guardians. A test that only asserts HTTP 200 is not cap evidence. A test that load-tests a live clinic is out of scope.

## What this page is not doing

Do not add a live flood. Do not log note bodies. Answer keys are not on this site.
