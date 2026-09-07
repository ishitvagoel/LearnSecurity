# The broken files must fail on a raw less-than

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We added a content-security policy” is not evidence. “React is on” is a tool observation. The check is: `render` of a string containing `<` has `&lt;` and does not contain the extra-tag marker `"<img"`. That observation must be **false** on `--impl vulnerable` (raw `<` remains) and **true** on `--impl fixed`.

## Picture: broken files must fail: raw <

A passing-test tally can still hide that unencoded markup still reaches HTML.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail raw angle bracket"]
  X["--impl fixed"] --> P["Must pass encoded lt"]
```

If both pass, you are not looking at encoding.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | Honest title still present (`test_honest_title_survives`; may pass on both) |
| Wrong input / abuse | `<` becomes `&lt;`; extra tags absent; broken files must fail |
| Not claimed | Attribute / JavaScript / URL contexts; live page attacks; content-security enforcement |

The checks are in `labs/6.2/6.2-lab/tests/test_property.py`. `test_angle_brackets_are_encoded` is there so unencoded markup still fails. The tame marker is enough; do not add an attack recipe to the check.

```text
python3 -m pytest labs/6.2/6.2-lab/tests --impl vulnerable
python3 -m pytest labs/6.2/6.2-lab/tests --impl fixed
```

An honest title may survive on both sides. You still have to encode `<`. If the broken files do not fail `"<img" not in out`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- Encoding for a JavaScript string (a different rule)
- Content-security policy, or reporting from it (extra, advanced)
- Trusted Types (**draft**)
- A markdown cleaner (2.1)
- HttpOnly cookies (2.3)

## Practice

Do not treat a grep for `Content-Security-Policy` as the check. Call `render`. A setup error is not proof the rule holds.

## Use it somewhere new

Clinic nickname. Asserting HTTP 200 is not this check (see 9.3). Do not run a check that loads a live board.

## What this page is not doing

Do not add an attack recipe. Do not log title bodies if they are patient data. Answer keys are not on this site.
