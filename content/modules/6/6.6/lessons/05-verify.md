# Using the same token a second time must fail

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“Unique constraint exists” is not evidence. “We return 400” is a tool observation. The check is: first `accept("t1")` is true and second `accept("t1")` is false. That second observation must be **false** on the broken files (the helper still returns true) and **true** on the repaired files.

## Picture: second t1 must fail the check

A check that only greps `UNIQUE` in a migration can still look green while `accept("t1")` is still true twice.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F["Must fail: second t1 true"]
  X["repaired files --impl fixed"] --> P["Must pass: consume-once"]
```

If both pass, the test is not looking at the second `t1`. First accept of `t1` may pass on both implementations. That does not excuse the second-accept test.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | first `t1` allowed; distinct `t2` allowed once |
| Wrong input / abuse | second `t1` denied; broken files must fail |
| Failure | store error denies (named in review; fail-closed smell) |
| Not claimed | threaded race; mail delivery; lock semantics |

The test `test_invite_token_is_single_use` is there so a second true still fails. Sequential calls are enough; do not add a race harness.

A test that only asserts HTTP 200 on `/accept` is not this topic's evidence. A test that only greps `UNIQUE` without calling `accept("t1")` twice is not this topic's evidence. This practice never opens a live mailer.

```text
python3 -m pytest labs/6.6/6.6-lab/tests --impl vulnerable
python3 -m pytest labs/6.6/6.6-lab/tests --impl fixed
```

Map the test to the second-`t1` deny row you wrote. If the broken files do not fail the second `t1`, the lab is miswired — fix the wiring, not the assertion. A setup error is not proof the rule holds.

## What the tests do not prove

- Atomic lock under threads (production shape)
- Transaction rollback
- Fail-open on errors, except as a named review smell
- Last-resort error handler (advanced; not this check)
- Mail delivery or recipient authenticity (4.2)

## Practice

```text
python3 -m pytest labs/6.6/6.6-lab/tests --impl vulnerable
python3 -m pytest labs/6.6/6.6-lab/tests --impl fixed
```

Reject a “test” that only greps `UNIQUE` in a migration without calling `accept("t1")` twice.

## Use it somewhere new

Clinic guardian invite. A test that only asserts HTTP 200 on `/accept` is not this rule (see 9.3). A test that clicks a live mail link is out of scope.

## What this page is not doing

Do not add a live race harness. Do not log tokens. Answer keys are not on this site.
