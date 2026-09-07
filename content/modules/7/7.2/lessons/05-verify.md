# Honest display_name vs secret_internal

**Kind:** verification-lab
**Loop step:** 5 Verify

## Until you can fail it, it is still a slogan

“Field authz is on” is not evidence. “The SPA hides the column” is a tool observation. The check is: `resolve("member", "secret_internal")` is false **and** `resolve("member", "display_name")` is true. The member-internal observation must be **false** on `--impl vulnerable` (returns true) and **true** on `--impl fixed`. Do not query public GraphQL.

## Picture: broken files must fail member × secret_internal

A check that only counts passing cases can still look green while a member still resolves `secret_internal`. Honest `display_name` may pass on both — that is the product, not an excuse to skip the deny.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail member secret_internal"]
  X["--impl fixed"] --> P["Must pass deny"]
```

If both pass, the check is not looking at the field table. If both fail, the fix is not structural or the check is wrong.

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | member × `secret_internal` false; broken files must fail |
| Normal | member × `display_name` true (may pass on both) |
| Service | service × `secret_internal` true |
| Not claimed | object×company (4.4); extra-key writes (7.1); advanced cache leftover |

The checks live in `labs/7.2/7.2-lab/tests/test_property.py`. `test_member_cannot_resolve_internal_field` is there so a dump that always returns true cannot sneak through. `test_member_can_resolve_display_name` is the honest path.

```text
python3 -m pytest labs/7.2/7.2-lab/tests --impl vulnerable
python3 -m pytest labs/7.2/7.2-lab/tests --impl fixed
```

Honest `display_name` may pass on both implementations. That does not excuse the member-internal deny test. If the broken files do not fail `test_member_cannot_resolve_internal_field`, the lab is miswired — fix the wiring, not the assertion. A setup error is not proof the rule holds.

## What the checks do not prove

- Immediate grant change through caches (advanced leftover)
- CSV / search / worker serializers
- That GraphQL production matches REST
- Object×company (4.4) — a passing field test does not prove Bob cannot GET Alice’s note
- Extra-key writes (7.1)

Write those down as leftover risk or later topics, not as silent passes.

## Practice

Execute both implementations this session from the lab directory if needed. Write the fail/pass pair next to the table row. Reject a “test” that only greps `@hide` in a GraphQL schema without calling `resolve("member", "secret_internal")`.

## Use it somewhere new

A clinic example: a test that only asserts HTTP 200 on `/patients/{id}` is 4.4, not this rule. A public GraphQL query is out of scope.

## What this page is not doing

Do not treat a live schema screenshot as proof. Do not log `secret_internal` values. Answer keys are not on this site.
