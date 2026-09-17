# Lab 4.3 — query string is not a session channel, and activity is not the same evidence as age

**Module:** `4.3`
**Authorized scope:** this directory only. Local course fixture. No live CDNs or log drains.
**Tier:** 1 (predicate). Both `session_from_request` and `session_is_active` are pure functions over plain dicts and floats, with no request cycle or persisted state either claim depends on. See `lab-realism.mdc`.

**Invariant (C1):** A session token in the query string is not an acceptable session. Cookie (`sc_session`, `HttpOnly`) or `Authorization` only.
**Invariant (C3):** A session is active only while it is within BOTH an idle window since it was last touched AND an absolute window since it was minted. Activity alone must never extend a session past its absolute lifetime.
**Root cause class:** trust (C1: token in a logged, shared channel) and an incomplete lifetime policy (C3: an idle-only check that never asks how long ago the session was minted).
**Non-goals:** live token replay, real cookies, production logs, a real wall clock.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/4.3/4.3-lab`.

## Vulnerable behavior (local only)

`session_from_request` returns `query.get("access_token")` first — the forbidden outcome is a session established from a query-string token.

`session_is_active` checks only whether a session was touched within the last 900 seconds (`IDLE_TIMEOUT_SECONDS`). It never reads how long ago the session was minted, so a session touched every few minutes — by a legitimate user who never closes a tab, or by an attacker replaying a stolen token on purpose to keep it "warm" — never expires, however old it actually is. `ABSOLUTE_TIMEOUT_SECONDS` is declared in the vulnerable file and never enforced; the constant existing is not the same thing as the constant being checked.

## Structural fix

For `session_from_request`: if the query has `access_token`, return `None` before looking at cookie or header at all. The fixed function has no code path that ever returns a value read from `query` — the deny is structural, not a denylist of one key name checked and then fallen through.

For `session_is_active`: enforce two independent clocks, not one checked more carefully. The fixed function requires `now - last_seen_at < IDLE_TIMEOUT_SECONDS` **and** `now - issued_at < ABSOLUTE_TIMEOUT_SECONDS`; either deadline reached or passed ends the session. A session record missing `issued_at` or `last_seen_at`, or carrying a timestamp that would put it in the future relative to `now`, fails closed (returns `False`) rather than being read with a convenience default that would treat unknown age as brand new.

## Verify

```bash
python3 -m pytest tests --impl vulnerable   # 3 of 9 fail
python3 -m pytest tests --impl fixed        # 9 of 9 pass
```

From the repository root:

```bash
python3 -m pytest labs/4.3/4.3-lab/tests --impl vulnerable
python3 -m pytest labs/4.3/4.3-lab/tests --impl fixed
```

Nine tests: the two channel happy paths (cookie, header) and the query forbidden outcome (C1); the lifetime normal case, the C3 forbidden outcome (a ~6-day-old session kept "active" by being touched a second ago), an idle-deadline boundary case, a missing-timestamp fail-closed case, and a two-test anti-fake pair that constructs its own never-elsewhere-used timestamps so a fix that special-cases the forbidden-outcome test's exact numbers cannot pass by memorizing them.

Verified against an actual fake: a "fixed" `session_is_active` that adds a single `if issued_at == <the forbidden-outcome test's exact constant>: return False` special case (rather than the general `now - issued_at >= ABSOLUTE_TIMEOUT_SECONDS` comparison) passes the forbidden-outcome test and fails exactly `test_anti_fake_absolute_expiry_with_fresh_never_elsewhere_used_values` — 8 of 9, not 9 of 9.

## Operate

Signal `query_token_rejected` with path; never the token. Signal `session_expired reason=idle` or `reason=absolute` separately — the distinction tells an operator whether a policy boundary was hit by design or something is generating traffic against sessions that should already be gone. Revoke a token that might have been used; purge logs that already captured it — revocation does not retroactively redact a log line already shipped. See [`lessons/06-operate.md`](../../../content/modules/4/4.3/lessons/06-operate.md).

## Transfer

Clinic appointment deep link; magic-link email ([6.6](../../../content/modules/6/6.6/lessons/01-property.md)). Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/4/4.3/lessons/07-transfer.md).
