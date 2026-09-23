# 2.3 — Browser security model

Pass A specification, plus the Step 2/3 deepening artifacts (teaching claims and coverage contract) required by `deepen-module`.

## Identity

- **id:** 2.3
- **slug:** browser-security-model
- **title:** Browser security model
- **phase / track / difficulty:** 2 / core / foundation
- **estimatedMinutes:** 330
- **prerequisites:** 2.1–2.2 Pass A; 1.2–1.3
- **routeTags:** complete, accelerated, web-api
- **releaseMilestone:** M0
- **masteryGate:** 2

## Objective hierarchy

1. Produce a **browser policy matrix**: origin vs site, navigation, DOM authority, cookies, storage, frames, CORS, Fetch metadata, CSP, Trusted Types, SRI, third-party resources, COI; **browser-enforced vs server-enforced**.
2. Show a local fixture where a **browser control is not an application guarantee** (a cookie flag, a reflected CORS origin, a Report-Only CSP header) and where a **server control that looks like an allow-list is actually an unchecked reflection of the caller's own claim**.
3. Transfer: third-party script or iframe and update 1.3 surface + 1.2 authority.

## Misconceptions

- Origin and site are the same.
- CSP/Trusted Types replace encoding (they are layers; CSP3 and Trusted Types are **Working Drafts** as of 2026-09-22).
- Cookies with HTTPS are therefore unreadable to JS.
- `Access-Control-Allow-Origin` can be validated by checking the hostname or the domain instead of the full origin.
- `Content-Security-Policy-Report-Only` is "CSP is on."

## Teaching claims

Five falsifiable claims, ordered by dependency. The module previously taught only claim 1 (`HttpOnly` vs `document.cookie`) across all eight lessons, despite a title and an objective hierarchy that promise CORS, CSP, Trusted Types, and the origin/site distinction as first-class content — the same one-narrow-predicate defect this skill's Step 2 describes for `5.2` and `4.3` before their own deepening passes.

1. **C1 — A session cookie's `HttpOnly` flag is a browser cell, and the browser is what enforces it.** For SecureCollab's `sc_session` cookie, page script in the origin cannot read the value through `document.cookie`, because the server sets `HttpOnly` on the `Set-Cookie` response header and the browser's cookie jar — not the application, and not a code review — refuses that one reader. Missing the flag on `sc_session`, or setting it on a second cookie name and not on a WebView bridge that copies the same value into JS, reopens exactly this failure, and no amount of stored- or reflected-XSS defense elsewhere makes the flag optional.
2. **C2 — Origin, not site, is the unit `Access-Control-Allow-Origin` must be checked against.** For SecureCollab's `/notes` endpoint, a caller's cross-origin script may read the response only if the server's `Access-Control-Allow-Origin` header names that caller's exact scheme+host+port. Checking only the hostname, a domain suffix, or a substring collapses "site" (the registrable domain a person reads aloud) into "origin" (the tuple the browser's same-origin policy actually protects), and lets a sibling subdomain, a scheme downgrade, or a lookalike domain through a check that looks like an allow-list but is not one.
3. **C3 — `Access-Control-Allow-Credentials: true` must never accompany an `Access-Control-Allow-Origin` that was not first validated against a fixed allow-list.** That pairing is the specific signal that tells a browser a cross-origin, cookie-carrying request's response may be handed to the calling script. Once a server sets it for whatever origin a caller happens to send, `sc_session`'s `HttpOnly`/`Secure` flags (C1) become irrelevant to this particular attack: the attacker's script never has to read the cookie's value, only to ride it inside a request the victim's browser attaches automatically.
4. **C4 — `Content-Security-Policy-Report-Only` is a detection channel, not an enforcement channel.** It asks the browser to send a violation report to a named endpoint; it does not ask the browser to refuse to load or execute anything. A deployment that carries only the Report-Only header — however clean its reports look, however long it has run without an incident — has not deployed the blocking control CSP3 describes, and a status line that calls this "CSP is on" is a false assurance distinguishable from the true one only by which exact header name the server sent.
5. **C5 — A third-party embed or a bridge is a new reader of the same cookie and DOM state, and its policy rows must be re-derived, not inherited.** An iframe, a third-party script, or a React Native WebView cookie bridge sits at a different origin (or in a different runtime) than the first-party page whose HttpOnly, CORS, and `frame-ancestors` rows this module builds. CORS, cookie `SameSite`, and `frame-ancestors` are each evaluated per navigation context, not once for "the app," so adding a new reader without rewriting those rows for it is the same mistake as C1–C4 wearing a different noun.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 4 Build, 5 Verify | `test_forbidden_outcome_session_cookie_missing_httponly`, `test_secure_attribute_is_also_present`, `test_anti_fake_httponly_text_inside_the_cookie_value_does_not_count` | items.md #1, #4, #7 |
| C2 | 1 Property, 2 Model, 4 Build, 5 Verify | `test_origin_vs_site_boundary_subdomain_scheme_and_port_are_each_denied`, `test_anti_fake_lookalike_domain_is_not_treated_as_the_trusted_origin` | items.md #2, #3, #5 |
| C3 | 3 Break, 4 Build, 5 Verify | `test_trusted_origin_is_reflected_with_credentials`, `test_forbidden_outcome_attacker_origin_gets_no_credentialed_access`, `test_missing_origin_header_does_not_crash_and_grants_nothing` | items.md #2, #8 |
| C4 | 1 Property, 4 Build, 5 Verify, 6 Operate | `test_csp_is_enforced_not_only_reported` | items.md #1, #6 |
| C5 | 7 Generalize | Not directly code-testable — the lab fixture has no iframe, no second origin server, and no WebView runtime to host a second reader. Modeled instead in `lessons/07-transfer.md`'s two scenarios and the design table in `lessons/02-model.md`. | items.md #7 |

C1, C2, C3, and C4 each carry a genuine lab assertion, well past the ≥2-claims-with-a-lab-assertion bar. C5 is honestly declared non-code-testable rather than mapped to a test that would not actually assert it — this fixture is one FastAPI process with no second origin to embed a real iframe or a real WebView bridge against, and pretending a unit test could check "the policy rows were re-derived, not inherited" would be a worse defect than naming the limit plainly.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Identify by exact header name and value which of Set-Cookie/ACAO/ACAC/CSP a browser treats as a guarantee vs a detection signal, and justify against ASVS V3 | C1, C4 | [`lessons/01-property.md`](lessons/01-property.md) §Four headers, four different promises | [`lessons/01-property.md`](lessons/01-property.md) §Four headers, four different promises (the `evil.example` worked trace) | [`lessons/01-property.md`](lessons/01-property.md) Practice | items.md #1, #4 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Produce a browser policy matrix for `/login`/`/notes` naming browser vs server enforcement per row | C1, C2, C4 | [`lessons/02-model.md`](lessons/02-model.md) §Step 2: write the rows | [`lessons/02-model.md`](lessons/02-model.md) §Step 3: draft versus final, and browser versus server | [`lessons/02-model.md`](lessons/02-model.md) Practice | items.md #2, #5, #6, #8 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given an Origin header and the allow-list, determine same-origin/same-site/neither and predict the exact CORS response | C2, C3 | [`lessons/01-property.md`](lessons/01-property.md) §Origin and site are not the same word | [`lessons/03-break.md`](lessons/03-break.md) §What to look at: the cause, not a hunt | `labs/2.3/2.3-browser-policy` `test_origin_vs_site_boundary_subdomain_scheme_and_port_are_each_denied` | items.md #3 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given a new reader of `sc_session`, rebuild the policy rows without assuming any row carries over | C5 | [`lessons/07-transfer.md`](lessons/07-transfer.md) §Picture: a new bridge is a new reader | [`lessons/07-transfer.md`](lessons/07-transfer.md) §Write this for a clinic patient-portal session cookie | [`lessons/07-transfer.md`](lessons/07-transfer.md) Practice | items.md #7 | (is the transfer task) |

## Known residuals

Genuinely out of scope for this module, not deferred by omission:

- A real browser's CORS/CORS-preflight enforcement of the header this fixture asserts → this lab's tests read the response header a browser would consult; they cannot run a real browser, so they never prove a browser actually blocked a script from reading a response. Named explicitly in [`lessons/05-verify.md`](lessons/05-verify.md).
- `postMessage` origin checks and DOM clobbering (ASVS V3.5.5, V3.2.3) → out of scope for this fixture's HTTP-only surface; picked up wherever this course teaches cross-frame messaging directly, not invented here.
- SRI and Trusted Types as implemented controls → labeled draft/Working Draft and modeled in the matrix; no lab exercises either, consistent with the module's Pass A scope.
- Output encoding and the rest of the injection-prevention chain (ASVS V1) → explicitly out of scope; `HttpOnly` removing one reader is never presented as XSS being solved. Picked up by this course's own injection modules.
- SameSite's CSRF-mitigation behavior in depth → named as a sister rule, not this module's oracle; a dedicated CSRF treatment is out of scope here.

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 2.3-LO-01 | concept-model | The browser enforces some rules; the server enforces the rest | 1 Property |
| 2.3-LO-02 | design-exercise | A browser policy matrix a second engineer can test | 2 Model |
| 2.3-LO-03 | mechanism-lab | Local fixture: a reflected origin and a script-readable session cookie | 3 Break |
| 2.3-LO-04 | design-exercise | An exact allow-list, HttpOnly, and an enforcing CSP — not three slogans | 4 Build |
| 2.3-LO-05 | verification-lab | What a header test can and cannot prove about a browser | 5 Verify |
| 2.3-LO-06 | operations-exercise | Notice a missing flag or a reflected origin; never log the value | 6 Operate |
| 2.3-LO-07 | transfer-challenge | Add a third-party widget or WebView bridge: new origin/site rows | 7 Generalize |
| 2.3-LO-08 | code-review | Seeded review of a SECURITY.md that mistakes tools for the property | 5 Verify |

## Lab briefs

**Lab `2.3-browser-policy`:** Tier 2, a local FastAPI app (`/login`, `/notes`) reached only through `fastapi.testclient.TestClient`. No driving learners to attack other sites via CORS/CSRF.

## Standards references

ASVS 5.0.0 V3 `final` (cookie setup V3.3.1/V3.3.2/V3.3.4; browser security mechanism headers V3.4.2/V3.4.3/V3.4.6). CSP Level 3 **draft** WD, live-checked 2026-09-22. Trusted Types **draft** WD, live-checked 2026-09-22.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-09-22 | Deepen (D1-D14 remediation): added teaching claims C1-C5 and this coverage contract; see `module.yaml` for the full entry. |
| 2026-09-23 | Deepen continuation: corrected this file's teaching-claims and coverage-contract item citations against `items.md`'s own tags, fixed a heading-citation typo, closed a lab test-gaming gap (raw substring search on `Set-Cookie`) with a 9th anti-fake test, and verified all standards citations live; see `module.yaml` for the full entry. |
