# Coverage audit (Phase 1 Pass A)

Date: 2026-08-23  
Scope: authored `module.yaml` files only (`1.1`–`1.4`). Not a lesson or lab audit. Awareness lists are **regression checks**, not a new outline.

## ASVS 5.0 chapters vs principal modules (blueprint §12.1)

| Chapter | Expected principal modules | Phase 1 Pass A |
|---|---|---|
| V1 Encoding and Sanitization | 2.1, 6.1, 6.2, 6.4 | **gap** (expected; Phase 2+) |
| V2 Validation and Business Logic | 3.4, 5.5, 6.1, 6.6, 6.7 | **gap** (expected) |
| V3 Web Frontend Security | 2.3, 4.3, 6.2, 6.3 | **gap** (expected) |
| V4 API and Web Service | 2.2, 7.1–7.3 | **gap** (expected) |
| V5 File Handling | 6.4 | **gap** (expected) |
| V6 Authentication | 4.1, 4.2 | **gap** (expected); 1.4 cites 800-63 CX only |
| V7 Session Management | 4.3, 6.3 | **gap** (expected) |
| V8 Authorization | 1.2, 4.4, 5.5, 7.2, 7.4 | **covered** at chapter level in 1.2 |
| V9 Self-contained Tokens | 4.3, 4.5, 7.4 | **gap** (expected) |
| V10 OAuth and OIDC | 4.5 | **gap** (expected) |
| V11 Cryptography | 5.2, 5.3, 7.3 | **gap** (expected) |
| V12 Secure Communication | 2.2, 5.4, 7.4 | **gap** (expected) |
| V13 Configuration | 2.2, 5.5, 10.2–10.4 | **gap** (expected) |
| V14 Data Protection | 5.1, 5.5, 10.5 | **gap** (expected) |
| V15 Secure Coding and Architecture | 1.2, 1.3, 3.2, 3.3, 9.2, 10.1 | **covered** chapter-level in 1.2 and 1.3 |
| V16 Logging and Error Handling | 2.4, 5.5, 6.6, 9.3, 10.5 | **partial** via 1.4 operate notes only |
| V17 WebRTC | E2 | **out of scope** |

No ASVS 4.x IDs found. No MASVS L1/L2/R language found.

## MASVS 2.1

Not expected in Phase 1. Shared later: STORAGE/CRYPTO/AUTH/PRIVACY with 5.x and 8.x.

## Awareness lists (regression only)

- Top 10:2025 — not used as learning order. A10 exceptional conditions belongs to 2.4; A06 insecure design belongs later Phase 3.
- API Top 10 / Mobile Top 10 / CWE Top 25 — not yet mapped in authored specs (expected).

## Defects

None that require stopping the Phase 2 spec pilot.

## Follow-up

Phase 2 Pass A (`2.1`–`2.4`) was authored in the same goal wave. Next queued unit is **1.1 Pass B** (pilot the seven-step lesson loop). Do not mass-author Phase 3+ until that loop is proven.

### Phase 2 ASVS (added)

| Chapter | 2.x coverage |
|---|---|
| V1 | 2.1 |
| V2 | 2.1, 2.4 |
| V3 | 2.3 |
| V4 | 2.2 |
| V7 | 2.4 |
| V9 | 2.4 |
| V12 | 2.2 |
| V13 | 2.2 |
| V16 | 2.4 |

CSP3 and Trusted Types pinned as **draft**. RFC 9846 pinned as **final**. Top 10 A10 as **awareness** on 2.4.
