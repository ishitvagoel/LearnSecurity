# Honest rename vs is_admin vs unknown keys

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We have OpenAPI” is not evidence. “The SPA has no admin checkbox” is a tool observation. The check is three observations, not one: an honest rename may change `display_name`; after `apply(user, {"is_admin": true})`, `is_admin` is false; unknown keys do not become columns. The `is_admin` observation must be **false** on `--impl vulnerable` (`user.update(body)` writes true) and **true** on `--impl fixed`. Do not probe public APIs.

## Picture: broken files must fail: is_admin

A passing-test tally can still hide that extra keys still write `is_admin`.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail is_admin"]
  X["--impl fixed"] --> P["Must pass is_admin false"]
```

If both pass, you are not looking at extra keys.

## Three things to look at

| Mode | Must show for this topic |
|---|---|
| Normal | Honest `display_name` may change (`test_display_name_can_be_patched`; may pass on both) |
| Wrong input / abuse | `is_admin` stays false; broken files must fail (`test_is_admin_cannot_be_patched`) |
| Extra | Unknown keys do not become columns (`test_unknown_key_does_not_appear`) |
| Not claimed | GraphQL cost; unused methods; production inventory matches OpenAPI |

The checks are in `labs/7.1/7.1-lab/tests/test_property.py`. `test_is_admin_cannot_be_patched` is there so a binder that writes `is_admin` still fails.

```text
python3 -m pytest labs/7.1/7.1-lab/tests --impl vulnerable
python3 -m pytest labs/7.1/7.1-lab/tests --impl fixed
```

Patching `display_name` may pass on both sides. You still have to drop `is_admin` from the body. If the broken files do not fail `test_is_admin_cannot_be_patched`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- GraphQL schema listing off in production
- Query cost (6.7)
- Unused HTTP methods (leftover, later, advanced)
- That OpenAPI matches every running handler
- Field *reads* of privileged columns (7.2)
- Job-payload binders (7.4)

## Practice

Do not treat a grep for `extra = 'forbid'` in a Pydantic model as the check. Call `apply(..., {"is_admin": true})`. A setup error is not proof the rule holds.

## Use it somewhere new

Clinic PATCH `{is_staff:true}`. Asserting HTTP 200 on `/patients/{id}` is not this check (see 9.3). Do not use a public API probe.

## What this page is not doing

Do not treat a live OpenAPI screenshot as proof. Do not log PATCH bodies. Answer keys are not on this site.
