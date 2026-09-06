# Lab 6.2 — a title is data, not HTML grammar

**Module:** `6.2`
**Authorized scope:** this directory only. Local course fixture. No live-target browsers.
**Invariant:** `render` encodes `<` as `&lt;` in HTML text. Extra tags must not survive.
**Root cause class:** HTML grammar mixed with data
**Non-goals:** exploit-kit payloads, live XSS, CSP as the property.

## Reset

Re-run pytest. Optional: `git checkout -- labs/6.2/6.2-lab`.

## Vulnerable behavior (local only)

`render` interpolates the body into HTML with no encoding. Forbidden outcome: unencoded markup reaches the HTML interpreter. The tame marker is `<`.

## Structural fix

HTML-escape for text context, then wrap. CSP3 (Working Draft) is not a substitute.

## Verify

```
python3 -m pytest labs/6.2/6.2-lab/tests --impl vulnerable
python3 -m pytest labs/6.2/6.2-lab/tests --impl fixed
```

The first command must fail on the encoding test. The second must pass. Honest titles may pass on both.

## Operate

Signal: `stored_field_review`. Do not log title bodies if they are PHI.

## Transfer

Clinic patient nickname. Prompt only.
