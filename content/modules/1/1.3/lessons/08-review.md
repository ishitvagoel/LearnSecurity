# 1.3 — Trust boundaries and attack surface (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
Review `labs/1.3/1.3-trust-boundaries/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/1.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): if request.headers.get('X-SecureCollab-Internal'): return all_notes()
- Seeded smell (label it yourself): SECURITY.md claims “API is private because we use HTTPS”
- Seeded smell (label it yourself): No test for header present + worker_bound false
- Seeded smell (label it yourself): Trusting X-Forwarded-For as client identity

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- TLS is a trust boundary for headers
- Security by an internal-sounding header name
- Defense in depth means any layer can be skipped

## Practice

Write three review notes. Do not open the keys file.

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?
