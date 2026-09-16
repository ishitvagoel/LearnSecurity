# Lint rules

`ERROR` blocks CI and blocks a review request. `WARN` is advisory.

All prose measurements exclude fenced code blocks, Mermaid blocks, table rows, headings, and frontmatter lines. Sentences split on `[.!?]` followed by whitespace.

| ID | Level | Scope | Check | Why |
|---|---|---|---|---|
| `L001` | ERROR | lesson | Body prose ≥900 words | ~460 words cannot carry a derivation, a worked example, a counterexample, limits, and a transfer task — so the authoring pass wrote labels for them instead |
| `L002` | ERROR | lesson | <8% of sentences are ≤5 words | 16% today outside modules 1.2/1.3; fragments assert conclusions the reader cannot re-derive |
| `L003` | ERROR | lesson | Median sentence length ≥11 words | 9 words today, 12 in the reference modules |
| `L004` | ERROR | repo | No heading text appears in >20 lesson files, except `## Practice` and `## Check yourself` | `## Use it somewhere new` appears in 446 of 456 files; identical scaffolding forces content into cells where it does not fit |
| `L005` | ERROR | lesson | Every Mermaid block has ≥5 node declarations or ≥4 sequence messages | 59 blocks have ≤3 nodes and restate the sentence above them |
| `L006` | ERROR | lesson | No `(later` or `later)` without an adjacent module-ID link | 603 occurrences; an IOU the reader cannot redeem |
| `L007` | ERROR | lesson | No bare module-ID citation matching `\(\d+\.\d+\)` or `\(E\d\)` — must be a Markdown link | Unsearchable, unlinkable, renders as plain text |
| `L008` | ERROR | lesson | At most one authorized-scope sentence per lesson | Four in ~450 words in `7.2/03-break.md`; crowds out teaching and trains skimming |
| `L009` | ERROR | lesson | `01-property.md` and `05-verify.md` carry a `**Standards:**` line whose identifiers are a subset of `module.yaml` `standardsRefs[].requirementIds` | 19 of 456 lessons carry one; traceability only a build script can see does not teach |
| `L010` | ERROR | any | No `v4\.` ASVS pattern, no `MASVS-L[12]`, no `MASVS-R` | `AGENTS.md` forbids mixing standard generations |
| `L011` | ERROR | `content/modules/**` | "answer key", "intended findings", "expected answer" appear only under `content/assessment/keys/` | Key isolation |
| `L012` | ERROR | `module.yaml` | Validates against `content/schema/module.schema.json` | Existing bar |
| `L013` | ERROR | `module.yaml` | If `reviewer` contains "pending", `lastReviewedAt` and `nextReviewAt` are absent | 53 modules assert a review date for a review that did not happen |
| `L014` | ERROR | `module.yaml` | No outcome begins with `Demonstrate:` followed by the module title | 21 modules; not an outcome, so it cannot be assessed |
| `L015` | ERROR | any Markdown | Every relative link resolves to an existing file | |
| `L016` | WARN | lesson | ≥1 worked example (a fenced non-Mermaid block with ≥60 words of surrounding prose) and ≥1 explicit counterexample | Publishability dimension "worked reasoning" |
| `L017` | WARN | `module.yaml` | `estimatedMinutes` within ±25% of the `metadata-honesty.mdc` formula | 47 modules claim 240 minutes for a two-line lab |

## Rules deliberately not mechanized

These are reviewer judgement and must not be faked with a regex:

- whether derivation precedes assertion;
- whether the two compared mechanisms in `04-build.md` are both plausible;
- whether the transfer task changed an assumption or only a noun;
- whether a diagram shows topology, sequence, or state rather than restating prose; and
- whether the word floor carried reasoning or padding.

Do not add heuristics for these. A weak automated proxy for a judgement call produces false confidence, which is worse than an honest gap.
