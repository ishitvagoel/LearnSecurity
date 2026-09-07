# Review of unbounded allow

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

You are reviewing export. Label each claim **rule**, **tool**, or **false assurance**. Say whether `allow(4)` is still true if they ship. Start at unbounded allow, not at a famous API-abuse list.

A comment “will cap later” is not a pass on `test_fourth_export_is_denied`.

## Picture: problems to find (name them yourself)

**No cap (`allow` always true)**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"allow 4 true"| Property["Rule - good if tested"]
  Q -->|"button disabled"| Mechanism[Tool - client]
  Q -->|"IP rate limit"| False[False assurance]
```

The fourth still has to be denied. If the change never checks a server `n <= 3`, that unbounded path is still open. An IP bucket at the edge without that check is still the same problem.

A disabled button in the browser (the leftover 3.4 already named for shares) does not bind `allow(4)`. GraphQL aliases (7.1) are another budget path — name them, do not skip `test_fourth_export_is_denied`.

## Problems to find (name them yourself)

- No cap (`allow` always true)
- Limit only in the frontend
- Global IP limit
- No test that the fourth is denied

Also reject: public load tests; closing findings without re-running `test_fourth_export_is_denied`; keys in learner notes; an edge-proxy screenshot as the rule.

## Common mix-ups

- Availability is ops, not app work
- CAPTCHA replaces quotas
- Autoscaling is the control
- A famous API-abuse list is the rule
- HTTP 429 from an edge proxy is this check

## Use it somewhere new

Clinic change that “rate-limited at the edge” without a per-person fourth-export test is an incomplete review of unbounded allow. Name the independent falsehood that would still keep `allow(4)` false.

## What this page is not doing

Do not merge by adding a comment “will cap later.” That comment is leftover without an owner. Do not load-test a public host to prove the finding.
