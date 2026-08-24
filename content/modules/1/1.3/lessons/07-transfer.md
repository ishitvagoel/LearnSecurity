# 1.3 — Trust boundaries and attack surface (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

**Product sketch:** Clinic booking: X-Internal-Admin on the public API.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | FastAPI dependency injection does not know your TCB. Next.js rewrite headers are… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/1.3/1.3-trust-boundaries` stays the only running system you may break.
