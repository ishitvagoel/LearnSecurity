# 5.4 — Secure communication and channel binding (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** mTLS service identity vs this header.

**Product sketch:** Clinic: “we’re on TLS” because the SPA uses https:// in axios baseURL while API is http internally logged as https.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | uvicorn --proxy-headers without a trusted proxy IP is this bug.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/5.4/5.4-lab` stays the only running system you may break.
