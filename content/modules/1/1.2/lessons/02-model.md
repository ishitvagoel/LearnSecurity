# 1.2-LO-02 — SecureCollab authority map and access matrix

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** Saltzer complete mediation and least privilege (1975, seminal); ASVS 5.0.0 V8 (final) as later testable requirements, not this exercise’s grading rubric.

## Property (start here)

Can a second engineer **execute** your matrix as tests without asking you what “member” meant?

## Attacker capabilities and trust assumptions

- **Attacker:** another tenant’s member; an org admin of tenant A who should not become ambient admin of tenant B; a future file object (named now as a review trigger).
- **Trust:** you are drawing policy, not deploying production. Synthetic names only.

## Draw the map (Phase 1)

**Subjects:** org (tenant), member, admin-of-this-tenant. Non-goal this phase: support impersonation, workers, webhooks (name them as **out of matrix** or you will forget them later).

**Objects:** tenant record, user record, note (body + id). Files: **non-goal**, listed as a hole.

**Actions:** read, create, update, delete, list. List is a different action from read-body (IDOR vs enumeration).

## Matrix (minimum)

Fill allow/deny/non-goal. Example rows (complete yours):

| Subject | Object | Action | Decision | Why (principle) |
|---|---|---|---|---|
| member tA | note n1 (tA) | read | allow | least privilege still allows own notes |
| member tB | note n1 (tA) | read | deny | fail-safe; not “unless they have the URL” |
| admin tA | note n1 (tA) | delete | allow? | if yes, is that one privilege or separated? |
| member tA | note n1 | list-other-tenant | deny | list ≠ read; still mediated |

Indirect paths to mark even if unimplemented: bulk export, admin JSON, search index, “share by link.” If the HTTP handler is the only check, write **complete-mediation risk**.

## Root cause / impact / prevention / detection / recovery

Skipping a cell is how ambient authority appears. Impact is a 1.1 confidentiality or integrity failure. Prevention is an explicit cell. Detection is a denied-action log. Recovery is revoke + notify.

## Practice

Produce a one-page matrix someone else can turn into pytest names (`test_bob_cannot_read_n1`).

## Transfer

Add **file** as an object class. Which cells copy from notes, and which must not (download vs preview vs delete)?
