# 2.3 — Browser security model

Pass A specification only.

## Identity

- **id:** 2.3
- **slug:** browser-security-model
- **title:** Browser security model
- **phase / track / difficulty:** 2 / core / foundation
- **estimatedMinutes:** 300
- **prerequisites:** 2.1–2.2 Pass A; 1.2–1.3
- **routeTags:** complete, accelerated, web-api
- **releaseMilestone:** M0
- **masteryGate:** 2

## Objective hierarchy

1. Produce a **browser policy matrix**: origin vs site, navigation, DOM authority, cookies, storage, frames, CORS, Fetch metadata, CSP, Trusted Types, SRI, third-party resources, COI; **browser-enforced vs server-enforced**.
2. Show a local fixture where a **browser control is not an application guarantee** (e.g. CSP draft vs missing output handling).
3. Transfer: third-party script or iframe and update 1.3 surface + 1.2 authority.

## Misconceptions

- Origin and site are the same.
- CSP/Trusted Types replace encoding (they are layers; CSP3 and Trusted Types are **Working Drafts** as of 2026-08-23).
- Cookies with HTTPS are therefore unreadable to JS.

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 2.3-LO-01 | concept-model | Origin vs site; browser vs server enforcement | 1 Property |
| 2.3-LO-02 | design-exercise | Browser policy matrix for SecureCollab web client | 2 Model |
| 2.3-LO-03 | mechanism-lab | Local page: cookie/storage/CORS confusion (authorized local) | 3 Break |
| 2.3-LO-04 | design-exercise | Header/cookie policy that matches the matrix; label draft standards | 4 Build |
| 2.3-LO-05 | verification-lab | Header/cookie verification tests | 5 Verify |
| 2.3-LO-06 | operations-exercise | CSP report-only vs enforce; what to log | 6 Operate |
| 2.3-LO-07 | transfer-challenge | Add third-party widget: new origin/site rows | 7 Generalize |
| 2.3-LO-08 | code-review | Seeded CSP that is treated as XSS-complete | 5 Verify |

## Lab briefs

**Lab `2.3-browser-policy`:** local app origin only. No driving learners to attack other sites via CORS/CSRF.

## Standards references

ASVS 5.0.0 V3 `final`. CSP Level 3 **draft** WD 2026-08-13. Trusted Types **draft** WD 2026-06-23.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
