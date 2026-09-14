# Model capability evidence separately from security evidence

**Kind:** design-exercise
**Loop step:** 2 Model

Use a boolean map for demonstrated tooling capabilities. Missing or unknown values are gaps:

```text
{"python": True, "browser": False, "sql": True, "network": False, "git": False}
→ ["bridge-browser", "bridge-network", "bridge-git"]
```

| Record | May change? | Must remain separate |
|---|---|---|
| tooling evidence | bridge assignment | 1.2/1.3/1.4 cells |
| quiz percentage | orientation pacing | Gate 1 evidence |
| bridge id | practice queue | authorization decision |

The model is useful because another reviewer can reproduce the path from the same evidence map. A badge, title, or green LMS tile is not a 1.2 allow cell.

The bridge ids are real local tasks: [Python test](/bridges/bridge-python/), [browser request](/bridges/bridge-browser/), [SQL reading](/bridges/bridge-sql/), [HTTP trace](/bridges/bridge-network/), and [Git inspection](/bridges/bridge-git/). Choose only the gaps your evidence shows; all security modules and Gate 1 still remain required.

## Practice

Mark which capabilities are actually demonstrated in `labs/0.2/0.2-bridge`, then predict the bridge list before running tests.
