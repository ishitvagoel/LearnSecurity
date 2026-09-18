# Verify forbidden outcomes, not control presence

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** Saltzer and Schroeder (1975, seminal) on complete mediation, which is why a single normal-case pass is not evidence about the abuse or failure path; NIST CSF 2.0 (final) Detect and Respond as outcome labels this lesson's evidence modes support, not proof by themselves.

## Why one passing test is a story, not evidence

A mechanism without a failed test attached to it is a claim resting entirely on the author's word, and the previous lessons have already shown why that is not enough for a bounded rule. This lesson names the four distinct things a SecureCollab catalogue row has to prove, and each one fails for a different reason, which is exactly why a single green check mark cannot stand in for all four: the **normal** case proves the property holds when nothing adversarial is happening, the **negative** case proves a disallowed action is actually refused and leaves no partial effect, the **abuse** case proves the refusal survives an adversary who deliberately varies identity, ordering, or volume to find a gap the normal case never exercised, and the **failure** case proves that when a dependency breaks — a policy lookup times out, an evidence sink goes down — the system denies rather than silently granting. A row that only specifies normal-case evidence has proven the mechanism works when nobody is trying to defeat it, which is the one condition under which almost every mechanism works.

## What each mode actually rules out

Take the cross-tenant confidentiality row from `fixed/security_claim.yaml` as the worked case. Its normal evidence is that a Tenant A member reads an A note and the resulting event records only actor, tenant, action, object identifier, decision, and correlation identifier — this rules out the possibility that the ordinary path leaks more than the schema promises even when everyone behaves. Its negative evidence is that a cross-tenant read or export returns no note body and commits no state — this rules out a denial that is cosmetic, one that returns a 403 on the surface while some background code path still touched the data. Its abuse evidence is that guessed identifiers and client-supplied tenant labels do not change the server-resolved tenant — this rules out the specific attack the model lesson's minimum adversary is defined around, a Tenant B member modifying every request field they control. Its failure evidence is that a policy-lookup or event-schema failure denies the read without emitting request or note content — this rules out the case where the dependency the whole check relies on breaks in a way that turns a denial into a silent grant, which is often the mode nobody tests because it requires deliberately breaking something to observe it.

```text
evidence:
  normal:   ["A Tenant A member reads an A note; the event records actor, tenant, action, object id, decision, correlation id"]
  negative: ["Cross-tenant reads and exports return no note body and commit no state"]
  abuse:    ["Guessed identifiers and client-supplied Tenant A labels do not change the server-resolved tenant"]
  failure:  ["Policy lookup or event-schema failure denies the read without emitting request or note content"]
```

Read that block against `catalogue_validator.py`'s actual behavior: `REQUIRED_EVIDENCE_MODES` demands all four keys be present with at least one item each, and a further check rejects any evidence item whose text contains "scanner is green," "middleware exists," or "configured correctly" — phrases that describe a control's *presence*, not an observation of the *forbidden outcome itself*. That second check is the oracle this lesson is about: it distinguishes "we have a piece of middleware for this" from "we watched the forbidden thing not happen," and only the second is evidence about the property. A control-presence statement can be true on a system that still fails the property — middleware can exist and be misconfigured, unreachable on one route, or bypassed by a retry path — so accepting it as evidence would let exactly the false-assurance pattern back in that [01-property-vs-mechanism.md](01-property-vs-mechanism.md) opened this module by warning against.

## The anti-fake tests, and the fakes they reject

`labs/1.1/1.1-invariant-catalogue/tests/test_claim_shape.py` carries two anti-fake tests, each built to fail on a specific plausible shortcut rather than on a strawman. `test_field_presence_alone_does_not_pass` builds a catalogue with five rows, each one a bare mechanism slogan with no other envelope field at all, and confirms the validator rejects it for both the slogan and the missing evidence — the fake this test rejects is "hit the row count and stop." `test_field_complete_but_causally_shallow_claim_does_not_pass` takes a real row from the fixed fixture, swaps its property for a slogan, and swaps its negative evidence for "middleware exists" while leaving every other field genuinely filled — the fake this test rejects is "one bad substitution hiding inside an otherwise-complete row," which a check that only counts non-empty fields would miss entirely.

A third anti-fake test, `test_five_padded_duplicate_rows_do_not_pass`, exists because reviewing this lab while deepening the module found a fake neither of the first two tests caught: five rows, each with every required field present, each avoiding every phrase on the mechanism-slogan list, and each one identical in substance to the other four — "notes must never leak," "a bad actor," "the server," "thing works," repeated five times under five different ids. That catalogue satisfies the row-count minimum, the field-presence check, and the slogan-phrase check simultaneously, and it teaches nothing, because none of its five rows says anything a reviewer could falsify that the other four do not already say. The fix pairs each claim's normalized `property` and `forbiddenOutcomes` text into a signature and flags a second row that repeats an earlier row's signature; this test asserts that the fix catches the padded fixture and, just as importantly, does not flag the real fixed fixture's five genuinely distinct rows as duplicates of each other — an anti-fake check that is too aggressive is its own kind of false result.

## What a green suite still does not prove

Passing all six tests in this lab proves that a specific catalogue is shaped, worded, and structured the way an independent reviewer can meaningfully challenge it. It does not prove SecureCollab has an implementation, does not prove the implementation (if one existed) actually behaves the way the catalogue claims, and does not prove the claims are true rather than merely well-formed and specific-sounding — a fluent, detailed, entirely invented claim about a mechanism SecureCollab does not have would still pass every check in this file. Write that limitation into your own lab notes rather than treating a green terminal as the finish line; [06-operate.md](06-operate.md) picks up from here by asking what has to keep watching after this verification step, precisely because verification at one point in time is not the same guarantee as an operating system continuing to hold the property tomorrow.

## Practice

Run this only inside `labs/1.1/1.1-invariant-catalogue/`. The data is synthetic.

```text
python -m pytest labs/1.1/1.1-invariant-catalogue/tests -q \
  --claim labs/1.1/1.1-invariant-catalogue/fixed/security_claim.yaml
```

For one row in the fixed fixture, write which concrete SecureCollab event each of its four evidence entries rules out, in your own words, before reading the block quoted above again. Then delete one evidence mode from a scratch copy of the row and confirm which specific check reports it missing.

## Check yourself

Explain, for the confidentiality row, why normal-case evidence alone would have let the vulnerable SECURITY.md's "scanner is green" pass if the validator checked only for evidence-key presence. Name the exact difference between a control-presence statement and a forbidden-outcome observation, and give one example of each drawn from a claim that is not about note confidentiality.

## What this page is not doing

This lesson does not claim a passing suite is a penetration test or proof that a real SecureCollab deployment is secure; it is evidence for this catalogue, in this lab, this week. Answer keys are not on this site.
