# Review of leftover defaults

**Kind:** code-review
**Loop step:** Review

Intended findings live only in the answer-key folder — not here. Do not open that file until your review has been evaluated.

## What you are reviewing

A colleague ships notes-app secret rotation. Review `labs/5.3/5.3-lab/vulnerable/` as that change. Your job is not to count suspicious lines. Reconstruct whether `auth("sk-lab-hardcoded", current="rotated-now")` is still true, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_hardcoded_default_does_not_auth`) is the rule test. A comment “will rotate later” is not.

## Picture: DEFAULT still accepted

Start with this seeded smell: **`DEFAULT = 'sk-lab-hardcoded'` still accepted**. Label it rule, tool, or false comfort before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"default still authenticates"| Property["Rule — good if tested"]
  Q -->|"we use Vault"| Mechanism[Tool — no rotate]
  Q -->|"gitignore"| False[False comfort]
```

Start from what must stay true (default dead after rotate; missing current denies). Everything that is not equality with current at that call is a candidate leftover path. A vault import without killing `DEFAULT` is the same problem, not a different kind of finding.

## Problems to find (name them yourself)

- `DEFAULT = 'sk-lab-hardcoded'` still accepted
- Secret in README “for convenience”
- No rotation test
- Same key for all tenants

Also reject: real production keys in practice files; closing findings without re-running `test_hardcoded_default_does_not_auth`; keys in learner notes; allow when current is missing.

## Common mix-ups

- gitignore means it was never leaked
- A key service equals rotated
- Passwords and API keys are the same lifecycle
- Vault brand is the rule
- Missing current should allow

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false comfort, suggested structural change, leftover you will **not** delete. Tie at least one to `test_hardcoded_default_does_not_auth`. Do not open the keys file.

## Use it somewhere new

Clinic change that “moved the key to Vault” without killing the default is an incomplete review. Name the independent falsehood that would still keep `sk-lab-hardcoded` from authenticating.

## What this page is not doing

Do not merge by adding a comment “will rotate later.” That comment is leftover risk without an owner. Do not fetch a live gist to prove the finding.
