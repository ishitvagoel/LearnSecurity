# 1.4-LO-01 — Residual risk, friction, and resilience as security properties

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST SP 800-63-4 (final) for CX/friction as security outcomes (not the full authenticator catalog); WCAG 2.2 (final); SAMM 2.0 (final) for not treating maturity scores as product proof; CISA Secure by Design (final).

## Property (start here)

If SecureCollab recovery is **unusable or inaccessible**, which 1.1 invariants fail? Often **safety** (coerced/locked-out user) and **accountability** (shared admin session). That is not “UI polish.”

## Attacker capabilities and trust assumptions

- **Attacker:** bulk password spraying (work factor); a tenant-mate who borrows a session because recovery failed; a coerced user.
- **Trust:** lab honesty; IdP/email not yet in TCB (1.3 transitive).

Residual risk is owned, dated, and tied to an invariant — not “scanner yellow.” SAMM scores are practice maturity, not note confidentiality.

## Root cause / impact / prevention / detection / recovery

Root cause: color-only confirm (lab). Impact: people bypass to ambient admin (1.2). Prevention: WCAG 2.2 operable named control. Detection: lockout tickets. Recovery: mediated degrade, not emailing passwords.

## Practice

Write one residual with owner and revisit trigger for inaccessible recovery.

## Transfer

Change actor to **coercion**: does a second-device-only recovery still hold?
