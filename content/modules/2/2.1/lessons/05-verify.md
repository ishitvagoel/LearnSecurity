# 2.1-LO-05 — Tests for unambiguous ingest

**Kind:** verification-lab  
**Loop step:** 5 Verify  

Clean JSON accepts. Duplicate tenant keys: not accepted **or** both views equal (the lab requires deny-or-equal). Happy path is insufficient.

## Practice

Add a case: missing tenant → deny (residual if not in fixture).
