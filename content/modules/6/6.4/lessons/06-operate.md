# 6.4 — Files, paths, uploads, archives, XML, deserialization (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | denied_escape metric. |
| Signal (no bodies) | path_escape_denied; malware-scan is extra. |
| Revoke / recover | Audit filesystem; restore. |
| Residual | Image codecs (memory) — E4. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/6.4/6.4-lab`.

## Transfer

XML entity expansion; pickle; YAML load.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
