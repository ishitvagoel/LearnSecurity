# 1.2-LO-01 — Subjects, objects, actions, matrix vs capability vs ambient authority

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** Saltzer & Schroeder (1975, seminal) — least privilege, complete mediation, fail-safe defaults, separation of privilege, open design; CISA Secure by Design (current public guidance, final) — secure defaults as the manufacturer’s job; OWASP ASVS 5.0.0 (final) chapters V8 Authorization and V15 architecture (chapter-level only).

## Property (start here)

For **SecureCollab** notes in Phase 1: **a member of tenant B must not read tenant A’s note body**, even if they are logged in, can guess or observe a note id, and can call the same FastAPI handler alice uses.

That is an **authorization invariant**. “We require JWT / session cookies / `Depends(get_current_user)`” is a **mechanism**. Login answers *who is authenticated*. It does not answer *may this subject perform this action on this object*.

## Attacker capabilities and trust assumptions

- **Attacker:** a logged-in member of another tenant; anyone who can send HTTP to the local lab API; later, a stolen worker identity (preview).
- **Trust:** application policy in the FastAPI process is in the TCB for this lab. The Next.js bundle is **not**. PostgreSQL roles are **not** yet the mediator (that is 5.5). Open design: assume the check’s location is known.

## Vocabulary (use these names)

| Name | SecureCollab example |
|---|---|
| Subject | `alice` (member, tenant `tA`); `bob` (member, tenant `tB`) |
| Object | Note `n1` (tenant `tA`) |
| Action | `read` |
| Access matrix cell | (alice, n1, read) = allow; (bob, n1, read) = deny |
| Capability | An unforgeable token that *is* the right (not used in Phase 1 notes UI) |
| Ambient authority | Process-wide `current_user` used as if it granted every object |

Ambient authority is leftover environment rights (shared DB user, global admin flag, “any authenticated user”) that were **not** granted for this object.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | This invariant |
|---|---|
| Root cause | Mediation skipped: handler trusts ambient login without a subject–object rule |
| Preconditions | Bob is a valid user; `n1` exists; local fixture only |
| Impact | Tenant A confidentiality (1.1) fails through an authorization hole |
| Prevention | Check tenant (or equivalent policy) on **this** object; deny on uncertainty |
| Detection | Log denied cross-tenant reads **without** note bodies |
| Recovery | Revoke bob’s session if it was stolen; notify tenant A if the body leaked |

## Framework defaults vs application guarantees

FastAPI security dependencies prove a user is authenticated if you wired them. They do **not** implement the matrix. `admin` as one ambient superuser is not Saltzer separation of privilege.

## Mechanism limits

A denylist of user ids, a scanner “IDOR” label, or hiding note ids (capability-by-obscurity) does not restore the cell when a third tenant or an export path appears. ASVS V8 is a requirement catalogue, not proof the matrix is complete.

## Practice

Write the four cells for `{alice, bob} × {n1, n2}` for action `read`. Mark which cell the vulnerable lab violates.

## Transfer (preview of LO-07)

Support impersonation: can support read `n1`? Under whose authority? That is a new subject, not “admin is true.”

## Usability

A matrix people cannot complete (mouse-only admin, color-only “allowed”) will be bypassed (1.4, WCAG 2.2).
