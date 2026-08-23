# 1.2-LO-08 — Seeded admin JSON route without a policy check

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V8 (final), chapter-level. Intended findings are **not** in this file.

## Property (start here)

Does a new route inherit the matrix, or does it reintroduce ambient authority?

## Attacker capabilities and trust assumptions

Review the **local** `vulnerable/notes.py` (and the idea of an `/admin/notes/{id}` handler that calls the same function). Do not review a live service.

## What to label

For each claim in `vulnerable/SECURITY.md` and the `read_note` body: **property**, **mechanism**, or **false assurance**.

Look for: login used as authorization; missing object tenant; fail-open on unknown ids; “admin” as a boolean.

## Practice

Write three review notes. Do not open the keys file.

## Transfer

A GraphQL `note(id:)` field is another path. Complete mediation is **every** path, not the first REST handler.
