# Notice invite_replay_denied

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A new accept route can skip consume after the token lives in a `set`. Notice the second join, keep the deny, remove a surprise member, and do not log the token.

Keep tokens, email addresses, and the mail link out of the ticket.

## Picture: second accept is a signal

If a second accept lands after consume, name the extra membership — not the token. Then remove the extra membership.

```mermaid
flowchart TD
  Acc[accept] --> Used{"already consumed?"}
  Used -->|yes| Metric["invite_replay_denied += 1"]
  Metric --> Alert["reason=invite_replay_denied no token"]
  Alert --> Revoke[Remove extra membership if one landed]
```

A log product does not consume the token.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `invite_replay_denied` |
| What the line holds | request id, invite id — **never** the raw token |
| Respond | Keep deny; stop the route that skipped consume |
| Recover | Remove surprise members; rotate the token scheme if leaked; re-run `test_invite_token_is_single_use` |
| Leftover | Email phishing (4.2) |

```text
log_denied reason=invite_replay_denied invite_id=inv_66a request_id=req_66a
```

A sample that still contains the token, a note body, a real email, or “the mailer said clicked once” is a second mailer dump.

A raw token in the second-accept ticket is a 4.3 leftover.

A unique-index screenshot does not consume the token. “Link clicked once” on a mail vendor tile does not consume `/accept` the second time. Treat **second `accept` false** as the miss, not a click counter. Password-reset consume is another once-token; the seat is not taken until that path is named.

## What the framework does vs what you still have to check

A mailer dashboard is not consume. FastAPI does not emit `invite_replay_denied` for you. A second join still has to fail `test_invite_token_is_single_use`.

## Can people still use it

If a human sees “link already used,” announce it in text a screen reader can speak. A silent retry loop looks like a broken link and pushes people to share the token (4.2).

## Practice

Second accept: ids and a reason, never the token. The token, a note body, or a real email would expose the mailer secret.

## Use it somewhere new

Notice guardian-invite replays; do not paste the mail link into the ticket. Do not click a live invite.

## What this page is not doing

Do not use live invite replay. This site does not mark you as finished. Answer keys are not on this site.
