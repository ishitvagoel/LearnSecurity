---
name: content-lint
description: Build, run, and interpret the mechanical content quality gate (scripts/lint_content.py and scripts/run_labs.sh). Use before requesting review, when CI fails a content check, or to implement W0.
---

# Content lint

Every rule in this repository's quality bar already existed on paper before 54 modules failed to meet it. Prose rules that nothing checks decay. This skill owns the mechanical gate.

## When to use

- Before handing a module to independent review (`deepen-module` step 8)
- CI failed a content check and you need to read the output
- The scripts do not exist yet and you are implementing **W0**

## The scripts

| Script | Purpose |
|---|---|
| `scripts/lint_content.py` | Rules `L001`–`L017` over `content/` |
| `scripts/run_labs.sh` | Vulnerable-fails / fixed-passes matrix over `labs/` |

Full rule specification, with thresholds and rationale: [`references/lint-rules.md`](references/lint-rules.md).

## Running

```bash
python scripts/lint_content.py                              # whole tree
python scripts/lint_content.py content/modules/4/4.3        # one module
python scripts/lint_content.py --rules L001,L002,L003       # one family
bash scripts/run_labs.sh
bash scripts/run_labs.sh 4.3
```

Exit non-zero on any `ERROR`. `WARN` is advisory and does not block.

## Implementing W0

Build `scripts/lint_content.py` as stdlib + PyYAML only, no third-party linters. Output `path:line: [RULE] message`, one finding per line, sorted by path. Support `--rules`, a path argument, and `--json` for CI annotation.

Build `scripts/run_labs.sh` to, for each `labs/*/*/conftest.py`: install `requirements.txt` when present, run the vulnerable variant (must fail) and the fixed variant (must pass), print a matrix, and exit non-zero on any anomaly. It must install before asserting — `labs/5.2/5.2-lab` needs `cryptography` and otherwise reports six errors that look like failures but are not.

Two known inconsistencies the runner must handle or fix: `labs/1.1/1.1-invariant-catalogue` takes `--claim` where the other 56 take `--impl`, and three phase-1 labs use non-`<id>-lab` directory names. Prefer converging both over teaching the runner two dialects.

### Calibration

Thresholds are set so that `content/modules/1/1.2` and `content/modules/1/1.3` pass and the other 54 modules fail. **Verify this before trusting the linter.** A threshold that passes everything is measuring nothing.

```bash
python scripts/lint_content.py content/modules/1/1.2   # expect: clean
python scripts/lint_content.py content/modules/1/1.3   # expect: clean
python scripts/lint_content.py content/modules/6       # expect: many ERRORs
```

Expected baseline on the pre-deepening tree: ~16% of sentences outside modules 1.2/1.3 are ≤5 words, 446 files share the heading `## Use it somewhere new`, 59 Mermaid blocks have ≤3 nodes, 603 unresolved "later" references, and 19 of 456 lessons carry a `**Standards:**` line. If your implementation does not find roughly these, it has a bug.

## Interpreting output

The linter is **necessary, not sufficient**. It cannot tell whether 900 words carried reasoning or restated the claim nine times — that is the reviewer's job, and `L001` exists to make room for reasoning, not to certify it.

Never raise a threshold to make a file pass. If a rule is wrong, argue it in the review artifact and change it deliberately for the whole repository; a local exemption is how a bar becomes a suggestion.
