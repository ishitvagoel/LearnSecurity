# 1.3 — Trust boundaries and attack surface (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).

## Property (start here)

A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.
- **Trust:** FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Anonymous client, logged-in member, bound worker |
| Objects | All notes export, single note, worker credential |
| Actions | export_notes, set header, bind worker |
| Channels | HTTP headers, internal mesh (future), queue (7.4) |
| TCB | Server-side worker_bound flag / mTLS later — never the client header. |
| Untrusted | Every header, cookie, JWT kid, IP, geo |
| State / time | A header that was “internal” on yesterday’s VPC is still untrusted from the browser today. |
| 1.1 cell | Confidentiality (1.1) via a boundary failure, not a new CWE slogan. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| browser | all notes | export | deny |
| browser+header | all notes | export | deny |
| bound worker | all notes | export | allow |
| member tA | tA notes | list | allow-via-1.2 |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/1.3/1.3-trust-boundaries` file `surface.py`.

## Transfer

CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?

## Residual risk

A real compromised worker still exports. Detect and revoke (7.4, 10.5).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
