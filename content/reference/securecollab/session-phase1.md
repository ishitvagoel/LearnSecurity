# SecureCollab Phase 1 — session channel

Design stub for Module 4.3. Not a production IdP.

## Freeze

- Local `session_from_request`. Synthetic token `secret`.
- No live CDN or log drain.

## Query is a postcard

`?access_token=` is not a session. Cookie or Authorization only. JWT format does not choose the channel.

## Tests

Query yields `None`. That is the evidence. “We use JWTs” is not.
