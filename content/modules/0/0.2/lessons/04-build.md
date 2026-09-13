# Build a deterministic bridge recommendation

**Kind:** design-exercise
**Loop step:** 4 Build

Implement the bridge function as a pure mapping from evidence to stable ids. Preserve a fixed capability order so a learner's path is reviewable. Treat absent evidence as not demonstrated.

```python
return [bridge for capability, bridge in CAPABILITY_BRIDGES.items()
        if evidence.get(capability) is not True]
```

Keep `quiz_score_grants_phase1_skip` unconditionally false. The bridge function assigns tooling practice only; it must not mint 1.2 cells or mark Gate 1 complete.

## Practice

Compare the fixed implementation with the vulnerable one. Explain why returning `[]` is unsafe even though it does not grant a security skip: it hides work the learner still needs.
