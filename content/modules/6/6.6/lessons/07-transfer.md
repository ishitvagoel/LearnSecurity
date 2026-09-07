# Same idea on a clinic invite-guardian token

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a **clinic invite-guardian token**. An “add guardian” mail link always returns 200.

Second `accept('t1')` must be false. For a clinic, consume-once, first true, second false.

Also name password reset, 2.4 share retry, and later jobs (7.4) as the same family with different “once” meanings.

## Picture: guardian invite is still a limited seat

The guardian invite is token `t1`. A click counter is not consume. FastAPI, a unique-index screenshot, and “we emailed the guardian” do not consume.

| Notes app | Clinic sketch |
|---|---|
| `t1` invite token | Guardian mail-link token |
| `accept` | Join analogue |
| second `accept` false | Second click must not add another guardian |
| Two tabs / copied link | Two clicks / copied link — **not** a live clinic |
| Password reset; 2.4 retry; 7.4 jobs | Same family — name the “once,” do not run them here |

```mermaid
flowchart LR
  Mail[mail link] --> Belief[UI believes one click]
  Twice[two accepts] --> Reality[two memberships if not consumed]
```

If the mail link always returns 200 and never writes used, the hole is open. A magic-link that stays a standing session is 4.3 — exchange it for a cookie; this check owns consume. Adding a unique index without a second-accept test leaves `accept` always true. The local check is `test_invite_token_is_single_use` — on a practice, not a live mail link.

## Write this for a clinic invite-guardian

1. who might try (two clicks or a copied link — **not** a live clinic);
2. what you trust (consume in the store is trusted; HTTP 400 is not);
3. what must not happen (second `accept` true);
4. first accept true, second accept false — **local** files (never on the real clinic);
5. leftover (two accepts that both see unused; fail-open; token in URL; phishing; last-resort error handler is advanced);
6. whether a human-read “link already used” status must not use color as the only cue.

## What is not good enough

| Reject | Why |
|---|---|
| “We return 400” | Error page is not consume |
| Live clinic probe | Course rules |
| A famous-bugs list as the rule | Awareness after the cause |
| HTTP 200 as consume evidence | Wrong observation |
| Unique index without a write | Tool theater |

## Practice

Consume the invite so the second accept is false. Keep the answer keys closed. The only running system you may break is `labs/6.6/6.6-lab`. Do not click a live invite.

## What this page is not doing

Do not try live-target races. Do not use real invite tokens. This page does not finish a check-in.
