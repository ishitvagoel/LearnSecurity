# Lab: 3.2-lab

**Module:** `3.2`
**Authorized scope:** this directory only. Local FastAPI fixture; synthetic threat ids, flow names, and owners; no production scanner tenant, no live vendor dashboard, no real company or system.
**Tier:** 2 (component). A real FastAPI request/response cycle through `fastapi.testclient.TestClient`, with server-side state (`_MODEL`, the stored threat-model document) that persists across calls within one test and resets between tests — see `lab-realism.mdc`.

**Invariant (C1):** A green scanner result must not let a stored threat model that omits `cross-tenant-read`, `hostile-browser`, or `stolen-worker` — each with a named owner and review trigger — pass the merge gate.
**Invariant (C2):** A gate that checks threat ids by string alone, without checking that the diagram's `declared_flows` actually trace the paths those ids depend on, can be satisfied by an incomplete trust-boundary diagram; the gate must check flow coverage independently of id presence.
**Invariant (C4):** A named review trigger firing demands a recorded re-review of the threat row it names, checked independently of any self-reported "last updated" field, so a submitter cannot fake freshness by rewriting a date instead of the content.
**Root cause class:** trust (a merge gate that substitutes one signal — a scanner's green result — for the several distinct properties a versioned threat model actually has to hold).
**Non-goals:** the mechanism that would actually enforce cross-tenant denial in the running application (module 4.4's `can_read` matrix); a production SAST/DAST/SCA integration; STRIDE facilitation quality; whether a human's `revisited_after` entry reflects an honest re-review rather than a rubber stamp (named as a residual in `lessons/05-verify.md`).

## Reset

No persistent state between tests. `conftest.py` loads a fresh module and calls `reset()` before every test. Optional: `git checkout -- labs/3.2/3.2-lab`.

## Vulnerable behavior (local only)

`evaluate_gate` returns `pass` as soon as `scanner_green` is `True`, without opening the stored threat-model document at all. See `vulnerable/SECURITY.md`.

## Structural fix

`evaluate_gate` always opens the stored model and checks five properties of it, independent of `scanner_green`: the always-name ids with owner and trigger; required-flow coverage; an integer priority on every mandatory threat; a non-placeholder mitigation on the top-priority one; and, for every fired trigger, a recorded re-review on every threat that names it. See `fixed/SECURITY.md`.

## Verify

```bash
python3 -m pytest labs/3.2/3.2-lab/tests --impl vulnerable   # 7 of 9 fail
python3 -m pytest labs/3.2/3.2-lab/tests --impl fixed         # 9 of 9 pass
```

If `fastapi`/`httpx` are not already installed: `pip install -r labs/3.2/3.2-lab/requirements.txt`.

Nine tests in `test_property.py`: the core forbidden outcome (a green scan must not pass a model missing `cross-tenant-read`), a malformed/failure case (a mandatory id with no owner), a boundary case proving that every id can be present as a string while the diagram still never traces the worker-redelivery path — the incomplete-trust-boundary failure this module is actually about — a normal case proving scanner findings are additive rather than replacing anything, a priority/mitigation case, a missing-priority malformed case, a stale-trigger case, and two tests (one of them explicitly an anti-fake test) proving that re-review status is checked per threat row, not globally.

**The anti-fake test is not decoration.** `test_anti_fake_revisit_is_checked_per_threat_not_globally` adds a second threat sharing the same review trigger as `cross-tenant-read`, marks only the second one as revisited, and requires the gate to still fail on `cross-tenant-read` specifically. A fake fix that checks "has *any* threat with this trigger name been revisited" — a plausible shortcut, since it is fewer lines than checking every row independently — passes the other eight tests and is caught only by this one, the same way `labs/3.1/3.1-lab`'s anti-fake tests catch a hardcoded field-pair cheat. `test_fired_trigger_without_revisit_fails` doubles as a second anti-fake check: a fake fix that infers freshness from a self-reported `model_last_updated`-style field instead of an explicit `revisited_after` list would pass a model that claims to be recent without actually recording what was re-reviewed; this fixture's schema does not expose a self-reported date field for that shortcut to key off, so a submitter cannot back-date their way past the check the way `lessons/06-operate.md` warns against.

## Operate

Signal a missing or stale mandatory threat as `missing_mandatory_threat reason=<not_present|no_owner|no_trigger|not_revisited> id=<threat-id>`, never carrying a note body, a session token, or any SecureCollab content. See [`lessons/06-operate.md`](../../../content/modules/3/3.2/lessons/06-operate.md).

## Transfer

Clinic SMS reminders: a new channel and a new gateway-vendor questionnaire that must not stand in for this gate's five checks. Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/3/3.2/lessons/07-transfer.md).

## Review

`review/candidate_fix.py` is a seeded, non-executable snapshot of a hypothetical pull request for [`lessons/08-review.md`](../../../content/modules/3/3.2/lessons/08-review.md)'s reading exercise. Findings and rationales live only in `content/assessment/keys/3.2.md`.
