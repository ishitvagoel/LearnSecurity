# 6.2 — Browser injection and active content (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Unencoded markup reaches the HTML interpreter |
| Failure | Fail closed: Encode for HTML text; framework safe constructors; CSP extra |

Lab tests: `test_property.py` under `labs/6.2/6.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Unencoded markup reaches the HTML interpreter`
- `--impl fixed`: **pass**

angle brackets encoded.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
