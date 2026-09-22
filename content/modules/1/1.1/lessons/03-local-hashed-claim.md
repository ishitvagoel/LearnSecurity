# Break a mechanism-only security claim

**Kind:** mechanism-lab
**Loop step:** 3 Break

## The smallest representative failure

The failure this lesson reproduces is not a crashed server or a leaked note; SecureCollab has no running service yet, so neither of those is available to break. The failure is a claim that fails to be a claim at all, and the smallest way to observe that failure is to hand a mechanism-only document to a validator that checks whether a claim is bounded, and watch it refuse. `labs/1.1/1.1-invariant-catalogue/vulnerable/SECURITY.md` states: "We are secure because passwords are hashed, TLS is enabled, and the scanner is green," and applies that one sentence to tenants, notes, exports, backups, logs, and account recovery all at once. Nothing about the sentence names an asset specific to any of those six things, names an attacker capability, or says what observable event would prove it false — it is the mechanism-only claim [01-property-vs-mechanism.md](01-property-vs-mechanism.md) described in the abstract, now sitting in a file a validator can actually be pointed at.

## What you may touch

Run this only inside `labs/1.1/1.1-invariant-catalogue/`. The data is synthetic; every tenant, member, note, and URL in the fixtures is a fixture label, and the one public-looking URL inside `vulnerable/security_claim.yaml` exists only so the validator can demonstrate rejecting it — do not visit it, and do not point the `--claim` option at anything outside this lab directory.

## Reproduce the failure

From the repository root:

```text
python -m pytest labs/1.1/1.1-invariant-catalogue/tests -q \
  --claim labs/1.1/1.1-invariant-catalogue/vulnerable/security_claim.yaml
```

The failing test is `test_selected_catalogue_is_semantically_reviewable`, and its failure is the observation this lesson exists to produce — read the assertion message before moving on, because it lists every specific defect rather than a single pass/fail bit. `catalogue.authorizedScope` fails because the vulnerable fixture's scope text points at a public domain instead of naming a local, course, or synthetic boundary; `catalogue.syntheticDataOnly` fails because the fixture sets that flag to false; `catalogue.claims` fails the five-row minimum because the vulnerable fixture contains exactly one; and that one claim fails on its own terms, because `is_mechanism_only` recognizes "we are secure because we use TLS" as one of the mechanism-slogan phrases the earlier lesson named, and every one of the envelope fields the model lesson demanded — attacker, trust, untrusted component, forbidden outcome, evidence, detection — is simply absent from a one-line property statement that never intended to carry them. A missing package or a bad path would also make this command exit non-zero, and that is not the same observation; five passing unit tests alongside the one failure (`test_mechanism_slogan_is_rejected`, `test_public_target_is_rejected_but_local_lab_is_allowed`, and three anti-fake tests covered in [05-forbidden-outcomes.md](05-forbidden-outcomes.md)) is how you confirm the environment is healthy and the failure you are looking at is the intended semantic one.

## Why this is the smallest version of the failure

A tempting way to make this lab "more real" would be to stand up an API endpoint that actually returns a Tenant B response containing Tenant A data, and prove the leak by watching bytes cross a real boundary. SecureCollab's Phase 1 model deliberately has no such endpoint, and building one here would not make the lesson sharper — it would replace the failure this module teaches with a different one, an implementation bug, that belongs to a later module once an implementation exists. What is missing from this lab, on purpose, is exactly that: a running service, a database, and a network call. What is not missing is the one thing the failure actually depends on, which is a claim shaped so that no reviewer, human or automated, can point to a concrete event that would falsify it. Removing the running service does not change that cause; it isolates it. If SecureCollab did have a running API tomorrow, the mechanism-only claim in `vulnerable/SECURITY.md` would still be exactly as false-assurance-generating as it is today, because the defect was never in the missing code — it was in the missing model.

## Read the causal document, not the examiner key

Before you compare notes with anyone, read `labs/1.1/1.1-invariant-catalogue/vulnerable/SECURITY.md` on your own and write down which SecureCollab assets it silently claims to cover. The document does not mention notes, tenants, or membership by name; it mentions passwords, TLS, and a scanner, and asks the reader to assume those three mechanisms settle every question the product might ever raise. Ask, for each of the six assets this phase's model actually names — note bodies, membership records, audit events, export capacity, retained logs, and deletion state — whether any sentence in the document would change if that asset did not exist. If the document reads identically whether or not SecureCollab has tenants at all, it has not made a claim about tenants; it has made a claim about credential storage and borrowed the appearance of covering everything else.

## What "fail closed" means for this validator

The validator's job is narrower than proving SecureCollab secure, and the lab's own README says so directly: passing it shows only that a catalogue is shaped and worded for independent semantic review, not that an implementation exists or behaves correctly. A validator that instead let a mechanism slogan through — because the YAML parsed, because five keys were present, because nothing crashed — would be failing open on the exact question this module is about, silently converting "shaped correctly" into "true," which is the same substitution the vulnerable SECURITY.md itself makes. When you reach [04-smallest-mechanism.md](04-smallest-mechanism.md), you will derive the structured record that replaces this one-line slogan, and see precisely which checks the validator runs to keep that substitution from happening again.

## Check yourself

Name the four distinct reasons `catalogue.claims`, `catalogue.syntheticDataOnly`, `claims[0].property`, and the missing envelope fields each fail independently — a reviewer who can only say "it's not shaped right" has not yet separated cause from symptom the way [01-property-vs-mechanism.md](01-property-vs-mechanism.md) asked. Then explain, in one sentence, why adding a real database to this lab would not make the observed failure any more real than it already is.

## What this page is not doing

This lesson does not start a network service, does not send a request to `https://production.example.org` or any other host named in the vulnerable fixture, and does not require you to write exploit code. Answer keys are not on this site; they live only under `content/assessment/keys/1.1.md`.
