# 4.3 — Sessions, cookies, and tokens (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
**Mechanism (not the property):** OAuth “implicit in URL” is obsolete; copying it is not ASVS.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 4.3 |
|---|---|
| Root cause | Token placed in a logged, shared channel. |
| Preconditions | session_from_request reads access_token query. |
| Impact (1.1 cell) | Authenticity/confidentiality of the session artifact. — Session theft without XSS. |
| Prevention | Reject query tokens; use cookie/header. |
| Detection | Access logs containing token-shaped query keys. |
| Recovery | Revoke those tokens; rotate. |

## Framework defaults vs application guarantees

OAuth “implicit in URL” is obsolete; copying it is not ASVS.

## Mechanism limits and bypasses

Authorization header still logs at some gateways — redact.

Fragment tokens, POST body in debug dumps, 4.1 leftover sessions.

## Residual risk

Referer on first-party navigations — strip on outbound.

## Practice

Name three sinks of a query token.

Run `labs/4.3/4.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).

Clinic appointment deep link.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
