# 1.2-LO-06 — Revoke and expire: who held which authority when

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST CSF 2.0 (final) Detect/Respond/Recover as *outcomes*; Saltzer compromise recording (1975, seminal). CSF does not prove ASVS.

## Property (start here)

If bob’s session is stolen, can an investigator see **that bob (or the thief) attempted n1**, without storing note bodies in the log (privacy ≠ ignore accountability)?

## Attacker capabilities and trust assumptions

- **Attacker:** stolen session cookie for bob; or bob himself enumerating ids.
- **Trust:** logs are another object class (1.3/5.1). Do not log `body`.

## Operate notes

- **Prevent** is not absolute: ids leak in URLs, clients, tickets.
- **Detect:** deny log `{subject, object, action, reason=cross-tenant}`.
- **Recover:** revoke session; rotate if you issued long-lived tokens (4.3).
- **Usability:** revocation UX must be keyboard-accessible (WCAG 2.2) or people will keep shared “admin” tabs.

## Practice

Write one log line you would accept in a review (no body, no real email).

## Transfer

Worker exports: the subject in the log is the **worker identity**, not “system.”
