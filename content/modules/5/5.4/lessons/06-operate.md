# Notice header/socket mismatch; revoke cleartext cookies

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A proxy that trusts `*` again will mint cookies on a cleartext socket. Cookie values and the session do not go in the ticket.

## Picture: header versus socket mismatch is a signal

If the client header says https while the socket is http, keep cookies out of the pager. Then revoke the cleartext cookies.

```mermaid
flowchart TD
  Req[Request] --> Mismatch{"header https and socket http?"}
  Mismatch -->|yes| Metric["header_https_socket_http += 1"]
  Metric --> Alert["reason=header_https_socket_http no cookie"]
  Alert --> Revoke[Revoke cookies issued on that path]
```

A TLS dashboard does not compare the client header to the socket.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `header_https_socket_http` |
| What the line holds | request id, socket scheme — **never** the cookie |
| Respond | Stop trusting the header |
| Recover | HSTS once TLS is real; revoke cleartext cookies; re-run `test_client_forwarded_proto_is_not_tls` |
| Leftover | Pinning (later on phones); cookies already copied |

```text
log_denied reason=header_https_socket_http socket=http request_id=req_54ch
```

A session cookie, a note body, or “HSTS handled” turns that sample into a cookie store.

Putting a session cookie or a note body in the alert leaves a second copy in the pager.

A “Force HTTPS” toggle does not prove the socket is TLS. A client `https` header on an http socket still has to fail `test_client_forwarded_proto_is_not_tls`. Page `https://` versus API socket `http` is another hop; do not call TLS done until that pair is named.

## What the framework does vs what you still have to check

A CDN dashboard will show “HTTPS only” and stay silent when the app still trusts `X-Forwarded-Proto` from anyone. Notice must observe **header https and socket http**, not a preload list. A server flag that trusts proxy headers does not emit this alert for you.

## Can people still use it

If a human sees a certificate or mixed-content warning, make the error readable. Do not encode “not TLS” as color only. A silent fail that pushes people onto http is leftover risk, not polish.

## Practice

Log ids and a reason for the header-versus-socket miss — never the cookie. A session cookie, a note body, or “HSTS handled” would turn the deny line into a cookie jar.

## Use it somewhere new

Notice page-https versus API-http; do not paste cookies into the ticket. Do not probe a live clinic.

## What this page is not doing

Do not use live TLS hunts. This site does not mark you as finished. Answer keys are not on this site.
