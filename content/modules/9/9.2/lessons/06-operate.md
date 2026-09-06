# 9.2-LO-06 — Detect review_block_eval without logging the payload

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** NIST CSF 2.0 (final) DE/RS/RC as outcome labels; NIST SSDF 1.1 (final) PW.7 / RV.1. ASVS 5.0.0 (final) `v5.0.0-1.3.2`.

## Prevention is not absolute

A later generated helper can reintroduce eval after `review_ok` was “fixed once.” Pair detect and recover. Do not log the user string that would have been eval’d (3.1). Do not paste template source with patient fields into Slack.

## Mental model: eval in a PR is a signal

```mermaid
flowchart TD
  Pr[PR] --> Ev{eval on user?}
  Ev -->|yes| Metric["review_block_eval plus 1"]
  Metric --> Revert[block merge]
```

| Outcome | This module |
|---|---|
| Detect | `review_block_eval` |
| Signal | PR id, file, reason=eval; never the payload |
| Recover | Keep reject; add 9.3 tests; review generated code |
| Residual | Substring stand-in; E1; 9.4 bots |

CSF 2.0 Detect / Respond / Recover name outcomes. They do not prove `v5.0.0-1.3.2`. A bot-vendor name is not the property. Re-run `test_eval_on_user_input_is_rejected` after any review-bot change; a green “formatter passed” tile is not that pytest. Terraform `local-exec` and Actions `run:` are other interpreter paths — inventory them before claiming Recover. The lab substring is a stand-in: an `exec(` helper can skip it, so keep the human interpreter question even after this metric is green.

## Framework defaults versus the operate guarantee

A GitHub checks dashboard will show ruff green and stay silent when `review_ok` is always true. Detection must observe **eval-on-user rejected**, not check count. If the alert includes the eval payload or note bodies, you have opened a 3.1 / 6.1 cell.

## Practice

Write one log line you would accept. Tie it to `labs/9.2/9.2-lab`.

```text
log_denied reason=review_block_eval pr=pr_92e file=export.py
```

Reject any line that includes eval payloads, note bodies, or a live GitHub trace.

## Transfer

Clinic: block a template PR; do not paste the template source with patient fields into Slack. Do not run eval on live input.

## Usability

A blocked review must say *why* in plain language (eval on user input), not only “policy P12” (WCAG 2.2 Success Criterion 4.1.3).

## Non-goals

A bot-vendor name is not the property. Gate 9 stays not-attempted.
