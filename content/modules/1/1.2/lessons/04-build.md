# 1.2-LO-04 — Restore complete mediation (structural)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** Saltzer least privilege + fail-safe defaults (1975, seminal); CISA Secure by Design — do not ship “auth on, policy later.”

## Property (start here)

After the fix, **unknown notes and cross-tenant reads deny**. Own-tenant reads still work.

## Attacker capabilities and trust assumptions

Same as LO-03. Trust the `fixed/` tree only as a teaching patch, not as production FastAPI.

## Structural vs denylist

Blocking `bob` by name fails when `cara` (tenant `tC`) appears. Checking `note.tenant == user.tenant` (or an equivalent policy engine) is the smallest mechanism that matches the matrix cell. Fail-safe: missing note → deny, not 200 with empty body that still confirms existence if that was a non-goal.

Framework `HTTPBearer` is still not the cell.

## Practice

In your own words, name subject, object, action, and the predicate that must be true.

## Transfer

Admin of tenant A deleting n1: extra privilege, not `if role == admin: return note` without tenant. Separation of privilege if delete also needs a second factor later (4.x).
