# 2.2-LO-02 — Request-path diagram for local SecureCollab plus edge

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP Application Security Verification Standard 5.0.0 (final). Awareness lists (Top 10, CWE Top 25) are regression checks, not the outline.

## Property (start here)

What must remain true of **SecureCollab** (or the elective system) regarding **DNS, transport, HTTP, TLS, proxies, CDNs, and caches** when an attacker with stated capabilities acts, a component fails, or a human follows a stressful recovery path?

Invariant prompt for this object: Origin does not treat unauthenticated forwarded headers as identity; Cache keys are explicit and in the threat model; No attacks against real CDNs or third-party sites

## Attacker capabilities and trust assumptions

State both, or the claim is a slogan:

- **Attacker:** anyone who can reach the local lab API; a logged-in member of another tenant; a stolen worker identity; a hostile mobile client where Phase 8 applies.
- **Trust:** FastAPI + PostgreSQL with least-privilege roles are in the TCB for server-side mediation; the Next.js bundle and Android client are **not**. Lab honesty is assumed; no public targets.

Threat-model prompts from the spec:

- Who authenticated the name, and to which hop?
- What is the cache key, and can an attacker influence it?
- After TLS termination, what identity is still bound to the request?

## Root cause, preconditions, impact, prevention, detection, recovery

| Slice | For DNS, transport, HTTP, TLS, proxies, CDNs, and caches |
|---|---|
| Root cause | Wrong trust in a mechanism, skipped mediation on an indirect path, or a confused interpreter — not “missing a scanner finding.” |
| Preconditions | The local fixture is reachable; the learner is authorized only on this lab; synthetic data only. |
| Impact | Tenant notes, identity, or availability of SecureCollab can fail the named property. |
| Prevention | Smallest structural mechanism that restores the invariant (not a blacklist-only patch). |
| Detection | Logs/alerts that fire when the forbidden outcome is attempted. |
| Recovery | Revoke, rotate, purge, restore from a known-good backup, and record residual risk. |

## Framework defaults vs application guarantees

FastAPI, Next.js, PostgreSQL, or Android “secure defaults” are not the application guarantee for **DNS, transport, HTTP, TLS, proxies, CDNs, and caches**. Name what the app must still enforce.

## Mechanism limits

A green scanner, a named product (JWT, TLS, bcrypt), or an awareness-list item does not prove the invariant. Universal checkboxes fail when risk-based selection is required.

## Practice (local, authorized)

Complete the associated lab under `labs/2.2/` if a labSpec exists. Observe the forbidden outcome on `vulnerable/`. Do not target non-lab systems. Do not copy weaponized payloads into notes.

Safe task: write one testable sentence that would fail if the **transport** property were false.

## Transfer

Change one asset, principal, or boundary (new worker, webhook, offline cache, or clinic-booking card). Redraw the claim without using a Top 10 item as the definition of security.

## Usability and accessibility

Where a human is part of the control (login, recovery, consent, admin impersonation), the journey must remain usable and accessible (WCAG 2.2 final as the web baseline). Do not rely on color, mouse-only, or memory-only secrets.

## Misconceptions to refuse

- TLS termination means the app can trust X-Forwarded headers and Host
- CDN cache is performance-only
- RFC 9846 is a checkbox that TLS 1.3 is enabled

## Non-goals

Live-target attacks, real PII, production secrets, and treating this lesson as a product tutorial.
