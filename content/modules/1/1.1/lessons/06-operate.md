# Logs, rotation, and a stolen laptop

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Keep it running

A hash on disk is not the end of the story. You still have to **notice** a bad store, **raise** hashing cost without lying about old files, and **say what you will do** if the laptop is stolen.

## What to log (and what never to log)

Log:

- user created (id, not password),
- sign-in succeeded or failed (id, not password),
- hashing settings used (algorithm name, cost — not the hash),
- fail-closed events (missing file, unknown settings).

Never log:

- the password,
- the salt,
- the hash,
- the pepper.

If your log line could be pasted into a password guesser, it is wrong.

## Rotation without fiction

When you raise Argon2 cost:

1. New users get the new settings.
2. Old rows keep their old settings until that user signs in (or you run a planned migrate).
3. The record always says which settings produced **that** hash.

Do not rewrite every hash with new settings unless you still have the password — you do not. Do not change the settings field and leave the old hash. That is a lie the next check will punish.

## Stolen laptop

Write three lines in your design note:

1. What an attacker with the disk gets (hashes, salts, settings — not plaintext if you did this topic).
2. What they do not get (the pepper, if it lived elsewhere; OS login; other users' machines).
3. What you do next (re-hash on next login after a pepper rotation; invalidate a later server session — out of scope this week, but name it so you do not forget).

This is not encryption of the disk. If you need that, say "full-disk encryption" as a **separate** control. Do not pretend Argon2 is BitLocker.

## Check yourself

Paste one log line you would emit on failed sign-in. If it contains a secret, rewrite it.

Write the three stolen-laptop lines. If line 1 says "nothing, we hashed," rewrite it. They get the hashes.

## What can still go wrong

Logs can become a second password store if you are sloppy. Rotation can brick old users if you drop settings. A stolen laptop is still a stolen laptop.

## Where this shows up later

The notes app will grow server sessions. Stolen laptop then also means stolen cookies unless you designed revocation. Remember this page when that happens.
