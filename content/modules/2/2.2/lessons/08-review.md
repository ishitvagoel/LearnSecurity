# 2.2 — HTTP, TLS, proxies, CDNs, and cache keys (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.

## Property (start here)

A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.

## Attacker capabilities and trust assumptions

- **Attacker:** Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.
- **Trust:** Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.
Review `labs/2.2/2.2-request-path/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/2.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): Cache-Control: public on /notes/{id}
- Seeded smell (label it yourself): Key is path only
- Seeded smell (label it yourself): Comment “TLS so cache is safe”
- Seeded smell (label it yourself): Purge API not in the incident runbook

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- HTTPS means no cache bugs
- CDNs are only a performance layer
- Vary: Cookie is enough forever

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Authenticated RSS or export CSV via CDN.
