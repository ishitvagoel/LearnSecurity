# Would you merge this always-accept exception?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

The files in `labs/E6/e6-lab/vulnerable/` are the leftover-risk register. Does `accept_exception({"owner": "", "review_by": None})` still return true?

Read `accept_exception` and the empty-owner row first. A maturity screenshot can wait. `test_exception_needs_owner_review_and_wcag` still fails if the only change is “will add dates later.”

## Picture: accept with empty owner

**Accept with empty owner**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|empty owner accepted| Property["Rule - good if tested"]
  Q -->|ticket type named risk| Mechanism[Tool - ticket]
  Q -->|maturity mapped| False[False assurance]
```

An empty owner still has to be denied. If the change never checks the schema, that always-accept leftover is still open. A maturity screenshot does not replace that check.

Unread register is leftover. Tech-debt rename is leftover. This page does not mark you as finished. Do not contact a live disclosure inbox to prove the finding.

## Problems to find (name them yourself)

- Accept with empty owner
- No `review_by`
- Accessibility not in the schema
- Maturity slide as the exception

Also reject: live disclosure; shipping without re-running `test_exception_needs_owner_review_and_wcag`; keys in learner notes; claiming a check-in; treating an unverified pledge as proven.

## Common mix-ups

- Leadership is soft skills, not rules
- Exceptions are failure
- People can always call support instead of accessible recovery
- A maturity score is the register
- A HIPAA slide is `accept_exception`

## Use it somewhere new

A HIPAA slide and a maturity score, without owner / review / accessibility, do not fill the register. What would still keep an empty-owner exception from being accepted?

## Can people still use it

A deny notice must say why the exception stayed incomplete (missing owner, review date, or accessibility check), not only “will add dates later.”

## What this page is not doing

An exception row with no owner and only “will add dates later” is still unowned leftover. Do not email a vendor disclosure inbox to prove the finding.
