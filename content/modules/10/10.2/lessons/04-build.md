# Require expected hash equals got hash

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

Last week’s package names are not a digest check. Muting a scanner finding does not compare hashes. Generating an SBOM is not the repair.

The structural change is: `install_ok` **returns `expected_hash == got_hash`**. Fail-safe: a mismatch denies. Provenance and an SBOM may *sit next to* a match; they do not replace it. Structural means that equality — not package name, not Dependabot, not a provenance badge.

The smallest fix for the notes app’s CI is: `aaa` vs `bbb` → do not install. Do not fail open because “the SBOM lists the package.” Do not accept `@v1` as a digest.

## Picture: equality is the gate

```mermaid
flowchart TD
  Call[install_ok] --> Eq{expected equals got?}
  Eq -->|yes| Allow[install]
  Eq -->|no| Deny[deny]
```

Install has to compare digest equality. Matching a malicious digest is a lying lockfile — the pin still has to be benign. Who can edit the lockfile is 10.1 / CODEOWNERS, not this check. A lookalike package still wins if you install by name somewhere else; equality is the local stand-in.

Provenance says *how* the artifact was built. It does not replace digest match. An SBOM can list hashes — generating the file is still not `install_ok`.

## What the repaired files must show

Do not treat `fixed/lock.py` as a production installer.

| After the fix | Must be true |
|---|---|
| aaa vs bbb | install false |
| aaa vs aaa | install true |

Fail closed: if the hashes do not match, do not install. Uncertainty is a **no** on “this may install,” not a yes because the SBOM listed the name.

## What this is not

- Dependabot.
- A provenance badge.
- A CISA-style SBOM file treated as verify.
- The ship gate complete.
- Pinning malware (leftover).
- npm audit.
- pip without a hash requirement as the trusted check.

## What the tool cannot do

- Matching a malicious pin still installs in this lab.
- Cache poisoning can serve old bytes after a good pin.
- Unpinned GitHub Actions `@v1` is a sibling grain, not this check.
- Secrets in fork pull requests remain 5.3.
- A lookalike on a public index still needs index policy beyond equality.

## Can people still use it

A denied install must say *digest mismatch* in words, not only “assert False.” Do not hide the reason behind a red X.

## Practice

Name who can edit the lockfile. Run:

```text
python3 -m pytest labs/10.2/10.2-lab/tests --impl fixed
```

## Use it somewhere new

Pin Actions by SHA, not `@v1`. That is the same equality idea on a different object.

## What can still go wrong

Malicious pin. Cache poisoning. Unpinned actions. Secrets in fork pull requests (5.3). A lookalike package that never hits this equality check.
