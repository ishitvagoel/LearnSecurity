# Would you merge this client booleans?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/8.1/8.1-lab/vulnerable/` as a change to the notes app’s Android export. Check whether `allow_export({"integrity": "ok"}, "fail")` still returns true.

You already ran `test_client_integrity_claim_is_not_authorization`. A comment “we will attest later” is not. A sticker about a mobile checklist is not this review.

## Picture: if integrity==ok: export

**`if integrity==ok: export`**.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{"What would prove it false?"}
  Q -->|client ok plus attest fail exports| Property["Rule — good if checked"]
  Q -->|Compose disabled| Mechanism[Tool — UI]
  Q -->|Play Integrity logo| False[False assurance]
```

Client ok plus attest fail still has to be denied. If the change never checks a server attest, that client-boolean path is still open. A Play Integrity logo without that check is still the same problem.

Shrinking the app and a platform-integrity check raise cost; they do not become 1.2. Feature flags and 8.4 debug clients are other hostile-client paths — name them, do not skip `test_client_integrity_claim_is_not_authorization`.

## Problems to find (name them yourself)

- `if integrity==ok: export`
- No server-attest check
- Secrets in the app file (8.4)
- A mobile checklist used as a sticker / old numbered levels

Also reject: live device farms; personal-phone cookbooks; closing findings without re-running `test_client_integrity_claim_is_not_authorization`; keys in learner notes.

## Common mix-ups this topic refuses

- Shrinking the app is authorization
- Kotlin is the guarantee
- Store listing equals device trust
- Play Integrity in the app is 1.2
- Old numbered mobile levels are current

## Use it somewhere new

A clinic change that “enabled Play Integrity” without a failing-attest deny check is an incomplete review. Name the independent falsehood that would still keep client ok plus attest fail false.

## What this page is not doing

Do not merge by adding a comment “will attest later.” That comment is leftover without an owner. Do not instrument a live device to prove the finding.
