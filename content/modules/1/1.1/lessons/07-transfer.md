# Same rule, a different app

**Kind:** transfer-challenge
**Loop step:** 7 Generalize

## Use it somewhere new

The rule was never "Argon2 on a JSON file." It was: **the password is not sitting there in a form you can read, and two users with the same password do not look the same on disk.**

Carry that to one other place you already know.

## Pick one

**A command-line tool** that stores a local login for a hobby project.

**A mobile app** that remembers "this device is enrolled" — different asset (device key vs password), same honesty: do not store the secret in a form you can copy out of a backup.

**A group project** that currently has `password` in a YAML practice files. Name the change: hash, unique salt, settings, compare that does not leak timing. Name what stays out of scope (no public website).

Write:

1. The asset (what secret).
2. The store (where it lives).
3. Who can read that store.
4. The smallest record that keeps the rule.
5. One test that would fail if someone stores the secret readable.

## Industry lists (after the design)

You may now look up password storage on the industry lists. You should see the same ideas: slow hash, unique salt, no plaintext. If a list says "encrypt passwords," read carefully — reversible encryption is not the password store this page is about.

We map to those lists on the sources page. Do not start a design from the list code. Start from the rule, then tick the list.

## Check yourself

If your transfer still says "because OWASP said so" and never names the store, it is not a transfer. It is a citation.

## What can still go wrong

A local hashed claim is not a server session. Copying this JSON to a VPS and opening port 443 does not inherit the evidence from this page.

## Where this shows up later

Auth topics will make you transfer again — this time across a network. Keep this page's five lines. You will reuse them.
