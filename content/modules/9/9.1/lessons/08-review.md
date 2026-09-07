# Would you merge this any-req-match covered?

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships the notes app’s coverage check. Review `labs/9.1/9.1-lab/vulnerable/` as that change. Don't just tally suspicious lines. Check whether a status-only AUTHZ-1 row still counts as covered, compare that with the rule, and write changes a developer can verify.

Start at `covered` and the AUTHZ-1 row, not at a scanner color or a PDF screenshot. The check you already ran (`test_status_only_row_is_not_coverage`) is the rule test. A comment “will map tests later” is not.

## Picture: matching any requirement id counts as covered

Look at this first: **any matching requirement id counts as covered**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|status-only covered| Property["Rule - good if tested"]
  Q -->|checklist PDF attached| Mechanism[Tool - inventory]
  Q -->|green CI| False[False assurance]
```

Keep this: status-only not covered. If that call never includes `req` **and** `asserts_isolation`, that false-comfort path is still open. A checklist PDF without that check is still the same problem.

HTTP-200 tests that lie about isolation are 9.3. Exceptions without expiry are E6. Do not skip `test_status_only_row_is_not_coverage`. Do not claim the verification gate.

## Problems to find (name them yourself)

- status-only coverage
- Checklist copied wholesale
- No isolation assert
- Exceptions without expiry

Also reject: live portals; closing findings without re-running `test_status_only_row_is_not_coverage`; keys in learner notes; claiming the verification gate; obsolete mobile-level stickers as the current bar.

## Common mix-ups

- Checklist certification exists as a sticker
- Number of tests is coverage
- Green build is the verification gate
- A later draft of a practice guide is final
- Old mobile-level stickers are current levels

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_status_only_row_is_not_coverage`. Do not open the keys file.

## Use it somewhere new

Clinic change that “marked HIPAA isolation done” without an isolation assert is an incomplete review of the proof. Name the independent falsehood that would still keep status-only uncovered.

## Can people still use it

A human exception path must say what is still uncovered and when it expires. Do not hide the gap behind “see PDF.”

## What this page is not doing

Do not merge by adding a comment “will map tests later.” That comment is leftover without an owner. Do not scrape a live portal to prove the finding.
