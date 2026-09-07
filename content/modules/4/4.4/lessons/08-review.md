# Review of leftover grants

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships notes-app who-is-allowed. Don't just tally suspicious lines. Check whether `can_read("bob", "n2")` is still true, compare that with the module rule, and write changes a developer can verify.

The folder `labs/4.4/4.4-lab/vulnerable/` is the change. The check you already ran (`test_grant_on_n1_is_not_grant_on_n2`) is the rule test. A comment “will add object checks later” is not.

## Picture: if user.has_any_share: return note

Look at this first: **`if user.has_any_share: return note`**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"bob reads n2"| Property["Rule - good if tested"]
  Q -->|"we use roles"| Mechanism[Tool - role costume]
  Q -->|"IDs are hard to guess"| False[False assurance]
```

Keep this: n2 denied for Bob. If that call never includes an object-keyed lookup, that leftover path is still open. A role list named `admin` without a company comparison is the eve×n1 smell.

Leftover permission is permission from the surroundings — a signed-in user, “has any share,” an unscoped admin flag — used as if it were a yes for this person, this note, and this action.

## Problems to find (name them yourself)

- `if user.has_any_share: return note`
- Missing n2 deny test
- Admin boolean bypass without company
- Search endpoint without a check

Also reject: trusting the client; closing findings without re-running `test_grant_on_n1_is_not_grant_on_n2`; keys in lessons; real people's data in the practice files; “IDOR” as the requirement.

## Common mix-ups

- A scanner “IDOR” name is the missing rule
- A role replaces object grants
- Signed ids are capabilities
- `Depends(get_user)` is who-is-allowed
- Id length is the grant

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one to `test_grant_on_n1_is_not_grant_on_n2`. Do not open the keys file.

## Use it somewhere new

Clinic change that “checks the user is a clinician” without keying the chart is an incomplete review of leftover permission. Name the independent falsehood that would still keep Bob from reading n2.

## What this page is not doing

Do not merge by adding a comment “will add object checks later.” That comment is leftover without an owner. Do not guess ids on a live API to prove the finding.
