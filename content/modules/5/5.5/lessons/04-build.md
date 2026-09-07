# Bind company and note id as parameters

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

A denylist of quotes is not the fix. “The ORM will handle it” is not the fix. A later row-level rule on in production and off in tests is not the fix.

Structural means the parser never sees those fields as grammar. Bind tenant and note id as parameters. `fetch_sql` must return `(sql, params)` with `%s` placeholders and a two-tuple of values.

The smallest restore for notes-app note fetch is: program beside data. Fail closed: if you cannot bind, **do not query**. Do not fail open because the id “looks like a UUID.”

## Picture: program beside data

```mermaid
flowchart TD
  Call[fetch_sql] --> Pair["sql text + params tuple"]
  Pair --> Bound{"is_bound?"}
  Bound -->|yes| Allow[Allow]
  Bound -->|no| Deny[Deny]
```

The lab’s repaired files return SQL text with `tenant=%s AND id=%s` and a `(tenant, note_id)` tuple. Production still needs 1.2 object grants (4.4) and a 3.3 database role as *second* checks. Identifier concatenation for ORDER BY stays leftover: allow-list column names instead of binding them as values. NoSQL operators and GraphQL arguments wait for 7.1 as the same shape.

Use parameterized queries. This week's check looks at `fetch_sql`.

## What the repaired files must show

Open `fixed/query.py`. Do not treat the snippet as a production query builder.

| After the fix | Must be true |
|---|---|
| honest `tA`, `n1` | bound tuple |
| hostile punctuation in `note_id` | still a param, still not a `str` query |
| `is_bound` | true only for the tuple shape |

Fail closed: if you cannot bind, the answer is no query. Uncertainty is a **deny**, not a yes because the id looked well-formed.

## What this is not

SQLAlchemy `text()` with an f-string. ORM `.filter` with a raw interpolated string. A later row-level rule as a substitute. Quote denylist. Web-filter signature. Scanner “parameterized” badge.

## What the tool cannot do

- ORDER BY / `COPY` / search language still mix identifiers with grammar unless allow-listed.
- 3.3 database role and 4.4 object grants remain required; this check is the interpreter.
- Replicas and backups (5.1) can still hold changed rows if concatenation already ran.
- `%s` *inside a concatenated string* is not `is_bound`.
- Advanced who-is-allowed-decision logging is not this practice.

## Practice

Name the check (`tuple` ∧ `"%s"` in sql ∧ params length 2). Run:

```text
python3 -m pytest labs/5.5/5.5-lab/tests --impl fixed
```

## Use it somewhere new

A clinic example: stop treating the search box as SQL text; bind the lookup string.

## What can still go wrong

ORDER BY identifiers; replicas; row-level-rule theater; 3.3 role still required; 7.1 same shape.

## What this page is not doing

Do not connect a live company. Do not claim a course gate from an ORM brand.
