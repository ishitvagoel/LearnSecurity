# Lab 5.4 — client Forwarded-Proto is not TLS

**Module:** `5.4`
**Authorized scope:** this directory only. Local course fixture. No live load balancers.
**Invariant:** `channel_is_https({"X-Forwarded-Proto": "https"}, "http")` is false. The server socket scheme is the channel, not a client header.
**Root cause class:** confused deputy (app believes the client about TLS)
**Non-goals:** live TLS handshakes, SSLStrip walkthroughs, pinning exploits.

## Reset

Re-run pytest. Optional: `git checkout -- labs/5.4/5.4-lab`.

## Vulnerable behavior (local only)

`channel_is_https` trusts `X-Forwarded-Proto` from the request. Forbidden outcome: client-supplied `https` on an `http` socket counts as TLS.

## Structural fix

Use the server’s view of the connection. A trusted proxy is a **bound peer**, not a header name. This lab has no trusted proxy, so the header is ignored.

## Verify

```
python3 -m pytest labs/5.4/5.4-lab/tests --impl vulnerable
python3 -m pytest labs/5.4/5.4-lab/tests --impl fixed
```

The first command must fail on the forwarded-proto test. The second must pass. Honest server-https may pass on both.

## Operate

Signal: `header_https_socket_http`. Do not mark cookies Secure on that path. Revoke cookies issued over cleartext.

## Transfer

Clinic SPA `https://` axios baseURL while the API socket is `http`. Prompt only.
