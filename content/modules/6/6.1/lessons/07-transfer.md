# 6.1-LO-07 — Transfer: clinic export-to-CSV filename

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-1.2.5`; `v5.0.0-1.2.10` Level 3 advanced for formula characters.

## Change the workplace; keep data-vs-grammar

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `argv_for_list` must not start `sh -c`. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic export-to-CSV filename chosen by a clerk. Also name Jinja, SQL (5.5), and mail headers as the same shape.

**Product sketch:** EHR-lite “download roster” that shells out to `ls` or to a CSV writer.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (clerk-chosen filename — not a live clinic);
2. trust assumptions (argv list is TCB; denylist of `;` is not);
3. forbidden outcome (`argv_for_list` starts `sh -c`, not “HIPAA”);
4. a test idea on a **local** fixture only (shape, no execution);
5. residual (argument injection; CSV formula Level 3; plugin shells);
6. WCAG if a human “export failed” path is in the claim (readable error, not a silent missing file).

## Mental model: filename is still an interpreter input

```mermaid
flowchart LR
  File[CSV filename] --> Belief[UI believes it is a label]
  Shell2["sh -c or formula cell"] --> Reality[grammar mixed with data]
```

If the clerk-chosen filename is concatenated into `sh -c`, the cell is gone. FastAPI, a denylist of semicolons, and “internal clerk” trust do not bind argv. Jinja, SQL (5.5), and mail headers are the same shape at other parsers — name them, do not run those systems here. Formula characters in the CSV *body* are `v5.0.0-1.2.10` Level 3 advanced, a different residual.

The clinic rewrite still has to keep the SecureCollab fork: the spawn helper returns a list whose program is not `sh`, and the name is one element. Sanitizing `;` while still calling `sh -c` leaves the second parser. The local pytest analogue is `test_does_not_invoke_shell` — on a fixture, not a live export worker.

## What graders reject

| Reject | Why |
|---|---|
| “We blacklist semicolons” | Incomplete mediation (2.1) |
| Live clinic probe | Lab policy |
| CWE-78 as the property | Awareness after the cause |
| HTTP 200 as argv evidence | Wrong observation |
| Executing argv to prove the finding | Lab policy |

## Practice

One page. No keys. `labs/6.1/6.1-lab` is the only running system you may break. Do not execute argv or run a live worker.

## Non-goals

Live-target shells. Real patient filenames. Claiming Gate 6 from this page.
