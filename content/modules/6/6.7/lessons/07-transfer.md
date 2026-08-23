# 6.7-LO-07 — Novel variation of 6.7

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer / generalize  
**Standards:** OWASP ASVS / module anchors (see spec) 5.0.0 (final). Awareness lists (Top 10, CWE Top 25) are regression checks, not the outline.

## Property (start here)

What must remain true of **SecureCollab** (or the elective system) regarding **Resource abuse, automation, and availability** when an attacker with stated capabilities acts, a component fails, or a human follows a stressful recovery path?

Invariant prompt for this object: Claims are properties of SecureCollab (or the elective system), not tool names; Labs stay in authorized local or official training scope; Draft standards are labeled draft

## Attacker capabilities and trust assumptions

State both, or the claim is a slogan:

- **Attacker:** anyone who can reach the local lab API; a logged-in member of another tenant; a stolen worker identity; a hostile mobile client where Phase 8 applies.
- **Trust:** FastAPI + PostgreSQL with least-privilege roles are in the TCB for server-side mediation; the Next.js bundle and Android client are **not**. Lab honesty is assumed; no public targets.

Threat-model prompts from the spec:

- What can go wrong for this module's assets?
- Which trust boundary or interpreter is in play?
- What residual remains if the primary control fails?

## Root cause, preconditions, impact, prevention, detection, recovery

| Slice | For Resource abuse, automation, and availability |
|---|---|
| Root cause | Wrong trust in a mechanism, skipped mediation on an indirect path, or a confused interpreter — not “missing a scanner finding.” |
| Preconditions | The local fixture is reachable; the learner is authorized only on this lab; synthetic data only. |
| Impact | Tenant notes, identity, or availability of SecureCollab can fail the named property. |
| Prevention | Smallest structural mechanism that restores the invariant (not a blacklist-only patch). |
| Detection | Logs/alerts that fire when the forbidden outcome is attempted. |
| Recovery | Revoke, rotate, purge, restore from a known-good backup, and record residual risk. |

## Framework defaults vs application guarantees

FastAPI, Next.js, PostgreSQL, or Android “secure defaults” are not the application guarantee for **Resource abuse, automation, and availability**. Name what the app must still enforce.

## Mechanism limits

A green scanner, a named product (JWT, TLS, bcrypt), or an awareness-list item does not prove the invariant. Universal checkboxes fail when risk-based selection is required.

## Practice (local, authorized)

Complete the associated lab under `labs/6.7/` if a labSpec exists. Observe the forbidden outcome on `vulnerable/`. Do not target non-lab systems. Do not copy weaponized payloads into notes.

Safe task: write one testable sentence that would fail if the **resource** property were false.

## Transfer

Change one asset, principal, or boundary (new worker, webhook, offline cache, or clinic-booking card). Redraw the claim without using a Top 10 item as the definition of security.

## Usability and accessibility

Where a human is part of the control (login, recovery, consent, admin impersonation), the journey must remain usable and accessible (WCAG 2.2 final as the web baseline). Do not rely on color, mouse-only, or memory-only secrets.

## Misconceptions to refuse

- Resource abuse, automation, and availability is a Top 10 memorization exercise
- Framework defaults are application guarantees
- A green scanner proves the invariant

## Non-goals

Live-target attacks, real PII, production secrets, and treating this lesson as a product tutorial.
