# Review of leftover analytics

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

This review is about notes-app deletion. Your job is to label each claim **rule**, **tool**, or **false assurance**, and to say whether `body_retained("alice")` is still `"secret"` after `delete_account("alice")` if they ship. Start at leftover analytics after delete, not at a scanner color or a contract ticket.

You already ran `test_deleted_account_leaves_no_analytics_body`. A comment “will add warehouse purge later” is not.

## Picture: problems to find (name them yourself)

**`delete_account` only `NOTES.pop`**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"body_retained after delete"| Property["Rule - good if tested"]
  Q -->|"we anonymized ids"| Mechanism[Tool - body kept]
  Q -->|"privacy policy"| False[False assurance]
```

Analytics and search bodies still have to be None after delete. If that same delete never pops those copies, that leftover path is still open. “We anonymized user ids” while the body column remains is still the same problem.

## Problems to find (name them yourself)

- `delete_account` only `NOTES.pop`
- Analytics “immutable for ML” without an exception record
- No test `body_retained` after delete
- Privacy policy PDF as the control

Also reject: trusting the client; closing findings without re-running `test_deleted_account_leaves_no_analytics_body`; keys in learner notes; real people's data in the practice files; encryption of a kept warehouse as deletion.

## Common mix-ups

- Encryption makes retention OK
- Privacy equals secrecy
- A privacy-law footer is the rule
- A database DELETE is warehouse DELETE
- HTTP 200 on `/account` is the graph

## Use it somewhere new

Clinic change that “deletes the patient” without walking the appointment-card notes is an incomplete review of leftover copies. Name the independent falsehood that would still keep `body_retained` None.

## Can people still use it

If the dashboard shows an “account deleted” badge, do not encode it as color only. That is a cue for operators, not the purge.

## What this page is not doing

Do not merge by adding a comment “will add warehouse purge later.” That comment is leftover without an owner. Do not dump a live warehouse to prove the finding.
