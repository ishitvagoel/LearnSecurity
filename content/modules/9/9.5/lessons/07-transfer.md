# 9.5 — Authorized assessment, reporting, and remediation (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** KEV vs internal-only.

**Product sketch:** Clinic pentest PDF shelf.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Jira Done is not retest.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/9.5/9.5-lab` stays the only running system you may break.
