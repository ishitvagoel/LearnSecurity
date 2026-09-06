# Lab 5.5 — note id is data, not SQL grammar

**Module:** `5.5`
**Authorized scope:** this directory only. Local course fixture. No live databases.
**Invariant:** `fetch_sql` returns a bound `(sql, params)` structure. Tenant and note id are not concatenated into SQL text.
**Root cause class:** data mixed into SQL grammar
**Non-goals:** live SQL attacks, weaponized cookbooks, ORDER BY identifier injection as an executed case.

## Reset

Re-run pytest. Optional: `git checkout -- labs/5.5/5.5-lab`.

## Vulnerable behavior (local only)

`fetch_sql` interpolates tenant and note id into the query string. Forbidden outcome: concatenated SQL.

## Structural fix

Return SQL with placeholders and a params tuple. `is_bound` is true only for that shape. A `%s` character inside a concatenated string is not a bound query.

## Verify

```
python3 -m pytest labs/5.5/5.5-lab/tests --impl vulnerable
python3 -m pytest labs/5.5/5.5-lab/tests --impl fixed
```

The first command must fail on the concatenated-SQL tests. The second must pass. Honest ids must still be bound on fixed.

## Operate

Signal: `sql_error_spike`. Do not log note bodies or SQL with values. Restore if rows mutated.

## Transfer

Clinic search box. Prompt only.
