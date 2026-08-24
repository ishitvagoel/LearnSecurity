# 1.3 — Trust boundaries and attack surface (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
**Mechanism (not the property):** FastAPI dependency injection does not know your TCB. Next.js rewrite headers are client-controlled after the browser.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 1.3 |
|---|---|
| Root cause | Transitive trust: the handler believed a string that crossed the boundary. |
| Preconditions | Public listener; header check instead of identity. |
| Impact (1.1 cell) | Confidentiality (1.1) via a boundary failure, not a new CWE slogan. — Cross-tenant dump; blast radius = all notes. |
| Prevention | Ignore client internal headers; bind worker identity in the process/mesh. |
| Detection | Alert on that header appearing on the public listener (it is a probe). |
| Recovery | Rotate worker credentials; audit export logs; notify tenants if bodies left. |

## Framework defaults vs application guarantees

FastAPI dependency injection does not know your TCB. Next.js rewrite headers are client-controlled after the browser.

## Mechanism limits and bypasses

A WAF dropping the header is defense in depth, not the property. Attackers will use another field.

Body field is_internal=true; GraphQL; gRPC metadata; websocket first message.

## Residual risk

A real compromised worker still exports. Detect and revoke (7.4, 10.5).

## Practice

Draw the line: browser | TLS | app | DB. Star every input that currently influences export_notes.

Run `labs/1.3/1.3-trust-boundaries` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

Clinic booking: X-Internal-Admin on the public API.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
