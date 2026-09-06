# SecureCollab Phase 1 — cryptographic properties at rest

Design stub for Module 5.2. Not a production cipher.

## Freeze

- Local `protect` / `looks_encrypted`. Plaintext stand-in `secret`.
- Fixed `aesgcm:` prefix is a teaching flag, not AES-GCM.

## Encoding is not confidentiality

Base64 round-trip of `secret` is the forbidden outcome. Argon2 (RFC 9106) is the password row. Keys are 5.3. TLS is 5.4.

## Tests

`protect` must not decode as Base64 of `secret`. Column names are not evidence.
