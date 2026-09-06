# SecureCollab Phase 1 — residual risk and usable recovery

Design stub for Module 1.4. Not a production runbook.

## Freeze

- Tenants, memberships, notes, and a **local recovery-confirm fixture**.
- No live IdP, no real mailboxes, no patient or banking data.

## Decision loop

Invariant (1.1) → actor capability and incentive → harm → control (1.2 + 1.3 + usable human path) → residual with owner and trigger → detect/recover when prevention is not absolute.

## Two work factors

Attacker cost to coerce, phish, or wait versus user cost to see, aim, remember, and confirm under stress. If user cost is impossible, the control has failed (lockout or workaround).

## Residual that must remain explicit

Coercion by a physically present attacker is not removed by WCAG. Support reading codes aloud is a new 1.2 cell, not a usability win.
