# 8.4 — Build, distribution, attestation, resilience (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
Review `labs/8.4/8.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/8.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): api_allowed debug+ok True
- Seeded smell (label it yourself): Signing key in the repo
- Seeded smell (label it yourself): Same API key in debug and release (5.3)
- Seeded smell (label it yourself): Resilience checklist as Gate 8 evidence

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Obfuscation = security
- Play App Signing means we don’t care
- Anti-debug proves the server can trust the client

## Practice

Write three review notes. Do not open the keys file.

## Transfer

SBOM of the APK (10.2).
