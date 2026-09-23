# Lab: 2.3-browser-policy

**Module:** `2.3`
**Authorized scope:** this directory only. A local FastAPI fixture reached
through `fastapi.testclient.TestClient`, never a real browser, a live
site, or a third-party origin.
**Tier:** 2 (component). A real FastAPI app answers `/login` and `/notes`
over an actual request/response cycle; the tests read real response
headers (`Set-Cookie`, `Access-Control-Allow-Origin`,
`Access-Control-Allow-Credentials`, `Content-Security-Policy`) rather than
a modeled dict. See `lab-realism.mdc`.
**Root cause class:** trust (C1: a cookie flag confused with an XSS
guarantee) and an unchecked caller claim (C2/C3: reflecting `Origin`
instead of validating it; C4: Report-Only confused with enforcement).
**Non-goals:** live sites, XSS payloads, a real browser, copy-paste
gadget chains, driving a learner to attack a third-party origin.

## Reset

```bash
git checkout -- labs/2.3/2.3-browser-policy
```

No persistent state; every test builds its own `TestClient`.

## Vulnerable behavior (local only)

`vulnerable/app.py`:

- `/login` sets `sc_session` with neither `HttpOnly` nor `Secure`.
- `/notes` reflects whatever `Origin` header a caller sends back as
  `Access-Control-Allow-Origin`, and always sets
  `Access-Control-Allow-Credentials: true` — for any origin, not only
  SecureCollab's own `https://app.securecollab.example`.
- `/notes` sends `Content-Security-Policy-Report-Only` and never a
  blocking `Content-Security-Policy`.

## Structural fix

`fixed/app.py`:

- `/login` sets `HttpOnly`, `Secure`, and `SameSite=Lax` on `sc_session`.
- `/notes` reflects `Access-Control-Allow-Origin` (with credentials) only
  when `Origin` is an **exact** member of `ALLOWED_ORIGINS`
  (`{"https://app.securecollab.example"}`) — not a suffix or substring
  match, so a lookalike or sibling-subdomain origin is denied along with
  an unrelated one.
- `/notes` sends an enforcing `Content-Security-Policy` with
  `object-src 'none'`, `base-uri 'none'`, and `frame-ancestors 'none'`.

## Verify

```bash
python3 -m pytest labs/2.3/2.3-browser-policy/tests --impl vulnerable   # 6 of 9 fail
python3 -m pytest labs/2.3/2.3-browser-policy/tests --impl fixed        # 9 of 9 pass
```

Nine tests: the cookie normal case (`Secure` present) and forbidden
outcome (`HttpOnly` missing), each parsed as a discrete Set-Cookie
attribute token rather than a raw substring search; a cookie anti-fake
test (a cookie *value* that merely spells out the text "HttpOnly" or
"Secure" must not satisfy either check); the CORS normal case (trusted
origin reflected with credentials); the CORS forbidden outcome (an
arbitrary attacker origin denied credentialed access); an origin-vs-site
boundary case (a sibling subdomain, a scheme change, and a port change
are each a different origin); a malformed/failure case (no `Origin`
header at all must not crash and must not manufacture a grant); an
anti-fake test (a domain that merely contains the trusted origin as a
trailing substring must still be denied); and the CSP enforcement case
(a real `Content-Security-Policy`, not only `Report-Only`).

**Verified against an actual fake fix:** a "fixed" `/notes` that checks
`origin.endswith("securecollab.example")` (no leading dot) instead of
exact set membership passes 6 of 9 tests — it defeats the plain reflected
CORS case — but fails exactly
`test_anti_fake_lookalike_domain_is_not_treated_as_the_trusted_origin` and
`test_origin_vs_site_boundary_subdomain_scheme_and_port_are_each_denied`,
because it also trusts `https://evilsecurecollab.example` (a substring
lookalike with no shared dot-delimited label) and
`https://evil.securecollab.example` (a real but unauthorized sibling
subdomain). A second fake fix was found and closed during independent
verification of this pass: the original `HttpOnly`/`Secure` tests read
the raw `Set-Cookie` header with a substring search, so
`set_cookie("sc_session", "tok-HttpOnly-Secure")` — a value that never
sets either flag — passed both tests. The tests now parse the header
into its `;`-delimited attribute tokens before checking, and a dedicated
anti-fake test pins that parsing down.

## What the tests do not prove

`TestClient` is not a browser: it never enforces CORS or same-origin
policy itself, so these tests can only assert the header a real browser
would consult, never that a browser actually blocked anything. They do
not prove output encoding, Trusted Types, SameSite's CSRF behavior, or a
WebView bridge's handling of the same cookie. See
[`content/modules/2/2.3/lessons/05-verify.md`](../../../content/modules/2/2.3/lessons/05-verify.md).

## Operate

Never log `sc_session`'s value, a note body, or a raw `Origin`/CSP report
blob. See
[`content/modules/2/2.3/lessons/06-operate.md`](../../../content/modules/2/2.3/lessons/06-operate.md).

## Transfer

Third-party iframe or a React Native WebView cookie bridge: a new reader
of the same cookie, and a new `frame-ancestors`/embedding row. This lab
does not prove CORS or clickjacking against any real target. See
[`content/modules/2/2.3/lessons/07-transfer.md`](../../../content/modules/2/2.3/lessons/07-transfer.md).
