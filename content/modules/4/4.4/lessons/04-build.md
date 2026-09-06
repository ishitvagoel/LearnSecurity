# 4.4-LO-04 — Key the grant by tenant and note id

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-8.2.2`, `v5.0.0-8.3.1`, `v5.0.0-8.4.1`. `v5.0.0-8.3.2` and `v5.0.0-8.3.3` are **Level 3, advanced**.

## Structural means the lookup is on this object

`can_read` must deny unless tenant matches **and** the user is the note owner **or** `GRANTS[(user, note_id)]` is true. Structural means the object is mediated — not a denylist of yesterday’s ids, not “hide the button,” not UUID length, not “they are a collaborator.”

The smallest restore for SecureCollab Phase 1 notes is: deny-by-default, then tenant equality, then owner or grant on **this** id. Fail-safe: missing note, missing user, or missing grant is **deny**. Do not fail open because the id “looks valid.”

## Mental model: deny default, then two keys

```mermaid
flowchart TD
  Call["can_read user note_id"] --> Known{"note and principal exist?"}
  Known -->|no| Deny[Deny]
  Known -->|yes| Ten{"same tenant?"}
  Ten -->|no| Deny
  Ten -->|yes| Own{"owner or grant on this id?"}
  Own -->|no| Deny
  Own -->|yes| Allow[Allow]
```

The lab’s fixed tree compares tenant then owner/grant. Module 3.3 adds a database role as a *second* mediation; this table is still required. A clinic admin named `eve` is not an acme capability. PostgreSQL RLS waits for 5.5 and does not replace this cell.

ASVS `v5.0.0-8.3.1` wants enforcement at a trusted service layer, not the Next.js client. This pytest is that sentence for `can_read`.

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

`Depends(get_user)`. Signed ids as capabilities. Casbin file without tests. RLS as a substitute (5.5). Worker `user_id` (7.4 / `v5.0.0-8.3.3` advanced). API1 as the finding title.

## Mechanism limits

- UUID obscurity is not a grant.
- GraphQL `node(id)`, export zip, search index (2.2), workers (7.4) are other paths of the same cell.
- Property-level title-vs-body is 7.2; this lab is object + tenant.
- Honest grant on n1 still reveals n1 — that is the product.
- Grant revocation lag is `v5.0.0-8.3.2` advanced.

## Practice

Name subject, tenant, object, and predicate. Run:

```text
python3 -m pytest labs/4.4/4.4-lab/tests --impl fixed
```

Must pass.

## Transfer

Clinic: appointment grant table keyed by chart id and tenant, not by “clinician role.”

## Residual risk

Search/export/GraphQL paths; grant revocation lag; honest n1 still readable; 3.3 DB role still required.

## Non-goals

Do not connect a live tenant. Do not claim Gate 4 from an RBAC product name.
