# Review of concatenating into sh -c

**Kind:** code-review
**Loop step:** Review

Wait until someone has looked at your review before opening the keys.

## What you are reviewing

This review is about notes-app export listing. Your job is to label each claim **rule**, **tool**, or **false assurance**, and to say whether `argv_for_list("notes")` still starts `["sh", "-c"]` if they ship. Start at `sh -c` concatenation, not at a scanner color.

The folder `labs/6.1/6.1-lab/vulnerable/` is the change. The check you already ran (`test_does_not_invoke_shell`) is the rule test. A comment “will switch to argv later” is not.

## Picture: problems to find (name them yourself)

**`shell=True` or `sh -c` concatenation**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"sh -c concat"| Property["Rule - good if tested"]
  Q -->|"denylist of punctuation"| Mechanism[Tool - still a shell]
  Q -->|"internal users"| False[False assurance]
```

The program still cannot be `sh`, and the name still has to be one element. If the change never uses an argv list, that second parser is still open. A denylist of punctuation while `uses_shell` stays true is still the same problem.

## Problems to find (name them yourself)

- `shell=True` or `sh -c` concatenation
- Blacklist of punctuation as the fix
- No `uses_shell` test
- Comment “user is trusted internally”

Also reject: live command execution; closing findings without re-running `test_does_not_invoke_shell`; keys in learner notes; punctuation cookbooks in the change.

## Common mix-ups

- Injection is one scanner name
- subprocess wrappers auto-escape shells
- A scanner finding is the rule
- Internal users make a shell safe
- Executing argv is how you test this rule

## Practice

Write the review that blocks this change. Mention `test_does_not_invoke_shell`.

## Use it somewhere new

Clinic change that “sanitized the filename” and still calls `sh -c` is an incomplete review of concatenating into a shell. Name the independent falsehood that would still keep `argv_for_list` from starting `sh -c`.

## What this page is not doing

Do not merge by adding a comment “will switch to argv later.” That comment is leftover without an owner. Do not execute a live command to prove the finding.
