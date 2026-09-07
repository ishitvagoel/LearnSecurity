# Would you merge this always-true ship_ok?

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships the notes app’s ship gate. Review `labs/9.4/9.4-lab/vulnerable/` as that change. Don't just tally suspicious lines. Check whether `ship_ok([HIGH], {})` still returns true, compare that with the rule, and write changes a developer can verify.

Start at `ship_ok` and the HIGH×map row, not at a scanner color or a dashboard screenshot. The check you already ran (`test_unmapped_high_blocks_ship`) is the rule test. A comment “will map later” is not.

## Picture: ship_ok true on unmapped HIGH

Look at this first: **`ship_ok` true on unmapped HIGH**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|unmapped HIGH ships| Property["Rule - good if tested"]
  Q -->|code scanning on| Mechanism[Tool - signal]
  Q -->|maturity score| False[False assurance]
```

Keep this: unmapped HIGH denied. If that call never includes a join to the coverage map, that always-ship leftover is still open. A scanner screenshot does not replace that check.

Who-is-allowed blind spots are review and isolation tests — name them, do not skip `test_unmapped_high_blocks_ship`. Do not claim the verification gate is done. Do not scan a live tenant to prove the finding.

## Problems to find (name them yourself)

- `ship_ok` true on unmapped HIGH
- Suppressions without owner
- SAST offered as the verification gate
- No blind-spot note for who-is-allowed / IDOR

Also reject: live tenants; closing findings without re-running `test_unmapped_high_blocks_ship`; keys in learner notes; claiming the verification gate is done.

## Common mix-ups

- Zero findings means secure
- A scanner replaces the requirement list
- Reachability is optional theater
- A maturity score is `ship_ok`
- A draft supply-chain paper is finished

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_unmapped_high_blocks_ship`. Do not open the keys file.

## Use it somewhere new

Clinic change that “enabled code scanning” without a mapping check is an incomplete ship-gate review. Name the independent falsehood that would still keep unmapped HIGH from shipping.

## Can people still use it

The triage screen must say *why* F1 is blocked, in words. Do not encode “blocked” as color only.

## What this page is not doing

Do not merge by adding a comment “will map later.” That comment is leftover without an owner. Do not scan a public repo to prove the finding.
