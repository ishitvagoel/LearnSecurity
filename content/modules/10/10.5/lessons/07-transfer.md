# 10.5 — Logging, detection, incident response, recovery, maintenance (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Ransomware restore vs note-level integrity.

**Product sketch:** Clinic: close ticket when SIEM is green.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | PagerDuty is not recovery.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/10.5/10.5-lab` stays the only running system you may break.
