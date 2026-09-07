# Would you merge this extras as=?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/8.3/8.3-lab/vulnerable/` as a change to the notes app’s App Link handling. Check whether `open_link({"as": "admin"})` still switches `current_user()`.

You already ran `test_deeplink_as_param_does_not_switch_user`. A comment “we should ignore extras later” is not. An App Links screenshot is not this review.

## Picture: current_user = extras['as']

**`current_user = extras['as']`**.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{"What would prove it false?"}
  Q -->|as= switches user| Property["Rule — good if checked"]
  Q -->|https only| Mechanism[Tool — transport]
  Q -->|App Links verified| False[False assurance]
```

Alice still has to stay unchanged. If the change never ignores identity keys, that session switch is still open. An App Links screenshot without that check is still the same problem.

WebView `addJavascriptInterface` and custom schemes are other IPC holes — name them, do not skip `test_deeplink_as_param_does_not_switch_user`.

## Problems to find (name them yourself)

- `current_user = extras['as']`
- Exported Activity without a permission
- WebView `addJavascriptInterface` too wide
- No `as=` test

Also reject: live malware APKs; closing findings without re-running `test_deeplink_as_param_does_not_switch_user`; keys in learner notes.

## Common mix-ups this topic refuses

- HTTPS App Links are trusted input
- WebView is just Chrome so 2.3 applies unchanged
- IPC is private to our app
- `exported=false` without a test is this rule
- A verified-host tile is the rule

## Use it somewhere new

A clinic change that “verified App Links” without an `as=` deny check is an incomplete review. Name the independent falsehood that would still keep alice.

## What this page is not doing

Do not merge by adding a comment “will ignore extras later.” That comment is leftover without an owner. Do not install a malware APK to prove the finding.
