# Break the score skip and the dropped gap

**Kind:** mechanism-lab
**Loop step:** 3 Break

Work only in `labs/0.2/0.2-bridge`. The vulnerable implementation has two defects: scores at least 80 grant a Phase 1 skip, and `bridge_recommendations` returns an empty list even when evidence is missing.

```text
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
```

The failing assertions show two unsafe shortcuts: a number treated as authorization and a capability gap silently discarded. Do not attack an LMS or any public target; the fixture uses fake scores and local evidence.

## Practice

Inspect the two functions and write the smallest property that each violates. A passing low-score test does not excuse the high-score or missing-bridge failure.
