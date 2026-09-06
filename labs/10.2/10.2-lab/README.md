# Lab 10.2 — a name is not a digest

**Module:** `10.2`
**Authorized scope:** this directory only. Local course fixture. No live registry, typosquat, or fork-PR attacks against real orgs.
**Invariant:** `install_ok("aaa", "bbb")` is false. Honest matching hashes may install.
**Root cause class:** name-only install
**Non-goals:** SBOM/SLSA as the hash check; claiming Gate 10 or M4.

## Reset

Re-run pytest. Optional: `git checkout -- labs/10.2/10.2-lab`.

## Vulnerable behavior (local only)

`install_ok` always returns true. Forbidden outcome: dependency installed when digest mismatches lockfile.

## Structural fix

Require `expected_hash == got_hash`.

## Verify

```
python3 -m pytest labs/10.2/10.2-lab/tests --impl vulnerable
python3 -m pytest labs/10.2/10.2-lab/tests --impl fixed
```

The first command must fail on mismatch. The second must pass. Honest matching hashes may pass on both.

## Operate

Signal: `hash_mismatch_denied`. Do not log tokens. Do not claim Gate 10 or M4.

## Transfer

Clinic npm install in prod pod. Prompt only.
