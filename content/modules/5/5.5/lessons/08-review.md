# Review of concatenated SQL

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships notes-app persistence. Your job is to label each claim **rule**, **tool**, or **false assurance**, and to say whether `fetch_sql` still returns a concatenated `str` if they ship. Start at concatenated SQL, not at a scanner color.

The folder `labs/5.5/5.5-lab/vulnerable/` is the change. The check you already ran (`test_query_is_bound_not_concatenated`) is the rule test. A comment “will parameterize later” is not.

## Picture: problems to find (name them yourself)

Look at this first: **f-string `SELECT` that interpolates `note_id`**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"concatenated str"| Property["Rule - good if tested"]
  Q -->|"quote denylist"| Mechanism[Tool - still grammar]
  Q -->|"row-level rule in prod"| False[False assurance]
```

Keep this: `fetch_sql` is a bound tuple. If that call never includes a params tuple, that grammar mix is still open. `%s` inside a concatenated string is still the same problem.

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

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_query_is_bound_not_concatenated`. Do not open the keys file.

## Use it somewhere new

Clinic change that “switched to SQLAlchemy” without a bound-tuple test is an incomplete review of concatenated SQL. Name the independent falsehood that would still keep `fetch_sql` from returning a `str`.

## What this page is not doing

Do not merge by adding a comment “will parameterize later.” That comment is leftover without an owner. Do not probe a live database to prove the finding.
