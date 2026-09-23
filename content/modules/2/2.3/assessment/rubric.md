# 2.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Browser security model

## Items

Eight module-specific items live in [`items.md`](items.md): two discrimination, two diagnosis, two design, one transfer, and one operate item, covering all five of this module's teaching claims (C1–C5, see `spec.md` §Teaching claims). Answers, distractor rationales, and four-state banding are in the isolated key at `content/assessment/keys/2.3.md` — do not open it before attempting the items.

## Evidence checklist

- [ ] Browser policy matrix for `/login`/`/notes` (Lesson 02), naming browser vs server enforcement per row
- [ ] Local reflected-origin and script-readable-cookie annotation (Lesson 03), naming both causes separately, not as one restated defect
- [ ] Lab `labs/2.3/2.3-browser-policy`: forbidden outcomes named as **a script-readable session cookie** and **an arbitrary origin granted Access-Control-Allow-Credentials: true**
- [ ] `vulnerable/` tests: 6 of 9 fail for the stated security reasons; `fixed/` tests: 9 of 9 pass (authorized local `TestClient` fixture only)
- [ ] Transfer task (items.md #7): clinic portal / WebView bridge scenario, naming which of C1–C5 change and which do not
- [ ] Seeded review checklist answers (Lesson 08) — do not look at the key first
- [ ] Operate signal (items.md #8) that carries no cookie value and no note body

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools or header names listed instead of a named enforcement mechanism; missing distinction between origin and site; a check that reflects a caller's own claim but is asserted as an allow-list |
| Competent | System-specific rule stated and checked against the lab; lab result correctly mapped to a row in the policy matrix; operate signal present and free of raw cookie or note content |
| Transfer-ready | Item 7 done: the WebView bridge's own policy row derived independently, rather than assumed to inherit the browser tab's `HttpOnly` row by association |

Knowledge-check items (retryable) are items 1–4 in `items.md` (discrimination and diagnosis); design, transfer, and operate items (5–8) require satisfactory evidence, not a retry-to-80% threshold — a critical gap here (for example, a CORS fix that only handles the one attacker origin the test file happens to show) is not compensated by strong answers elsewhere.

## Seeded review

Apply the falsifiability question in `lessons/08-review.md` §Picture: what would falsify each claim to `vulnerable/SECURITY.md` yourself before reading that lesson's worked example. Intended findings live only in `content/assessment/keys/2.3.md`.
