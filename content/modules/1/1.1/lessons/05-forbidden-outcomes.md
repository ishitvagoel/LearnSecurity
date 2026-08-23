# 1.1-LO-05 — Forbidden outcomes and evidence

**Kind:** verification-lab  
**Loop step:** 5 Verify

## Property

An invariant that cannot fail a test is not yet an invariant.

## Task

From your catalogue, list **forbidden outcomes** (what must not happen) and **evidence** (what you would run or review):

| Forbidden outcome | Evidence |
|---|---|
| Tenant B reads Tenant A’s note via GET | Cross-tenant test (later 4.4); not “auth middleware exists” |
| Note body in logs | Test fixture that greps/captures log JSON |
| Scanner green, catalogue empty | Reviewer rejects; not a test pass |

Happy path is not enough. Include one **failure** case (backup restore still respects tenant isolation—later 5.5; here, just name it).

## Practice

Add this table to `invariants-v1.md`.

## Transfer

If you cannot name evidence, the line is still a slogan—rewrite or mark non-goal.
