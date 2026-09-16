---
name: content-lint
description: Build, run, and interpret the mechanical content quality gate (scripts/lint_content.py and scripts/run_labs.sh). Use before requesting review, when CI fails a content check, or to implement W0.
---

# Content lint

Every rule in this repository's quality bar already existed on paper before 54 modules failed to meet it. Prose rules that nothing checks decay. This skill owns the mechanical gate.

## When to use

- Before handing a module to independent review (`deepen-module` step 8)
- CI failed a content check and you need to read the output
- A rule looks wrong and you are considering changing a threshold

## The scripts

| Script | Purpose |
|---|---|
| `scripts/lint_content.py` | Rules `L001`–`L017` over `content/` |
| `scripts/run_labs.sh` | Vulnerable-fails / fixed-passes matrix over `labs/` |

Full rule specification, with thresholds and rationale: [`references/lint-rules.md`](references/lint-rules.md).

## Running

```bash
python scripts/lint_content.py                              # whole tree, ratcheted
python scripts/lint_content.py content/modules/4/4.3        # one module
python scripts/lint_content.py --rules L001,L002,L003       # one family
python scripts/lint_content.py --no-baseline                # the true total
python scripts/lint_content.py --json                       # machine-readable
bash scripts/run_labs.sh                                    # all 57 labs
bash scripts/run_labs.sh 4.3 5.2                            # named modules
```

Exit non-zero on any `ERROR`. `WARN` is advisory and does not block.

Repo-level rules (`L004`, heading reuse) run only on a full-tree lint — "is this heading a template artifact?" is not a per-file question, and attributing it to one module would blame it for what 445 other files did.

## The baseline ratchet

2,419 findings exist on the pre-deepening tree, so `scripts/lint_content.py` runs against `scripts/lint_baseline.json` and reports only **new or regressed** findings. CI separately fails if the committed baseline is stale.

After deepening a module, regenerate it and confirm the count fell:

```bash
python scripts/lint_content.py --update-baseline
git diff --stat scripts/lint_baseline.json
```

**Never add a finding to the baseline to make a deepened module pass.** The baseline is for work not yet done, not for work done badly.

## Calibration

The thresholds were set from measurement, not guessed. On the pre-deepening tree:

| Signal | Reference (1.2, 1.3) | The other 54 |
|---|---|---|
| Sentences ≤5 words | 7% median, 11% worst | 19% median, 56% worst |
| Median sentence length | 11–12 words | 8 words |
| Lessons below the 900-word floor | 2 of 16 | 440 of 440 |

`L002` sits at 12%: it flags **none** of the reference modules and 78% of the rest.

Re-verify after any threshold change. A threshold that passes everything measures nothing; one that fails the reference teaches workhorses to degrade good writing.

```bash
python scripts/lint_content.py content/modules/1/1.2 content/modules/1/1.3 --no-baseline
python scripts/lint_content.py content/modules/4/4.3 --no-baseline   # expect ~33 errors
```

Two known findings remain on the reference: `1.2/03-break.md` (892 words) and `1.2/08-review.md` (715) sit below the 900-word floor. Both are carried in the baseline. The reference modules are the best content in the repository; they are not flawless, and the linter says so rather than bending to them.

## Known lab inconsistencies

`labs/1.1/1.1-invariant-catalogue` takes `--claim` where the other 56 take `--impl`, and three phase-1 labs use non-`<id>-lab` directory names. `run_labs.sh` handles both dialects today; converging them is queued in `lab-realism.mdc`.

## Interpreting output

The linter is **necessary, not sufficient**. It cannot tell whether 900 words carried reasoning or restated the claim nine times — that is the reviewer's job, and `L001` exists to make room for reasoning, not to certify it.

Never raise a threshold to make a file pass. If a rule is wrong, argue it in the review artifact and change it deliberately for the whole repository; a local exemption is how a bar becomes a suggestion.
