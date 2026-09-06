# Review of an all-powerful runtime role

**Kind:** code-review
**Loop step:** Review

Intended findings live only in the answer-key folder — not here. Do not open that file until your review has been evaluated.

## What you are reviewing

A colleague ships the notes app’s database role. Review `labs/3.3/3.3-lab/vulnerable/` as that change. Your job is not to count suspicious lines. Reconstruct whether `can_select("app", "tB", "tA")` is still true, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_app_role_cannot_read_other_tenant`) is the rule test. A comment “row-level security later” is not.

## Picture: DATABASE_URL uses superuser

Start with this seeded smell: **`DATABASE_URL` uses superuser**. Label it rule, tool, or false comfort before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"can_select app tB tA is True"| Property["Rule — good if tested"]
  Q -->|"we use microservices"| Mechanism[Tool — no same-company check]
  Q -->|"VPC is isolation"| False[False comfort]
```

Classification starts at the protected effect (tB cannot SELECT tA). Everything that is not a same-company check at that call is a leftover path.

## Problems to find (name them yourself)

- `DATABASE_URL` uses superuser
- Comment “row-level security later” in the production path
- Analytics role `SELECT *`
- No test that `can_select("app", "tB", "tA") is False`

Also reject: treating the client as what you trust; closing findings without re-running `test_app_role_cannot_read_other_tenant`; keys in learner notes; real personal data in practice files; a manufacturer pledge as GRANT.

## Common mix-ups

- Microservices are automatically isolated
- A later row-level rule replaces who-is-allowed (the handler check remains required)
- A private network is company isolation
- SQLAlchemy session is the same-company check
- A managed-database product name is the second check

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false comfort, suggested structural change, leftover you will **not** delete. Tie at least one to `test_app_role_cannot_read_other_tenant`. Do not open the keys file.

## Use it somewhere new

A serverless change that “uses a managed database” without a same-company check is an incomplete review. Name the independent falsehood that would still keep `tB` from reading `tA`.

## What this page is not doing

Do not merge by adding a comment “row-level security later.” That comment is leftover risk without an owner. Do not connect to a live cloud database to prove the finding.
