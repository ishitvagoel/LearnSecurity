# 6.4 — Files, paths, uploads, archives, XML, deserialization (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** XML entity expansion; pickle; YAML load.

**Product sketch:** Clinic scan upload.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Starlette UploadFile.filename is hostile.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/6.4/6.4-lab` stays the only running system you may break.
