# Proving the gate catches a missing id, an untraced flow, and a stale row

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** OWASP ASVS 5.0.0 `v5.0.0-13.1.4` (final, Level 3, labeled advanced), `v5.0.0-15.1.4` (final, Level 3, labeled advanced), `v5.0.0-15.1.5` (final, Level 3, labeled advanced).

## What ten tests have to distinguish

A suite that only checks "does the gate return `fail` sometimes and `pass` other times" would be satisfied by a function that returns `fail` on every odd-numbered call, which is worthless. Every test in `labs/3.2/3.2-lab/tests/test_property.py` has to distinguish a pass for the *stated reason* from a pass that merely happened to occur, and the same discipline applies to failures: a test that expects `fail` must confirm the failure names the specific defect it introduced, not an unrelated one.

The **normal case**, `test_complete_model_passes_on_green_scan`, submits a model with all three always-name ids present, owned, triggered, correctly flowed, prioritized, and mitigated, with no trigger fired, and asserts `result["reasons"] == []` — not merely `result["gate"] == "pass"`. Checking the reasons list, not only the gate verdict, matters because a fixed implementation that happened to swallow a real reason string while still returning `"pass"` would pass a weaker assertion while hiding a bug; requiring an empty list is the observation that distinguishes "correctly found nothing wrong" from "found something wrong and reported it incorrectly as nothing."

The **forbidden-outcome case**, `test_green_scanner_missing_cross_tenant_read_fails`, removes `cross-tenant-read` from an otherwise-complete model and asserts both `result["gate"] == "fail"` and that the specific string `"cross-tenant-read"` appears in one of the returned reasons. The second assertion is the one that matters for this module's property specifically: a gate that failed the model for an unrelated reason — say, a bug that made it reject every submission — would satisfy `gate == "fail"` without proving anything about whether the *missing-id* check works at all. Asserting on the reason's content, not just the pass/fail verdict, is what turns "the gate said no" into "the gate said no for the reason this lesson is about."

The **boundary case**, `test_untraced_worker_flow_fails_even_with_all_ids_present`, is this module's most important test precisely because it does *not* touch any threat's id, owner, or trigger — every mandatory row is left fully compliant. It removes only `worker-share-redelivery` from `declared_flows`. If this test passed against a gate that only checked id presence, it would prove the module's actual property false: that a threat id, present and fully documented, is not by itself evidence that the flow it depends on was traced. The observation distinguishing a real pass here from a false one is that the failure reason must name the *flow*, not the *id* — a gate that reported "missing threat id" for this case would be failing for the wrong reason, which would mean the flow-coverage check does not actually exist and the test is only passing because a different, unrelated check happened to also reject the input.

The **malformed/failure cases**, `test_mandatory_threat_without_owner_fails` and `test_missing_priority_field_fails`, submit structurally valid JSON — the framework's own request parsing accepts both without a 422 — that is missing one required field each. Both prove the gate's own field-presence checks run independently of the id-and-flow checks above them, because in both cases every id is present and every flow is traced; only one field on one threat is absent.

## The two anti-fake tests, and the specific fakes they reject

`test_fired_trigger_without_revisit_fails` and `test_anti_fake_revisit_is_checked_per_threat_not_globally` together defend the claim that staleness is about what was actually re-reviewed, not about what a date field claims, and each rejects a distinct, plausible-sounding shortcut.

The first fires one trigger against a model where the threat that names it has an empty `revisited_after` list, and requires the gate to fail, naming that specific threat as not revisited. A fake fix a reasonable engineer might reach for under time pressure is to skip building a `revisited_after` mechanism at all and instead compare a `model_last_updated` timestamp field against "now" — reasoning that a model updated recently is probably a model someone actually looked at. This fixture's schema deliberately gives that fake nothing to key off: there is no self-reported date field in the request at all, so a shortcut built around trusting one has no field to read, and the only way to satisfy this test is to build the actual per-threat, per-trigger check the property requires.

The second test is the sharper anti-fake case, and it targets a fake that *does* attempt the real mechanism but cuts a corner inside it: checking "has *any* threat that shares this trigger name been revisited" instead of checking every threat with that trigger independently. This is a genuinely tempting shortcut, because it is fewer lines of code and passes every other test in the suite — including the first anti-fake test, since a model with only one threat per trigger name cannot distinguish the two implementations. `test_anti_fake_revisit_is_checked_per_threat_not_globally` adds a second threat sharing `cross-tenant-read`'s trigger, marks only the second one as revisited, and asserts the gate still fails, naming `cross-tenant-read` specifically as unrevisited. A global "any" check would incorrectly pass this case, because *some* threat with that trigger name was marked revisited; only a per-threat check catches it. This is the same shape of anti-fake test `labs/3.1/3.1-lab` uses to catch a hardcoded two-field allow-list — a fix that looks structurally like the real mechanism, passes the obvious tests, and fails only the one test built specifically to distinguish "checks every row" from "checks that some row exists."

## What a green suite still does not prove

Nine green tests prove that this specific gate, against this specific fixture's schema, correctly implements the five checks [`lessons/04-build.md`](04-build.md) derived. They do not prove that any *real* SecureCollab threat model, submitted by an actual engineer, is complete — a human could write a `mitigation` string that is grammatically real, non-placeholder text and still describes a mechanism that does not actually exist or does not actually work, and no test here can tell the difference between an honest mitigation and a well-written but false one. They do not prove that `revisited_after` entries reflect an honest re-review of the four questions rather than a teammate appending a trigger name to make the gate pass; that gap is not a defect in this lesson's mechanism, it is the boundary [`lessons/04-build.md`](04-build.md) already named between what an automated check can verify from outside and what still needs a human reviewer reading the actual reasoning, not just the shape of the record. They also do not prove anything about whether `cross-tenant-read`'s named mitigation — [4.4's `can_read` matrix](../../../4/4.4/spec.md) — is itself implemented correctly; that is a different property with its own tests, owned by a different module, and this gate's job stops at confirming the threat model names it, traces it, and keeps it current.

## Practice

Run both variants and confirm the counts match what this lesson describes:

```bash
python3 -m pytest labs/3.2/3.2-lab/tests --impl vulnerable   # 8 of 10 fail
python3 -m pytest labs/3.2/3.2-lab/tests --impl fixed         # 10 of 10 pass
```

Then, without editing any file, predict which of the ten tests would still pass against the vulnerable fixture if a future change made `scanner_green` default to `False` instead of `True` in every test's request payload, and explain why the property this module teaches would remain exactly as broken either way.

## What this lesson is not doing

This lesson does not authorize weakening any assertion to make a fake implementation pass, and it does not authorize testing against a real scanner integration, a real CI system, or any system outside `labs/3.2/3.2-lab`.
