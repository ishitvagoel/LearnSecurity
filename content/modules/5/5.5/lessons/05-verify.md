# Glued-together SQL must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We parameterized queries” is not evidence. “ORM is on” is a tool observation. The check is: `fetch_sql` is not a `str`, and `is_bound` is true for the `(sql, params)` shape. That observation must be **false** on the broken files (returns concatenated SQL) and **true** on the repaired files.

## Picture: concatenated SQL must fail the check

A passing-test tally can still hide that the query is still glued.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: concatenated str]
  X["repaired files --impl fixed"] --> P[Must pass: is_bound]
```

If both pass, you are not looking at concatenated SQL.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | Honest company and note id are still a bound tuple |
| Wrong input / abuse | Concatenated SQL is not bound; hostile punctuation stays a param |
| Failure | If you cannot bind, do not query |
| Not claimed | ORDER BY identifiers; live row-level rules; NoSQL operators |

The test `test_query_is_bound_not_concatenated` is there so a concatenated `str` still fails. The hostile `note_id` in that test is **data** for the params tuple — a class of extra grammar, not a cookbook to paste into a live query.

Searching for `%s` inside a concatenated string without asserting the tuple shape is not evidence. This practice never opens a live database.

```text
python3 -m pytest labs/5.5/5.5-lab/tests --impl vulnerable
python3 -m pytest labs/5.5/5.5-lab/tests --impl fixed
```

Honest bound shape must pass on repaired. Concatenated `str` must fail on broken. If the broken files do not fail the `isinstance(q, str)` branch, the lab is miswired — fix the wiring, not the assertion. A setup error is not proof the rule holds.

## What the tests do not prove

- Identifier allow-lists for ORDER BY (named leftover)
- Cross-company 1.2 without a stolen query (3.3 / 4.4)
- Backup/restore of changed rows (5.1)
- Advanced who-is-allowed-decision logging
- GraphQL / NoSQL operator injection (7.1)

## Practice

```text
python3 -m pytest labs/5.5/5.5-lab/tests --impl vulnerable
python3 -m pytest labs/5.5/5.5-lab/tests --impl fixed
```

Do not treat a grep for `%s` inside a concatenated string as the check. Assert the tuple shape.

## Use it somewhere new

Clinic search box. Asserting HTTP 200 is not this check (see 9.3). Do not run a test that hits a live clinic system.

## What this page is not doing

Do not treat a live SQL screenshot as proof. Do not log bound parameter values that are bodies. Answer keys are not on this site.
