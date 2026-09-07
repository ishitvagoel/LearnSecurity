# Log the deny, not the app file

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A new client field (`premium`, `hipaaMode`) can skip the attest check after `allow_export` was “fixed once.” Do not log note bodies or attestation blobs (3.1). Do not attach the Android app file to the ticket.

## Picture: failed attest is a signal

```mermaid
flowchart TD
  Exp[export] --> Attest{server attest fail?}
  Attest -->|yes| Metric["attest_fail_export_denied plus 1"]
  Metric --> Revoke[Revoke app session if automated]
```

A dashboard tile does not prove the server attest.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `attest_fail_export_denied` |
| What the line holds | request id, app version, attest result class; never the app file or body |
| Recover | Keep deny; revoke tokens; owned rooted-device policy |
| Leftover | Attestation farms; 8.4 debug clients; old app files shipping the boolean |

A mobile-device product name is not the check. Re-run `test_client_integrity_claim_is_not_authorization` after any export-route change. Enabling Play Integrity does not authorize the export. Feature flags and `premium=true` are other client booleans of the same family — list those before you call the server the authority.

## What the framework does vs what you still have to check

A Play Console dashboard will show attestation counts and stay silent when FastAPI still binds `integrity=ok`. Notice must observe **client ok plus attest fail is false**, not store-listing health. If the alert includes a Play Integrity token or note bodies, you have opened a logging leak (3.1 / 4.3).

`attest_fail_export_denied` fires without the app file.

## Practice

```text
log_denied reason=attest_fail_export_denied app_ver=1.0 request_id=req_81e
```

Reject any line that includes note bodies, a Play Integrity token, or a live device trace.

## Use it somewhere new

Notice `hipaaMode` client claims on a local helper; do not attach the chart to the ticket. Do not instrument a live hospital device.

## Can people still use it

If export is denied, say so in a readable message. Do not trap TalkBack users in a spinner that retries a failing attest.

## What this page is not doing

A mobile-device product name is not the check. Do not use live Play traces. Opening this page does not finish a check-in.
