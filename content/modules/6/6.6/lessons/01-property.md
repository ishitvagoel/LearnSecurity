# 6.6 — Workflow, race, and exceptional-condition failures (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
**Mechanism (not the property):** DB unique constraint helps but must be the actual consume.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.6 |
|---|---|
| Root cause | Non-atomic check-then-set; token not marked used. |
| Preconditions | second accept True. |
| Impact (1.1 cell) | Integrity of membership workflow. — Extra member or replay after revoke. |
| Prevention | Single-use in a transaction; expire; bind to recipient. |
| Detection | token_replay metric. |
| Recovery | Remove extra membership; rotate token scheme. |

## Framework defaults vs application guarantees

DB unique constraint helps but must be the actual consume.

## Mechanism limits and bypasses

Used flag without locking still races.

New token via fail-open email error.

## Residual risk

Email is a phishable channel (4.2).

## Practice

State: issued → consumed → dead.

Run `labs/6.6/6.6-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

Clinic invite-guardian token.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Invite errors (“link already used”) must be announced accessibly so people do not retry into a support backdoor.
