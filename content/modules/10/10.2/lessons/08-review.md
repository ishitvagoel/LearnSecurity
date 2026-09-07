# Would you merge this always-true install_ok?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Treat `labs/10.2/10.2-lab/vulnerable/` as a CI-install change. Does `install_ok("aaa", "bbb")` still return true?

Compare the two hash strings in `install_ok`. An SBOM screenshot can wait. The review is whether `test_hash_mismatch_refuses_install` passes, not whether someone wrote “will pin later.”

## Picture: install_ok true on hash mismatch

**install_ok true on hash mismatch**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|mismatch installs| Property["Rule - good if tested"]
  Q -->|SBOM attached| Mechanism[Tool - inventory]
  Q -->|provenance badge| False[False assurance]
```

A digest mismatch still has to be denied. If the change never checks digest equality, that always-install leftover is still open. An SBOM screenshot without that check is still the same problem.

Unpinned Actions are a sibling grain. Secrets in fork pull requests are 5.3. Do not claim the ship gate. Do not fetch a live package to prove the finding.

## Problems to find (name them yourself)

- install_ok true on hash mismatch
- Unpinned action
- Secrets in PR from forks
- SBOM generated but never used

Also reject: live registry attacks; installing without re-running `test_hash_mismatch_refuses_install`; keys in learner notes; claiming the ship gate.

## Common mix-ups

- Lockfile without verify is integrity
- Private npm is safe
- A provenance badge is the app’s hash check
- Generating an SBOM verifies installs
- Dependabot is `install_ok`
- The ship gate follows from a green audit job

## Use it somewhere new

CycloneDX and Dependabot without a digest check do not finish the install gate. What still has to compare so a hash mismatch cannot install?

## Can people still use it

A denied install must say *digest mismatch* in words. Do not hide the reason behind a red X.

## What this page is not doing

A hash mismatch that still installs, plus “will pin later,” has no owner. Do not typosquat a public registry to prove the finding.
