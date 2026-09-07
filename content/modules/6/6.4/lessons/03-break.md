# Practice: a resolved path leaves the lab folder

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Try it

The practice is not a website you attack. `resolve` does not open a live upload folder, an employer imaging store, or a classmate preview. The name is joined onto the folder and returned as a string, with no canonicalize-and-prefix, so the joined string is treated as the file.

> After join and canonicalize, `resolve` must still be `/tmp/sc-lab` or a child. A filename is data, not a filesystem object.

## Where you may practice

Stay inside `labs/6.4/6.4-lab`. Fake names under the lab folder `/tmp/sc-lab`. Tests must not read host files outside that folder. Restore the broken and repaired folders when you are done.

Do not open a live upload folder. Do not walk a public filesystem. Do not point this exercise at an employer imaging store, a classmate preview, or anyone else’s disk.

`resolve("../outside")` leaving `/tmp/sc-lab` after canonicalize is the escaped path.

Picture a member who can supply an upload **filename** (data) — a clinic scan name, a zip member path (leftover, later and harder), or `UploadFile.filename` from Starlette. `resolve` joins, canonicalizes, and denies unless the object is still `/tmp/sc-lab` or a child — not A denylist of `..`, a UUID filename sticker, or `Content-Type`.

## Picture: join without canonicalize

```mermaid
flowchart TD
  Call["resolve ../outside"] --> Join["root / name"]
  Join --> Escapes["canonical path leaves folder"]
```

Path grammar is mixed with data. The name `../outside` is **data**. Do not use it against other directories. `resolve` returns `str(ROOT / name)` without canonicalize-and-prefix. You do not need to `open()` the result. You must not.

An awareness list that names “path walk” is not the failing check.

## What to look at: the cause, not a hunt

`vulnerable/path.py` joins the name onto `/tmp/sc-lab` and returns the string. Checks:

- `test_dotdot_does_not_escape_root` — `ValueError` **or** resolved path still under the folder
- `test_honest_relative_stays_under_root`

## Why it happens, what it costs, how you stop it, how you notice, how you recover

| Slice | This practice |
|---|---|
| The rule | Resolved object is still under `/tmp/sc-lab` |
| Why it happens | Path grammar mixed with data; no canonicalization |
| What's already wrong | `resolve` returns join without a prefix check |
| Trigger | `resolve("../outside")` |
| What it costs | Who is allowed to pick *which object*; the host store can change |
| How you stop it | Canonicalize then prefix; deny if uncertain |
| How you notice | `path_escape_denied`; never the raw filename if it is a patient id |
| How you recover | Deny; audit; restore if a file landed outside |
| Not the lesson | An awareness-list name, UUID rename, or a host-file hunt |

## What the framework does vs what you still have to check

Starlette `UploadFile.filename` is client data. `pathlib.Path / name` does not canonicalize. FastAPI will write wherever you tell it. `../outside` does not leave `/tmp/sc-lab`.

## Practice

```text
python3 -m pytest labs/6.4/6.4-lab/tests --impl vulnerable
```

Record the failing test `test_dotdot_does_not_escape_root`. Do not open host files. An environment or import error is not security evidence.

## Use it somewhere new

A scan upload can join the original filename onto a public folder. Predict, without leaving this directory, whether that join still leaves the imaging root. Do not touch a live imaging folder.

## What this page is not doing

No live-target steps. Fake names only. Do not read files outside the lab folder. Do not “fix” the practice by deleting the check.
