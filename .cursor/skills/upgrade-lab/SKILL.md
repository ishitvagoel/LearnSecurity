---
name: upgrade-lab
description: Raise an existing lab from a toy predicate to a component or cross-component fixture with a real request cycle, state, and an anti-fake test. Use when deepening a module or when a lab is too artificial to exhibit its module's failure.
---

# Upgrade lab

`author-lab` creates labs. This skill raises an existing one to a tier that can actually exhibit the module's failure.

## The problem being fixed

23 labs are a two-line pure function with two tests. Grep across all of `labs/` finds zero Kotlin files and zero database drivers, against a declared FastAPI + PostgreSQL + Next.js + Android/Kotlin environment. A pure function cannot show authority resolved across a boundary, state mutated between check and use, a parser disagreeing with its consumer, or a cache keyed without a tenant — which is most of what this course teaches.

Determinism, speed, isolation, and resettability are real virtues and survive the upgrade unchanged. `lab-safety.mdc` and `labs-content.mdc` still bind in full.

## When to use

- `deepen-module` step 5
- A review artifact scored "Safe executable lab" below 2
- A lab's fixed variant can be satisfied by a label or a hard-coded allow-list

## Procedure

1. **Read** `references/lab-tiers.md`, the module's teaching claims from `spec.md`, and the current lab.
2. **Assign a tier.** Default Tier 2. Tier 1 only if a reviewer could argue the property genuinely *is* a pure function. Record the justification in the README.
3. **Choose the failure to stage.** It must be the module's forbidden outcome, reachable through the fixture's real control flow — not asserted by a boolean the test reads back.
4. **Build `vulnerable/` and `fixed/`.** They differ by the *structural* change the module teaches, and by nothing else. A diff that also renames, reformats, or fixes an unrelated bug makes the lesson unreadable.
5. **Write the tests**, minimum five and per the tier table: normal, forbidden outcome, boundary, malformed/failure, and an **anti-fake test**.
6. **Cover ≥2 teaching claims.** A lab that tests one predicate is what we are replacing.
7. **Pin dependencies** in `requirements.txt` when the lab needs any, and document the install in the README.
8. **Update** `module.yaml` `labSpec` and the README: invariant, root cause, impact, structural fix, detection and recovery, reset, and the exact two commands.
9. **Run both variants in a clean environment** and paste the real output.
10. **Ask for `lab-safety-reviewer`** before the lab is considered done.

## The anti-fake test

The test that distinguishes the taught fix from a plausible cheat. It passes on the real repair and fails on the fake.

`labs/5.2` is the cautionary case: its fixed variant once returned an `aesgcm:` prefix plus the plaintext length, and `looks_encrypted` checked only the prefix. Every test passed. The executable success condition rewarded a security *label* — exactly the "awareness list as proof" failure the course exists to prevent.

Name the fake explicitly in `05-verify.md` so the learner sees the trap they did not fall into.

## Do not

- Introduce a network call, a public target, real PII, or a non-disposable secret.
- Make the fixture slow or order-dependent. Tests run in a clean environment on every push.
- Ship a `vulnerable/` variant whose failure is a raised exception rather than the forbidden outcome — the test must fail *for the security reason*.
- Leave `--claim` as a new lab's entry point. The convention is `--impl vulnerable|fixed`.
