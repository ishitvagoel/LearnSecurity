# The broken files must fail when a link claims admin

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“App Links are verified” is not evidence. “The link is https” is a tool observation. The check is: after `open_link({"as": "admin"})`, `current_user()` is still `"alice"`. The `as=admin` observation must be **false** on `--impl vulnerable` (session becomes admin) and **true** on `--impl fixed`. Do not fire live Intents.

## Picture: broken files must fail: as=admin

A passing-test tally can still hide that `as=` still switches the session.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail as=admin"]
  X["--impl fixed"] --> P["Must pass alice"]
```

If both pass, you are not looking at identity keys.

## Three things to look at

| Mode | Must show for this topic |
|---|---|
| Normal | `note=n1` keeps alice (`test_note_deep_link_keeps_session`; may pass on both) |
| Wrong input / abuse | `as=admin` keeps alice; broken files must fail (`test_deeplink_as_param_does_not_switch_user`) |
| Not claimed | WebView; custom schemes; live OAuth; real `exported` flags |

The checks are in `labs/8.3/8.3-lab/tests/test_property.py`. `test_deeplink_as_param_does_not_switch_user` is there so a link that switches the principal still fails.

```text
python3 -m pytest labs/8.3/8.3-lab/tests --impl vulnerable
python3 -m pytest labs/8.3/8.3-lab/tests --impl fixed
```

A deep link that only names the note may pass on both sides. You still have to ignore `as=`. If the broken files do not fail `test_deeplink_as_param_does_not_switch_user`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- WebView bridges (6.2)
- Claimed HTTPS App Links in production
- `exported` flags on a real manifest
- 4.5 audience after a valid OAuth redirect
- That a locator `note=n1` is authorized (4.4)

## Practice

Do not treat a grep for `android:autoVerify` as the check. Call `open_link({"as": "admin"})`. A setup error is not proof the rule holds.

## Use it somewhere new

Asserting the Activity launched is not this check. Do not use a sideloaded malware APK.

## What this page is not doing

Do not treat a live Intent screenshot as proof. Do not log full URLs that contain tokens. Answer keys are not on this site.
