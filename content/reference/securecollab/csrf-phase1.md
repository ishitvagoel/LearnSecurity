# SecureCollab Phase 1 — share CSRF

Design stub for Module 6.3. Not a production browser.

## Freeze

- Local `allow_share(origin, expected, token, session_cookie)`.
- Synthetic origins only.

## Cookie is not consent

Foreign origin without token is denied. Same origin still needs the token. SameSite is a helper, not the predicate.

## Tests

Foreign-origin deny is the evidence. A CORS header is not.
