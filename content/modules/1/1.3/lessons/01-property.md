# 1.3-LO-01 — TCB, entry points, transitive trust, shared mechanisms, blast radius

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP Threat Modeling Project (maintained guidance, final) — Four Questions, not a single tool; Saltzer (1975, seminal); ASVS 5.0.0 (final) V15 chapter-level.

## Property (start here)

What must remain true **across** the browser→API boundary if the Next.js client is **fully hostile**? For SecureCollab Phase 1: **authorization and note integrity are not properties of the browser**. The client is not in the TCB for those invariants.

## Attacker capabilities and trust assumptions

- **Attacker:** anyone who can send HTTP; a modified Next.js bundle; a CDN that caches the wrong tenant (later); a stolen worker identity.
- **Trust:** FastAPI process + (later) PostgreSQL roles. Email/IdP are **transitive trust** — if they are wrong, invite/recovery invariants fail (1.4/4.x).

## Names

| Term | SecureCollab |
|---|---|
| TCB | Code that must be right for bob∉read(n1) |
| Entry point | Public HTTP `read_note` / future export |
| Shared mechanism | `X-SecureCollab-Internal` header used by both “edge” and app |
| Blast radius | All tenants’ note bodies if export trusts that header |
| Defense in depth | A second check that reads the **same** header is **not** independent |

## Root cause / impact / prevention / detection / recovery

Root cause: treating an untrusted-side identifier as worker identity. Impact: 1.1 confidentiality × every tenant on export. Prevention: split the mechanism (server-side bind). Detection: alert on the header still being sent. Recovery: rotate worker credentials; notify tenants if export leaked.

## Framework defaults vs application guarantees

TLS to the API does not put the client in the TCB. “HTTPS therefore trusted frontend” is false.

## Practice

List three entry points and one shared mechanism for Phase 1 SecureCollab.

## Transfer

Add object storage for files: is the bucket policy in the TCB or a residual on AWS?
