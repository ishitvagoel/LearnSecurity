# Security notes (vulnerable variant)

**Status:** Reviewed and merged. Seeded for module 2.3's code-review lesson
(`lessons/08-review.md`) — a learner should find these claims false against
the code in this directory, not against a live site.

- The web client mirrors `sc_session` into `document.cookie` on load, so a
  second tab can restore sign-in state without another round trip to
  `/login`.
- Because `sc_session` is `HttpOnly`, stored or reflected XSS cannot be
  used to steal a session — `document.cookie` access to it is safe by
  construction.
- CORS on `/notes` reflects the caller's `Origin` with credentials
  enabled on purpose: the mobile team's staging builds change hostname
  every sprint, and pinning one allowed origin would break their pipeline
  each time they redeploy.
- `Content-Security-Policy-Report-Only` is deployed and is actively
  blocking disallowed script sources while we finish enumerating the
  allow-list; CSP is on.
- `Secure` is not yet set on `sc_session`; tracked separately as
  low-priority since the cookie is already believed unreadable to script.

Do not use this variant against any real site. Local fixture only. Fake
session and note values.
