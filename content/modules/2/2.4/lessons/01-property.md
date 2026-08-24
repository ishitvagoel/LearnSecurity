# 2.4 — State, time, concurrency, and distributed failure (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
**Mechanism (not the property):** FastAPI does not dedupe POSTs. HTTP 201 twice is still two rows.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 2.4 |
|---|---|
| Root cause | Non-idempotent side effect + retry = extra grant. |
| Preconditions | Timeout; client retries same key; handler inserts again. |
| Impact (1.1 cell) | Integrity of authorization state over time. — Extra principal on the note (1.2 cell changes). |
| Prevention | Persist key → share id; second POST returns the first. |
| Detection | Duplicate-key metric; share_count anomaly. |
| Recovery | Revoke extra shares; notify owner. |

## Framework defaults vs application guarantees

FastAPI does not dedupe POSTs. HTTP 201 twice is still two rows.

## Mechanism limits and bypasses

Keys that expire too fast replay as new shares.

New key each retry (client bug); GET-with-side-effect.

## Residual risk

Lost first response still needs a read-your-write path.

## Practice

Draw the state machine: pending → shared; retry edges labeled.

Run `labs/2.4/2.4-state-time` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

Clinic: double-book the last slot.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Disable-on-submit is not the property (users retry). Accessible “still working” status (WCAG 4.1.3) must not encourage extra POSTs with new keys.
