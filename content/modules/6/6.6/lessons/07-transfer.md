# 6.6 — Workflow, race, and exceptional-condition failures (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Password reset; 2.4 share retry; 7.4 jobs.

**Product sketch:** Clinic invite-guardian token.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | DB unique constraint helps but must be the actual consume.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/6.6/6.6-lab` stays the only running system you may break.
