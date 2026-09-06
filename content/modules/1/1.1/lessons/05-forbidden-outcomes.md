# What must never show up in the file

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

A mechanism without a **failed test** is a story. This page names the stories that must not pass.

## Tests you should be able to name

**Normal**

- Create a user with a throwaway password. The store has a hash, a unique salt, and hashing settings. The password is not in the file.
- Sign in with the right password. The app accepts. Sign in with the wrong one. The app refuses.

**Wrong input**

- Empty password, huge password, password with spaces or unicode: rejected or handled on purpose — not hashed as `None`, not crashed into a 500 with a stack trace on a public page (there is no public page yet; still do not print the password).

**Abuse**

- Two users, same password: salts differ, hashes differ.
- Compare uses a secret-safe function, not a shortcut that can leak timing.
- Pepper, if present, is not sitting in the same file as the hashes.

**When things break**

- Missing store file: fail closed, not "treat everyone as signed in."
- Unknown hashing settings in an old row: fail closed or migrate on purpose — not silently check with today's settings against yesterday's hash.

Write the test names in your notes. Then run them:

```text
cd labs/phase1/lab-1.1-local-hashed-identity/fixed
python -m pytest tests/ -q
```

## What "fail closed" means here

If the store cannot be read, or the row cannot be verified, the app does **not** invent a success. A broken file is not a free login.

## Check yourself

Which test would catch "I hashed with SHA-256 and called it Argon2"? If you do not have one, add a check that the algorithm name in the record is the one you pinned.

Which test would catch "one salt for everyone"? If you do not have one, create two users and compare salts.

## What can still go wrong

Green tests on this laptop are not a pentest of a website. They are evidence for **this** store, **this** week.

## Where this shows up later

Check-in 1 asks for this kind of evidence, not a screenshot of a green arrow with no test names.
