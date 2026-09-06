# exception_incomplete_denied without logging secrets

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Stopping it is not enough

A new “fast-track risk” form can drop `review_by` after the schema was “set once.” Pair notice and recover. Do not log leftover-risk writeups that contain secrets. Do not paste chart text into the ticket.

## Picture: incomplete row is a signal

An accept that skipped owner, review date, or accessibility is a notice-and-recover problem, not a licence to quote secrets in the ticket. Notice names the missing fields. Recover expires the hole or re-accepts with a complete record. Neither reprints a secret.

```mermaid
flowchart TD
  Call[accept_exception] --> Ok{schema complete?}
  Ok -->|no| Metric["exception_incomplete_denied plus 1"]
  Metric --> Expire[expire or re-accept]
```

Industry lists name detect, respond, recover. They do not pick a governance product. They do not prove this schema. Someone still has to own the leftover.

Re-run `test_exception_needs_owner_review_and_wcag` after any register-form change. A green “maturity 2.5” tile is not that pytest. Expired `review_by` dates are the same family — inventory them before claiming recover.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `exception_incomplete_denied` |
| What the line holds | Missing fields, proposed owner; **never** secret writeups |
| Respond | Stop the accept that ignored the schema; do not paste secrets into chat |
| Recover | Expire; fix or re-accept with fields |
| Leftover | Unread register; tech-debt rename |

A governance dashboard will show exception counts and stay silent when CI’s `accept_exception` is always true. Detection must observe **empty owner is deny**, not “we have a risk register.” If the alert includes a secret writeup or chart text, you have opened a leftover-secret leak.

A log line a reviewer can accept looks like:

```text
log_denied reason=exception_incomplete_denied missing=owner,review_by
```

Not: a secret, an “assurance gate complete,” or a pledge screenshot.

If your alert includes the matching writeup, you have copied the leak into the ticket.

## What the framework does vs what you still have to check

The same always-true accept, unread register, and tech-debt rename that bypass this fixture will also bypass a “scan our risk dashboard” detector. Name those places before you claim recover. A maturity-model name is not the rule.

Cause vs cost stays split here too: the **cause** is oral acceptance treated as a row; the **cost** is unowned leftover and inaccessible recovery kept; **how you stop it** is the schema; **how you notice** is `exception_incomplete_denied`; **how you recover** is expire-or-re-accept. What the tool cannot do: this alert does not prove anyone reads the register, and it does not verify the accessibility flag.

## Can people still use it

The exception must record whether people can complete recovery. The deny message must say *missing owner / review date / accessibility check*, not only “assert False.” Under stress, do not use color-only severity.

## Practice

Write one log line you would accept in review. Tie it to `labs/E6/e6-lab`.

```text
log_denied reason=exception_incomplete_denied missing=owner,review_by
```

Reject any line that includes a secret, an “assurance gate complete,” or a pledge screenshot.

## Use it somewhere new

Clinic: deny the HIPAA exception; do not paste chart text into the ticket. Do not open a live governance tenant.

## What this page is not doing

A maturity-model name is not the rule. Do not claim you finished an assurance gate. An unverified pledge stays unverified. Answer keys stay out of lessons.
