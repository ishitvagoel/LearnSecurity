# 4.2 — Authentication and phishing-resistant authenticators (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | User, phishing site, real origin |
| Objects | password, webauthn assertion, origin |
| Actions | phishing_resistant |
| Channels | browser, authenticator |
| TCB | Origin-bound authenticator ceremony. |
| Untrusted | User’s ability to distinguish URLs; password reuse |
| State / time | Ceremony at login; later step-up (transfer). |
| 1.1 cell | Authenticity of the principal to *this* origin. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| user | password | real origin | phishable |
| user | password | evil origin | deny-and-not-resistant |
| user | webauthn | evil origin | deny |
| user | webauthn | real origin | resistant-authn-only |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/4.2/4.2-lab` file `authn.py`.

## Transfer

Step-up for export: still origin-bound?

## Residual risk

Users with only passwords — honest residual, not a slogan.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
