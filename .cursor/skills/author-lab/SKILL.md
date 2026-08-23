---
name: author-lab
description: Pass B labs — create authorized break/fix/verify labs with vulnerable and fixed pairs, forbidden-outcome tests, and reset docs. Use when adding labs, seeded failures, or isolated vulnerable code for a module.
---

# Author lab (Pass B)

## When to use

- Spec lists a lab brief and Pass B is in progress
- User asks for a break/fix lab, seeded vulnerability, or local training target

## Instructions

1. Confirm authorized scope (course-local app, official vuln project, published challenge terms, or written authorization). **Stop** if the request implies a public or third-party target.
2. Copy [`assets/lab-readme.stub.md`](assets/lab-readme.stub.md) to `labs/<module-id>/<lab-slug>/README.md`.
3. Create `vulnerable/` and `fixed/` (or equivalent) plus tests that fail on the vulnerable tree for the **forbidden outcome** and pass on the fixed tree.
4. Teach cause, invariant, impact, **structural** fix (not a blacklist-only patch unless the spec says why), and verification. Detection/recovery notes required when the module’s operate step applies.
5. Synthetic data only. Disposable secrets. Isolation and reset documented.
6. Do not put copy-paste weaponized exploits in learner-facing lesson Markdown. Lab READMEs describe reproduction at the minimum fidelity needed to show cause in the local target.
7. Link the lab from the module spec / `module.yaml` `labSpec`.
8. Ask the parent to delegate **`lab-safety-reviewer`** before marking the lab complete.
9. Update STATUS notes; do not jump `pass` to C.

Default stack: FastAPI + PostgreSQL + Next.js unless the module is mobile (Android/Kotlin first).
