# 8.3 — Network, deep links, WebViews, IPC (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** OAuth redirect to app (4.5).

**Product sketch:** Clinic: deep link as=doctor.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | exported=true defaults on old Android.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/8.3/8.3-lab` stays the only running system you may break.
