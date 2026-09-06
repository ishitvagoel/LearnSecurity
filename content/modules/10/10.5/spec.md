# 10.5 — Logging, detection, incident response, recovery, and maintenance

Pass A specification. Lesson prose lives in `lessons/`. A green SIEM is not recovery — and logs are not a second note store. Do not mark M4 or Gate 10 complete.

## Identity

- **id:** 10.5
- **slug:** logging-detection-incident-response-recovery-and-maintenance
- **title:** Logging, detection, incident response, recovery, and maintenance
- **phase / track / difficulty:** 10 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 3.1 log bodies; 5.1 extra copies; 8.5 crash sinks; 4.3 stolen sessions.
- **routeTags:** complete, web-api
- **releaseMilestone:** M4
- **masteryGate:** 10

## Objective hierarchy

1. Produce a **close predicate** so `close_incident({"recovery": "todo", "logs": "ok"})` is false, and logs must not contain `note_body`.
2. Name attacker capabilities (optimistic closer; real incident still in; observability pipeline as exfil) and trust assumptions (local `close_incident`).
3. Transfer: clinic close ticket when SIEM is green; ransomware restore vs note-level integrity — without treating PagerDuty as recovery.

## Prerequisite concepts

3.1 / `v5.0.0-16.2.5` protection-level logging; 5.1 extra copies; 8.5 crash JSON; 4.3 revoke leftover sessions. NIST CSF 2.0 DE/RS/RC as *outcome labels*. CISA KEV as **awareness** for patch SLA, not close. OWASP Logging Cheat Sheet as vocabulary.

## Misconceptions

- MTTD is the goal.
- Backups untested are recovery.
- Disclosure is legal-only.
- PagerDuty / SIEM green closes the incident.
- Logs may contain note bodies “for forensics.”

## Concept map

Always-true close (break) → require recovery=done and no note_body (this module) → separate log system (`v5.0.0-16.4.3`) → restore drill (CSF Recover) → patch SLA (KEV awareness). Residual: imperfect forensics; support-tool god-mode (3.3).

## Invariant prompts

- What must remain true for `close_incident({"recovery": "todo", "logs": "ok"})`?
- What fails if recovery is done but logs contain `note_body`?

## Threat-model prompts

- What can go wrong if you close on SIEM green?
- What residual remains if the observability pipeline is a 3.1 sink?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/10.5/10.5-lab`. Forbidden: incident closed without recovery evidence; note body in logs. No live IR/SIEM.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-16.1.1` logging inventory (Level 2); `v5.0.0-16.2.5` logging by protection level; `v5.0.0-16.4.2` logs protected from unauthorized modification; `v5.0.0-16.4.3` logs to a logically separate system. The L3 clause of `v5.0.0-16.3.2` (log all authorization decisions without the sensitive data) is **Level 3, labeled advanced**.
- NIST CSF 2.0 (final): Detect / Respond / Recover as outcome labels, not a product.
- OWASP Logging Cheat Sheet (maintained): vocabulary; not the close predicate.
- CISA KEV (awareness): patch-priority input, not close, not a live-scan authorization.

## Review triggers

Close with recovery todo; note bodies in logs; no restore evidence; support tool is god-mode.

## Time budget and SecureCollab

Evidence: detection rule + playbook + restore named. Feeds Gate 10 / M4 (not-attempted).

## Operational considerations

`incident_closed_without_recovery`. Some incidents never get perfect forensic certainty — say so.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: SIEM-green is not recovery; logs are not a body store |
