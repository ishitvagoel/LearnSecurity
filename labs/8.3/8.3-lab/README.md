# Lab 8.3 — the Intent is untrusted input

**Module:** `8.3`
**Authorized scope:** this directory only. Local course fixture. No live Intents or malware APKs.
**Invariant:** after `open_link({"as": "admin"})`, `current_user()` is `"alice"`.
**Root cause class:** identity taken from the link
**Non-goals:** live App Link attacks, custom-scheme hijack cookbooks.

## Reset

Re-run pytest. Optional: `git checkout -- labs/8.3/8.3-lab`.

## Vulnerable behavior (local only)

`open_link` copies `as` onto the session. Forbidden outcome: `as=` switches the user.

## Structural fix

Ignore extras. Session stays `'alice'`.

## Verify

```
python3 -m pytest labs/8.3/8.3-lab/tests --impl vulnerable
python3 -m pytest labs/8.3/8.3-lab/tests --impl fixed
```

The first command must fail on `as=admin`. The second must pass. Honest `note=` locators may pass on both.

## Operate

Signal: `deeplink_identity_ignored`. Do not log full URLs.

## Transfer

Clinic `as=doctor`. Prompt only.
