# The broken files must fail when the phone says ok but attest fails

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

Naming Play Integrity in a README does not ignore the client boolean. A disabled Compose button is the UI. `allow_export({"integrity": "ok"}, "fail")` has to be false, and `allow_export({"integrity": "ok"}, "play_integrity_pass")` may be true. On `--impl vulnerable` client-ok-plus-attest-fail still returns true. On `--impl fixed` it does not. Do not call live attestation APIs.

## Picture: broken files must fail: client ok plus attest fail

A passing-test tally can still hide that client `integrity=ok` still authorizes export.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail client ok plus attest fail"]
  X["--impl fixed"] --> P["Must pass deny"]
```

If both pass, you are not looking at the client boolean.

## Three things to look at

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | client ok, attest fail → false; broken files must fail (`test_client_integrity_claim_is_not_authorization`) |
| Normal | client ok, attest pass → true (`test_server_attest_may_allow_export`; may pass on both) |
| Extra | missing client claim, attest fail → false (`test_missing_client_claim_does_not_authorize`) |
| Not claimed | emulator farms; 4.4 object grant; live Play; platform integrity on a physical phone |

The checks are in `labs/8.1/8.1-lab/tests/test_property.py`. `test_client_integrity_claim_is_not_authorization` is there so a client boolean that authorizes export still fails.

```text
python3 -m pytest labs/8.1/8.1-lab/tests --impl vulnerable
python3 -m pytest labs/8.1/8.1-lab/tests --impl fixed
```

A server that already says yes may pass on both sides. You still have to deny a failing client integrity claim. If the broken files do not fail `test_client_integrity_claim_is_not_authorization`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- Real Play Integrity token verification
- Platform integrity on a physical phone
- 8.4 debug/release split
- iOS App Attest (later mirror)
- 4.4 object grants after export is allowed
- 6.7 quota

## Practice

Do not treat a grep for `PlayIntegrity` in Gradle as the check. Call `allow_export({"integrity": "ok"}, "fail")`. A setup error is not proof the rule holds.

## Use it somewhere new

Asserting the Android button is disabled is not this check. Do not make a live Play Console call.

## What this page is not doing

Do not treat a device-farm screenshot as proof. Do not log attestation blobs. Answer keys are not on this site.
