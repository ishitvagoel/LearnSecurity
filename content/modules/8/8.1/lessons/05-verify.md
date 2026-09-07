# The broken files must fail when the phone says ok but attest fails

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We use Play Integrity” is not evidence. “The Compose button is disabled” is a tool observation. The check is: `allow_export({"integrity": "ok"}, "fail")` is false, and `allow_export({"integrity": "ok"}, "play_integrity_pass")` may be true. The client-ok-plus-attest-fail observation must be **false** on `--impl vulnerable` (returns true) and **true** on `--impl fixed`. Do not call live attestation APIs.

## Picture: broken files must fail: client ok plus attest fail

A check that only counts passing cases can still look green while client `integrity=ok` still authorizes export.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail client ok plus attest fail"]
  X["--impl fixed"] --> P["Must pass deny"]
```

If both pass, the check is not looking at the client boolean. If both fail, the fix is not structural or the check is wrong.

## Three things to look at

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | client ok, attest fail → false; broken files must fail (`test_client_integrity_claim_is_not_authorization`) |
| Normal | client ok, attest pass → true (`test_server_attest_may_allow_export`; may pass on both) |
| Extra | missing client claim, attest fail → false (`test_missing_client_claim_does_not_authorize`) |
| Not claimed | emulator farms; 4.4 object grant; live Play; platform integrity on a physical phone |

The checks live in `labs/8.1/8.1-lab/tests/test_property.py`. `test_client_integrity_claim_is_not_authorization` is there so a client boolean that authorizes export cannot sneak through.

```text
python3 -m pytest labs/8.1/8.1-lab/tests --impl vulnerable
python3 -m pytest labs/8.1/8.1-lab/tests --impl fixed
```

Honest server-pass may pass on both implementations. That does not excuse the failing-attest deny check. If the broken files do not fail `test_client_integrity_claim_is_not_authorization`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- Real Play Integrity token verification
- Platform integrity on a physical phone
- 8.4 debug/release split
- iOS App Attest (later mirror)
- 4.4 object grants after export is allowed
- 6.7 quota

## Practice

Run both implementations this session from the lab directory if needed. Reject a “check” that only greps `PlayIntegrity` in Gradle without calling `allow_export({"integrity": "ok"}, "fail")`. A setup error is not proof the rule holds.

## Use it somewhere new

A clinic example: a check that only asserts the Android button is disabled is not this rule. A live Play Console call is out of scope.

## What this page is not doing

Do not add a device-farm trophy. Do not log attestation blobs. Answer keys are not on this site.
