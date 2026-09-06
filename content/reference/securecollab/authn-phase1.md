# SecureCollab Phase 1 — phishing-resistant authentication

Design stub for Module 4.2. Not a live authenticator.

## Freeze

- Local `phishing_resistant` classifier. Synthetic origins only.
- No live phishing sites.

## Origin binding

Passwords and OTP are not phishing-resistant. WebAuthn must fail at a lookalike origin. HTML `autocomplete=webauthn` is not the ceremony.

## Tests

Password-at-evil is false. That boolean is the evidence. “MFA” is not.
