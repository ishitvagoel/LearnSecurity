# Break a tools-only security claim

**Kind:** mechanism-lab
**Loop step:** 3 Break

## The failure

The local practice contains a vulnerable `SECURITY.md` and a claim file that says control names and a scanner result prove the notes app is secure. That claim omits the product model, attacker capability, forbidden outcomes, evidence, and recovery.

Run the catalogue validator from the repository root:

```text
python -m pytest labs/1.1/1.1-invariant-catalogue/tests --claim labs/1.1/1.1-invariant-catalogue/vulnerable/security_claim.yaml
```

The expected failure is semantic: the catalogue does not establish bounded, testable claims. A missing Python package or malformed command is an environment failure, not the security observation.

## What to record

Group the validator findings as missing property, missing model, unsupported evidence, missing operation, and unsafe scope. Then draft one corrected row before opening the fixed fixture.

This lab is local and synthetic. Do not visit the public URL included as text in the vulnerable fixture.
