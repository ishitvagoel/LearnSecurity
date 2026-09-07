# The broken files must fail when company B reads company A

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We have row-level security in the backlog” is not evidence. “Private subnet” is a topology observation. The check is: `can_select("app", "tB", "tA") is False`. That observation must be **false** on the broken files (the helper returns true) and **true** on the repaired files.

## Picture: broken must fail — tB reads tA

A check that only counts passing cases can still look green while tB still reads tA. Repaired files still have to deny the other company and still allow own-company read.

```mermaid
flowchart LR
  V["broken files"] --> F["Must fail: tB reads tA"]
  X["repaired files"] --> P["Must pass: deny plus own-company allow"]
```

| Mode | Must show for this topic |
|---|---|
| Normal | After the fix, `can_select("app", "tA", "tA") is True` |
| Wrong input / abuse | `can_select("app", "tB", "tA") is False`; broken files must fail that check |
| When things break | migrator cannot SELECT at runtime; connection is not `postgres` |
| Not claimed | Production row-level security; replica fleet; SQL injection complete |

The checks live in `labs/3.3/3.3-lab/tests/test_property.py`. `test_app_role_cannot_read_other_tenant` is there so a shared app role reading tA as tB cannot sneak through.

```text
python3 -m pytest labs/3.3/3.3-lab/tests --impl vulnerable
python3 -m pytest labs/3.3/3.3-lab/tests --impl fixed
```

Map each test to a row you wrote on the compartments page. Do not paste keys. If the broken files do not fail the cross-company check, the lab is miswired — fix the wiring, not the check. A setup error is not proof the rule holds.

## What the tests do not prove

- SQL injection beyond the forgotten-WHERE analogy
- Table-owner / function-as-owner walk-around (later topic)
- Billing replica (transfer)
- Kubernetes network policy
- That who-is-allowed handler checks are present (they remain required)

## Practice

Write fail or pass next to the matrix row. Reject a “test” that only greps `GRANT` in a migration without calling `can_select`.

## Use it somewhere new

A serverless admin string. A test that only asserts HTTP 200 is not architecture evidence. A test that connects to a live cloud database is out of scope.

## What this page is not doing

Do not add a live database. Do not log note bodies. Answer keys are not on this site.
