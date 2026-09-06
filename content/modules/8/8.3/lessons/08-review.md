# Review extras as= like a pull request

**Kind:** code-review
**Loop step:** Review

Intended findings live only in the answer-key folder — not here. Do not open that file until your review has been evaluated.

## What you are reviewing

A colleague ships the notes app’s App Link handling. Review `labs/8.3/8.3-lab/vulnerable/` as that change. Your job is not to count suspicious lines. Reconstruct whether `open_link({"as": "admin"})` still switches `current_user()`, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_deeplink_as_param_does_not_switch_user`) is the rule check. A comment “we should ignore extras later” is not. An App Links screenshot is not this review.

## Picture: current_user = extras['as']

Start with this seeded smell: **`current_user = extras['as']`**. Label it **rule**, **tool**, or **false comfort** before you accept the change.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{"What would prove it false?"}
  Q -->|as= switches user| Property["Rule — good if checked"]
  Q -->|https only| Mechanism[Tool — transport]
  Q -->|App Links verified| False[False comfort]
```

Classification starts at the protected effect (alice unchanged). Everything that is not “ignore identity keys” at that call is a candidate session switch. An App Links screenshot without that pytest is the same smell, not a different finding class.

WebView `addJavascriptInterface` and custom schemes are other IPC holes — name them, do not skip `test_deeplink_as_param_does_not_switch_user`.

## Seeded smells (label them yourself)

- `current_user = extras['as']`
- Exported Activity without a permission
- WebView `addJavascriptInterface` too wide
- No `as=` test

Also reject: live malware APKs; closing findings without re-running `test_deeplink_as_param_does_not_switch_user`; keys in learner notes.

## Common mix-ups this topic refuses

- HTTPS App Links are trusted input
- WebView is just Chrome so 2.3 applies unchanged
- IPC is private to our app
- `exported=false` without a test is this cell
- A verified-host tile is the rule

## Practice

Write three review notes a peer could act on. Each note: what you saw, rule or false comfort, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_deeplink_as_param_does_not_switch_user`. Do not open the keys file.

## Use it somewhere new

A clinic change that “verified App Links” without an `as=` deny check is an incomplete review. Name the independent falsehood that would still keep alice.

## What this page is not doing

Do not merge by adding a comment “will ignore extras later.” That comment is leftover without an owner. Do not install a malware APK to prove the finding.
