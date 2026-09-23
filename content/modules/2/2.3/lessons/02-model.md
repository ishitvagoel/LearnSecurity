# A browser policy matrix a second engineer can test

**Kind:** design-exercise
**Loop step:** 2 Model

## Could someone else name the checks from your table?

A slide that says "we use CSP, cookies, and CORS" tells a reviewer nothing that could be tested, because it names three product categories rather than three specific, falsifiable checks against SecureCollab's own `/login` and `/notes` handlers. A model earns its keep only when a second engineer, reading nothing but the table, could write the exact request that should be denied and predict the exact response headers that denial produces — the same standard [`lessons/01-property.md`](01-property.md) set for the property itself. This lesson builds that table for the local fixture this module's lab exercises, so the next four lessons have one shared map to break, repair, verify, and operate against.

Two artifacts feed the table. First, [`lessons/01-property.md`](01-property.md) named four response headers and, for each, who enforces it and what a wrong value costs. Second, the fixture itself has exactly two endpoints and one cookie: `POST /login`, which sets `sc_session`, and `GET /notes`, which reads it and answers with note text. Everything this model needs to say is already implied by those two artifacts; the work here is turning "who enforces it" into rows specific enough that a test could fail, and specific enough that a second engineer, handed only the finished table, could write that failing test without ever reading this lesson's prose again.

## Step 1: name the pieces

| Piece | This system |
|---|---|
| Who | Page script in `https://app.securecollab.example` (including the member's own bundle after any future XSS); the browser's cookie jar and CORS check; a cross-origin script at an arbitrary origin; a network attacker (TLS, not this fixture's oracle) |
| What | `sc_session`'s value; the `Origin` request header; `Access-Control-Allow-Origin`/`-Credentials`; `Content-Security-Policy`/`-Report-Only` |
| Actions | Read `document.cookie`; send a credentialed cross-origin `fetch`; load or execute a script the policy names |
| Paths | `POST /login` response headers; `GET /notes` request and response headers; a later WebView bridge that copies the cookie into JS |
| What you trust | The browser honors `HttpOnly`, honors `Access-Control-Allow-Origin`/`-Credentials`, and honors an enforcing `Content-Security-Policy`; the server sets each header correctly for `sc_session` and for `/notes` |
| What you do not trust | Any JavaScript running in the origin; any value a caller sends in its own `Origin` header, as a claim about who it is |
| Time | The cookie's lifetime vs. the window during which a cross-origin script could be running against a signed-in member |
| The rule | Session secrecy against script (C1); response secrecy against an uninvited cross-origin, credentialed caller (C2, C3); load/execution containment against untrusted script sources (C4) |

## Step 2: write the rows

A row is only useful if it names an input, an action, and a decision specific enough to fail a test. The table below is the same fixture's policy matrix, one row per header from [`lessons/01-property.md`](01-property.md), plus the origin/site distinction that header table left implicit.

| Who | What | Action | Decision |
|---|---|---|---|
| Page script in `https://app.securecollab.example` | `sc_session` (HttpOnly) | Read via `document.cookie` | Deny |
| `https://app.securecollab.example` (exact) | `/notes` | Cross-tab credentialed `fetch` | Allow, with `Access-Control-Allow-Credentials: true` |
| `https://evil.securecollab.example` (same site, different origin) | `/notes` | Credentialed `fetch` | Deny — a shared registrable domain is not a shared origin |
| `http://app.securecollab.example` (scheme downgrade) | `/notes` | Credentialed `fetch` | Deny — scheme is part of origin |
| Any origin with no `Origin` header at all (same-origin navigation) | `/notes` | Ordinary same-origin request | Allow; no CORS header needed or added |
| A script source not in the CSP allow-list | Any script tag or inline handler | Load/execute | Deny, only if the header sent is enforcing `Content-Security-Policy` — never if it is only `-Report-Only` |

A missing row here is exactly how a second cookie, a staging subdomain, or a "just for now" wildcard quietly becomes the actual attack surface. If a teammate later adds `sc_refresh` or a debug cookie, or widens `ALLOWED_ORIGINS` to a pattern instead of a literal set, that change is a new row this table has to gain — not a detail the existing rows already covered by implication.

## Step 3: draft versus final, and browser versus server

Two axes matter for every row, and conflating them is the specific misconception this module lists: whether a control is *finished as a standard* (final vs. draft) says nothing about whether it is *enforced by the browser or by the application*, and vice versa.

| Control | Status in this snapshot | Who enforces it |
|---|---|---|
| `HttpOnly` on `sc_session` | ASVS v5.0.0-3.3.4, final | Browser (cookie jar) |
| `Secure` on `sc_session` | ASVS v5.0.0-3.3.1, final | Browser (refuses to send over plaintext) |
| Exact-origin CORS allow-list | ASVS v5.0.0-3.4.2, final | Server decides the header value; browser enforces the resulting grant or denial |
| Enforcing `Content-Security-Policy` | ASVS v5.0.0-3.4.3, final | Browser (blocks load/execution); server must send the enforcing header, not only `-Report-Only` |
| CSP3 (the specification defining newer CSP directives) | W3C Working Draft | N/A — this row is about the spec text's maturity, not about whether *this fixture's* CSP header is enforcing |
| Trusted Types | W3C Working Draft | Browser, where implemented; not exercised by this fixture |

The CSP3/Trusted Types row is worth sitting with, because it is where the two axes most often get merged into one wrong conclusion: ASVS's requirement that a response carry a Content-Security-Policy header is a *final*, settled piece of guidance, even though the W3C specification that defines several of CSP's newer directives is still a *Working Draft* text. A team can therefore ship a fully compliant, fully enforcing CSP header today using only stable directives, while accurately describing CSP3 itself as draft — "draft" describes the specification document's maturity, not whether the header your server sends this minute blocks anything.

## Worked example: filling in a row from the fixture, not from imagination

A matrix built from imagination tends to describe the system its author wishes existed rather than the one running in `labs/2.3/2.3-browser-policy/vulnerable/app.py`. Reading that file's `/notes` handler line by line is what actually fills in the CORS row correctly:

```python
origin = request.headers.get("origin")
if origin:
    response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
```

There is no comparison here at all — no `if origin in ALLOWED_ORIGINS`, no `endswith`, nothing that reads as an allow-list even loosely. The condition `if origin:` only asks whether a caller sent *some* `Origin` header, not which one, so the row this code actually implements is "any origin that sends one → allow, with credentials," which is a materially different row from "the origins we trust → allow, with credentials." A matrix filled in from the variable name `Access-Control-Allow-Origin` alone, without reading this function, would have quietly assumed a check exists here that the code never performs.

## Counterexample: a matrix that lists every header but still misses the failure

A table can name `Set-Cookie`, `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`, and `Content-Security-Policy` — every header [`lessons/01-property.md`](01-property.md) named — and still fail to model this fixture, if every row's "who enforces it" column stops at "the browser" without also stating what value the *server* must send for that enforcement to matter. "The browser enforces `Access-Control-Allow-Origin`" is true and worthless on its own, because the browser enforces whatever value the server happens to send, including a value that grants everyone. The row is only complete once it names the comparison the server must perform before choosing that value — exact set membership against `ALLOWED_ORIGINS` — which is precisely the sentence the worked example above shows is missing from the vulnerable fixture.

## Practice

Fill in one additional row for a hypothetical `sc_refresh` cookie that SecureCollab issues alongside `sc_session` for silent token renewal, using the same six columns Step 1 lists, and state which existing row's decision it would break if `sc_refresh` were issued without `HttpOnly`.

## Use it somewhere new

[2.2 DNS, transport, HTTP, TLS, proxies, CDNs, and caches](../../2.2/spec.md) covers a CDN sitting in front of this same `/notes` endpoint. Before opening that module's own materials, predict which row above a CDN that caches the `Access-Control-Allow-Origin` response header per-path, rather than per-request, would silently break.

## What can still go wrong

A row can be correct today and wrong tomorrow if `ALLOWED_ORIGINS` is edited to a pattern instead of a literal set, if a load balancer strips or rewrites `Origin` before the application sees it, or if a CDN caches a CORS response keyed only by path rather than by the caller's `Origin`. None of those failures are visible from this table alone; they are why [`lessons/06-operate.md`](06-operate.md) exists.

## What this page is not doing

Do not use live sites or third-party CORS probing. This is a design model for [`labs/2.3/2.3-browser-policy`](../../../../../labs/2.3/2.3-browser-policy/README.md), not a claim that SecureCollab has a deployed CDN, a real WebView, or production DNS. Answer keys are not on this site.
