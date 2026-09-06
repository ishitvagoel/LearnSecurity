# Would you merge this password file?

**Kind:** code-review
**Loop step:** 7 Generalize

## Review

You are reviewing a change that "adds login" to the local notes app. The patch is small. That is not the same as safe.

## What to look for

Read the store write path:

- Is the password written as itself, as Base64, or as a slow hash?
- Is there a **unique** salt per user, or one salt in a config file?
- Are hashing settings stored next to the hash?
- Is the compare a secret-safe function?

Read the log path:

- Do failed sign-ins print the password "for debugging"?

Read the tests:

- Is there a test that the file has no readable password?
- Is there a test that two users with the same password have different salts?

Read the comments:

- Do they claim "production ready" or "secure by default"?
- Do they admit this is **local-only**?

## Merge or block

**Block** if any of these are true:

- readable password in the store,
- fast hash sold as a password store,
- shared salt,
- `==` on secret strings as the only check,
- password in logs,
- no test for plaintext-absent,
- comment says the laptop is now safe from theft because of Argon2.

**Merge** (for this week) if:

- Argon2id (or the pinned slow hash) plus unique salt plus settings,
- secret-safe compare,
- tests named above pass,
- comments tell the truth about local-only and leftover risk.

## What to write in the review

Two sentences:

1. What evidence you ran or read.
2. What leftover risk you are accepting (disk theft, no server).

"Looks good to me" is not a review.

## Check yourself

Take the broken tree from the practice. Write the review that **blocks** it. Then take the repaired tree and write the review that **merges** it with leftover risk named. Keep both in your notes for the first check-in.
