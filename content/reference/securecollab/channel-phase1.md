# SecureCollab Phase 1 — channel binding

Design stub for Module 5.4. Not a production load balancer.

## Freeze

- Local `channel_is_https(headers, server_scheme)`.
- No trusted proxy in this lab; ignore client Forwarded-Proto.

## Socket, not header

`X-Forwarded-Proto: https` on an `http` socket must be false. RFC 9846 is the TLS 1.3 pin. Pinning is a later trade-off.

## Tests

Header/socket mismatch is the evidence. SPA `https://` is not.
