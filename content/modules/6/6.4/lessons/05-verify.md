# A path that leaves the folder must fail

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We use UUID names” is not this topic’s evidence. “We strip `..`” is a tool observation. The check is: `resolve("../outside")` raises `ValueError` **or** the canonical path is still `/tmp/sc-lab` or a child. That observation must be **false** on the broken files (join leaves the folder) and **true** on the repaired files. Tests must not read host files outside the lab folder.

## Picture: a path that leaves the folder must fail

A grep for `uuid` in a filename helper can still hide that `resolve("../outside")` still leaves the folder.

```mermaid
flowchart LR
  V["broken files"] --> F["Must fail: ../ leaves folder"]
  X["repaired files"] --> P["Must pass: prefix or ValueError"]
```

| Mode | Must show for this topic |
|---|---|
| Normal | Honest `notes/a.txt` stays under the folder (may pass on both) |
| Wrong input / abuse | `../outside` does not leave the folder; broken files must fail |
| When things break | If canonicalize is uncertain, deny (write it as leftover if this check does not cover it) |
| Not claimed | Zip members; XML entities; pickle; live host reads; awareness-list “compliant” |

Lab tests: `test_dotdot_does_not_escape_root` and `test_honest_relative_stays_under_root` in `labs/6.4/6.4-lab/tests/test_property.py`. The first test is there so an escaped object still fails. The name `../outside` is data for the prefix check — not a cookbook for other directories.

```text
python3 -m pytest labs/6.4/6.4-lab/tests --impl vulnerable
python3 -m pytest labs/6.4/6.4-lab/tests --impl fixed
```

A relative name under the lab folder may pass on both sides. You still have to stop `../` from leaving it. Map each test to the prefix row you wrote on the map page. If the broken files do not fail the prefix check, the lab is miswired — fix the wiring, not the check. A setup error is not proof the rule holds.

## What the tests do not prove

- Zip members that walk out
- Magic-byte vs extension
- Uploads not run as code, except as leftover you name
- Antivirus — extra, not the rule
- XML/pickle/YAML parsers

## Practice

Do not treat a grep for `uuid` in a filename helper as the check. Call `resolve("../outside")`.

## Use it somewhere new

Clinic scan filename. Asserting HTTP 200 on upload is not this check. Do not run a test that opens host files outside the lab folder.

## What this page is not doing

Do not treat a host-file screenshot as proof. Do not log original filenames if they are patient ids. Answer keys are not on this site.
