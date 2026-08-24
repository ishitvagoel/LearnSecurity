# 1.2-LO-03 — Ambient current_user without an object check

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** Saltzer complete mediation (1975, seminal). Authorized **local** fixture only.

## Property (start here)

Does `read_note(user, note_id)` fail when the user is authenticated but **not** granted that note?

## Attacker capabilities and trust assumptions

- **Attacker:** `bob` in the lab store (tenant `tB`), calling the same function alice uses, with note id `n1`.
- **Trust:** this directory is the only target. No public URL, no real accounts.

## What to observe

In `labs/1.2/1.2-authority-matrix/`, `vulnerable/notes.py` returns tenant A’s body to bob. Root cause: **ambient authority** (any authenticated user). Preconditions: bob exists; n1 exists. Impact: 1.1 confidentiality cell fails. This is not a “new Top 10 item”; it is a missing matrix cell.

Do not write exploit scripts for other hosts. Calling `read_note("bob", "n1")` in-process is enough.

## Practice

Run the README pytest commands. Record which test name is the forbidden outcome.

## Transfer

If note ids were random 128-bit values, would the vulnerable function still be wrong? (Yes—obscurity is not the cell.)
