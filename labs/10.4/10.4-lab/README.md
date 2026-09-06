# Lab 10.4 — production must not boot with debug

**Module:** `10.4`
**Authorized scope:** this directory only. Local course fixture. No live production hosts.
**Invariant:** `boot_ok("prod", True)` is false. Production without debug may boot.
**Root cause class:** fail-open defaults
**Non-goals:** NODE_ENV as the invariant; claiming Gate 10 or M4.

The `env`/`debug` pair is a **teaching stand-in** for FastAPI/Next.js compose flags, Django `DEBUG`, and ASVS `v5.0.0-13.4.2`. It does not enumerate every leaky endpoint.

## Reset

Re-run pytest. Optional: `git checkout -- labs/10.4/10.4-lab`.

## Vulnerable behavior (local only)

`boot_ok` always returns true. Forbidden outcome: production process boots with debug enabled.

## Structural fix

Refuse boot when `env == "prod"` and `debug` is true.

## Verify

```
python3 -m pytest labs/10.4/10.4-lab/tests --impl vulnerable
python3 -m pytest labs/10.4/10.4-lab/tests --impl fixed
```

The first command must fail on prod+debug. The second must pass. Honest prod without debug may pass on both.

## Operate

Signal: `prod_debug_forbidden`. Do not log secret values from traces. Do not claim Gate 10 or M4.

## Transfer

Clinic: Django `DEBUG=True`. Feature flag that disables authz. Prompt only.
