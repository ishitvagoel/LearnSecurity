# SecureCollab Phase 1 — browser cookie jar

Design stub for Module 2.3. Not a production cookie policy.

## Freeze

- Local `js_read_session` model of `document.cookie`.
- No real XSS pages, no third-party CORS tests.

## Two interpreters

The jar may send `Cookie` to the origin. Script must not read an HttpOnly session token. TLS/`Secure` is a different cell.

## Drafts

CSP3 and Trusted Types remain Working Drafts in this snapshot. Report-Only is detection, not HttpOnly.
