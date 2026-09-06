# 3.2-LO-08 — Review the empty model as a PR, not a ceremony

**Kind:** code-review
**Loop step:** Review
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-15.1.3`; OWASP Threat Modeling Project (maintained). Appendix D is awareness, not a requirement id.

## Review the fixture as if it were SecureCollab’s threat-model assembler

Review `labs/3.2/3.2-lab/vulnerable/` as a SecureCollab PR. Your job is not to count suspicious lines. Reconstruct whether `threats_from_scan(True)` still omits `cross-tenant-read`, compare that with the module invariant, and write changes a developer can verify.

Intended findings live only in `content/assessment/keys/3.2.md` — not here. Do not open the keys file until your review has been evaluated.

## Mental model: threats = [] if scanner_green

Start with this seeded smell: **threats = [] if `scanner_green`**. Label it property, mechanism, or false assurance before you accept the PR.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"cross-tenant-read missing on green scan"| Property["Property - good if tested"]
  Q -->|"we ran STRIDE"| Mechanism[Mechanism - no seed]
  Q -->|"scanner was green"| False[False assurance]
```

Classification starts at the protected effect (mandatory id present on green). Everything that is not a seeded union at that call is a candidate ambient path.

## Seeded smells (label them yourself)

- threats = [] if `scanner_green`
- No `cross-tenant-read` item
- Model not in git (only a slide)
- STRIDE letters without assets, owners, or invalidation

Also reject: client trust as TCB; Appendix D cited as an ASVS requirement id; closing findings without re-running `test_green_scanner_is_not_an_empty_threat_model`; keys in lessons; real PII in fixtures; Top 10 as the threat list.

## Misconceptions this module refuses

- Green scan means no threats
- Threat models are pre-code only
- Awareness lists are the threat list
- Threat Dragon is the property
- SP 800-154 (draft) is a verification catalogue

## Practice

Write three review notes a maintainer could act on. Each note: observation, property or false assurance, suggested structural change, residual you will **not** delete. Tie at least one to `test_green_scanner_is_not_an_empty_threat_model`.

## Transfer

Clinic SMS PR that “adds a HIPAA sticker” without seeding `sms-content-leak` is an incomplete mediation review. Name the independent falsehood that would still keep `cross-tenant-read` present on green.

## Non-goals

Do not merge by adding a comment “will threat-model later.” That comment is a residual without an owner. Do not run a live scanner to prove the finding.
