# Lab 6.2 — a title is data, not HTML grammar

**Module:** `6.2`
**Authorized scope:** this directory only. Local course fixture. No live-target browsers.
**Invariant:** `render` encodes `<` as `&lt;` in HTML text. Extra tags must not survive.
**Root cause class:** HTML grammar mixed with data
**Non-goals:** exploit-kit payloads, live XSS, CSP as the property.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/6.2/6.2-lab`, then run `git restore --source=HEAD -- labs/6.2/6.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

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
