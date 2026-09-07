# Review of trusted Forwarded-Proto

**Kind:** code-review
**Loop step:** Review

Wait until someone has looked at your review before opening the keys.

## What you are reviewing

Review `labs/5.4/5.4-lab/vulnerable/` as a change to notes-app channel binding. Check whether `channel_is_https({"X-Forwarded-Proto": "https"}, "http")` is still true.

The check you already ran (`test_client_forwarded_proto_is_not_tls`) is the rule test. A comment “will bind the proxy later” is not.

## Picture: problems to find (name them yourself)

**`channel_is_https` trusts `X-Forwarded-Proto` from anyone**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"header https socket http"| Property["Rule - good if tested"]
  Q -->|"Force HTTPS"| Mechanism[Tool - header trust]
  Q -->|"HSTS preload"| False[False assurance]
```

A mismatch still has to be false. If the change never checks `server_scheme == "https"`, the leftover is still there. A server flag that trusts proxy headers from `*` is still the same problem.

## Problems to find (name them yourself)

- `channel_is_https` trusts `X-Forwarded-Proto` from anyone
- A server flag that trusts proxy headers from `*`
- No test of header versus socket mismatch
- HSTS on an app that still accepts http

Also reject: live TLS attacks; closing findings without re-running `test_client_forwarded_proto_is_not_tls`; keys in learner notes; treating the client URL bar as the socket.

## Common mix-ups

- An HTTPS URL in the client proves TLS
- Forwarded headers are for security
- Pinning is always required
- HSTS preload is the rule
- A CDN “HTTPS only” tile binds the socket

## Practice

Write the review that blocks this change. Mention `test_client_forwarded_proto_is_not_tls`.

## Use it somewhere new

Clinic change that “enabled HTTPS” by trusting Forwarded-Proto is an incomplete review of channel binding. Name the independent falsehood that would still keep the header from counting as TLS.

## Can people still use it

If the dashboard shows an HTTPS badge, do not encode it as color only. That is a cue for operators, not the socket check.

## What this page is not doing

Do not merge by adding a comment “will bind the proxy later.” That comment is leftover without an owner. Do not probe a live host to prove the finding.
