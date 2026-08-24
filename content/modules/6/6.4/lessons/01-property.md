# 6.4 — Files, paths, uploads, archives, XML, deserialization (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
**Mechanism (not the property):** Starlette UploadFile.filename is hostile.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.4 |
|---|---|
| Root cause | Path grammar mixed with data; no canonicalization. |
| Preconditions | resolve('../etc/passwd') escapes root. |
| Impact (1.1 cell) | Authorization of *which file object* plus integrity of the host. — Read/write outside the note store. |
| Prevention | Join + canonicalize + prefix; random stored names; never execute uploads. |
| Detection | denied_escape metric. |
| Recovery | Audit filesystem; restore. |

## Framework defaults vs application guarantees

Starlette UploadFile.filename is hostile.

## Mechanism limits and bypasses

Allow-list of .png still fails if the processor parses XML (XXE) — name it.

Absolute paths, UNC, zip slip, content-type vs magic.

## Residual risk

Image codecs (memory) — E4.

## Practice

Corpus: ../, encoded dots, zip members — as *test names*, not payloads to fire at strangers.

Run `labs/6.4/6.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

XML entity expansion; pickle; YAML load.

Clinic scan upload.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
