# Review of a “resistant password” claim

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships notes-app login copy. Review `labs/4.2/4.2-lab/vulnerable/` as that change. Reconstruct whether `phishing_resistant("password", EVIL, REAL)` is still true, compare that with the rule, and write changes a developer can verify.

The check you already ran (`test_password_is_not_phishing_resistant`) is the rule check. A banner “phishing-resistant password” is not.

## Picture: problems to find (name them yourself)

Look at this first: **`phishing_resistant('password', evil, real)` True**. Label it **rule**, **tool**, or **false assurance** before you accept the change.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{"What would prove it false?"}
  Q -->|"password at lookalike is true"| Property["Rule — good if checked"]
  Q -->|"autocomplete webauthn"| Mechanism[Tool — no origin]
  Q -->|"MFA equals resistant"| False[False assurance]
```

For each claim and each branch: label **rule**, **tool**, or **false assurance**. Keep this: password at lookalike is false. If that call never includes origin binding, the leftover is still there.

Problems to find (name them yourself; do not open the keys file):

- `phishing_resistant('password', evil, real)` True
- Marketing copy “MFA = phishing resistant”
- Recovery SMS as default
- No wrong-origin WebAuthn check

Also reject: trusting the client; closing findings without re-running `test_password_is_not_phishing_resistant`; keys in learner notes; real credentials in helpers; an unlabeled later hardware bar as baseline; live-kit language.

## Common mix-ups

- Any 2FA is phishing-resistant
- WebAuthn replaces who-is-allowed
- A usable login is a nice-to-have
- A passkey vendor name is the rule
- Training users to read the URL is what you trust

## Practice

Write three review notes a peer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_password_is_not_phishing_resistant`. Do not open the keys file.

## Use it somewhere new

Clinic SSO change that “adds MFA” without an origin-fail check is an incomplete review. Name the independent falsehood that would still keep password-at-lookalike false.

## What this page is not doing

Do not merge by adding a comment “will add WebAuthn later.” That comment is a leftover without an owner. Do not visit a live lookalike to prove the finding.
