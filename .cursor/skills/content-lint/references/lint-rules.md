# Lint rules

`ERROR` blocks CI and blocks a review request. `WARN` is advisory.

All prose measurements exclude fenced code blocks, Mermaid blocks, table rows, headings, and frontmatter lines. Sentences split on `[.!?]` followed by whitespace.

| ID | Level | Scope | Check | Why |
|---|---|---|---|---|
| `L001` | ERROR | lesson | Body prose ≥900 words | ~460 words cannot carry a derivation, a worked example, a counterexample, limits, and a transfer task — so the authoring pass wrote labels for them instead |
| `L002` | ERROR | lesson | <12% of sentences are ≤5 words | Measured: reference modules top out at 11%, the rest run 19% median and 56% worst. 12% flags none of the reference and 78% of the rest |
| `L003` | ERROR | lesson | Median sentence length ≥11 words | 9 words today, 12 in the reference modules |
| `L004` | ERROR | repo | No heading text appears in >20 lesson files, except `## Practice` and `## Check yourself` | `## Use it somewhere new` appears in 446 of 456 files; identical scaffolding forces content into cells where it does not fit |
| `L005` | ERROR | lesson | A diagram must show structure: not disconnected 2-node fragments, and not <4 nodes in a straight line. Sequence diagrams need ≥4 messages | A raw node count cannot separate a good small diagram from a bad one — `1.3/05-verify.md` earns its three nodes by branching, while `6.2/07-transfer.md` lists four labels in two disconnected pairs |
| `L006` | ERROR | lesson | No `(later` or `later)` without an adjacent module-ID link | 603 occurrences; an IOU the reader cannot redeem |
| `L007` | ERROR | lesson | No bare module-ID citation matching `\(\d+\.\d+\)` or `\(E\d\)` — must be a Markdown link | Unsearchable, unlinkable, renders as plain text |
| `L008` | ERROR | lesson | Authorized-scope sentences ≤ max(2, words/700) | The defect is a ratio: four in 380 words (`7.2/03-break.md`) crowds out teaching; three across 1,552 words does not |
| `L009` | ERROR / WARN | lesson | A `**Standards:**` line whose identifiers are a subset of `module.yaml` `standardsRefs[].requirementIds`. ERROR on `01-property.md`, WARN on `05-verify.md` | 19 of 456 lessons carry one. `01-property` is calibrated — reference module 1.3 has it. `05-verify` is an improvement the reference does not yet demonstrate, so it advises rather than blocks |
| `L010` | ERROR | any | No `v4\.` ASVS pattern, no `MASVS-L[12]`, no `MASVS-R` | `AGENTS.md` forbids mixing standard generations |
| `L011` | ERROR | `content/modules/**` | "answer key", "intended findings", "expected answer" appear only under `content/assessment/keys/` | Key isolation |
| `L012` | ERROR | `module.yaml` | Validates against `content/schema/module.schema.json` | Existing bar |
| `L013` | ERROR | `module.yaml` | If `reviewer` contains "pending", `lastReviewedAt` and `nextReviewAt` are absent | 53 modules assert a review date for a review that did not happen |
| `L014` | ERROR | `module.yaml` | No outcome begins with `Demonstrate:` followed by the module title | 21 modules; not an outcome, so it cannot be assessed |
| `L015` | ERROR | any Markdown | Every relative link resolves to an existing file | |
| `L016` | WARN | lesson | ≥1 worked example (a fenced non-Mermaid block with ≥60 words of surrounding prose) and ≥1 explicit counterexample | Publishability dimension "worked reasoning" |
| `L017` | WARN | `module.yaml` | `estimatedMinutes` within ±25% of the `metadata-honesty.mdc` formula | 47 modules claim 240 minutes for a two-line lab |

## Measurement conventions

These decide whether a rule measures the defect or an artifact of layout. Each was added after calibration flagged good prose in the reference modules:

- **Colon lead-ins are not sentences.** A segment ending in `:` introduces a block. Counting "Exercise the attacker ability that motivated the rule:" as a four-word fragment punishes good signposting.
- **Bullet runs rejoin.** Items ending in `;` or `,` are clauses of one sentence laid out vertically. Splitting them made `1.3/05-verify.md` read as 26% fragments when the prose is sound.
- **Bare tokens are not sentences.** A standalone path, command, or permission identifier (`membership:grant`, `labs/1.3/.../surface.py`) is a vocabulary entry. Counting them dropped `1.2/02-model.md` from 19% to 7%.
- **Inline code and fenced blocks are examples.** Neither is link-checked or prose-measured.
- **Percent-encoded link targets are decoded** before resolution, so Next.js `[id]` routes resolve.
- **A line that rejects a term is teaching against it.** `L010` and `L011` skip lines carrying a negation cue or pointing at `content/assessment/keys/`. Without this, a rubric saying "without MASVS-L1 language as the definition of security" is flagged for the thing it forbids.
- **`content/progress/**` is exempt from `L010` and `L011`** — plans and audits quote banned patterns in order to forbid them — but is still link-checked.

`L011` is a coarse guard and the negation skip can be defeated by a leak phrased as a denial. The real protection is the directory convention plus the CI grep over `site/out`.

## Baseline

2,419 findings exist on the pre-deepening tree. A gate that is red the day it lands is a gate people learn to ignore, so `scripts/lint_baseline.json` records the known findings and CI fails only on **new or regressed** ones.

```bash
python scripts/lint_content.py                    # ratcheted; what CI runs
python scripts/lint_content.py --no-baseline      # the true total
python scripts/lint_content.py --update-baseline  # after remediation lands
```

CI also fails if the committed baseline is stale, so the numbers cannot drift. **They should only ever go down.** Never add a finding to the baseline to make a deepened module pass — the baseline is for work not yet done, not for work done badly.

## Rules deliberately not mechanized

These are reviewer judgement and must not be faked with a regex:

- whether derivation precedes assertion;
- whether the two compared mechanisms in `04-build.md` are both plausible;
- whether the transfer task changed an assumption or only a noun;
- whether a diagram shows topology, sequence, or state rather than restating prose; and
- whether the word floor carried reasoning or padding.

Do not add heuristics for these. A weak automated proxy for a judgement call produces false confidence, which is worse than an honest gap.
