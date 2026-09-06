# Lab 5.3 — hardcoded default after rotation

**Module:** `5.3`
**Authorized scope:** this directory only. Local course fixture. No live vaults.
**Invariant:** After rotation to `current="rotated-now"`, `auth("sk-lab-hardcoded")` is false. The old default is not a backdoor.
**Root cause class:** secret that outlived rotation / default credential
**Non-goals:** live cloud KMS, real production keys, quantum attacks.

`sk-lab-hardcoded` is a **disposable lab string**, not a production secret.

## Reset

Re-run pytest. Optional: `git checkout -- labs/5.3/5.3-lab`.

## Vulnerable behavior (local only)

`auth` accepts the hardcoded `DEFAULT` even when `current` has rotated. Forbidden outcome: old hardcoded key still authenticates after rotation.

## Structural fix

Authenticate only the current secret. Missing current is deny. Defaults in source are not credentials.

## Verify

```
python3 -m pytest labs/5.3/5.3-lab/tests --impl vulnerable
python3 -m pytest labs/5.3/5.3-lab/tests --impl fixed
```

The first command must fail on the default-key and missing-current tests. The second must pass. The honest current-secret test may pass on both.

## Operate

Signal: `default_secret_used`. Rotate again; rebuild images; purge logs of the old value.

## Transfer

Clinic lab API key in a gist. Envelope DEK vs KEK. Prompt only.
