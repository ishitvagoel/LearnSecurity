# 3.2-LO-08 — Review the empty model as a PR, not a ceremony

**Kind:** code-review
**Loop step:** Review
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-15.1.3`; OWASP Threat Modeling Project (maintained).

## Review the fixture as if it were SecureCollab’s threat-model assembler

Review `labs/3.2/3.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/3.2.md` — not here.

## Mental model: threats = [] if scanner_green

Start with this seeded smell: **threats = [] if `scanner_green`**. Label it property, mechanism, or false assurance before you accept the PR.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{What would falsify it?}
  Q -->|"cross-tenant-read missing on green scan"| Property["Property - good if tested"]
  Q -->|"we ran STRIDE"| Mechanism[Mechanism - no seed]
  Q -->|"scanner was green"| False[False assurance]
```

Seeded smells (label them yourself; do not open the keys file):

- threats = [] if `scanner_green`
- No `cross-tenant-read` item
- Model not in git (only a slide)
- STRIDE letters without assets, owners, or invalidation

Also reject: client trust as TCB, Appendix D cited as an ASVS requirement id, closing findings without retest, keys in lessons, real PII in fixtures.

## Misconceptions

- Green scan means no threats
- Threat models are pre-code only
- Awareness lists are the threat list

## Practice

Write three review notes. Tie at least one to `test_green_scanner_is_not_an_empty_threat_model`.

## Transfer

Clinic SMS PR that “adds a HIPAA sticker” without seeding `sms-content-leak` is incomplete.
