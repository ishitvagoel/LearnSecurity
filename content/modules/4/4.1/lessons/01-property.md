# 4.1 — Identity lifecycle (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
**Mechanism (not the property):** Starlette SessionMiddleware does not know HR offboarding.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 4.1 |
|---|---|
| Root cause | Authentication artifact outlived the subject. |
| Preconditions | delete_user removes profile only. |
| Impact (1.1 cell) | Authorization over time (1.2 + 2.4). — Ex-employee or attacker with the cookie still reads tenant notes. |
| Prevention | Invalidate sessions (and tokens, workers) in the same use-case. |
| Detection | Use of session after user_state=deleted. |
| Recovery | Mass revoke; rotate signing keys if tokens self-verify. |

## Framework defaults vs application guarantees

Starlette SessionMiddleware does not know HR offboarding.

## Mechanism limits and bypasses

Email “you’re deleted” is not revocation.

Refresh tokens, mobile offline cache (8.2), shared device.

## Residual risk

Backups still contain the user row — 5.1.

## Practice

List every artifact that must die with the user.

Run `labs/4.1/4.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Contractor access end-date; support impersonation tickets.

Clinic: departing clinician.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Offboarding confirmation must be accessible (1.4). A mouse-only “delete user” is a missed revoke.
