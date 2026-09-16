# Content quality improvement plan — 2026-09-16

**Target:** `main` / `claude/content-quality-review-plan-dq4jkt`
**Scope:** learner-facing quality of `content/`, `labs/`, and the rendering layer in `site/lib/`.
**Audience:** execution models ("workhorses") doing bulk authoring, plus the human who sequences them.
**Relationship to prior work:** this plan *extends* [`reviews/2026-09-07-full-repository-content-review.md`](reviews/2026-09-07-full-repository-content-review.md). That review diagnosed structure. This plan adds the prose-level, lab-level, and enforcement-level diagnosis, and converts every finding into an executable procedure with acceptance tests.

---

## 1. How to use this document

Read sections 2–4 once to understand *why*. Then execute from section 6 onward.

- Section 5 lists workstreams **W0–W8** in dependency order. Do not start a workstream whose prerequisites are unmet.
- Section 7 is the **per-module runbook**. One module = one unit of work = one branch = one commit = one review artifact.
- Section 8 gives the **target shape of each of the eight lesson files**. Follow it literally.
- Section 13 is the **definition of done**. A module is not finished until every box there is checked.

Two rules override everything else in this plan:

1. **A generator may not approve its own output.** `.cursor/skills/quality-gate/SKILL.md` step 5 and `deepen-curriculum/references/publishable-depth.md` are binding. A workhorse authoring a module may never set `depth: publishable`, `quality: competent`, `reviewer:`, or `lastReviewedAt`.
2. **Modules 1.2 and 1.3 are the quality bar.** When this plan is ambiguous, open `content/modules/1/1.3/lessons/01-property.md` and match it.

---

## 2. Verdict

The repository is a **structurally excellent, pedagogically underbuilt** curriculum. The architecture (seven-step loop, property-first framing, forbidden-outcome labs, key isolation, standards pinning) is genuinely good and should not be redesigned. The *writing* is the problem: 54 of 57 modules are template fills that assert conclusions instead of teaching the reasoning that produces them.

Measured on this commit:

| Signal | Reference modules (1.2, 1.3) | The other 54 modules |
|---|---|---|
| Words per lesson | 1,507 / 2,049 | 391 – 601 (median ~460) |
| Median sentence length | 12 words | 9 words |
| Sentences of ≤5 words | rare | **16% of all sentences** |
| Lab implementation size | 140 / 234 LOC | 2–24 LOC (23 labs are 2 LOC) |
| Tests per lab | 6 | **2 or 3 in 41 of 57 labs** |

Aggregate: 57 modules, 456 lesson files, 235,127 lesson words, 552 Mermaid diagrams, 57 labs, 114 vulnerable/fixed invocations.

The gap is not length for its own sake. It is that ~460 words cannot carry derivation, a worked example, a counterexample, mechanism limits, and a transfer task — so the authoring pass produced *labels* for those things instead.

---

## 3. Inherited constraints (do not violate)

These come from `AGENTS.md`, `.cursor/rules/`, and the blueprint. They are not up for revision in this plan.

- Offensive work only in `labs/` against local synthetic fixtures. No live targets, no weaponized payloads, no real PII, no production secrets.
- Answer keys only under `content/assessment/keys/`. Never linked from `site/`.
- Standards: ASVS 5.0 (never 4.x IDs), MASVS 2.1 profiles (never L1/L2/R). Drafts labelled draft.
- Stack defaults: FastAPI + PostgreSQL + TypeScript/Next.js; Android/Kotlin for mobile.
- Do not reorganize the course around OWASP Top 10 / CWE Top 25.
- `content/` holds prose and metadata; executable code lives in `labs/`.

---

## 4. Defect catalogue

Each defect has an ID used throughout the rest of this plan. Fix them by ID so review artifacts can cite them.

### D1 — Telegraphic prose that asserts instead of derives
**Where:** all 456 lesson files except `content/modules/1/1.2/**` and `content/modules/1/1.3/**`.
**Evidence:** 16% of sentences outside the reference modules are ≤5 words. Example, `content/modules/4/4.3/lessons/04-build.md`: *"localStorage JWT. Implicit grant. Magic-link standing session. TLS as the log control. HttpOnly as 'not in the URL.' A referrer policy as the parser."* Six noun phrases, no verbs, no explanation of why any of them is wrong.
**Why it matters:** the blueprint's thesis is that security is derived from properties under adversarial conditions. A reader who cannot follow the derivation memorizes the conclusion, which is exactly the "awareness list" failure mode the course exists to prevent. Fragments also defeat the transfer goal: you cannot re-derive a claim you never saw derived.
**Fix:** rewrite in connected prose. Every claim gets the chain *what changes → why that lets the attacker win → what therefore has to be true*. See §8 for per-lesson shape and §9 for the sentence-level rules.

### D2 — Teaching by negation list
**Where:** pervasive; concentrated in `## What this is not`, `## What is not good enough`, and inline "not X, not Y" clauses.
**Evidence:** `4.3/lessons/01-property.md`: *"Copying that pattern is not those checklists."* — literally incoherent. `7.2/lessons/03-break.md`: *"Not the lesson | A bug-list sticker, object GET as this grain, or live GraphQL."*
**Why it matters:** negation only teaches once the positive model exists. Listing six wrong answers before explaining the right one produces recognition without understanding, and the compressed phrasing has already degraded into nonsense in places.
**Fix:** each lesson keeps **at most three** rejected alternatives, each given one full sentence saying *what the reader would plausibly believe*, *why it fails here*, and *what the reader should check instead*. Delete the rest.

### D3 — One narrow predicate stretched across eight lessons
**Where:** most modules. Confirmed examples: `5.2` (Base64-is-not-encryption), `4.5` (an `aud` comparison), `10.2` (a digest mismatch), `E1` (an `exec_sql` allow-list), `7.2` (a `resolve(role, field)` boolean), `4.3` (a query-string check).
**Why it matters:** the module title promises a topic; the lessons deliver one boolean. "Sessions, cookies, and tokens" never explains session lifetime, fixation, rotation, or binding. Naming the rest as "residuals" is honest but is not coverage.
**Fix:** per module, define **three to five teaching claims** in `spec.md` (not one), distribute them across the loop, and ensure the lab exercises at least two of them. See §7 step 2.

### D4 — Template sameness across all modules
**Where:** heading frequency across 456 lessons: `## Use it somewhere new` 446, `## What this page is not doing` 430, `## Practice` 392, `## What the framework does vs what you still have to check` 136.
**Why it matters:** identical scaffolding signals generation rather than authorship, and it forces content into cells where it does not fit — which is how empty cells got filled with slogans. It also makes the site's per-lesson pages indistinguishable.
**Fix:** headings must describe *this* lesson's content. Keep the loop-step label in frontmatter, drop the fixed heading vocabulary. The only headings that may repeat verbatim across modules are `## Practice` and `## Check yourself`.

### D5 — Safety boilerplate crowding out teaching
**Where:** most `03-break.md` and `07-transfer.md` files.
**Evidence:** `7.2/lessons/03-break.md` says "do not query a public GraphQL host / employer API / live clinic" four separate times in ~450 words — roughly 15% of the lesson.
**Why it matters:** the safety rule is correct and must stay, but repeating it four times crowds out the explanation and trains readers to skim past it.
**Fix:** exactly **one** scope statement per lesson, placed immediately before the first command, in this form: *"Run this only inside `labs/<id>/<slug>/`. The data is synthetic; `<label>` is a fixture label, not a real credential."* Delete every other instance. The full policy already lives in `labs/<id>/<slug>/README.md` and the site policy page.

### D6 — Decorative diagrams
**Where:** 552 Mermaid blocks; 59 (11%) have three or fewer nodes.
**Evidence:** `6.2/lessons/07-transfer.md` renders `Nick[nickname] --> Belief[UI believes it is a label]` — two disconnected two-node edges that restate the sentence above them.
**Why it matters:** a diagram earns its place by showing something prose cannot: topology, sequence, state, or a boundary. Restating a sentence as boxes adds load without adding information.
**Fix:** every diagram must be one of four kinds — **trust-boundary map**, **protocol sequence**, **state machine**, or **data-flow with authority annotations** — and must have ≥5 nodes or ≥4 sequence messages. Diagrams that cannot meet that become prose. Compare `1.3/lessons/01-property.md`, whose diagram carries nine nodes and two distinct authority paths.

### D7 — Unresolved forward references
**Where:** 603 occurrences of "later" across lesson files; bare module IDs like "(2.1)", "(6.6)", "(4.4)" used as citations.
**Why it matters:** "(later)" is an IOU the learner cannot redeem. A bare "2.3" is unsearchable and unlinkable, and the site renders it as plain text.
**Fix:** every cross-reference becomes a named link: `[2.3 Browser cookies and the cookie jar](../../2/2.3/lessons/01-property.md)`. Every "(later)" either (a) names the module that resolves it, or (b) is deleted. A forward reference with no destination is a defect, not a teaser.

### D8 — Labs are predicates, not systems
**Where:** `labs/**`. 23 labs have exactly 2 tests; 18 have 3. Most `vulnerable/*.py` files are 2–8 lines. Grep across all of `labs/`: **0** Kotlin files, **0** database drivers, 3 incidental FastAPI mentions.
**Why it matters:** the declared learning environment is FastAPI + PostgreSQL + Next.js + Android/Kotlin. A two-line pure function cannot exhibit the failures the course is about — authority resolved across a boundary, state mutated between check and use, a parser disagreeing with a consumer, a cache keyed without a tenant. Learners get a unit-test kata and no transfer.
**Why it is still partly right:** determinism, speed, isolation, and resettability are real virtues and must survive the upgrade.
**Fix:** tiered. See §10.

### D9 — Assessment has no items
**Where:** `content/modules/*/*/assessment/rubric.md` (57 files, all ~175–185 words); `site/lib/assessment.ts`.
**Evidence:** 53 rubrics state that knowledge-check items "live in the session worksheet" — no such worksheet exists. The site's seven prompts in `assessment.ts` are **identical for all 57 modules**; only the hints vary, and those are pulled from `module.yaml`.
**Why it matters:** blueprint §10 promises mastery gates with four states and non-compensating evidence. What exists is a checklist plus seven generic prompts. Learners cannot self-assess, and the mastery-gate model is unimplementable.
**Fix:** per module, author 6–10 module-specific items with answers and distractor rationales in the isolated key. See §11.

### D10 — Render-time rewriting makes the source not the product
**Where:** `site/lib/plainCopy.ts` — 1,333 lines, ~583 regex/replace operations.
**Evidence:** heading maps (`"Non-goals" → "What this page is not doing"`), vocabulary substitutions (`invariant → rule`, `TCB → what you trust`, `pytest → the check`, `Phase N → part N`), whole-sentence rewrites, and repair regexes that patch damage done by earlier substitutions (`"Build the the notes app " → "Build the notes app "`).
**Why it matters, in three ways:**
  - *Reviewability:* `quality-gate` reviews `content/`, but learners read the transformed output. The reviewed artifact is not the shipped artifact.
  - *Fragility:* 583 ordered regexes over authored prose is a compounding bug source, and the file already carries repair passes for its own collisions.
  - *Pedagogy:* suppressing `XSS`, `CSP`, `invariant`, and `attack surface` leaves readers unable to search, read a standard, or speak in a design review. The circumlocutions are frequently *harder* than the terms — "a content-security header in report-only mode" is worse than "CSP in Report-Only mode".
**Fix:** move plain language into the source. Author the dual form once — *"a security invariant (a rule that must stay true)"* — in `content/`, then delete the corresponding rule from `plainCopy.ts`. Target: `plainCopy.ts` under 150 lines, retaining only structural normalization (mark stripping, heading casing), no vocabulary or sentence rewrites.

### D11 — Standards traceability invisible to the learner
**Where:** only **19 of 456** lesson files carry a `**Standards:**` line; the rest keep `standardsRefs` in `module.yaml` only, which the lesson page does not render.
**Why it matters:** blueprint §16.4 requires current canonical standards with maturity labels *in the lesson*. Traceability that only a build script can see does not teach.
**Fix:** every `01-property.md` and every `05-verify.md` carries a `**Standards:**` line with exact identifiers, version, and status, matching `module.yaml`. A linter check enforces that they agree.

### D12 — Metadata overstates maturity
**Where:** `content/modules/*/*/module.yaml`.
**Evidence:** 53 of 57 carry `reviewer: pending independent quality and lab-safety review` while also carrying `lastReviewedAt: '2026-08-24'` and `nextReviewAt: '2027-02-24'`. 21 modules carry fully templated outcomes (`Demonstrate: <module title>` plus four boilerplate lines shared verbatim). 47 modules claim `estimatedMinutes: 240` for ~460-word lessons and a 2-line lab.
**Why it matters:** a review date with no review is the one thing the repo's own governance model exists to prevent. Templated outcomes are not outcomes — they cannot be assessed, so §7's coverage contract cannot be built from them.
**Fix:** clear `lastReviewedAt`/`nextReviewAt` wherever `reviewer` is `pending`; rewrite the 21 templated outcome blocks as observable behaviours; recompute estimates from actual content (see §11 formula).

### D13 — Governance is unenforced
**Where:** no `.github/` directory — there is no CI. Lab entry points are inconsistent: `labs/1.1/1.1-invariant-catalogue` uses `--claim` while the other 56 use `--impl`. Lab directory naming is inconsistent (`1.1-invariant-catalogue`, `1.2-authority-matrix`, `1.3-trust-boundaries` vs `<id>-lab`). `content/glossary/` is empty while the site hardcodes 30 terms in `site/lib/glossary.ts`.
**Why it matters:** every rule in this plan degrades without a mechanical check. The quality bar already exists on paper and was not met.
**Fix:** ship the linter and CI in W0 *before* bulk authoring, so every workhorse gets fast feedback.

### D14 — The capstone does not integrate
**Where:** `content/modules/11/**`, `labs/11/11-lab/`.
**Evidence:** `estimatedMinutes: 1200`, ~4,068 lesson words, an 18-line fixed implementation, one in-memory revocation predicate.
**Why it matters:** the capstone is the course's proof that the parts compose. As built, it is a 58th narrow module.
**Fix:** last workstream (W8), after enough phases are deep enough to integrate.

---

## 5. Workstreams and dependency order

| ID | Workstream | Depends on | Output |
|---|---|---|---|
| **W0** | Enforcement scaffolding: content linter + CI + lab runner | — | `scripts/lint_content.py`, `scripts/run_labs.sh`, `.github/workflows/content.yml` |
| **W1** | Source-side plain language; shrink `plainCopy.ts` | W0 | dual-form vocabulary in `content/`, `plainCopy.ts` ≤150 lines |
| **W2** | Metadata honesty pass (D12) | W0 | 57 corrected `module.yaml` |
| **W3** | Pilot deepening: 3 modules end to end | W0–W2 | 3 modules at 1.3 quality + 3 review artifacts |
| **W4** | Assessment system (D9) | W3 | item banks + isolated keys + site rendering |
| **W5** | Lab realism tiers (D8) | W3 | tiered lab upgrades |
| **W6** | Bulk deepening, phase by phase | W3–W5 | 54 modules |
| **W7** | Glossary and cross-reference integrity (D7, D13) | W1 | `content/glossary/terms.yaml`, linked references |
| **W8** | Capstone rebuild (D14) | W6 for phases 1–10 | integrating capstone |

**Critical path:** W0 → W3 → W6. W1, W2, W4, W5, W7 can run in parallel with W6 once the pilot has validated the runbook.

**Do not start W6 until the W3 pilot has passed independent review.** The entire current state of the repository is what happens when a template is applied 54 times before anyone checks whether the template teaches.

---

## 6. W0 — Enforcement scaffolding (build this first)

### 6.1 `scripts/lint_content.py`

Pure-Python, stdlib + PyYAML only. Exit non-zero on any ERROR. Emit `file:line: [RULE] message`.

| Rule | Level | Check |
|---|---|---|
| `L001` | ERROR | Lesson body (excluding code fences and tables) has ≥900 words. |
| `L002` | ERROR | Fewer than 8% of sentences are ≤5 words. |
| `L003` | ERROR | Median sentence length ≥11 words. |
| `L004` | ERROR | No heading text appears in more than 20 lesson files repo-wide, except `## Practice` and `## Check yourself`. |
| `L005` | ERROR | Every Mermaid block has ≥5 node declarations or ≥4 sequence messages. |
| `L006` | ERROR | The string "later)" or "(later" does not appear without an adjacent module-ID link. |
| `L007` | ERROR | Every bare module-ID citation matching `\(\d+\.\d+\)` or `\(E\d\)` is instead a Markdown link. |
| `L008` | ERROR | At most one authorized-scope sentence per lesson (match on "Do not" + target nouns). |
| `L009` | ERROR | `01-property.md` and `05-verify.md` carry a `**Standards:**` line whose identifiers are a subset of `module.yaml` `standardsRefs[].requirementIds`. |
| `L010` | ERROR | No ASVS 4.x ID pattern (`v4\.`), no `MASVS-L[12]`, no `MASVS-R`. |
| `L011` | ERROR | Lesson files contain no answer text; the words "answer key", "intended findings", "expected answer" appear only under `content/assessment/keys/`. |
| `L012` | ERROR | `module.yaml` validates against `content/schema/module.schema.json`. |
| `L013` | ERROR | If `reviewer` contains "pending", then `lastReviewedAt` and `nextReviewAt` are absent. |
| `L014` | ERROR | No outcome begins with `Demonstrate:` followed by the module title. |
| `L015` | ERROR | Every relative Markdown link resolves to an existing file. |
| `L016` | WARN | Lesson has ≥1 worked example (a fenced non-Mermaid block with surrounding prose ≥60 words) and ≥1 explicit counterexample. |
| `L017` | WARN | `estimatedMinutes` within ±25% of the §11 formula. |

Thresholds L001–L003 are calibrated against `1.2`/`1.3` (which pass) and the current 54 (which fail). Do not relax them; raising a number to make a file pass is a defect, not a fix.

### 6.2 `scripts/run_labs.sh`

Single entry point. For each `labs/*/*/conftest.py`: install `requirements.txt` if present, run vulnerable (must fail) and fixed (must pass), print a matrix, exit non-zero on any anomaly. Also normalizes the D13 inconsistency: migrate `labs/1.1/1.1-invariant-catalogue` to `--impl`, or teach the runner both flags and open a follow-up to converge. Prefer converging.

Known baseline on this commit: all pairs behave correctly except `labs/5.2/5.2-lab`, which needs `pip install -r labs/5.2/5.2-lab/requirements.txt` first. The runner must install before asserting.

### 6.3 `.github/workflows/content.yml`

On push and PR: `python scripts/lint_content.py`, `bash scripts/run_labs.sh`, `npm --prefix site ci && npm --prefix site run lint && npm --prefix site run build`, plus a grep asserting `site/out` contains no `assessment/keys` path.

**Acceptance for W0:** the workflow runs green on a branch where the three reference modules are the only ones linted, and reports the expected large failure count when pointed at the other 54.

---

## 7. The per-module deepening runbook

This is the core procedure. One module per unit of work. Estimated 3–6 hours of model time per module.

**Step 0 — Set up.** Branch `deepen/<module-id>`. Read, in order: `secure-application-engineering-curriculum-blueprint.md` §§3, 9, 10, 16; `content/modules/<phase>/<id>/spec.md`; `module.yaml`; all eight lessons; `labs/<id>/**`; `content/modules/<phase>/<id>/assessment/rubric.md`; `content/assessment/keys/<id>.md`; `content/standards/pins.yaml`; and **both** `content/modules/1/1.3/lessons/01-property.md` and `02-model.md` as the quality reference. A directory listing is not reading.

**Step 1 — Pin standards.** Run `standards-pin`. Verify every `requirementIds` entry still exists at the pinned version and that `status` is accurate. Record `reviewedAt`. If a standard moved, write a migration note in the changelog. Do not proceed on a stale pin.

**Step 2 — Write the teaching claims (fixes D3).** In `spec.md`, replace the single implicit predicate with **three to five numbered teaching claims**, ordered by dependency. Each claim is one falsifiable sentence about the reference system, in the form: *"For `<asset>` in `<system at this phase>`, `<actor with these capabilities>` cannot `<effect>` because `<the check that must hold>`; if `<context>` is missing, the answer is no."*

Worked example for `4.3 Sessions, cookies, and tokens`, which currently teaches only claim 1:

1. A session secret placed in a URL is no longer a secret, because the URL is copied into access logs, `Referer`, history, and screenshots.
2. A session identifier must be unguessable *and* bound to the authentication event that minted it, so a pre-authentication identifier cannot survive login (fixation).
3. A session must have both an idle and an absolute lifetime, because an unbounded session converts a one-time theft into permanent access.
4. Logout and revocation must invalidate server-side state, because a token the server still honours is not revoked.
5. `HttpOnly`, `Secure`, and `SameSite` each defend a different attacker capability, and naming one does not cover the others.

Then map each claim to loop steps and to at least one lab assertion. **At least two claims must be exercised by the lab.** A claim with no assessment item and no lab assertion is not taught — either build the evidence or delete the claim.

**Step 3 — Build the coverage contract.** A table in `spec.md`: one row per outcome in `module.yaml`, with columns *explanation file*, *worked example*, *practice*, *assessment item ID*, *transfer task*. Any empty cell is a blocker (this is `quality-gate` step 2, made explicit and reviewable).

**Step 4 — Rewrite the eight lessons.** Follow §8 for shape and §9 for style. Rewrite; do not patch. The existing files are template fills and are cheaper to replace than to repair.

**Step 5 — Upgrade the lab.** Follow §10. Tier assignment comes from §10.4.

**Step 6 — Author the assessment.** Follow §11.

**Step 7 — Correct metadata.** Rewrite templated outcomes as observable behaviours ("Given a session parser, identify which of four channels can carry a session secret and justify the ranking" — not "Demonstrate: Sessions, cookies, and tokens"). Recompute `estimatedMinutes`. Add a changelog entry naming the defect IDs fixed. Leave `reviewer`, `lastReviewedAt`, `depth`, and `quality` untouched.

**Step 8 — Validate.** `python scripts/lint_content.py content/modules/<phase>/<id>`, then the lab pair in a clean environment, then `npm --prefix site run build`. Paste exact commands and output into the review request.

**Step 9 — Request independent review.** A *different* agent/session runs `quality-reviewer` and, for executable labs, `lab-safety-reviewer`. It scores all twelve dimensions of `.cursor/skills/quality-gate/references/publishability.md` with cited passages, and writes `content/progress/reviews/<id>-<YYYY-MM-DD>.md` including the reviewed commit, files inspected, per-dimension scores, blockers, lab commands and results, reviewer identity, and an independence statement.

**Step 10 — STATUS.** Only after review passes, and only by the reviewing agent or the human: update `content/progress/STATUS.yaml` and `module.yaml` `reviewer`/`lastReviewedAt`.

---

## 8. Target shape of each lesson

All eight files carry the existing frontmatter (`**Kind:**`, `**Loop step:**`) plus, for `01` and `05`, `**Standards:**`. Word targets are floors, not ceilings. Headings are *descriptions of the content*, not the fixed vocabulary listed below — the bracketed labels say what the section does.

**`01-property.md` — Property (concept-model, 1,200–2,000 words).** Open with the falsifiable sentence from Step 2, claim 1. Then: unpack every clause of that sentence and say what would make it false. Define each technical term on first use in dual form. One trust-boundary diagram (≥5 nodes). Name what must be trusted *for this claim*, and show that the list changes if the claim changes. State the attacker's capabilities explicitly and the ones deliberately excluded. Close with the remaining claims previewed by name, with links.

**`02-model.md` — Model (design-exercise, 1,200–2,000 words).** Actors, principals, components, channels, entry points, boundaries — as a table with a *precise question* column and a *this system, this phase* column, exactly as `1.3/lessons/02-model.md` does. Then two worked discriminations: one place that looks like a boundary and is not, one that does not look like one and is. State, time, and concurrency: what can change between check and use. One diagram (state machine or authority-annotated data flow).

**`03-break.md` — Break (mechanism-lab, 900–1,500 words).** The representative failure, derived not announced: preconditions, the exact step where authority or grammar or state goes wrong, and the blast radius. **One** authorized-scope sentence, placed before the first command. Name the failing test and what its failure means. Explain why this is the *smallest* representative failure — what was deliberately left out and why. No payloads.

**`04-build.md` — Build (design-exercise, 1,000–1,600 words).** Derive the fix from the property rather than presenting it. Compare **two** candidate mechanisms honestly, including one that a competent engineer would reasonably propose, and say precisely where the weaker one breaks. State where the chosen mechanism itself stops working. Separate framework default from application guarantee with a concrete example of the default being insufficient.

**`05-verify.md` — Verify (verification-lab, 900–1,500 words).** Normal, negative, abuse, and failure cases, each with the observation that distinguishes pass from pass-for-the-wrong-reason. Explain the oracle: *why* this assertion catches the forbidden outcome and what a green suite still does not prove. `**Standards:**` line with exact identifiers.

**`06-operate.md` — Operate (operations-exercise, 900–1,400 words).** Signal design (fields that are useful without becoming a second leak — say which field is omitted and why), alert threshold and its false-positive cost, the human who receives it, containment, revocation, recovery, and the accessibility of any human-in-the-loop path. Model operator failure as residual risk.

**`07-transfer.md` — Transfer (transfer-challenge, 900–1,500 words).** Change an asset, actor, authority relation, boundary, state transition, or time horizon — **not** product nouns. State explicitly which original claims survive, which break, and why. No step-by-step scaffold; give success criteria instead. Current transfer tasks mostly swap "notes app" for "clinic" while keeping every assumption — that is a rename, not a transfer.

**`08-review.md` — Code review (code-review, 900–1,400 words).** A realistic diff (10–40 lines, in `labs/<id>/review/`) containing 3–5 seeded issues of differing severity, at least one of which is a *non-issue* that looks like an issue. Teach the reading order — where authority is resolved, where state changes, where data crosses a grammar — rather than listing what to find. Findings stay in the key.

---

## 9. Style rules (the D1/D2/D5 fix, in mechanical form)

1. **Every paragraph is ≥3 sentences and connected.** No standalone noun phrases as paragraphs.
2. **Derive before you assert.** A rule sentence is preceded by the mechanism that makes it necessary. Ban the shape "X is not Y." unless the next sentence explains what X actually is.
3. **Define on first use, then use the real term.** `cross-site scripting (XSS)`, then `XSS`. `Content-Security-Policy (CSP)`, then `CSP`. `security invariant (a rule that must stay true)`, then `invariant`. Never invent a circumlocution to avoid a term the industry uses; the reader needs the word to read a standard, search, or pass an interview.
4. **One scope statement per lesson**, immediately before the first command, in the form given in D5.
5. **At most three rejected alternatives**, each a full sentence with a reason.
6. **Every cross-reference is a titled link.** No bare `(2.3)`, no unanchored "later".
7. **Tables carry data, not prose.** The "Slice | For this rule" table that appears across dozens of lessons is a template artifact: move the causal chain into prose and keep tables for genuine comparisons (channel × property, actor × capability, standard × requirement).
8. **No sentence whose meaning depends on repository jargon a first-time reader has not met** — "cell", "grain", "sticker", "oracle" all currently appear undefined.

---

## 10. Lab realism tiers (D8)

Keep what works: local, synthetic, deterministic, resettable, vulnerable-fails/fixed-passes.

**Tier 1 — Predicate (current state).** Keep only where the property genuinely *is* a pure function (encoding, comparison, parsing a single value). Minimum raised to **5 tests**: normal, forbidden outcome, boundary, malformed input, and one test that fails if the fix is faked (e.g. a hard-coded allow-list that passes the happy path).

**Tier 2 — Component (the new default).** A small FastAPI app with a real request/response cycle, an SQLite or Postgres-backed store, session or token state, and tests that drive it through `httpx`/`TestClient`. This is where authority-across-a-boundary, check-then-use races, and parser/consumer disagreements can actually be shown. Target: 60–200 LOC per variant, 6–10 tests. Use for phases 3–7, 9, 10 and most electives.

**Tier 3 — Cross-component (selected).** Two or more processes or layers: API + worker + queue, API + database with row-level policy, app + cache, mobile client + backend. Reserve for one module per phase plus the capstone. This is where the "residuals" currently listed in `STATUS.yaml` (retries, webhook races, cache copies, GraphQL aliases) become teachable.

**Mobile (phase 8).** Currently zero Kotlin. Either author real Kotlin/JVM fixtures with Gradle and unit tests, or — if the toolchain cost is unacceptable — state that decision explicitly in `STATUS.yaml` and relabel phase 8 as analysis-only. The current position, claiming an Android/Kotlin track with Python fixtures, is the one thing that must not persist.

**Tier assignment rule:** a module is Tier 1 only if a reviewer can argue the property is genuinely a pure function. Default to Tier 2.

**Specific correction:** `labs/1.1/1.1-invariant-catalogue` uses `--claim` where all 56 others use `--impl`, and three labs use non-`<id>-lab` directory names. Converge both in W0.

---

## 11. Assessment system (D9)

Per module, create `content/modules/<phase>/<id>/assessment/items.md` (learner-facing) and extend `content/assessment/keys/<id>.md` (examiner).

**Item bank, 6–10 items per module, module-specific:**
- 2–3 **discrimination** items: given four candidate statements, identify which is the property and which are mechanisms, with a written justification.
- 2–3 **diagnosis** items: given a short code or config excerpt, name the root cause, the preconditions, and the impact — distinct from each other.
- 1–2 **design** items: choose between two mechanisms under a stated constraint and defend the trade-off.
- 1 **transfer** item: the §8 `07-transfer` scenario with success criteria.
- 1 **operate** item: write the signal and the recovery step.

**In the key,** for each item: the expected answer, the *reason each distractor is attractive*, and the four-state banding (not attempted / developing / competent / transfer-ready) with a concrete example of each band. Distractor rationales are the part that makes an item teach rather than test.

**Rubrics:** rewrite all 57 to describe module-specific evidence and delete the 53 references to the non-existent "session worksheet".

**Site:** `site/lib/assessment.ts` currently synthesizes seven identical prompts for every module. Change it to load `items.md` when present and fall back to the generic prompts only for modules not yet converted. Keys stay unlinked; verify with the `site/out` grep in CI.

**`estimatedMinutes` formula (D12):** `reading_words / 200` + `lab_minutes` (Tier 1: 45, Tier 2: 120, Tier 3: 240) + `assessment_items × 12` + `transfer_task: 60`, rounded to the nearest 30. For a deepened Tier-2 module this lands near 240–300, which makes the current 240 honest *after* the work rather than before it.

---

## 12. Batching and sequencing

Dependency order matters: later modules cite earlier ones, so deepening out of order creates links into shallow pages.

| Batch | Modules | Rationale |
|---|---|---|
| **B0 (pilot, W3)** | `1.4`, `2.1`, `4.3` | One per difficulty class: a phase-1 module adjacent to the reference, a mechanics module, and a module whose narrowness is well understood. Validates the runbook before scale. |
| **B1** | `0.1`, `0.2`, `1.1` | Orientation and the one reference module below bar. `1.1` at 566 words/lesson does not meet the bar it is cited as setting. |
| **B2** | `2.2`–`2.4`, `3.1`–`3.4` | Mechanics and design; heavy downstream citation. |
| **B3** | `4.1`–`4.5` | Identity. `4.5` needs the PKCE/`state` correction carried through all eight lessons, not just `01-property.md`. |
| **B4** | `5.1`–`5.5` | Data protection. `5.2` already has a real AEAD fixture — use it as the Tier-2 template. |
| **B5** | `6.1`–`6.7` | Vulnerability families. Highest payoff from naming XSS/CSRF/SSRF/SQLi directly (D10). |
| **B6** | `7.1`–`7.4`, `9.1`–`9.5` | APIs and verification. |
| **B7** | `8.1`–`8.5` | Mobile — blocked on the Kotlin decision in §10. |
| **B8** | `10.1`–`10.5` | Supply chain, cloud, operations. |
| **B9** | `E1`–`E6` | Electives. |
| **B10 (W8)** | `11` | Capstone, after B1–B8. |

**Parallelism:** up to four workhorses, one module each, never two modules in the same batch that cite each other. Each finishes with an independent review by a *different* agent. Batch closes when every module in it has a passing review artifact.

**Stop conditions:** if two consecutive modules in a batch fail independent review on the same dimension, halt the batch and fix the runbook or the linter rule instead of continuing.

---

## 13. Definition of done

**Per lesson:** passes L001–L015; at least one worked example and one counterexample; every cross-reference is a titled resolving link; exactly one scope statement; every diagram is one of the four kinds with ≥5 nodes; every term defined on first use in dual form.

**Per module:** coverage contract has no empty cells; 3–5 teaching claims, each with a lab assertion or an assessment item; lab at its assigned tier with the minimum test count; item bank with distractor rationales in the isolated key; `estimatedMinutes` from the formula; changelog entry naming defect IDs; **a dated independent review artifact under `content/progress/reviews/`**; STATUS updated only by the reviewer.

**Repo-wide (end state):** `plainCopy.ts` ≤150 lines with no vocabulary rewrites; `content/glossary/terms.yaml` is the single glossary source and `site/lib/glossary.ts` reads it; CI green; every `module.yaml` with a pending reviewer carries no review date; zero bare module-ID citations; zero unresolved "later".

**Tracking metrics** (report after each batch): median lesson words; % sentences ≤5 words; count of headings appearing in >20 files; mean tests per lab; count of Tier-2/3 labs; modules with item banks; modules with review artifacts; `plainCopy.ts` line count.

---

## 14. Explicit non-goals

- Do not redesign the seven-step loop, the phase order, or the property-first thesis. They are the repository's strongest asset.
- Do not reorganize around OWASP Top 10 or CWE Top 25.
- Do not remove the safety discipline. D5 reduces *repetition*, not rigor.
- Do not add length without derivation. L001 is a floor to make room for reasoning; padding a lesson to 900 words is the same defect in a new form.
- Do not mark anything publishable from an authoring session.

---

## 15. Immediate next actions

1. Build W0 (`scripts/lint_content.py`, `scripts/run_labs.sh`, `.github/workflows/content.yml`) and calibrate thresholds against `1.2`/`1.3`.
2. Run W2 (metadata honesty) — mechanical, low risk, and it removes the false review dates immediately.
3. Run the B0 pilot on `1.4`, `2.1`, `4.3` using §7, one module per session, each independently reviewed.
4. Decide the phase-8 Kotlin question and record it in `content/progress/STATUS.yaml`.
5. Only then open W6.
