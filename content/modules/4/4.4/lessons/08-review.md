# Review of leftover grants

**Kind:** code-review
**Loop step:** Review

Intended findings live only in the answer-key folder — not here. Do not open that file until your review has been evaluated.

## What you are reviewing

A colleague ships notes-app who-is-allowed. Your job is not to count suspicious lines. Reconstruct whether `can_read("bob", "n2")` is still true, compare that with the module rule, and write changes a developer can verify.

The folder `labs/4.4/4.4-lab/vulnerable/` is the change. The check you already ran (`test_grant_on_n1_is_not_grant_on_n2`) is the rule test. A comment “will add object checks later” is not.

## Picture: if user.has_any_share: return note

Start with this seeded smell: **`if user.has_any_share: return note`**. Label it rule, tool, or false comfort before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"bob reads n2"| Property["Rule - good if tested"]
  Q -->|"we use roles"| Mechanism[Tool - role costume]
  Q -->|"IDs are hard to guess"| False[False comfort]
```

Start from what must stay true (n2 denied for Bob). Everything that is not an object-keyed lookup at that call is a candidate leftover path. A role list named `admin` without a company comparison is the eve×n1 smell, not a different finding class.

Leftover permission is permission from the surroundings — a signed-in user, “has any share,” an unscoped admin flag — used as if it were a yes for this person, this note, and this action.

## Seeded smells (label them yourself)

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

Write three review notes a maintainer could act on. Each note: what you saw, rule or false comfort, suggested structural change, leftover you will **not** delete. Tie at least one to `test_grant_on_n1_is_not_grant_on_n2`. Do not open the keys file.

## Use it somewhere new

Clinic change that “checks the user is a clinician” without keying the chart is an incomplete review of leftover permission. Name the independent falsehood that would still keep Bob from reading n2.

## What this page is not doing

Do not merge by adding a comment “will add object checks later.” That comment is leftover without an owner. Do not guess ids on a live API to prove the finding.
