# Would you merge this always-true boot_ok?

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships the notes app’s compose boot check. Review `labs/10.4/10.4-lab/vulnerable/` as that change. Don't just tally suspicious lines. Check whether `boot_ok("prod", True)` still returns true, compare that with the rule, and write changes a developer can verify.

Start at `boot_ok` and the prod-plus-debug pair, not at a scanner color or a `NODE_ENV` screenshot. The check you already ran (`test_prod_debug_must_not_boot`) is the rule test. A comment “will turn debug off later” is not.

## Picture: boot_ok true on prod plus debug

Look at this first: **`boot_ok` true on prod plus debug**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|prod debug boots| Property["Rule - good if tested"]
  Q -->|NODE_ENV production| Mechanism[Tool - string]
  Q -->|canary 10 percent| False[False assurance]
```

Keep this: prod plus debug denied. If that call never includes the both-at-once check, that always-boot path is still open. A `NODE_ENV` screenshot does not replace that check.

Feature flags are leftover you still have to trust. Admin bound to all interfaces is leftover in the same family (docs and monitoring pages). Do not skip `test_prod_debug_must_not_boot`. This page does not mark you as finished. Do not boot a live host to prove the finding.

## Problems to find (name them yourself)

- `boot_ok` true on prod plus debug
- Admin on all interfaces
- Migration fail-open
- No rollback drill

Also reject: live production attacks; booting without re-running `test_prod_debug_must_not_boot`; keys in learner notes; claiming an assurance gate; treating a manufacturer-defaults program page as verified.

## Common mix-ups

- IaC means hardened
- Canary equals secure config
- Feature flags are not something you trust
- `NODE_ENV` is `boot_ok`
- A famous-bugs list is this week’s rule

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_prod_debug_must_not_boot`. Do not open the keys file.

## Use it somewhere new

Clinic change that “set `NODE_ENV` and added a canary” without a prod-plus-debug deny is an incomplete boot-gate review. Name the independent falsehood that would still keep prod plus debug from booting.

## Can people still use it

A refused boot must say *prod debug refused*, not only “will turn debug off later.”

## What this page is not doing

Do not merge by adding a comment “will turn debug off later.” That comment is leftover without an owner. Do not hit a public debug endpoint to prove the finding.
