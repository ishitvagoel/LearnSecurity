# Lab 8.1 — the APK is not in the TCB

**Module:** `8.1`
**Authorized scope:** this directory only. Local course fixture. No live Play Integrity, Frida, or device farms.
**Invariant:** `allow_export({"integrity": "ok"}, "fail")` is false. Honest server `play_integrity_pass` may allow.
**Root cause class:** policy evaluated on the attacker’s CPU
**Non-goals:** live attestation APIs, obfuscation cookbooks as authorization.

## Reset

Re-run pytest. Optional: `git checkout -- labs/8.1/8.1-lab`.

## Vulnerable behavior (local only)

`allow_export` returns true when the client says `integrity=ok`. Forbidden outcome: client claim authorizes export.

## Structural fix

Use only `server_attest == "play_integrity_pass"` (lab stand-in for a server-verified result). Ignore the client boolean.

## Verify

```
python3 -m pytest labs/8.1/8.1-lab/tests --impl vulnerable
python3 -m pytest labs/8.1/8.1-lab/tests --impl fixed
```

The first command must fail on client ok + attest fail. The second must pass. Honest server-pass may pass on both.

## Operate

Signal: `attest_fail_export_denied`. Do not log bodies or attestation blobs.

## Transfer

Clinic `hipaaMode`. Prompt only.
