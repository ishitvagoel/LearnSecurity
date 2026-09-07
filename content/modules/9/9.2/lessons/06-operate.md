# Block eval in review without logging the payload

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A later generated helper can put `eval` back after `review_ok` is green. Page that helper, quarantine the file, and keep the reject.

Keep the eval’d user string and template source with patient fields out of chat.

## Picture: eval in a change is a signal

If a pull request still grants `eval` on a user string, keep the payload out of the pager. Then block the merge and keep the reject.

```mermaid
flowchart TD
  Pr[change] --> Ev{eval on user?}
  Ev -->|yes| Metric["review_block_eval plus 1"]
  Metric --> Revert[block merge]
```

A review-bot vendor does not reject `eval` on a user string.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `review_block_eval` |
| What the line holds | change id, file, reason=eval; **never** the payload |
| Respond | Block merge |
| Recover | Keep reject; add tests (9.3); review generated code |
| Leftover | Substring stand-in; generated code; later review bots |

```text
log_denied reason=review_block_eval pr=pr_92e file=export.py
```

Not: an eval payload, a note body, or a live GitHub trace.

Putting the eval payload or note bodies in the alert leaves a second copy (logging topic / interpreter topic) in the pager.

A formatter passing does not reject `eval`. If the review bot changes, `test_eval_on_user_input_is_rejected` still has to fail on the broken files. Terraform `local-exec` and GitHub Actions `run:` still eval user strings; do not merge until those interpreters are named. The lab substring is a stand-in: an `exec(` helper can skip it, so keep the human interpreter question even after this metric is green.

## What the framework does vs what you still have to check

A GitHub checks dashboard will show the formatter green and stay silent when `review_ok` is always true. Detection must observe **eval-on-user rejected**, not check count. If the alert includes the eval payload or note bodies, you have opened a second leak.

## Practice

```text
log_denied reason=review_block_eval pr=pr_92e file=export.py
```

Reject any line that includes eval payloads, note bodies, or a live GitHub trace.

## Use it somewhere new

Block a template change; do not paste the template source with patient fields into chat. Do not run eval on live input.

## Can people still use it

A blocked review must say *why* in plain language (eval on user input), not only a policy code. Color or a code alone is not enough.

## What this page is not doing

A review-bot sticker does not reject `eval`. This site does not mark you as finished. Answer keys are not on this site.
