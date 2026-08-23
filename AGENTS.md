# LearnSecurity — agent instructions

This repository produces the **Secure Application Engineering from First Principles** curriculum (web, API, and mobile). The canonical map is [`secure-application-engineering-curriculum-blueprint.md`](secure-application-engineering-curriculum-blueprint.md) (revision 1.1). Do not replace or silently contradict it. Generated files must cite module IDs from the blueprint.

This pass is a **Cursor harness plus empty content scaffold**. Do not invent a parallel syllabus.

## Locked production defaults

Override only by recording a human decision in [`content/progress/STATUS.yaml`](content/progress/STATUS.yaml).

- **Web stack:** Python/FastAPI + PostgreSQL + TypeScript/Next.js
- **Mobile:** Android/Kotlin first. iOS/Swift is a later mirror. React Native is allowed only with required native Android/iOS security exercises.
- **Assurance:** tailored OWASP ASVS 5.0 Level 2 plus selected Level 3; MASVS 2.1 testing profiles (never obsolete MASVS L1/L2/R)
- **AI security:** elective E1, not core
- **Website progress:** local-first until accounts are justified
- **Authoring order:** Pass A for Phase 1, then Phase 2, as the pilot before mass-authoring

## Content generation passes

| Pass | Produce | Skill |
|---|---|---|
| A | Module specifications only (no lesson prose) | `author-module-spec` |
| B | Lessons, diagrams, examples, isolated labs | `author-lesson`, `author-lab` |
| C | Assessments, rubrics, keys (keys isolated) | `author-assessment` |
| D | Vercel learning site | not until A/B pilots exist; see `site/AGENTS.md` |
| E | Independent coverage and security review | `coverage-audit`, review subagents |

Start each session with **`next-iteration`**: read `content/progress/STATUS.yaml`, do **one unit**, update status, stop.

A unit is one of: one module spec; one module’s learner-facing lessons; one lab set; one assessment pack; one spiral revisit of SecureCollab artifacts; or one quality/coverage audit of already-authored work.

## Do not

- Skip phases or gates, or reorganize the course around OWASP Top 10 / CWE Top 25 (those are regression checks after causal design).
- Treat awareness lists as compliance or proof of security.
- Build the Pass D site before Phase 1–2 Pass A/B pilots exist.
- Instruct attacks on public, third-party, or production systems.
- Put weaponized exploit payloads, copy-paste PoCs, or live-target walkthroughs in learner-facing pages.
- Mix ASVS 4.x requirement IDs, draft standards presented as final, or MASVS L1/L2/R levels.

## Seven-step learning loop

Every substantive module uses this template (blueprint §3):

1. **Property** — precise security invariant
2. **Model** — assets, actors, authority, boundaries, state, time
3. **Break** — smallest representative failure in an **authorized lab**
4. **Build** — smallest trustworthy mechanism that restores the invariant
5. **Verify** — normal, negative, abuse, and failure cases
6. **Operate** — log, alert, rotate, revoke, recover
7. **Generalize** — limits, trade-offs, standards mapping

Thesis: security is **maintaining invariants under adversarial conditions**. Derive every control from a threat and a required property. Pair prevention with detection and recovery where appropriate.

## Laboratory policy

Offensive work is limited to: (1) local applications created for this course; (2) intentionally vulnerable training projects (e.g. Juice Shop, WebGoat, crAPI) or official labs; (3) challenges whose published terms authorize the action; or (4) systems with written authorization and defined scope.

In authorized labs, teach **cause, invariant, impact, structural fix, and tests**. Vulnerable snippets belong only under `labs/` with warnings and reset instructions. Lab data is synthetic. Secrets are disposable. Vulnerable configurations stay isolated from personal and production environments.

## File conventions

- Modules: `0.1`–`10.5`, capstone `11`, electives `E1`–`E6`, milestones `M0`–`M5`, gates `0`–`11`
- Metadata (schema) is separate from lesson prose — blueprint §14.2 and `content/schema/module.schema.json`
- Specs: `content/modules/<phase>/<id>/spec.md` plus `module.yaml`
- Lessons: `content/modules/<phase>/<id>/lessons/`
- Assessments: learner material under `content/modules/.../assessment/`; answer keys only under `content/assessment/keys/`
- Reference system: SecureCollab evolves by phase (blueprint §9.1); spiral revisits after assumption changes (`spiral-revisit`)

## Standards

Before generating or materially revising a module, run **`standards-pin`**. Check the canonical source; record `version`, `status`, `publishedAt`, `reviewedAt`; label drafts and candidate recommendations; keep migration notes when guidance changes.

## Skills and subagents

Skills: `next-iteration`, `author-module-spec`, `author-lesson`, `author-lab`, `author-assessment`, `standards-pin`, `quality-gate`, `spiral-revisit`. Slash-only: `pilot-phase-1`, `coverage-audit`.

Review subagents (read-only, do not rewrite in the same pass): `standards-auditor`, `quality-reviewer`, `lab-safety-reviewer`, `curriculum-architect`.
