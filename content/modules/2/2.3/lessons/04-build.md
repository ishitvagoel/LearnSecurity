# 2.3-LO-04 — Honor HttpOnly; do not claim XSS is finished

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-3.3.4` and `v5.0.0-3.3.1`; CSP3 and Trusted Types labeled **Working Drafts** (see pins).

## Structural means the script interpreter is excluded

`js_read_session` must return `None` when `httponly` is true. Structural means the lab’s cookie model actually branches on the flag—not a comment, not Report-Only CSP, not “we will encode later in 6.2.”

The smallest restore for SecureCollab’s `sc_session` is: if the cookie is a session token, set HttpOnly, and make the script reader fail closed. Moving the token into `localStorage` enlarges the script share. Prefixes (`__Host-`) and `Secure` are sister cells (`v5.0.0-3.3.1`); they do not replace this branch.

## Mental model: one cell restored

```mermaid
flowchart TD
  Read["js_read_session"] --> Flag{httponly?}
  Flag -->|yes| None[Return none]
  Flag -->|no| Value[Return value - not a session token]
```

The fixed tree honors the flag. XSS is **not** solved: encoding (6.2), CSP (draft), and Trusted Types (draft) remain later work. Fail-safe for a session token: if the flag is missing, treat it as a defect, not as “readable is fine.”

## Why this restores the cell

| After the fix | Must be true |
|---|---|
| `httponly: True` on `sc_session` | `js_read_session` is `None` |
| Cookie header to the origin | Still allowed; the jar may send `Cookie` |
| Non-session cookies | May remain script-readable if that is the product intent; do not silently reuse the session name |

ASVS `v5.0.0-3.3.4` (Level 2) wants HttpOnly when the value is not meant for scripts. The lab is that sentence, not a full cookie catalogue.

## What this is not

CSP3, Trusted Types, SameSite, `__Host-`, or moving the token to `localStorage`. Next.js `cookies()` defaults are not this cookie. Report-Only CSP (E2) is detection theater if you count it as this cell. FastAPI `Response.set_cookie(httponly=True)` is a mechanism; the pytest still has to observe unreadability.

## Mechanism limits

HttpOnly does not stop the script from calling `/notes` as the user, reading note bodies already in the DOM, or exfiltrating them. It does not stop extensions that see cookies. It does not set `Secure`. A WebView bridge can still expose the value if the bridge ignores the flag—name that as a later 8.x residual, not as a silent pass.

## Practice

Name subject (script in the origin), object (`sc_session` value), action (read), and the predicate (`httponly` ⇒ `None`). Run:

```text
python3 -m pytest labs/2.3/2.3-browser-policy/tests --impl fixed
```

Must pass.

## Transfer

Clinic portal session cookie. The fix is still “script cannot read the session token,” not “we shipped a CSP.” If the clinic also has a WebView, the same predicate must hold on that bridge.

## Residual risk

Extensions; XSS without cookie theft; missing `Secure` on the same cookie; WebView bridges; draft CSP/Trusted Types unused.

## Usability

The login form remains a 1.4 / 4.2 control. HttpOnly is invisible to the keyboard user. Do not trade an accessible login for a script-readable store.
