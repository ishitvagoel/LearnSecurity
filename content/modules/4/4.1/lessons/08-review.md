# Review of a leftover session after delete

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

This review is about notes-app offboarding. Your job is to label each claim **rule**, **tool**, or **false assurance**, and to say whether `session_valid("alice")` is still true after `delete_user` if they ship. Start at the leftover session after delete, not at a scanner color or an HR ticket.

A comment “will revoke sessions later” is not a pass on `test_deleted_user_session_is_dead`.

## Picture: problems to find (name them yourself)

**`DELETE FROM users` without session purge**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"session_valid true after delete"| Property["Rule - good if tested"]
  Q -->|"we emailed them"| Mechanism[Tool - no revoke]
  Q -->|"single sign-on is on"| False[False assurance]
```

The session still has to be dead after delete. If that same delete never kills leftovers, the leftover is still there.

## Problems to find (name them yourself)

- `DELETE FROM users` without session purge
- Token `exp` 30d ignored on delete
- Worker still has `user_id`
- No test `session_valid` after delete

Also reject: trusting the browser as the vault; closing findings without re-running `test_deleted_user_session_is_dead`; keys in learner notes; real people's data in the practice files; production cookies in the review notes.

## Common mix-ups

- Disable login is enough
- Single sign-on magically revokes
- Deleted means gone from backups
- SessionMiddleware knows HR
- An “account deleted” email is the kill

## Use it somewhere new

Clinic change that “disables the badge” without killing the chart session is an incomplete review of leftover access. Name the independent falsehood that would still keep `session_valid` false after offboard.

## Can people still use it

If the dashboard shows a signed-out badge, do not encode it as color only. That is a cue for operators, not the kill.

## What this page is not doing

Do not merge by adding a comment “will revoke sessions later.” That comment is leftover without an owner. Do not replay a live cookie to prove the finding.
