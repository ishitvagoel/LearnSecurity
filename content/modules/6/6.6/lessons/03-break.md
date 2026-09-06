# Practice: an invite token accepted twice

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Try it

The practice is not a website you attack. It is a tiny Python `accept`. The failure is already in the function: `accept` returns true and never marks the token used. You are here to see that the check treats a second true as a **failed rule**, not as a retry nit.

The rule under test:

> `accept("t1")` may be true once. The second `accept("t1")` must be false. If it is still true, an invite token was accepted twice.

## Where you may practice

Only `labs/6.6/6.6-lab` is in scope. The practice is an in-process `accept` with synthetic tokens `t1` / `t2`. It does not send mail, open two hosts, or touch an employer invite link.

Do not probe public invite links. Do not click a live mail link. Do not build a race harness. You do not need two processes. You must not.

What you trust for this check: `accept` is supposed to consume the token in the same step that it returns true. A unique index you never write, HTTP 400 after membership already exists, and “the email proves the recipient” are not what you trust.

Who can act, in this story: two tabs, a copied link, or a retry of the same token. That stands in for a clinic guardian invite, a password-reset consume, or 2.4’s share retry.

## Picture: accept always true

```mermaid
flowchart TD
  Call["accept t1"] --> True[returns true]
  Again["accept t1 again"] --> True
```

The broken files take that path on purpose. The token is never consumed. Sequential double-accept is enough. You do not need a new token string. The leftover still returning true *is* the leak.

Industry lists want locking so a limited seat cannot be booked twice. This pytest is sequential consume-once, not a threaded trophy.

## What to look at — cause, not a dump

Read `vulnerable/invite.py`. It returns true every time. `reset()` exists so tests start clean. `_used` in the broken files is unused. Tests:

- `test_invite_token_is_single_use` — second `accept("t1")` is false
- `test_distinct_tokens_are_independent` — `t2` still succeeds once on the repaired files

You do not need a new token string. The failure of `test_invite_token_is_single_use` *is* the evidence.

Do not open the repaired files yet. Diagnose the cause first.

| What you see | What kind of failure | Not the lesson |
|---|---|---|
| `accept` returns true every time | Token never marked used | “We return 400” |
| `_used` unused | Consume is missing | A unique index screenshot |
| Second `t1` still true | Invite accepted twice | A live race harness |

## Why it happens vs what it costs

| Slice | Practice |
|---|---|
| Required rule | Second accept of `t1` is false |
| Why it happens | Token not marked used |
| What has to be true first | `accept` always returns true |
| Trigger | `accept("t1")` then `accept("t1")` |
| What it costs | Integrity of membership; extra member or replay after revoke |
| How you stop it later | Write used in the same step; fail closed on store errors |
| How you notice later | `invite_replay_denied`; never the raw token |
| How you recover later | Keep deny; remove surprise members |
| Out of scope | A famous-bugs list, HTTP 400, or a live race harness |

FastAPI will run `accept` twice if two requests arrive. Postgres unique indexes do nothing until you write the used row. Next.js will happily POST the mail link again. The app's promise this week is: **these** local files, second `t1` is False.

## Practice

From the repository root, in a throwaway environment:

```text
python3 -m pytest labs/6.6/6.6-lab/tests --impl vulnerable
```

Record the failing test `test_invite_token_is_single_use`. Do not probe public invite links. An environment error is not security evidence.

## Use it somewhere new

Clinic guardian invite. Predict, without leaving this directory, whether a second click still joins. Do not click a live mail link.

## What this page is not doing

No live-target instructions. Synthetic tokens only. Sequential double-accept only — no race harness. Do not “fix” the practice by deleting the test.
