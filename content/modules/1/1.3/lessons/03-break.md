# 1.3 — Trust boundaries and attack surface (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
**Forbidden outcome:** Client internal header dumps all tenants' notes

**Authorized scope:** `labs/1.3/1.3-trust-boundaries` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable/surface.py treats X-SecureCollab-Internal as worker identity.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Public listener; header check instead of identity.

## Vulnerable fixture (local)

```python
"""Vulnerable: client-supplied internal header is treated as the worker identity."""

NOTES = [
    {"id": "n1", "tenant": "tA", "body": "tenant-A-note"},
    {"id": "n2", "tenant": "tB", "body": "tenant-B-note"},
]


def export_notes(headers: dict, *, worker_bound: bool = False) -> list[dict]:
    if headers.get("X-SecureCollab-Internal") == "1":
        return list(NOTES)
    if worker_bound:
        return list(NOTES)
    return []
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Transitive trust: the handler believed a string that crossed the boundary. |
| Impact | Cross-tenant dump; blast radius = all notes. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/1.3/1.3-trust-boundaries/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

## Non-goals

No live-target instructions. Synthetic data only.
