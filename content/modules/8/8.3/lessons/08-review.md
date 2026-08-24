# 8.3 — Network, deep links, WebViews, IPC (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
Review `labs/8.3/8.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/8.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): current_user = extras['as']
- Seeded smell (label it yourself): exported Activity without permission
- Seeded smell (label it yourself): WebView addJavascriptInterface too wide
- Seeded smell (label it yourself): No as= test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- https App Links are trusted input
- WebView is just Chrome so 2.3 applies unchanged
- IPC is private to our app

## Practice

Write three review notes. Do not open the keys file.

## Transfer

OAuth redirect to app (4.5).

## HITL / WCAG 2.2

Deep-link errors should not trap users in a broken WebView without a keyboard-accessible exit.
