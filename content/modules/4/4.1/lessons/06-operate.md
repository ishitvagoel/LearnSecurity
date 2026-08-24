# 4.1 — Identity lifecycle (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Use of session after user_state=deleted. |
| Signal (no bodies) | session_after_delete; offboarding checklist in 10.1. |
| Revoke / recover | Mass revoke; rotate signing keys if tokens self-verify. |
| Residual | Backups still contain the user row — 5.1. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/4.1/4.1-lab`.

## Transfer

Contractor access end-date; support impersonation tickets.

## Usability

Offboarding confirmation must be accessible (1.4). A mouse-only “delete user” is a missed revoke.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
