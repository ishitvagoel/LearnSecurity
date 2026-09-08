# Lab E3 — the same key must not double-charge

**Module:** `E3`
**Authorized scope:** this directory only. Local course fixture. No live payment processors, real PAN, or clinic billing systems.
**Invariant:** two `capture("k1")` calls leave `charge_count() == 1`. The first capture may succeed.
**Root cause class:** non-idempotent side effect
**Non-goals:** PCI SAQ as this cell; claiming Gate 7.

The in-memory `SEEN` set is a **teaching stand-in** for an idempotency primary key. It is not Stripe.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/E3/e3-lab`, then run `git restore --source=HEAD -- labs/E3/e3-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

Every `capture` appends. Forbidden outcome: duplicate capture double-charges the lab ledger.

## Structural fix

Treat the key as identity: second `k1` does not append.

## Verify

```
python3 -m pytest labs/E3/e3-lab/tests --impl vulnerable
python3 -m pytest labs/E3/e3-lab/tests --impl fixed
```

The first command must fail the duplicate test. The second must pass. Honest first capture may pass on both.

## Operate

Signal: `duplicate_capture_denied`. Do not log PAN-like strings (there are none). Do not claim PCI scope.

## Transfer

Health record append-only. Simulated copay. Prompt only.
