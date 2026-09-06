# Lab 4.4 — grant on n1 is not a grant on n2

**Module:** `4.4`
**Authorized scope:** this directory only. Local course fixture. No live tenants.
**Invariant:** `can_read("bob", "n2")` is false when the only grant is `(bob, n1)`. Tenant `acme` cannot read `clinic`. An `admin` role is not an object grant.
**Root cause class:** complete mediation / ambient authority (collection-level flag and role costume)
**Non-goals:** live APIs, real PII, scanner-named IDOR walkthroughs.

## Reset

conftest calls `reset()`. Re-run pytest. Optional: `git checkout -- labs/4.4/4.4-lab`.

## Vulnerable behavior (local only)

`can_read` treats any grant for the user as global, and treats `owner`/`admin` roles as ambient across notes and tenants. Forbidden outcomes: grant on n1 authorizes n2; acme owner reads clinic; clinic admin reads acme.

## Structural fix

Look up `(user, note_id)` and require matching tenant. Owner is per-note. Deny default. Role strings are not capabilities.

## Verify

From repo root:

```
python3 -m pytest labs/4.4/4.4-lab/tests --impl vulnerable
python3 -m pytest labs/4.4/4.4-lab/tests --impl fixed
```

The first command must fail on the deny tests. The second must pass. Honest grant and owner-read tests may pass on both.

## Operate

Signal: `authz_deny` with object id and tenant; never a note body. Investigate grant-table drift.

## Transfer

Clinic: grant on appointment A ≠ chart B. Prompt only; do not leave this directory.
