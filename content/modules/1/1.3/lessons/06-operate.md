# 1.3 — Trust boundaries and attack surface (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Alert on that header appearing on the public listener (it is a probe). |
| Signal (no bodies) | Public-edge log: internal-header-seen without worker identity. |
| Revoke / recover | Rotate worker credentials; audit export logs; notify tenants if bodies left. |
| Residual | A real compromised worker still exports. Detect and revoke (7.4, 10.5). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/1.3/1.3-trust-boundaries`.

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
