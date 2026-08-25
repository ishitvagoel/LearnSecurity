# Curriculum depth audit — 2026-08-25

## Decision

The curriculum map, module metadata, site rendering, and safe local-lab convention are useful foundations. The repository was not justified in marking all 57 units publishable and competent. Those claims are reset to map-complete/developing until each unit receives module-specific deepening and independent semantic review.

Module 1.1 is the reference remediation. It may return to publishable only after its new lessons, lab, assessment, SecureCollab artifact, schema, and clean lab pair pass independent quality and lab-safety review.

This audit does not reset historical authoring pass E. Pass records describe which pipeline stages occurred; depth and quality describe whether the result currently meets the semantic teaching bar.

## Scope and method

Reviewed:

- blueprint revision 1.1 and repository AGENTS instructions;
- STATUS, Pass E, and quality-gate records;
- all module metadata and lesson structure;
- generator behavior;
- lab implementation inventory and representative tests;
- SecureCollab reference artifacts and capstone claims;
- Pass D site behavior.

The audit distinguished structural presence from semantic evidence. Word counts and duplication are diagnostic signals, not automatic publication decisions.

## Evidence

### Status exceeded the review evidence

Before this remediation:

- 57 of 57 units were marked depth publishable and quality competent;
- revision.remaining was empty;
- the Pass E record itself said generated Phase 0, Phase 3–11, and elective lessons were thinner than the hand-authored pilot;
- no post-rewrite independent semantic review artifact existed for the 2026-08-24 bulk rewrite.

A historical review of earlier files cannot approve later generated replacements.

### The bulk generator crossed the author/reviewer boundary

scripts/emit_publishable_lessons.py generated lesson and assessment scaffolds, rewrote module metadata, assigned a quality-reviewer identity, set review dates, and appended a “publishable rewrite” changelog entry. Its uniqueness checks compared only selected property and forbidden-outcome strings.

A generator can create drafts and run deterministic checks. It cannot provide independent semantic judgment. This remediation adds an explicit opt-in, protects the reference modules, clears review metadata on rewritten units, and labels output draft.

### Prose was structurally repetitive

The audit counted 456 lesson files. Fifty-five of 57 modules shared the same broad generated lesson scaffolding. Repeated phrases and section-level templates occupied a material share of the corpus, while many module packs remained short relative to their scope.

Repetition is not automatically a defect; consistent learning loops are intentional. Here, the repeated form often replaced the causal explanation, worked reasoning, practice progression, and module-specific failure analysis that the form was meant to organize.

### Metadata and implementation disagreed

Fifty-six module specifications still described build work as deferred to Pass B even after STATUS called them publishable. The repository held local fixture labs but not the promised cross-phase SecureCollab application. Gate and milestone states correctly remained not-attempted.

This means the honest current claim is curriculum-map coverage plus local fixtures, not a completed secure-application engineering program.

### Labs often tested claim shape rather than module behavior

The lab tree was overwhelmingly small Python/YAML fixtures and did not contain the locked Next.js/TypeScript or Android/Kotlin application slices. Many vulnerable/fixed pairs checked whether a security claim had expected words or fields. That can be appropriate for Module 1.1, whose educational object is the quality of an invariant claim, but is not sufficient for later parser, browser, authorization, state, mobile, or operations modules.

Later revisions must implement the module-specific forbidden outcome in the appropriate locked stack or record a justified exception.

### The site was not the truncation point

The Next.js site renders source lesson Markdown. The shallow experience originates primarily in the authored source, not a site excerpting bug. Site readability work is valuable but cannot manufacture missing explanation.

## Remediation controls

1. **Truthful status:** all units reset to map-complete/developing; revision.remaining contains 56 units after the 1.1 reference.
2. **Semantic rubric:** publication requires scores of at least 2 on every required dimension, with no critical failure or compensating average.
3. **Coverage contract:** every outcome maps to explanation, worked reasoning, learner practice, assessment evidence, and transfer.
4. **Independent evidence:** each publishable unit needs a dated review record naming files, scores, blockers, exact lab results, reviewer, and independence.
5. **Generator boundary:** bulk generation produces drafts, clears prior review metadata, and cannot update STATUS to publishable.
6. **Module-specific labs:** vulnerable must fail and fixed must pass for the taught forbidden outcome, not a generic keyword.
7. **One-unit queue:** standards pin, spec, lessons, lab, assessment, SecureCollab revisit, execution, independent review, then STATUS.

## Reference-module acceptance criteria

Module 1.1 must demonstrate:

- a coherent seven-step causal progression rather than eight disconnected prompts;
- a complete SecureCollab claim envelope and worked counterexamples;
- a semantic local lab that checks more than key presence and explicitly states its limits;
- practical, non-compensating assessment and an isolated examiner key;
- a materially changed transfer case;
- standards used within their actual role;
- privacy-safe operations and human-factor constraints;
- clean vulnerable-fail and fixed-pass results;
- independent quality and lab-safety approval recorded under content/progress/reviews.

## Queue policy

The next unit is 1.2, followed by the remaining Phase 1/2 pilot, bridge/orientation, later core phases, capstone, and electives as listed in STATUS. A unit leaves revision.remaining only when its own review evidence passes. Similar filenames, schema validity, or generator output do not move the queue.
