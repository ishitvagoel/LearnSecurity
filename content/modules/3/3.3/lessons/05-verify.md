# 3.3 — Secure architecture patterns (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | App DB role can SELECT another tenant's rows |
| Failure | Fail closed: Least-privilege role; RLS as extra layer (5 |

Lab tests: `test_property.py` under `labs/3.3/3.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `App DB role can SELECT another tenant's rows`
- `--impl fixed`: **pass**

app cannot select other tenant.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Serverless function with a shared “admin” connection string.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
