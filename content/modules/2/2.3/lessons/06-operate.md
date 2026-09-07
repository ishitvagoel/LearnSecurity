# Notice session cookies without HttpOnly; never log the value

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A new cookie, a WebView, a “debug” `Set-Cookie`, or a second name (`sc_refresh`) can drop the flag. Do not log session values, note bodies, or recovery codes.

## Picture: scan the flags, rotate if script could have read

A missing HttpOnly flag still has to be noticed. Do not paste the session into a ticket. The notice should name the cookie. Recovery should rotate it. Neither logs the value.

```mermaid
flowchart TD
  Scan["Staging Set-Cookie review"] --> Flag{HttpOnly on session names?}
  Flag -->|no| Metric["cookie_session_missing_httponly += 1"]
  Metric --> Log["name=sc_session reason=missing_httponly no value"]
  Log --> Rotate[Rotate session ids]
```

A log product and a checklist name do not restore this rule. Report-Only CSP is a **different** notice path.

| Outcome | This topic |
|---|---|
| Notice | `Set-Cookie` without HttpOnly on session names in staging or canary |
| What the line holds | cookie **name** + reason + request id; never the value |
| Respond | Stop issuing the broken setter; do not “help” by emailing the session |
| Recover | Rotate session ids; fix the setter; re-run `test_script_cannot_read_httponly_session` |
| Leftover | Extensions; physical access; XSS that never needed the cookie |

```text
cookie_denied reason=missing_httponly name=sc_session env=staging request_id=req_4b11
```

Not: `synthetic-session`, a note body, or a personal mailbox.

## Practice

Reject any line that includes the dummy session value. Name who owns the WebView leftover and what trigger reopens it.

## Use it somewhere new

Clinic portal. Staging scans must include WebView or second-cookie names, not only `sc_session`. A privacy-safe notice still has no chart text.

## Can people still use it

The alternate path after rotation (sign in again) must itself meet keyboard, name, and not-color-only. Those rules apply to that path too. They are not a cookie policy.

## What this page is not doing

Answer keys are not on this site.
