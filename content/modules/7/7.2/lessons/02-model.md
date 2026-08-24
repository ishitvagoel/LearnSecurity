# 7.2 — Object, property, and function security (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | member vs admin |
| Objects | secret_internal, title |
| Actions | resolve |
| Channels | field picker, GraphQL |
| TCB | Per-field policy. |
| Untrusted | requested field names |
| State / time | One query. |
| 1.1 cell | Authorization at property grain. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| member | title | resolve | allow |
| member | secret_internal | resolve | deny |
| admin | secret_internal | resolve | allow-audit |
| anon | title | resolve | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/7.2/7.2-lab` file `field.py`.

## Transfer

Bulk update; search highlighting leaking snippets.

## Residual risk

Admin sees secret_internal — audited.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
