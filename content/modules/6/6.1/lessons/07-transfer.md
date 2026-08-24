# 6.1 — Interpreter confusion and injection (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Jinja, SQL, mail headers.

**Product sketch:** Clinic export-to-CSV filename.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | subprocess defaults are easy to misuse; FastAPI has no opinion.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/6.1/6.1-lab` stays the only running system you may break.
