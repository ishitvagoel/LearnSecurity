# Coverage audit — Pass A map coverage

Date: 2026-08-23  
Scope: authored `module.yaml` files for core `0.1`–`10.5`, capstone `11`, electives `E1`–`E6`. Pass B/C exists for the same set. Awareness lists are **regression checks**, not a new outline.

> This 2026-08-23 audit answers whether the blueprint map includes the expected standards areas. It does not approve lesson depth, lab semantics, or later generated rewrites. Current depth decisions live in [`depth-audit-2026-08-25.md`](depth-audit-2026-08-25.md) and dated per-module reviews.

## ASVS 5.0 chapters vs principal modules (blueprint §12.1)

| Chapter | Expected principal modules | Pass A map |
|---|---|---|
| V1 Encoding and Sanitization | 2.1, 6.1, 6.2, 6.4 | covered |
| V2 Validation and Business Logic | 3.4, 5.5, 6.1, 6.6, 6.7 | covered |
| V3 Web Frontend Security | 2.3, 4.3, 6.2, 6.3 | covered |
| V4 API and Web Service | 2.2, 7.1–7.3 | covered |
| V5 File Handling | 6.4 | covered |
| V6 Authentication | 4.1, 4.2 | covered |
| V7 Session Management | 4.3, 6.3 | covered |
| V8 Authorization | 1.2, 4.4, 5.5, 7.2, 7.4 | covered |
| V9 Self-contained Tokens | 4.3, 4.5, 7.4 | covered |
| V10 OAuth and OIDC | 4.5 | covered |
| V11 Cryptography | 5.2, 5.3, 7.3 | covered |
| V12 Secure Communication | 2.2, 5.4, 7.4 | covered |
| V13 Configuration | 2.2, 5.5, 10.2–10.4 | covered |
| V14 Data Protection | 5.1, 5.5, 10.5 | covered |
| V15 Secure Coding and Architecture | 1.2, 1.3, 3.2, 3.3, 9.2, 10.1 | covered |
| V16 Logging and Error Handling | 2.4, 5.5, 6.6, 9.3, 10.5 | covered |
| V17 WebRTC | E2 | elective E2 only |

No ASVS 4.x IDs found. No MASVS L1/L2/R language found.

## MASVS 2.1

Phase 8 (`8.1`–`8.5`) plus shared STORAGE/CRYPTO/AUTH/PRIVACY with 5.x. Profiles, not L1/L2/R.

## Awareness lists (regression only)

- Top 10:2025, API Top 10, Mobile Top 10, CWE Top 25 — not used as learning order. Mapped only as regression/awareness where specs already pin them.

## Drafts that must stay labeled draft

OAuth 2.1, SSDF 1.2 IPD, Privacy Framework 1.1 IPD, WebAuthn L3 CR, CSP3, Trusted Types — do not present as final.

## Pass A finding

None that reopen Pass A sequencing. Thin generated specs (Phase 0, 3–11, electives) remain map-complete; later revision may deepen them without changing STATUS pass.

## Current follow-up

Pass D static site remains in `site/`, and the historical Pass E record remains at [`pass-e-review.md`](pass-e-review.md). The 2026-08-25 semantic audit reset generator-derived depth claims. Module 1.1 is the independently reviewed reference revision; the other 56 units remain queued beginning with 1.2. Mastery gates and product milestones remain learner/product evidence.
