# 6.5 — Server-side requests and protocol parsing (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
Review `labs/6.5/6.5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): requests.get(user_url)
- Seeded smell (label it yourself): https-only regex still allows metadata IP
- Seeded smell (label it yourself): Follows redirects off allow-list
- Seeded smell (label it yourself): No 169.254 test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- HTTPS URLs cannot SSRF
- Private IP blocklists are complete
- Open redirect is just UX

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Webhook delivery (7.3) is egress too.
