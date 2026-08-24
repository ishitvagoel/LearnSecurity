# 5.4 — Secure communication and channel binding (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
Review `labs/5.4/5.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/5.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): channel_is_https trusts X-Forwarded-Proto from anyone
- Seeded smell (label it yourself): --proxy-headers with *
- Seeded smell (label it yourself): No test header vs socket mismatch
- Seeded smell (label it yourself): HSTS on an app that still accepts http

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- HTTPS URL in the client proves TLS
- Forwarded headers are for security
- Pinning is always required

## Practice

Write three review notes. Do not open the keys file.

## Transfer

mTLS service identity vs this header.
