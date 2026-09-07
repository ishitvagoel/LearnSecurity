# Would you merge this path-trusted callbacks?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/7.3/7.3-lab/vulnerable/` as a change to a notes-app billing webhook. Check whether `accept("", "body", "lab-secret")` is still true.

You already ran `test_missing_signature_is_rejected` — that is the rule. A comment “will HMAC later” is not. A famous-bugs ticket is not.

## Picture: accept always true / process because the path matched

**Accept always true / process because the path matched**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|empty sig accepted| Property["Rule - good if tested"]
  Q -->|TLS only| Mechanism[Tool - hop]
  Q -->|vendor CIDR| False[False assurance]
```

An empty sig still has to be denied. If the change never checks a raw-body MAC, that path-trust is still open. A TLS terminator without that check is still the same problem.

Parse-before-MAC (2.1) and secret-in-query (4.3) are other authenticity holes — name them, do not skip `test_missing_signature_is_rejected`.

## Problems to find (name them yourself)

- Accept always true / process because the path matched
- JSON parsed before MAC
- No missing-sig test
- Secret in query string (4.3)

Also reject: live provider attacks; closing findings without re-running `test_missing_signature_is_rejected`; keys in learner notes; a web filter as the rule.

## Common mix-ups

- TLS to us proves the sender
- An IP allow-list is authenticity
- Webhooks are just APIs in reverse so JWT login applies
- Vendor SDK verify is the same as a custom MAC over parsed JSON
- A famous-bugs nickname is the rule

## Practice

Write the review that would block this change. Name `test_missing_signature_is_rejected`.

## Use it somewhere new

Clinic change that “terminated TLS and allow-listed the vendor” without a missing-sig test is an incomplete review of path-trusted callbacks. Name the independent falsehood that would still keep empty sig false.

## What this page is not doing

Do not merge by adding a comment “will HMAC later.” That comment is leftover without an owner. Do not POST a live provider to prove the finding.
