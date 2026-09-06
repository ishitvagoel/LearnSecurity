# review_block_eval without logging the payload

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Stopping it is not enough

Even after `review_ok` was “fixed once,” a later generated helper can put eval back. Running it for real is the rest of the loop: notice, contain, and recover.

Do not log the user string that would have been eval’d. Do not paste template source with patient fields into chat.

## Picture: eval in a change is a signal

A pull request whose diff still grants `eval` on a user string is a notice-and-recover problem, not a licence to quote the payload in the paging channel. Notice names the event. Recover blocks the merge and keeps the reject. Neither reprints the payload.

```mermaid
flowchart TD
  Pr[change] --> Ev{eval on user?}
  Ev -->|yes| Metric["review_block_eval plus 1"]
  Metric --> Revert[block merge]
```

Industry lists name detect, respond, recover. They do not prove avoid-eval. A bot-vendor name is not the rule. Someone still has to own the always-approve path.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `review_block_eval` |
| What the line holds | change id, file, reason=eval; **never** the payload |
| Respond | Block merge |
| Recover | Keep reject; add tests (9.3); review generated code |
| Leftover | Substring stand-in; generated code; later review bots |

A log line a reviewer can accept looks like:

```text
log_denied reason=review_block_eval pr=pr_92e file=export.py
```

Not: an eval payload, a note body, or a live GitHub trace.

If your alert includes the eval payload or note bodies, you have opened a second leak in the paging channel (logging topic / interpreter topic).

A green “formatter passed” tile is not that pytest. Re-run `test_eval_on_user_input_is_rejected` after any review-bot change. Terraform `local-exec` and GitHub Actions `run:` are other interpreter paths — inventory them before claiming recover. The lab substring is a stand-in: an `exec(` helper can skip it, so keep the human interpreter question even after this metric is green.

## What the framework does vs what you still have to check

A GitHub checks dashboard will show the formatter green and stay silent when `review_ok` is always true. Detection must observe **eval-on-user rejected**, not check count. If the alert includes the eval payload or note bodies, you have opened a second leak.

## Practice

Write one log line you would accept in review. Tie it to `labs/9.2/9.2-lab`.

```text
log_denied reason=review_block_eval pr=pr_92e file=export.py
```

Reject any line that includes eval payloads, note bodies, or a live GitHub trace.

## Use it somewhere new

Clinic: block a template change; do not paste the template source with patient fields into chat. Do not run eval on live input.

## Can people still use it

A blocked review must say *why* in plain language (eval on user input), not only a policy code. Color or a code alone is not enough.

## What this page is not doing

A bot-vendor name is not the rule. This site does not mark you as finished. Answer keys are not on this site.
