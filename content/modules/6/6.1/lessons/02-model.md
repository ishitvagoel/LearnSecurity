# 6.1 — Interpreter confusion and injection (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app, /bin/sh, user input |
| Objects | argv vector, name |
| Actions | argv_for_list, uses_shell |
| Channels | subprocess |
| TCB | argv list without shell=True. |
| Untrusted | name string |
| State / time | One export click. |
| 1.1 cell | Integrity of the OS interpreter boundary. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| user | name | as-argv | data |
| user | name | as-shell | deny |
| app | ls | exec | fixed-binary |
| worker | same name | 7.4 | same-cell |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.1/6.1-lab` file `argv.py`.

## Transfer

Jinja, SQL, mail headers.

## Residual risk

Needed shell for a plugin — isolate that binary.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
