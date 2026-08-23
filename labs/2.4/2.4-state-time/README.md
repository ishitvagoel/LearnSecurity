# Lab: 2.4-state-time

**Module:** `2.4`  
**Authorized scope:** this directory only.  
**Invariant:** A retried `share_note` with the same idempotency key does not create a second share (exceptional conditions / TOCTOU of “did it land?”). Top 10 A10:2025 is **awareness**, not this lesson’s outline.  
**Root cause class:** state / time  
**Non-goals:** live race exploits against production, wall-clock attacks on NTP.

## Reset

Git restore; tests call `reset()`.

## Vulnerable behavior (local only)

Every call appends a share. A client retry after timeout duplicates the side effect.

## Structural fix

Remember the idempotency key; replay returns without a second append. Fail-closed: missing key still performs one share (lab simplicity) — production should require keys for high-impact actions (residual).

## Verify

```bash
python3 -m pytest tests/test_idempotency.py --impl vulnerable
python3 -m pytest tests/test_idempotency.py --impl fixed
```

## Operate

Log duplicate-key hits. Do not return HTTP 200 with a new share hidden in a catch-all.

## Transfer

Worker retry with a **stale** 1.2 grant: time is part of mediation (preview 7.4).
