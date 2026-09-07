# A leftover default secret must fail

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“Secrets Manager is enabled” is not this topic’s evidence. “The wiki says we rotated” is a tool observation. The check is: `auth("sk-lab-hardcoded", current="rotated-now")` is False and `auth("rotated-now", current=None)` is False. That observation must be **false** on the broken files (default still authenticates / missing current allows) and **true** on the repaired files.

## Picture: leftover default must fail

A check that only counts passing cases can still look green while a leftover default still counts as a valid key.

```mermaid
flowchart LR
  V["broken files"] --> F["Must fail: default still authenticates"]
  X["repaired files"] --> P["Must pass: default is dead"]
```

| Mode | Must show for this topic |
|---|---|
| Normal | current secret authenticates (`test_current_secret_authenticates`; may pass on both) |
| Wrong input / abuse | hardcoded default false after rotate; missing current denies; broken files must fail |
| Not claimed | hardware box; timed rotation; worker second default |

The checks live in `labs/5.3/5.3-lab/tests/test_property.py`. `test_hardcoded_default_does_not_auth` is there so a leftover default cannot sneak through.

```text
python3 -m pytest labs/5.3/5.3-lab/tests --impl vulnerable
python3 -m pytest labs/5.3/5.3-lab/tests --impl fixed
```

The honest current-secret test may pass on both. That does not excuse the default-dead and missing-current tests. If the broken files do not fail `sk-lab-hardcoded`, the lab is miswired — fix the wiring, not the check. A setup error is not proof the rule holds.

## What the tests do not prove

- Envelope wrapping (data key vs wrapping key)
- Hardware box / timed rotation (advanced extras)
- Keys baked into a phone app (later topic)
- A second default on a worker (later topic)

## Practice

Run both this session. Write the fail/pass pair next to the matrix row. Reject a “test” that only greps `Vault` in a README without calling `auth("sk-lab-hardcoded", current="rotated-now")`.

## Use it somewhere new

Clinic gist. A test that only asserts HTTP 200 on login is not rotation evidence (later testing topic). A test that fetches a live gist is out of scope.

## What this page is not doing

Do not add a live gist search. Do not log the secret value. Answer keys are not on this site.
