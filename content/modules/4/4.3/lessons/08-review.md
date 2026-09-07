# Review of a query-string session token

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships notes-app session parsing. Review `labs/4.3/4.3-lab/vulnerable/` as that change. Check whether `session_from_request` still returns the query token, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_query_string_token_is_rejected`) is the rule test. A comment “will move to cookies later” is not.

## Picture: session_from_request uses query

**`session_from_request` uses query**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"query returns secret"| Property["Rule — good if tested"]
  Q -->|"we use JWT"| Mechanism[Tool — format]
  Q -->|"TLS hides logs"| False[False assurance]
```

What has to stay true: query yields `None`. If that call never includes a dropped query channel, that leftover path is still open. “We use JWTs” and “SPA best practice” are tool slogans until the pytest fails on the broken files.

## Problems to find (name them yourself)

- `session_from_request` uses query
- JWT in localStorage as “SPA best practice”
- No Referer policy
- Tokens printed in uvicorn logs

Also reject: treating the client as what you trust; closing findings without re-running `test_query_string_token_is_rejected`; keys in learner notes; real tokens in practice files; “HTTPS so logs are fine.”

## Common mix-ups

- Query strings are fine over TLS
- JWT means secure
- HttpOnly is the same as “not in the URL”
- NextAuth defaults are the channel guarantee
- Magic-link URL is a standing session

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one to `test_query_string_token_is_rejected`. Do not open the keys file.

## Use it somewhere new

Clinic deep-link change that “adds a token query param for convenience” is an incomplete review. Name the independent falsehood that would still keep query-only requests at `None`.

## What this page is not doing

Do not merge by adding a comment “will move to cookies later.” That comment is leftover risk without an owner. Do not dump live logs to prove the finding.
