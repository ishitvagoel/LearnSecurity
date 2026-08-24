# 6.3 — Cross-site and cross-context attacks (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
**Mechanism (not the property):** SameSite=Lax is not complete (GET side effects, chrome exceptions).

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.3 |
|---|---|
| Root cause | Cookie authority used without site-bound intent. |
| Preconditions | allow_share(evil, app, token=None) True. |
| Impact (1.1 cell) | Integrity of share grants (3.4/1.2) against the browser’s confused-deputy. — Unwanted share grant. |
| Prevention | Reject foreign Origin; require token for cookie sessions. |
| Detection | csrf_rejected metric. |
| Recovery | Revoke surprise shares; notify. |

## Framework defaults vs application guarantees

SameSite=Lax is not complete (GET side effects, chrome exceptions).

## Mechanism limits and bypasses

Bearer tokens in Authorization are a different deputy model.

subdomain XSS, open redirect (6.5), old browsers.

## Residual risk

User clicking “share” on a lookalike UI — 4.2 phishing.

## Practice

Matrix: origin × token × method.

Run `labs/6.3/6.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

postMessage, clickjacking, CORS * with credentials.

Clinic “share record with partner” POST.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

CSRF errors must be readable (not color-only). Do not make the secure path harder than a cross-site GET that still mutates.
