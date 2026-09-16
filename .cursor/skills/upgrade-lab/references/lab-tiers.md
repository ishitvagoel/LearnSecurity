# Lab tiers

| Tier | Shape | LOC per variant | Tests | Use when |
|---|---|---|---|---|
| **1 — Predicate** | Pure function, no I/O | 5–30 | ≥5 | The property genuinely *is* a pure function |
| **2 — Component** | FastAPI app, real request/response cycle, SQLite or Postgres store, session or token state, driven through `httpx`/`TestClient` | 60–200 | 6–10 | **Default.** Phases 3–7, 9, 10, most electives |
| **3 — Cross-component** | Two or more processes or layers | 120–400 | 8–14 | One module per phase, plus the capstone |

## Tier 1 — keep it honest

Legitimate: an HTML-text encoder, a constant-time comparison, a single-value parser, a canonicalization routine.

Not legitimate: anything whose failure needs a *caller* to be wrong. `resolve(role, field)` returning a boolean does not teach field-level authorization; it teaches that a function returns what it returns.

Raised minimum: five tests, including the anti-fake test.

## Tier 2 — the default

A component lab has a request that arrives, a decision made somewhere, and state that persists between requests. That is the minimum structure in which the course's actual subjects appear:

- authority resolved on one side of a boundary and consumed on the other;
- state that changes between the check and the use;
- a parser and its consumer disagreeing about the same bytes;
- a cache or a query keyed without the tenant;
- an error path that fails open.

Sketch for a session module:

```
labs/4.3/4.3-lab/
  vulnerable/app.py      FastAPI app; session_from_request accepts a query token
  fixed/app.py           same app; query channel refused, cookie and header kept
  tests/test_property.py TestClient drives real requests
  tests/conftest.py      --impl selects the variant; fresh SQLite per test
  requirements.txt       pinned
  README.md
```

Tests drive the app, not the function: `client.get("/notes?access_token=...")` and assert on the response and on what the store recorded. That is what makes the access-log and `Referer` story in the lesson concrete rather than asserted.

## Tier 3 — selected

Reserve for one module per phase plus the capstone, where the interaction *is* the lesson: API + worker + queue (retry and idempotency), API + database with row-level policy (tenant isolation), app + cache (a copy that outlives a revocation), client + backend (a hostile client).

This is where the residuals currently listed in `STATUS.yaml` — retries, webhook races, cache copies, GraphQL aliases, revoked-token reads — stop being residuals and become teachable.

Keep them deterministic: a real queue process is fine, wall-clock sleeps and racing threads with no barrier are not.

## Mobile

Phase 8 has no Kotlin. Either author real Kotlin/JVM fixtures with Gradle and unit tests, or record a human decision in `content/progress/STATUS.yaml` relabelling phase 8 as analysis-only. Do not resolve this inside a module pass — it is a curriculum-level decision.
