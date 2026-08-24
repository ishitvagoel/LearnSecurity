# 8.3 — Network, deep links, WebViews, IPC (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | ignored_as_param metric. |
| Signal (no bodies) | deeplink_identity_ignored. |
| Revoke / recover | Force re-login. |
| Residual | User installs attacker app — OS model. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/8.3/8.3-lab`.

## Transfer

OAuth redirect to app (4.5).

## Usability

Deep-link errors should not trap users in a broken WebView without a keyboard-accessible exit.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
