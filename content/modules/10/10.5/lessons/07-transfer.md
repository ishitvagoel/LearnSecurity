# 10.5-LO-07 — Transfer: clinic close ticket when SIEM is green

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** ASVS `v5.0.0-16.2.5`. NIST CSF 2.0 Recover. CISA KEV as awareness not close. L3 clause of `v5.0.0-16.3.2` is **Level 3, advanced**.

## Change the workplace; keep SIEM-green from meaning recovered

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `close_incident({"recovery": "todo", "logs": "ok"})` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic: close ticket when SIEM is green. Also name ransomware restore vs note-level integrity.

**Product sketch:** EHR-lite “alerts stopped so we closed INC-12,” plus “we have nightly backups and a KEV dashboard.”

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (optimistic closer / still-in actor — not a live clinic SIEM attack);
2. trust assumptions (recovery=done and no note_body is TCB; SIEM/PagerDuty/KEV/backups-untested are not);
3. forbidden outcome (`close_incident` true while recovery is todo, not “HIPAA”);
4. a test idea on a **local** fixture only (no live PagerDuty);
5. residual (imperfect forensics, observability exfil, support-tool god-mode, L3 clause of `v5.0.0-16.3.2`);
6. WCAG if the runbook is human-read under stress (not color-only severity).

## Mental model: green vs restored

```mermaid
flowchart LR
  Green[SIEM green] --> Belief[over]
  Todo[recovery todo] --> Reality[still broken]
```

If alerts stopped while `close_incident` is always true, the cell is gone. PagerDuty, KEV, and untested nightly backups do not set `recovery` to `"done"`. Ransomware restore (disk image) is a different grain from note-level integrity (5.1) — name both, do not run a live IR exercise here. CSF 2.0 Recover is an outcome label. KEV is patch-SLA input, not close. The L3 clause of `v5.0.0-16.3.2` is advanced: log all authz decisions without the sensitive data.

The clinic rewrite still has to keep the SecureCollab fork: recovery todo denied, note_body denied, done + ok may close. Wiring PagerDuty without the conjunction leaves `close_incident` true on todo. The local pytest analogue is `test_cannot_close_without_recovery` — on a fixture, not a live SIEM.

## What graders reject

| Reject | Why |
|---|---|
| “we have backups” | Untested is not Recover |
| Live SIEM / ransomware tutorial | Lab policy |
| “KEV listed so we closed” | Awareness / patch input, not close |
| “MTTD improved” | Detect metric, not recover |
| “Gate 10 complete” | Forbidden stamp |

## Practice

One page. No keys. `labs/10.5/10.5-lab` is the only running system you may break. Do not query a live SIEM.

## Non-goals

Live-IR attacks. Real PHI in logs. Claiming Gate 10 or M4 from this page.
