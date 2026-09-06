# What the notes app already holds

**Kind:** design-exercise
**Loop step:** 2 Model

## Picture

The notes app already has more than one kind of thing worth protecting. Until you name those things, it is easy to treat "hash the password" as if it were the whole job.

At this point the app is still **local-first**. There is no public login page and no server account. You still have:

- notes you type,
- a local claim that you are you (after this topic),
- a computer with files on disk,
- later, a shared workspace (not yet).

This page is a **catalogue**, not a full threat model. You name the assets, who can reach them, and what "done" means for this week. The next topic is where you draw the line around what you trust.

## Worked example

Here is a table you can copy into a design note. Fill the last column in your own words.

| What | Who can reach it | What "safe" means this week |
| --- | --- | --- |
| Notes you type | You, and anyone who can use this computer | Stay on this machine until you choose to share |
| Local claim ("this is me") | The app, this computer, later a server | Only this machine's claim is treated as you — and it is not a server login |
| Password at rest | Disk, backups, anyone with the file | Stored as a slow hash plus a unique salt — never as the password itself |
| Hashing settings | The same store as the hash | Honest about what they are, so you can raise the cost later without pretending the old file was stronger |
| App code | You, your editor, later git | You can read it. It is not a vault. |

**Who might try something**

- You, using the app as meant.
- Someone else on the same laptop (family, classmate, stolen session).
- You, later, connecting a real server (out of scope this week).
- A person on the internet (also out of scope — there is no public login yet).

**Where the line is**

- The browser is not the vault. DevTools can show what the page holds.
- Files on disk are not automatically private. Another account on the machine may still open them.
- A later API is a new boundary. Do not smuggle a "logged in" bit in a URL or a cookie and call it done.

**Time**

- Hashing settings can get stronger. An old file is not secretly upgraded.
- "Logged in" on this laptop is not "logged in" on a server. Different clock, different store, different attacker.

## Check yourself

1. List three things this app already holds that are not "the password file."
2. For one of them, write one sentence: who can reach it, and what must not happen.
3. Circle anything in your notes that assumes a **server**. Put it on a later list.

If you wrote only "passwords" and "notes," add the hashing settings and the local claim. Those are easy to forget and easy to get wrong.

## What can still go wrong

This catalogue does not encrypt the disk, lock the OS user, or stop someone with your laptop and your session. It stops you from pretending "I hashed it" covers every object in the table.

## Where this shows up later

- Next topic: the trust line around this catalogue.
- Auth topics: which of these objects move to a server, and which stay local.
- The first check-in: you will show this kind of table, not only a hash function name.
