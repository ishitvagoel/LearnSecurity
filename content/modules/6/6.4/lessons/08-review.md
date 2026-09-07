# Review of join-without-canonicalize

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Look at `labs/6.4/6.4-lab/vulnerable/` as an upload PR. Does `resolve("../outside")` still leave `/tmp/sc-lab`?

“Will canonicalize later” does not close `test_dotdot_does_not_escape_root`.

## Picture: open(user_path) / join without canonicalize

**`open(user_path)` / join without canonicalize**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"../ leaves folder"| Property["Rule — good if tested"]
  Q -->|"denylist of .."| Mechanism[Tool — encodings remain]
  Q -->|"Content-Type"| False[False assurance]
```

The canonical object still has to stay under the folder. A `..` denylist without a prefix test still walks out of the root. A `..` denylist without a prefix test is still the same problem.

Zip member paths are another parser of this rule, not a reason to skip `test_dotdot_does_not_escape_root`. Starlette `UploadFile.filename` is still client data after the change “randomizes names.”

## Problems to find (name them yourself)

- `open(user_path)` / join without canonicalize
- Blacklist of `..` only
- Trust `Content-Type`
- No prefix test

Also reject: host-file trophies; treating the client as what you trust; an awareness-list name as the finding title; closing findings without re-running `test_dotdot_does_not_escape_root`; keys in learner notes; live walks against a public filesystem.

## Common mix-ups

- UUID filenames replace path checks
- Antivirus is the upload control
- JSON is always a safe deserialize
- An awareness-list name is the rule
- Starlette `UploadFile` already canonicalizes

## Use it somewhere new

Randomized filenames without a prefix test still let `..` walk out of the root. Randomized filenames are not a prefix test — write the path-prefix hold.

## What this page is not doing

If the change never joins, canonicalizes, and checks the prefix, “will canonicalize later” is not a merge. Do not open host files to prove the finding.
