# 2.3-LO-01 — Origin vs site; browser vs server enforcement

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** HTML/Fetch living standards (as pinned); CSP Level 3 **Working Draft**; Trusted Types **Working Draft** (snapshot 2026-08-23). Cookies: HttpOnly/Secure as deployed facts.

## Property (start here)

A SecureCollab **session** cookie marked HttpOnly is not readable to script. That is a **browser** cell. It does **not** mean XSS is impossible or that CSP3 (draft) replaced output encoding (6.2).

## Attacker capabilities and trust assumptions

- **Attacker:** script in `https://app.securecollab.example` origin (lab model); a different site; a subframe.
- **Trust:** browser honors HttpOnly. Server still must set the flag. Next.js “secure cookies” defaults are not the whole matrix.

Origin ≠ site. Same-site cookies ≠ authorization (1.2).

## Practice

Fill one row: cookie `sc_session` — HttpOnly, Secure, browser-enforced vs server-enforced.

## Transfer

`document.cookie` vs Cookie header on API: different interpreters (2.1 family).
