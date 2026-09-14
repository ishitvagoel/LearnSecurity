# Verify the forbidden outcome

**Kind:** verification-lab
**Loop step:** 5 Verify

## Run the intended lab

From the repository root, run the vulnerable and fixed catalogue fixtures:

```text
python -m pytest labs/1.1/1.1-invariant-catalogue/tests --claim labs/1.1/1.1-invariant-catalogue/vulnerable/security_claim.yaml
python -m pytest labs/1.1/1.1-invariant-catalogue/tests --claim labs/1.1/1.1-invariant-catalogue/fixed/security_claim.yaml
```

The vulnerable fixture should fail for the intended semantic and scope defects. The fixed fixture should pass. The validator is deliberately incomplete; record one meaningful defect it cannot detect.

## Four evidence modes

For one catalogue row, specify a normal case, a negative case, an abuse case, and a failure case. Each must name an observable oracle. “Scanner is green” or “the field exists” is not an oracle for the product property.

## Check yourself

Write the forbidden outcome in one sentence. Then write the smallest observation that would falsify it. If your check cannot fail, it is not evidence yet.
