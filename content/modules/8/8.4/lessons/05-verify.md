# The broken files must fail when a debug build looks ok

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

`minifyEnabled` true does not keep the debug client id off the API. Play App Signing is a store setting. `api_allowed("debug", "ok")` has to be false, and `api_allowed("release", "ok")` may be true. On the broken helper, debug-plus-ok still returns true. Repair refuses a debug client talking to prod. Do not unpack store APKs.

## Picture: broken files must fail: debug plus ok

Debug can still call prod even when the suite is green.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail debug plus ok"]
  X["--impl fixed"] --> P["Must pass deny"]
```

If the broken flavor still passes, debug-to-prod was never denied.

## Three things to look at

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | debug + ok → false; broken files must fail (`test_debug_build_cannot_call_prod_export`) |
| Normal | release + ok → true (`test_release_with_attest_may_call_prod`; may pass on both) |
| Extra | release + fail → false (`test_release_without_attest_is_denied`) |
| Not claimed | real Play Integrity; R8; live signing; hardware-backed keys |

Debug-plus-ok talking to prod is why `test_debug_build_cannot_call_prod_export` lives in `labs/8.4/8.4-lab/tests/test_property.py`.

```text
python3 -m pytest labs/8.4/8.4-lab/tests --impl vulnerable
python3 -m pytest labs/8.4/8.4-lab/tests --impl fixed
```

A release build talking to prod is not the whole check. Deny a debug build calling the prod export. If the broken files do not fail `test_debug_build_cannot_call_prod_export`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- Hardware-backed signing
- Resilience checks on a physical device
- That debug cannot reach a *lab* API (it should)
- Real Play Integrity token checks (8.1)
- That signing keys are absent from the repo (5.3)
- Completeness of an APK inventory list (10.2)

## Practice

Call `api_allowed("debug", "ok")`. `minifyEnabled` is the shrink flag. A setup error is not proof the rule holds.

## Use it somewhere new

A debug APK that builds is the compile, not debug-client-id off. Do not unpack a store APK.

## What this page is not doing

A live Play screenshot is not the debug client id off. Do not log signing keys. Answer keys are not on this site.
