# Verify every missing capability gets a bridge

**Kind:** verification-lab
**Loop step:** 5 Verify

Run both implementations:

```text
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
python3 -m pytest labs/0.2/0.2-bridge/tests --impl fixed
```

The vulnerable run must fail the score-deny and missing-bridge assertions. The fixed run must pass for mixed evidence and for a complete map. These checks prove the diagnostic contract only; they do not prove a learner can threat-model, write a deny rule, or pass Gate 1.

## Practice

Add one absent capability to the input and predict the new bridge. Keep the assertion about the security skip unchanged.
