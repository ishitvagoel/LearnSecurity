# Review a security claim like an engineer

**Kind:** code-review
**Loop step:** 7 Generalize

## Review the vulnerable fixture

Read `labs/1.1/1.1-invariant-catalogue/vulnerable/SECURITY.md` and its claim file. Write four actionable review comments. Each comment must identify the unsupported conclusion, the missing model or mechanism limit, the minimum useful change, and the evidence that would test it.

“Looks secure” is not a review. Neither is replacing one product name with another.

## Review the repaired fixture

Read the fixed claim only after writing your review. Explain which rows became bounded, which evidence modes were added, and what the validator still cannot prove. Keep the review local and synthetic; examiner keys are not needed for this exercise.

## Ready to continue

Your 1.1 evidence pack should now contain five catalogue rows, the causal review, vulnerable-fail and fixed-pass results, four-mode evidence, operate notes, and the CivicClinic transfer. The next topic turns the model into explicit authority decisions.
