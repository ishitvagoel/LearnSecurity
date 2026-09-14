# Lab 0.2 — diagnostic evidence chooses bridges, never security clearance

**Module:** `0.2`
**Authorized scope:** this directory only. Local course fixture.
**Invariant:** `quiz_score_grants_phase1_skip(100)` is false, and every missing tooling capability gets a named bridge.
**Root cause class:** a number treated as a capability, or a capability gap silently dropped
**Non-goals:** NICE work-role fluency as Gate 1; LMS percentage as ASVS; live LMS testing.

## Reset

Re-run pytest. Optional: `git checkout -- labs/0.2/0.2-bridge`.

## The diagnostic contract

The input is a small, reviewable evidence map for `python`, `browser`, `sql`, `network`, and `git`. The fixed implementation returns deterministic bridge ids for every capability not demonstrated:

```text
{"python": True, "browser": False, "sql": True, "network": False, "git": False}
→ ["bridge-browser", "bridge-network", "bridge-git"]
```

A bridge id assigns tooling practice. It does not create 1.2 cells, complete 1.3 or 1.4, or waive Gate 1. Unknown or absent evidence is treated as a gap so the learner gets practice instead of an accidental skip.

## Vulnerable behavior (local only)

The vulnerable function still grants a Phase 1 skip at score ≥ 80 and returns no bridge recommendations. Both are forbidden outcomes: a score is not authorization, and a missing bridge must not disappear from the learner's path.

## Verify

```text
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
python3 -m pytest labs/0.2/0.2-bridge/tests --impl fixed
```

The vulnerable run must fail the score and missing-bridge assertions. The fixed run must pass all checks. A setup error is not evidence that the contract holds.

## Operate and transfer

Record bridge ids and evidence summaries, never quiz answers or badges. Audit that 1.2/1.3/1.4 and Gate 1 remain required after a bridge is assigned. Apply the same contract to a clinic onboarding diagnostic or a vendor-cert intake: missing tool fluency gets a bridge; security review still needs its own evidence.
