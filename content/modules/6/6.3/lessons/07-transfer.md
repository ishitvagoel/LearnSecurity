# 6.3 — Cross-site and cross-context attacks (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** postMessage, clickjacking, CORS * with credentials.

**Product sketch:** Clinic “share record with partner” POST.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | SameSite=Lax is not complete (GET side effects, chrome exceptions).… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/6.3/6.3-lab` stays the only running system you may break.
