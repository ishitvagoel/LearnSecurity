# 4.4-LO-04 — Key the grant by tenant and note id

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-8.2.2`, `v5.0.0-8.3.1`, `v5.0.0-8.4.1`.

## Structural means the lookup is on this object

`can_read` must deny unless tenant matches **and** the user is the note owner **or** `GRANTS[(user, note_id)]` is true. Structural means the object is mediated — not a denylist of yesterday’s ids, not “hide the button,” not UUID length.

## Mental model: deny default, then two keys

```mermaid
flowchart TD
  Call["can_read user note_id"] --> Known{note and principal exist?}
  Known -->|no| Deny[Deny]
  Known -->|yes| Ten{"same tenant?"}
  Ten -->|no| Deny
  Ten -->|yes| Own{"owner or grant on this id?"}
  Own -->|no| Deny
  Own -->|yes| Allow[Allow]
```

Fail-safe: missing note, missing user, or missing grant is **deny**. Do not fail open because the id “looks valid.”

## Why this restores the cell

| After the fix | Must be true |
|---|---|
| bob × n1 | allow (honest grant) |
| bob × n2 | deny |
| alice × n2 | allow (owner) |
| alice × n3 | deny (cross-tenant) |
| eve × n1 | deny (admin ≠ acme) |
| eve × n3 | deny (admin ≠ object grant) |

## What this is not

`Depends(get_user)`. Signed ids as capabilities. Casbin file without tests. RLS as a substitute (5.5). Worker `user_id` (7.4 / `v5.0.0-8.3.3` advanced).

## Practice

Name subject, tenant, object, and predicate. Run:

```
python3 -m pytest labs/4.4/4.4-lab/tests --impl fixed
```

Must pass.

## Transfer

Clinic: appointment grant table keyed by chart id and tenant, not by “clinician role.”

## Residual risk

Search/export/GraphQL paths; grant revocation lag (`v5.0.0-8.3.2` advanced); honest n1 still readable.
