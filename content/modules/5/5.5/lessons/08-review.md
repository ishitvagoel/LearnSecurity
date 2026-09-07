# Review of concatenated SQL

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

You are reviewing persistence. Label each claim **rule**, **tool**, or **false assurance**. Say whether `fetch_sql` still returns a concatenated `str` if they ship. Start at concatenated SQL, not at an ORM sticker.

Do not treat “will parameterize later” as a green `test_query_is_bound_not_concatenated`.

## Picture: problems to find (name them yourself)

**f-string `SELECT` that interpolates `note_id`**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"concatenated str"| Property["Rule - good if tested"]
  Q -->|"quote denylist"| Mechanism[Tool - still grammar]
  Q -->|"row-level rule in prod"| False[False assurance]
```

`fetch_sql` is a bound tuple. If the change never uses a params tuple, that grammar mix is still open. `%s` inside a concatenated string is still the same problem.

## Problems to find (name them yourself)

- f-string `SELECT` that interpolates `note_id`
- ORM `.filter` with raw strings
- Row-level rule disabled in tests “for speed” and forgotten
- No `is_bound` assertion

Also reject: live SQL attacks; closing findings without re-running `test_query_is_bound_not_concatenated`; keys in learner notes; web filter as the rule; payload cookbooks in the change.

## Common mix-ups

- ORM means no injection
- A later row-level rule replaces parameterization
- A denylist of quotes is complete mediation
- A scanner finding is the rule
- HTTP 500 absence means the query was bound

## Use it somewhere new

Clinic change that “switched to SQLAlchemy” without a bound-tuple test is an incomplete review of concatenated SQL. Name the independent falsehood that would still keep `fetch_sql` from returning a `str`.

## What this page is not doing

A concatenation path with only “will parameterize later” has no owner. Do not probe a live database to prove the finding.
