# 7.3 — Webhooks, callbacks, and third-party APIs (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
Review `labs/7.3/7.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/7.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): if path==/webhook: process
- Seeded smell (label it yourself): JSON parsed before MAC
- Seeded smell (label it yourself): No missing-sig test
- Seeded smell (label it yourself): Secret in query (4.3)

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- TLS to us proves the sender
- IP allowlist is authenticity
- Webhooks are just APIs in reverse so JWT login applies

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Signed redirects; outbound webhook SSRF (6.5).
