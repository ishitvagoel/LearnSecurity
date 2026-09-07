# Review of an all-powerful runtime role

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships the notes app’s database role. Review `labs/3.3/3.3-lab/vulnerable/` as that change. Check whether `can_select("app", "tB", "tA")` is still true, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_app_role_cannot_read_other_tenant`) is the rule test. A comment “row-level security later” is not.

## Picture: DATABASE_URL uses superuser

**`DATABASE_URL` uses superuser**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"can_select app tB tA is True"| Property["Rule — good if tested"]
  Q -->|"we use microservices"| Mechanism[Tool — no same-company check]
  Q -->|"VPC is isolation"| False[False assurance]
```

What has to stay true: tB cannot SELECT tA. If that call never includes a same-company check, that leftover path is still open.

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

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one to `test_app_role_cannot_read_other_tenant`. Do not open the keys file.

## Use it somewhere new

A serverless change that “uses a managed database” without a same-company check is an incomplete review. Name the independent falsehood that would still keep `tB` from reading `tA`.

## What this page is not doing

Do not merge by adding a comment “row-level security later.” That comment is leftover risk without an owner. Do not connect to a live cloud database to prove the finding.
