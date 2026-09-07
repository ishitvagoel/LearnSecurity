# Would you merge this always-true close_incident?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Look at `labs/10.5/10.5-lab/vulnerable/` as an incident-close PR. Does `close_incident({"recovery": "todo", "logs": "ok"})` still return true?

Read `close_incident` and the recovery-todo row before a SIEM tile. Shipping “will restore later” leaves `test_cannot_close_without_recovery` failing.

## Picture: close with recovery todo

**close with recovery todo**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|todo still closes| Property["Rule - good if tested"]
  Q -->|SIEM green| Mechanism[Tool - detect]
  Q -->|known-exploited dashboard| False[False assurance]
```

A recovery todo still has to be denied. If the change never checks the conjunction, that always-close leftover is still open. A SIEM screenshot does not replace that check.

Note bodies in logs are the second what must not happen. Support-tool god-mode is leftover from earlier cluster lessons. This page does not mark you as finished. Do not query a live SIEM to prove the finding.

## Problems to find (name them yourself)

- close with recovery todo
- note bodies in logs
- no restore evidence
- support tool is god-mode

Also reject: live incident attacks; closing without re-running both deny tests; keys in learner notes; treating this recovery lesson as a check-in; treating a known-exploited list as close.

## Common mix-ups

- Time-to-detect is the goal
- Untested backups are recovery
- A paging ack closes the incident
- A green SIEM is recover
- Logging note bodies is forensics

## Use it somewhere new

Paging and a known-exploited feed, without a recovery-done check, do not close the incident. What would still keep a recovery-todo incident from closing?

## Can people still use it

A reopen notice must say why the ticket stayed open (recovery still todo), not only “will restore later.”

## What this page is not doing

A close without recovery, plus “will restore later,” is still an unowned leftover. Do not run a live incident against a third-party system to prove the finding.
