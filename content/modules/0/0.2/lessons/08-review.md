# Review the diagnostic contract as a PR

**Kind:** code-review
**Loop step:** Review

Review `labs/0.2/0.2-bridge` as if it were a placement-service change. Ask:

- Does score 100 still return false for the Phase 1 skip?
- Does every missing or unknown capability produce a stable bridge id?
- Does a complete map produce no bridge ids?
- Are bridge assignments kept separate from 1.2/1.3/1.4 and Gate 1 evidence?
- Does the record avoid quiz answers, badges, and production data?

Reject a PR that returns `[]` for missing evidence or that maps a job title to security clearance. Approve only when the vulnerable run fails the intended assertions and the fixed run passes them.
