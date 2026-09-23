# Security notes (fixed variant)

- `sc_session` is set with `HttpOnly`, `Secure`, and `SameSite=Lax`.
  `HttpOnly` removes one reader (page script); it does not remove
  cross-site scripting (XSS) as a class, and it does not replace output
  encoding, CSP, or Trusted Types. Do not mirror the value into
  `document.cookie` for a second tab — that reintroduces the exact reader
  the flag exists to remove.
- `/notes` reflects `Access-Control-Allow-Origin` and sets
  `Access-Control-Allow-Credentials: true` only when the request's
  `Origin` is an exact match against `ALLOWED_ORIGINS`
  (`https://app.securecollab.example`). No other origin — not a
  subdomain, not a different scheme, not a different port — is granted
  credentialed access. A staging build on a new hostname is added to the
  allow-list explicitly; it is never granted by loosening the match to a
  suffix or substring check.
- `Content-Security-Policy` (enforcing) is present with `object-src
  'none'`, `base-uri 'none'`, and `frame-ancestors 'none'` (ASVS
  v5.0.0-3.4.3, v5.0.0-3.4.6). `Content-Security-Policy-Report-Only` would
  be a reasonable *addition* for testing a stricter policy before turning
  it on, but it never substitutes for this header — Report-Only never
  blocks a resource, however clean its reports look.

Local fixture only. Fake session and note values.
