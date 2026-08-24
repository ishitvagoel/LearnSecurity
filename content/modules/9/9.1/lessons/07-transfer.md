# 9.1 — Verification requirements and traceability (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** MASVS STORAGE for 8.2.

**Product sketch:** Clinic: HIPAA “done” column.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | ASVS PDF is not your matrix.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/9.1/9.1-lab` stays the only running system you may break.
