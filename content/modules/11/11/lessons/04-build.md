# Consult owner-or-grant on read

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

A revoke *event* is not the fix. HTTP 200 is not the fix. A scanner badge is not the fix. “We called revoke” is not the fix.

The structural change is: `revoke` **discards the grant**, and `read` **returns the body only if `tenant == owner` or `(nid, tenant) in GRANTS`**. Missing grant denies. A revoke that is not consulted on the next read is still the break. Structural means that consultation — not HTTP 200, not a scanner badge, not a YAML pack.

The smallest restore for the notes app’s share is: B after revoke → None, A still reads, B before revoke still reads. Fail-safe: if you are unsure whether the grant still exists, deny. Do not fail open because DELETE returned 200.

## Picture: consult on the path

```mermaid
flowchart TD
  Call[read] --> Own{owner?}
  Own -->|yes| Body[body]
  Own -->|no| G{in GRANTS?}
  G -->|yes| Body
  G -->|no| Deny[None]
```

Do not accept “we called revoke” as consultation. The repaired files require owner-or-grant on this `read`. Production still needs every *other* read path — delayed workers and phone caches can serve the old grant. Copies already sent are gone from what this check can prove. Access-rights change inside an already-open session without signing in again is extra, advanced work: storing a revoke row is not in-session deny.

Industry lists ask for permission enforced. This pytest is that sentence for post-revoke read.

## What the repaired files must show

Read `fixed/capstone.py` against this checklist. Do not treat the snippet as a production share product.

| After the fix | Must be true |
|---|---|
| B after revoke | read None |
| A after revoke | read secret |
| B before revoke | read secret |

Fail closed: if you are unsure whether the grant is gone, return None. Uncertainty is a **no** on the body, not a yes because revoke was called.

## What this is not

- Scanner green.
- A YAML pack.
- An assurance-gate sticker.
- Cache wipe (phone leftover).
- Copies already sent.
- A mobile testing profile used as a web oracle.

## What the tool cannot do

- Delayed worker leftover session is a different grain from an earlier week.
- Phone cache is a different grain.
- Email already sent is leftover copies.
- Access-rights change in the same session without signing in again is not this check.
- A second note `n2` is not in the practice files.

## Practice

Name every read path. Run:

```text
python3 -m pytest labs/11/11-lab/tests --impl fixed
```

It must pass. Run from the lab directory if a collection at the repo root is polluted. Then write one sentence: which rule is restored, and which leftover you refused to delete.

## Use it somewhere new

Clinic guardian: the next chart read must consult the grant, not the last login.

## What can still go wrong

Delayed worker. Phone cache. Access-rights change in the same session. Email already sent.

## What this page is not doing

Do not hit a live tenant. This page does not mark you as finished. from a scanner screenshot. Do not treat a README checklist as mastery.
