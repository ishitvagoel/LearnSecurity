# Review of empty-model-on-green-scan

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/3.2/3.2-lab/vulnerable/` as a change to the notes-app threat list. Check whether `threats_from_scan(True)` still omits `cross-tenant-read`.

A comment “will threat-model later” is not a pass on `test_green_scanner_is_not_an_empty_threat_model`.

## Picture: threats = [] if scanner_green

**threats = [] if `scanner_green`**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"cross-tenant-read missing on a green scan"| Property["Rule — good if tested"]
  Q -->|"we ran STRIDE"| Mechanism[Tool — no seed]
  Q -->|"scanner was green"| False[False assurance]
```

The always-name id still has to be present on green. If the change never checks a seeded join, that leftover path is still open.

## Problems to find (name them yourself)

- threats = [] if `scanner_green`
- No `cross-tenant-read` item
- Model not in version control (only a slide)
- STRIDE letters without assets, owners, or “what would prove this row wrong”

Also reject: treating the client as what you trust; an awareness list cited as a passing score; closing findings without re-running `test_green_scanner_is_not_an_empty_threat_model`; keys in learner notes; real personal data in the practice; a Top 10 as the threat list.

## Common mix-ups

- Green scan means no threats
- Threat models are pre-code only
- Awareness lists are the threat list
- Threat Dragon is the rule
- The data-centric modeling note (**draft**) is a verification list

## Use it somewhere new

Clinic SMS change that “adds a HIPAA sticker” without seeding `sms-content-leak` is an incomplete review. Name the independent falsehood that would still keep `cross-tenant-read` present on green.

## What this page is not doing

Do not merge by adding a comment “will threat-model later.” That comment is leftover risk without an owner. Do not run a live scanner to prove the finding.
