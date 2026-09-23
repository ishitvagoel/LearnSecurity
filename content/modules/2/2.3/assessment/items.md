# 2.3 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/2.3.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — guarantee, detection signal, or false assurance

Four statements a reviewer might find in a pull request touching SecureCollab's `/login` and `/notes`:

**A.** "`sc_session` is `HttpOnly`, so the browser's cookie jar refuses `document.cookie` a value — that is a browser-enforced guarantee against script in the origin."
**B.** "We ship `Content-Security-Policy-Report-Only`, and our violation-report volume has been zero for three months, so CSP is effectively on."
**C.** "`Access-Control-Allow-Origin` reflects whatever `Origin` the caller sends, so any page can call `/notes`, but that's fine because we also require the session cookie."
**D.** "We send an enforcing `Content-Security-Policy` with `object-src 'none'` and `base-uri 'none'`, so the browser refuses to load or execute anything the policy disallows."

Sort each statement into **guarantee**, **detection signal**, or **false assurance**, and for each one that is not a guarantee, name specifically what would have to change in the code — not in the prose — for it to become one.

**Claim assessed:** C1, C4 · **Outcome:** Identify by exact response-header name and value which of Set-Cookie, Access-Control-Allow-Origin, Access-Control-Allow-Credentials, and Content-Security-Policy (or -Report-Only) a browser treats as an enforceable guarantee versus a detection-only signal, and justify each answer against OWASP ASVS 5.0.0 V3

## 2. Discrimination — property vs. mechanism for the CORS grant

Four statements about `/notes`:

**A.** "We validate that `Origin` is present in the request before answering."
**B.** "In six months of staging traffic, we've never seen a request from an origin we didn't recognize."
**C.** "The response's `Access-Control-Allow-Origin` names the caller's exact origin only when that origin is a member of a literal, fixed set; otherwise no CORS header is sent at all."
**D.** "Any cross-origin, credentialed request must be denied a readable response unless the server first checks that request's exact origin against a fixed, known set — otherwise the browser is told, by the server's own header, to expose the response anyway."

Identify which statement states the property this module is actually protecting and which state mechanisms or proxies for it, and rank the three mechanism claims by how close each comes to being real evidence for the property.

**Claim assessed:** C2, C3 · **Outcome:** Produce a browser policy matrix for SecureCollab's /login and /notes surface -- origin vs site, cookie flags, CORS, CSP, frame-ancestors -- that names, for every row, whether the browser or the server enforces it and what happens when the row is absent

## 3. Diagnosis — a different checker's gap

```python
ALLOWED_SUFFIX = "securecollab.example"

def is_trusted(origin: str) -> bool:
    return origin.endswith(ALLOWED_SUFFIX)
```

This function is not `vulnerable/app.py`'s check (which performs no comparison at all) and not `fixed/app.py`'s check (exact set membership) — it is a third implementation a teammate might propose as "the allow-list version." Give it the two origins `https://evilsecurecollab.example` and `https://evil.securecollab.example`. Name the root cause of why this function accepts each one, the precondition under which each gap matters in practice, and the impact if this ships — as three distinct answers for each origin, not one answer restated three times.

**Claim assessed:** C2 · **Outcome:** Given a caller's Origin header and SecureCollab's exact-origin allow-list, determine whether that caller is the same origin, the same site, or neither, and predict the exact Access-Control-Allow-Origin and Access-Control-Allow-Credentials response each variant of the lab would produce

## 4. Diagnosis — reading a candidate fix

A teammate proposes this fix for the cookie defect, reasoning that it directly addresses the module's own example:

```python
@app.post("/login")
def login(response: Response) -> dict:
    response.set_cookie("sc_session", "synthetic-session", httponly=True)
    return {"ok": True}
```

Determine, without running any code, whether this fix passes `test_secure_attribute_is_also_present`, and explain your reasoning by naming exactly which keyword argument this call is missing and which specific browser-enforced behavior that omission leaves unprotected.

**Claim assessed:** C1 · **Outcome:** Identify by exact response-header name and value which of Set-Cookie, Access-Control-Allow-Origin, Access-Control-Allow-Credentials, and Content-Security-Policy (or -Report-Only) a browser treats as an enforceable guarantee versus a detection-only signal, and justify each answer against OWASP ASVS 5.0.0 V3

## 5. Design — two candidate origin checks under a constraint

Given the vulnerable fixture, two engineers propose fixes for the CORS branch: Engineer A writes `origin in ALLOWED_ORIGINS` where `ALLOWED_ORIGINS` is a literal `frozenset`; Engineer B writes `origin.endswith(".securecollab.example")` (with the leading dot), reasoning that it will automatically cover any future subdomain SecureCollab provisions without a code change. Under the constraint that SecureCollab's threat model treats a compromised or unreviewed subdomain as a realistic risk, choose between the two proposals and defend your choice, including the specific case where your chosen proposal still falls short of a complete guarantee.

**Claim assessed:** C2 · **Outcome:** Produce a browser policy matrix for SecureCollab's /login and /notes surface -- origin vs site, cookie flags, CORS, CSP, frame-ancestors -- that names, for every row, whether the browser or the server enforces it and what happens when the row is absent

## 6. Design — CSP Report-Only as a rollout tool vs. as a substitute

A teammate proposes shipping only `Content-Security-Policy-Report-Only` for the next quarter, "to see what breaks before we turn on the real thing," and treating the eventual switch to enforcing `Content-Security-Policy` as a low-priority follow-up once the report volume looks acceptable. Under the constraint that `/notes` currently ships no CSP header of either kind, evaluate this plan: name what Report-Only alone does and does not protect during that quarter, and propose a design that gets the same rollout-safety benefit without leaving the enforcing header absent the whole time.

**Claim assessed:** C4 · **Outcome:** Produce a browser policy matrix for SecureCollab's /login and /notes surface -- origin vs site, cookie flags, CORS, CSP, frame-ancestors -- that names, for every row, whether the browser or the server enforces it and what happens when the row is absent

## 7. Transfer — clinic portal and WebView bridge

Using the two scenarios from `lessons/07-transfer.md`, state which of this module's five claims (C1–C5) transfer unchanged to the clinic patient-portal session cookie, which claims need a materially different treatment for the React Native WebView bridge, and why "the browser honors `HttpOnly`" does not, by itself, say anything about whether a native bridge method exposes the same cookie's value to injected JavaScript running inside that WebView.

**Success criteria:** Your answer must explain, in your own words, why `HttpOnly` is enforced by the browser's cookie jar specifically, not by any code that happens to call `document.cookie`, and must connect this explicitly to why a WebView bridge — a different runtime, not a browser tab — needs its own, separately-argued policy row rather than inheriting the browser tab's row by association.

**Claim assessed:** C1, C5 · **Outcome:** Given a new reader of sc_session (a third-party iframe or a WebView cookie bridge), rebuild this module's policy rows for that reader without assuming any row from the first-party page carries over unchanged

## 8. Operate — the CORS-misconfiguration signal

Write the log line your system would emit when a staging scan finds `/notes` granting `Access-Control-Allow-Credentials: true` to an origin outside the known allow-list. State which fields it must carry, which field it must never carry, and why "we've seen this origin before and it looks benign" is not sufficient justification to skip rotating sessions that were live during the exposure window.

**Claim assessed:** C3 · **Outcome:** Produce a browser policy matrix for SecureCollab's /login and /notes surface -- origin vs site, cookie flags, CORS, CSP, frame-ancestors -- that names, for every row, whether the browser or the server enforces it and what happens when the row is absent

---

## Evidence checklist

- [ ] Browser policy matrix for `/login`/`/notes` (Lesson 02), naming browser vs server enforcement per row
- [ ] Local reflected-origin and script-readable-cookie annotation (Lesson 03), naming both causes separately
- [ ] Lab `labs/2.3/2.3-browser-policy`: forbidden outcomes named as **a script-readable session cookie** and **an arbitrary origin granted Access-Control-Allow-Credentials: true**
- [ ] `vulnerable/` tests show 6 of 8 failing for the stated security reasons; `fixed/` tests show 8 of 8 passing
- [ ] Transfer answer (item 7) naming which claims change for the WebView bridge and which do not
- [ ] Operate signal (item 8) that carries no cookie value and no note body
