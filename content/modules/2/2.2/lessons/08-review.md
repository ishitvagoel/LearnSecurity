# 2.2-LO-08 — Review the path-only cache as a PR, not a slogan

**Kind:** code-review
**Loop step:** Review
**Standards:** IETF RFC 9110 (final); IETF RFC 9846 TLS 1.3 (final); OWASP ASVS 5.0.0 (final) `v5.0.0-14.2.2`.

## Review the fixture as if it were SecureCollab edge cache

Review `labs/2.2/2.2-request-path/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/2.2.md` — not here.

## Mental model: property, mechanism, or false assurance

```mermaid
flowchart TD
  Claim[PR claim] --> Q{What would falsify it?}
  Q -->|tB get returns tA body| Property["Property - good if tested"]
  Q -->|we use TLS 1.3| Mechanism[Mechanism - ask which hop]
  Q -->|HTTPS so cache is safe| False[False assurance]
```

For each claim and each branch: label **property**, **mechanism**, or **false assurance**.

Seeded smells (label them yourself; do not open the keys file):

- `Cache-Control: public` on `/notes/{id}`
- Key is path only
- Comment “TLS so cache is safe”
- Purge API not in the incident runbook

Also reject: client `X-Tenant` as key input, `Vary: Cookie` as forever, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- HTTPS means no cache bugs
- CDNs are only a performance layer
- `Vary: Cookie` is enough forever

## Practice

Write three review notes a peer could act on. Tie at least one note to `test_other_tenant_does_not_receive_cached_body`.

## Transfer

Authenticated RSS or export CSV via CDN. A PR that “turns on HTTPS” on only the browser hop is an incomplete mediation review.
