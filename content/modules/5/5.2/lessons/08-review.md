# Review of Base64 sold as encryption

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships notes-app at-rest protection. Review `labs/5.2/5.2-lab/vulnerable/` as that change. Check whether Base64 decode of `protect("secret")` still equals `"secret"`, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_protect_is_not_mere_encoding`) is the rule test. A comment “will add AES later” is not.

## Picture: protect equals base64

**`protect = base64`**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|"Base64 of secret"| Property["Rule - good if tested"]
  Q -->|"we use AES"| Mechanism[Tool - no test]
  Q -->|"HTTPS"| False[False assurance]
```

What has to stay true: decode is not the plaintext. If `protect` never includes a keyed, non-encoding transform, that reversible leftover is still open. A comment that says AES without a round-trip test is tool theater.

## Problems to find (name them yourself)

- `protect = base64`
- AES-ECB “because we need it deterministic”
- JWT as encryption
- No `looks_encrypted` test

Also reject: rolling a cipher; closing findings without re-running `test_protect_is_not_mere_encoding`; keys in learner notes; real people's data in the practice files; HTTPS as at-rest encryption.

## Common mix-ups

- HTTPS means data at rest is encrypted
- Base64 is hashing
- Stronger algorithm fixes a bad key story
- Column rename is secrecy
- Argon2 belongs on the note body

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_protect_is_not_mere_encoding`. Do not open the keys file.

## Use it somewhere new

Clinic change that renames a column to `ssn_encrypted` without a reversibility test is an incomplete review. Name the independent falsehood that would still keep Base64 from round-tripping the SSN.

## What this page is not doing

Do not merge by adding a comment “will add AES later.” That comment is leftover without an owner. Do not decode a live column to prove the finding.
