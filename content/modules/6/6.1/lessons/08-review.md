# Review of concatenating into sh -c

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Export listing: start at `sh -c` concatenation. For each claim, say **rule**, **tool**, or **false assurance**, and whether `argv_for_list("notes")` still starts `["sh", "-c"]`. Skip the green scan.

Someone still has to make `test_does_not_invoke_shell` pass; “will switch to argv later” does not do that.

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

## Use it somewhere new

Sanitizing the filename and still calling `sh -c` still concatenates into a shell. What would still keep `argv_for_list` off `sh -c` after the filename is sanitized?

## What this page is not doing

Do not merge a shell call because a comment promises argv later. Do not execute a live command to prove the finding.
