# 2.1-LO-06 — Parse failures without storing bodies

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** CSF 2.0 (final) Detect — outcomes.

Log `ambiguous_tenant` with subject and size, not body. Alert on a spike. Recovery: do not replay the raw body into a second parser “to be helpful.”
