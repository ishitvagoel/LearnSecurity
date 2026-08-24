# 1.3 — Trust boundaries and attack surface (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Client internal header dumps all tenants' notes |
| Failure | Fail closed: Ignore client internal headers; bind worker identity in the process/mesh |

Lab tests: `test_boundary.py` under `labs/1.3/1.3-trust-boundaries`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Client internal header dumps all tenants' notes`
- `--impl fixed`: **pass**

{} -> []; header-only -> []; worker_bound -> two notes.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
