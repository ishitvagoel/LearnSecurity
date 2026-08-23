# Lab: Invariant catalogue vs mechanism slogan

**Module:** `1.1`  
**Authorized scope:** local course application (this directory only)  
**Invariant:** Security claims are testable system-specific properties, not mechanism names.  
**Root cause class:** trust (false assurance / property–mechanism collapse)  
**Non-goals:** Password cracking, attacking third-party sites, collecting PII.

## Reset

```bash
cd labs/1.1/1.1-invariant-catalogue
# work on a copy of vulnerable/ or check out this folder again
```

Synthetic data only. No secrets.

## Vulnerable behavior (local only)

`vulnerable/security_claim.yaml` and `vulnerable/SECURITY.md` assert that the system is secure **because passwords are hashed**. That does not state a SecureCollab invariant (e.g. note confidentiality). Tests that require property-shaped claims **fail** on `vulnerable/`.

## Structural fix

`fixed/` states property, attacker, trust, time horizon, and evidence. A hash algorithm name may appear only as a *mechanism under* a password-at-rest property—not as a substitute for note confidentiality.

A scanner-only “use bcrypt” finding does not restore the catalogue invariant.

## Verify

```bash
cd labs/1.1/1.1-invariant-catalogue/tests
pip install pyyaml pytest -q
python3 -m pytest test_claim_shape.py --claim ../vulnerable/security_claim.yaml
# expect failure
python3 -m pytest test_claim_shape.py --claim ../fixed/security_claim.yaml
# expect pass
```

- Happy path: fixed claim documents a note-confidentiality invariant.
- Forbidden outcome: claim file that is only a tool slogan.
- Failure: missing attacker/trust fields.

## Operate

If production docs regress to slogans, treat it as lost accountability: the operate note in the learner catalogue must say how false assurance would be caught (review checklist, not a SIEM product name).

## Transfer

Replace “bcrypt” with “we use JWT” and repeat the shape test mentally—still not an authorization invariant (1.2).
