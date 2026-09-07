# Review of an unencoded title

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/6.2/6.2-lab/vulnerable/` as a change to the notes app’s HTML drawing. Check whether `render` still leaves `<` as markup.

You already ran `test_angle_brackets_are_encoded` — that is the rule. A comment “we should encode later” is not.

## Picture: template concatenates title

**template concatenates title**.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{"What would prove it false?"}
  Q -->|"raw angle bracket in output"| Property["Rule — good if checked"]
  Q -->|"content-security report-only"| Mechanism[Tool — not encoding]
  Q -->|"cleaner after innerHTML"| False[False assurance]
```

`&lt;` is present, extra tags are absent. If that sink never encodes, that grammar mix is still open. A content-security header in report-only mode without an encode check is still the same problem.

A markdown pipeline that emits raw tags after this template is encoded is 2.1, not a reason to skip `test_angle_brackets_are_encoded`. HttpOnly cookies (2.3) do not encode HTML.

## Problems to find (name them yourself)

- Template concatenates title
- Content-security policy in report-only mode as the fix
- No `&lt;` check
- Cleaner after `innerHTML` assignment

Also reject: attack-recipe payloads in the change description; closing findings without re-running `test_angle_brackets_are_encoded`; keys in learner notes.

## Common mix-ups this topic refuses

- A content-security policy replaces encoding
- HttpOnly makes script in the page harmless
- Markdown is inert
- React everywhere means this template is encoded
- A famous-bugs nickname is the rule

## Use it somewhere new

A clinic change that “added a content-security policy” without an encode check is an incomplete review. Name the independent falsehood that would still keep `<` from remaining markup.

## What this page is not doing

Do not merge by adding a comment “will encode later.” That comment is leftover without an owner. Do not load a live page to prove the finding.
