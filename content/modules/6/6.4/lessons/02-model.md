# 6.4 — Files, paths, uploads, archives, XML, deserialization (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app, filesystem, user filename |
| Objects | resolved path, root |
| Actions | resolve |
| Channels | upload name, archive member (transfer) |
| TCB | realpath + prefix check after normalization (2.1). |
| Untrusted | filename, symlink, zip slip members |
| State / time | Extract then later process. |
| 1.1 cell | Authorization of *which file object* plus integrity of the host. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| user | safe name | store | under-root |
| user | .. path | resolve | deny |
| zip member | .. | extract | deny |
| processor | upload | exec | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.4/6.4-lab` file `path.py`.

## Transfer

XML entity expansion; pickle; YAML load.

## Residual risk

Image codecs (memory) — E4.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
