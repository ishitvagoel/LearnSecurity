# 1.3 — Trust boundaries and attack surface (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
export_notes ignores client headers; requires worker_bound=True.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
"""Fixed: worker identity is a server-side bind, not a client header (split shared mechanism)."""

NOTES = [
    {"id": "n1", "tenant": "tA", "body": "tenant-A-note"},
    {"id": "n2", "tenant": "tB", "body": "tenant-B-note"},
]


def export_notes(headers: dict, *, worker_bound: bool = False) -> list[dict]:
    del headers  # untrusted side of the boundary; never a TCB input
    if worker_bound:
        return list(NOTES)
    return []
```

## Why this restores the cell

Ignore client internal headers; bind worker identity in the process/mesh.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

FastAPI dependency injection does not know your TCB. Next.js rewrite headers are client-controlled after the browser.

A WAF dropping the header is defense in depth, not the property. Attackers will use another field.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

## Residual risk

A real compromised worker still exports. Detect and revoke (7.4, 10.5).
