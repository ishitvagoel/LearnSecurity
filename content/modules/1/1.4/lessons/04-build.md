# 1.4-LO-04 — Reduce friction without weakening the 1.1 invariant; document the trade-off

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** CISA Secure by Design current-public-guidance (final). Awareness lists (Top 10, CWE Top 25) are regression checks, not the outline.

## Property (start here)

What must remain true of **SecureCollab** (or the elective system) regarding **Risk, people, economics, usable security, and resilience** when an attacker with stated capabilities acts, a component fails, or a human follows a stressful recovery path?

Invariant prompt for this object: Every high-impact 1.1 invariant has residual, owner, and revisit trigger; Inaccessible or unusable security flows are recorded as security failures; Vanity metrics are not presented as residual risk; No live-target or real-PII instructions appear in this module

## Attacker capabilities and trust assumptions

State both, or the claim is a slogan:

- **Attacker:** anyone who can reach the local lab API; a logged-in member of another tenant; a stolen worker identity; a hostile mobile client where Phase 8 applies.
- **Trust:** FastAPI + PostgreSQL with least-privilege roles are in the TCB for server-side mediation; the Next.js bundle and Android client are **not**. Lab honesty is assumed; no public targets.

Threat-model prompts from the spec:

- Who is harmed (user, tenant, coerced user, bystander)?
- What is the cheapest abuse that still pays?
- Which assumptions are untested (honest lab, trusted operator, honest IdP)?

## Root cause, preconditions, impact, prevention, detection, recovery

| Slice | For Risk, people, economics, usable security, and resilience |
|---|---|
| Root cause | Wrong trust in a mechanism, skipped mediation on an indirect path, or a confused interpreter — not “missing a scanner finding.” |
| Preconditions | The local fixture is reachable; the learner is authorized only on this lab; synthetic data only. |
| Impact | Tenant notes, identity, or availability of SecureCollab can fail the named property. |
| Prevention | Smallest structural mechanism that restores the invariant (not a blacklist-only patch). |
| Detection | Logs/alerts that fire when the forbidden outcome is attempted. |
| Recovery | Revoke, rotate, purge, restore from a known-good backup, and record residual risk. |

## Framework defaults vs application guarantees

FastAPI, Next.js, PostgreSQL, or Android “secure defaults” are not the application guarantee for **Risk, people, economics, usable security, and resilience**. Name what the app must still enforce.

## Mechanism limits

A green scanner, a named product (JWT, TLS, bcrypt), or an awareness-list item does not prove the invariant. Universal checkboxes fail when risk-based selection is required.

## Practice (local, authorized)

Complete the associated lab under `labs/1.4/` if a labSpec exists. Observe the forbidden outcome on `vulnerable/`. Do not target non-lab systems. Do not copy weaponized payloads into notes.

Safe task: write one testable sentence that would fail if the **risk** property were false.

## Transfer

Change one asset, principal, or boundary (new worker, webhook, offline cache, or clinic-booking card). Redraw the claim without using a Top 10 item as the definition of security.

## Usability and accessibility

Where a human is part of the control (login, recovery, consent, admin impersonation), the journey must remain usable and accessible (WCAG 2.2 final as the web baseline). Do not rely on color, mouse-only, or memory-only secrets.

## Misconceptions to refuse

- Residual risk is a yellow scanner
- Usability is the opposite of security; accessibility is later compliance
- Work factor is key length
- Users who bypass a control are the problem

## Non-goals

Live-target attacks, real PII, production secrets, and treating this lesson as a product tutorial.
