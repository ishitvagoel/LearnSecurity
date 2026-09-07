# Coverage requires an isolation assert

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

Last week’s spreadsheet cells are not an isolation assert. Muting a scanner finding does not cover `AUTHZ-1`. Running the checklist once is not the repair.

The structural change is: `covered` **requires `req == req_id` and `asserts_isolation`**. A row that only stores status is uncovered. Structural means that conjunction — not “we ran the checklist,” not pytest-cov, not a tracker Done column.

The smallest fix for the notes app’s AUTHZ-1 tracking is: status-only → not covered. Fail-safe: a missing flag is false. Do not fail open because the PDF was attached. Do not accept “we ran the checklist” as the isolation flag.

## Picture: coverage and isolation are both gates

```mermaid
flowchart TD
  Call[covered] --> Req{req matches?}
  Req -->|no| Deny[not covered]
  Req -->|yes| Iso{asserts isolation?}
  Iso -->|yes| Allow[covered]
  Iso -->|no| Deny
```

The repaired files require both gates. Production still needs the later shape lesson (9.3): a test that sets `asserts_isolation` while only checking HTTP 200 is a lying flag. Extra advanced rows stay unmapped if you never raise them. Mobile storage without a matching test is the same hole on a phone (8.2). Exceptions need an expiry date (E6) or they are silent uncovered rows.

A development-practice guide that wants executable tests against requirements covers AUTHZ-1 status-only. The check is the local stand-in.

## What the repaired files must show

Do not treat `fixed/trace.py` as a production governance product.

| After the fix | Must be true |
|---|---|
| status-only row | `covered` false |
| isolation-assert row | `covered` true |
| empty list | `covered` false |

Fail closed: if you are unsure whether a test asserts isolation, it does not count. Uncertainty is a **no** on “this may count as coverage,” not a yes because the PDF was attached.

## What this is not

- pytest-cov.
- A tracker done column.
- Copied-wholesale checklists.
- A later draft of a practice guide used as a sticker.
- The verification gate complete.
- A test named `test_authz` that asserts HTTP 200 (9.3).

## What the tool cannot do

- A test named `test_authz` that asserts HTTP 200 is a later failure (9.3), not this check.
- Extra advanced rows stay unmapped if you never elevate them.
- A mobile storage spreadsheet without a matching test is the same hole on a phone (8.2).
- Exceptions without expiry (E6) are silent uncovered rows.

## Can people still use it

A human exception path must say what is still uncovered and when it expires. Do not hide the gap behind “see PDF.”

## Practice

Name the check (`req` matches **and** `asserts_isolation`). Run:

```text
python3 -m pytest labs/9.1/9.1-lab/tests --impl fixed
```

## Use it somewhere new

Mobile storage (8.2): require a matching test id, not a control-group checkbox.

## What can still go wrong

HTTP-200 tests that set `asserts_isolation` by mistake (9.3). Unnamed extra advanced rows. Exceptions without expiry (E6).
