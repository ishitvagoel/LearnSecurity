# E2 — Advanced browser and edge security (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | browser, app |
| Objects | CSP header |
| Actions | isolation_enforced |
| Channels | HTTP headers |
| TCB | Enforcing CSP (and others) actually parsed as enforcing. |
| Untrusted | Report-Only, comments in HTML |
| State / time | Rollout. |
| 1.1 cell | Integrity of the browser policy mechanism (2.3 layered with 6.2). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| CSP enforce | script | block | maybe |
| CSP Report-Only | script | block | no |
| encoding 6.2 | title | safe | still-required |
| cache 2.2 | header | strip | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/E2/e2-lab` file `csp.py`.

## Transfer

Trusted Types, COOP/COEP.

## Residual risk

XS-Leaks — named as elective depth.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
