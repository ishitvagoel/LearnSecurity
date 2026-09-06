# Fail on the broken files, then pass on the repaired ones

**Kind:** verification-lab
**Loop step:** 5 Verify

## If you cannot test it, it is still a slogan

“We filled in the store’s privacy form” is not evidence. “The crash product uses HTTPS” is a tool observation. The check is: `'secret' not in str(crash_report("secret"))` and an honest crash still has a `stack` key. That body-absent observation must be **false** on the broken files and **true** on the repaired files. Do not call a crash vendor.

## Picture: a broken crash report must fail the check

A test that only counts passing tests can pass while the body is still in the report. This check asks whether a confidential field in this crash JSON still counts as a passing control. Broken must fail that question. Repaired must pass it.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: body in report]
  X["repaired files --impl fixed"] --> P[Must pass: omit body]
```

If both pass, the test is not looking at the body substring. If both fail, the fix is not structural or the check is wrong.

## Four modes, even for a crash dict

| Mode | Must show for this topic |
|---|---|
| Normal | Honest crash still has a `stack` key (may pass on both) |
| Wrong input | `'secret'` not in `str(crash_report('secret'))`; broken files must fail |
| Abuse | Unsure values are not attached (fail closed; leftover if not in this pytest) |
| Not claimed | A real crash console; the public store; screenshot pipelines; vendor DLP |

The file is `labs/8.5/8.5-lab/tests/test_property.py`. The test `test_crash_report_omits_note_body` is a **what-must-not-happen** test: a report that includes the body is not allowed to count as a passing control.

Honest stack-present may pass on both implementations. That does not excuse the body-omit test. If the broken files do not fail `test_crash_report_omits_note_body`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/8.5/8.5-lab/tests --impl vulnerable
python3 -m pytest labs/8.5/8.5-lab/tests --impl fixed
```

A test that only greps a crash product name in Gradle without calling `crash_report("secret")` is not this topic's evidence. This practice never opens a live crash project.

## What the tests do not prove

- Vendor DLP after send
- A privacy list on a physical device
- That debug logcat is empty on a rooted phone (8.1)
- Screenshot / frozen-app pipelines
- Last-chance error handlers (an advanced extra)
- Web crash reports (10.5)

Record those as leftover or later topics, not as silent passes.

## Practice

Run both this session from the lab directory if needed:

```text
python3 -m pytest labs/8.5/8.5-lab/tests --impl vulnerable
python3 -m pytest labs/8.5/8.5-lab/tests --impl fixed
```

Paste nothing from answer keys. Write fail/pass into your notes next to the body×crash row. Reject a “test” that only greps a crash product name without calling `crash_report("secret")`.

## Use it somewhere new

Clinic: a test that only asserts “crash dialog shown” is not this topic. A test that only asserts HTTP 200 is the wrong observation. A live web-crash call is out of scope.

## What this page is not doing

Do not add a live crash trophy. Do not log note bodies. Answer keys stay out of this file.
