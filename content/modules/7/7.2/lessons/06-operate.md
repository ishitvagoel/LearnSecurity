# 7.2 — Object, property, and function security (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | field_denied. |
| Signal (no bodies) | field_denied{field}. |
| Revoke / recover | Rotate the secret; audit. |
| Residual | Admin sees secret_internal — audited. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/7.2/7.2-lab`.

## Transfer

Bulk update; search highlighting leaking snippets.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
