# Lab 8.4 — resilience raises cost; it is not trust

**Module:** `8.4`
**Authorized scope:** this directory only. Local course fixture. No live Play Console or store APK unpacking.
**Invariant:** `api_allowed("debug", "ok")` is false. Honest release+ok may be true.
**Root cause class:** prod trusts a client attest string from any build
**Non-goals:** R8 cookbooks as authorization, live reverse engineering.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/8.4/8.4-lab`, then run `git restore --source=HEAD -- labs/8.4/8.4-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`api_allowed` always returns true. Forbidden outcome: debug calls prod export.

## Structural fix

Require `build_type == "release"` and `attest == "ok"`.

## Verify

```
python3 -m pytest labs/8.4/8.4-lab/tests --impl vulnerable
python3 -m pytest labs/8.4/8.4-lab/tests --impl fixed
```

The first command must fail on debug+ok. The second must pass. Honest release+ok may pass on both.

## Operate

Signal: `debug_to_prod_denied`. Do not log APKs or signing keys.

## Transfer

Clinic debug vs prod FHIR. Prompt only.
