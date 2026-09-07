# Would you merge this Report-Only-as-on?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/E2/e2-lab/vulnerable/` as a change to the notes app’s header middleware. Check whether Report-Only still makes `isolation_enforced` true.

You already ran `test_report_only_is_not_enforcement` — that is the rule. A comment “we should enforce later” is not.

## Picture: Report-Only counted as on

**Report-Only counted as on**.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{"What would prove it false?"}
  Q -->|Report-Only counts| Property["Rule - good if tested"]
  Q -->|Helmet added| Mechanism[Tool - library]
  Q -->|dashboard green| False[False assurance]
```

Report-Only is not enforcement. If the change never uses the enforcing header name, that always-on leftover is still open. A dashboard screenshot does not replace that check.

Encoding is 6.2. CDN strip is 2.2. Do not skip `test_report_only_is_not_enforcement`. Do not claim check-in 7. Do not load a live page to prove the finding.

## Problems to find (name them yourself)

- Report-Only counted as on
- JSONP leftover
- Trusted Types claimed as encoding
- Edge cache stripping CSP

Also reject: a live script hunt; shipping without re-running `test_report_only_is_not_enforcement`; keys in learner notes; claiming check-in 7; presenting the current content-security spec as final.

## Common mix-ups this topic refuses

- Report-Only is isolation
- Helmet defaults are the guarantee
- A content-security policy replaces encoding
- A green reporting dashboard is encoding (6.2)
- Trusted Types is encoding

## Use it somewhere new

A clinic change that “added Report-Only and a dashboard” without an enforcing header is an incomplete isolation review. Name the independent falsehood that would still keep Report-Only from counting as on.

## What this page is not doing

Do not merge by adding a comment “will enforce later.” That comment is leftover without an owner. Do not load a public page to prove the finding.
