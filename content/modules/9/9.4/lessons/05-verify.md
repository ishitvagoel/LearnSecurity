# A broken ship_ok must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

Turning on code scanning does not map HIGH findings. A high maturity score is a dashboard. `ship_ok([HIGH], {})` has to be false, and a mapped HIGH may ship. On the broken files the empty map still ships. On the repaired files it does not. Do not scan public repos.

## Picture: a broken ship_ok must fail the check

A passing-test tally can still hide that unmapped HIGH still ships.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: empty map]
  X["repaired files --impl fixed"] --> P[Must pass: deny unmapped HIGH]
```

If both pass, you are not looking at the empty map.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | Mapped HIGH may ship (may pass on both) |
| Wrong input | Unmapped HIGH → not ship; broken files must fail |
| Abuse | Suppression with no owner is still deny (leftover if not in this check) |
| Not claimed | A real GitHub tenant; the verification gate; a maturity score; that the mapped requirement is the right row |

The test `test_unmapped_high_blocks_ship` is there so always-true `ship_ok` still fails.

A HIGH with an owner on the map may pass on both sides. You still have to deny an unmapped HIGH. If the broken files do not fail `test_unmapped_high_blocks_ship`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/9.4/9.4-lab/tests --impl vulnerable
python3 -m pytest labs/9.4/9.4-lab/tests --impl fixed
```

A scanner name in a workflow is not `ship_ok([HIGH], {})`. This practice never opens a live GitHub org.

## What the tests do not prove

- That the mapped requirement is the right coverage-map row
- That an isolation test exists
- Live SCA reachability
- Dependency confusion as an advanced leftover
- That the verification gate is done

## Practice

Call `ship_ok([HIGH], {})`. A `codeql` job in a workflow is the scanner, not the map.

## Use it somewhere new

A scanner job that ran is the workflow, not a mapped HIGH. Do not use a live GitHub tenant.

## What this page is not doing

A live org screenshot is not a mapped HIGH. Do not log secret-scanner payloads. Answer keys are not on this site.
