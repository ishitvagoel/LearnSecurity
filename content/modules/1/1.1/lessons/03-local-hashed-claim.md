# Try a local hashed login

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Try it

Open the practice for this topic. Two trees sit side by side: one that stores the password in a form you can read, and one that stores a slow hash plus a unique salt.

**What you are showing**

Not "hashing exists in a textbook." You are showing that a **readable password file** fails the rule, and that a **slow hash plus a unique salt, checked with a compare that does not leak timing,** restores it **on this computer**.

**What you may touch**

- Only the practice folder for this topic.
- Synthetic users (`practice-user-1`, `practice-user-2`).
- Disposable pepper values in `.env.example`. Never a password you use on a real site.

Do **not** point these steps at a public website, a school portal, or anyone else's login.

## What to look at

**The broken store**

1. Create a local user with a throwaway password.
2. Open the store file (JSON in the practice).
3. Write down: can you read the password in the file? Could a unique salt exist if there is no salt field?

**The repaired store**

4. Create the same user in the repaired tree.
5. Open that store. You should see a hash, a unique salt, and hashing settings — not the password.
6. Run the tests in that folder. They fail closed if the password is stored readable, if two users share a salt, or if the check uses a compare that can leak timing.

**Copy this into your lab notes** (short answers):

- Store path (broken):
- Readable password? (yes/no):
- Store path (repaired):
- Unique salt per user? (yes/no):
- Hashing settings present? (yes/no):
- Tests run (command + pass/fail):

```text
cd labs/phase1/lab-1.1-local-hashed-identity/fixed
python -m pytest tests/ -q
```

If Python or Argon2 is missing, use the README in that folder. Do not paste real passwords into tickets or git.

## The rule, in one line

A readable password in the store is a failed rule. A slow hash plus a unique salt is the start of a passing one — still only on this computer.

## Fix

The next page names the smallest store that keeps this rule. You do not need to invent Argon2. You do need to refuse a store that cannot tell a hash from a password.

## Check

The tests in the repaired tree are the check for "password not stored readable" and "unique salt." They are not a check for "safe on the internet." Do not write that sentence in your notes.
