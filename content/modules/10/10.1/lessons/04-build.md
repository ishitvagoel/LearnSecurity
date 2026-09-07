# Require a threat-model identifier

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

A denylist of yesterday’s pull requests is not the fix. Hiding a scanner warning is not the fix. “We have CODEOWNERS” is not the fix.

The structural change is: `merge_ok` **is false unless the change has a truthy `threat_model`**. Fail-safe: a missing id is deny. Structural means that citation — not CODEOWNERS, not HIPAA training, not a maturity score.

The smallest restore for the notes app’s merge culture is: `{}` → do not merge. Do not fail open because branch protection is “on.” Do not accept “training complete” as a threat-model id. The id is **opaque** — `"TM-12"` is enough for this lab. Whether the document actually covers this change is 3.2 and 10.4.

## Picture: empty threat-model fails closed

```mermaid
flowchart TD
  Call[merge_ok] --> Tm{"threat_model truthy?"}
  Tm -->|yes| Allow[may merge]
  Tm -->|no| Deny[deny]
```

The repaired files require `bool(pr.get("threat_model"))`. Production still needs the cited model to *cover this change’s files* — citing `TM-12` that never mentions OAuth is a lying citation. Authorization surfaces remain 3.2. An extra advanced row about documenting a dangerous function is a reason to *require* a threat model. It is not this check.

A design-review guide that wants security in the design covers empty-change merge. This week's check is the local stand-in.

## What the repaired files must show

Check `fixed/sdl.py` against the list above. Do not treat the snippet as a production merge bot.

| After the fix | Must be true |
|---|---|
| `{}` | `merge_ok` false |
| `{"threat_model": "TM-12"}` | `merge_ok` true |

Fail closed: if you are unsure whether a threat-model id is present, the change does not merge. Uncertainty is a **no** on “this may merge,” not a yes because CODEOWNERS is on.

## What this is not

- GitHub branch protection.
- CODEOWNERS.
- A process-maturity score.
- An unverified “secure by design” page treated as a product.
- Gate 10 or M4 complete.
- A threat-model quality review.
- FastAPI defaults.

## What the tool cannot do

- An opaque id: `"TM-12"` is not proof the model covers this change.
- Python `bool()` truthiness: an empty string is false; `"0"` is true — write down the convention.
- No file-path check: a README-only change and an authorization change look the same if both cite TM-12.
- No actor check: anyone can type TM-12.
- A docs exemption must be an explicit check, not a deleted gate.

## Can people still use it

The merge screen has to say *missing threat-model id*, in words, not only a red X. Do not hide the gap behind “see CODEOWNERS.”

## Practice

Name the leftover (a stale threat model; a docs exemption). Run:

```text
python3 -m pytest labs/10.1/10.1-lab/tests --impl fixed
```

## Use it somewhere new

A “docs: update README” change with no threat-model id still fails `merge_ok` in this lab. If you exempt it, write the exemption in the check.

## What can still go wrong

Stale TM-12. Vanity ticket counts. Exceptions without expiry (E6). An extra advanced row about documenting a dangerous function that you still never wrote down.
