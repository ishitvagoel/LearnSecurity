# Build the smallest mechanism that restores the invariant

**Kind:** design-exercise
**Loop step:** 4 Build

## Deriving the fix from the failure, not from a template

The previous lesson observed a validator reject a one-line mechanism slogan for missing every envelope element the model lesson required. The fix that follows from that observation is not "write a longer SECURITY.md" — a competent engineer's first instinct, and a plausible one, because more prose sounds like more rigor. Try it anyway, mentally: expand "we are secure because passwords are hashed, TLS is enabled, and the scanner is green" into three paragraphs of narrative explaining each mechanism in more detail. The expanded version still names no asset a reviewer could point to, still has no attacker capability, still has no forbidden outcome a concrete event could falsify, and — this is the part that matters for a design review, not just a lint check — free-form prose gives every future author their own opinion about which fields to include, so the next SECURITY.md drifts back to a mechanism list the moment nobody is enforcing structure. The failure was never verbosity; it was that a mechanism-only claim has no place for the six missing elements to go, no matter how many words surround it. The smallest mechanism that actually restores the invariant is not more prose — it is a **schema** that has a required place for each element, and a validator that refuses to accept the document until every place is filled with something more specific than a placeholder.

## The structure that closes the gap

Here is the skeleton the schema requires, with every key traced to a gap the vulnerable fixture left open:

```yaml
id: SC-CONF-01
property: "Tenant A note bodies must never be returned to a Tenant B member ..."
assets: [note body, application log event, tenant export]
attackers: [an authenticated Tenant B member who can modify every client request]
trust: [the API policy path binds subject, note, action, and tenant]
untrusted: [browser and client-supplied tenant labels]
timeHorizon: "Request handling plus retained logs and generated exports"
forbiddenOutcomes: [any Tenant B response contains a Tenant A note body]
mechanisms: [server-side subject-object-action policy evaluation]
mechanismLimits: [does not cover a cloud administrator with snapshot access]
evidence: {normal: [...], negative: [...], abuse: [...], failure: [...]}
detection: {signal: ..., threshold: ..., eventFields: [...], prohibitedFields: [...]}
recovery: [revoke the session, remove exposed copies and repair the path]
residualRisk: "Direct database access by the cloud administrative plane"
nonGoals: [hiding note existence from the database administrative plane]
reviewTriggers: [files, sharing links, or workers add a new read path]
```

Every one of the sixteen keys above is a place the vulnerable fixture's two-line claim had no room to put anything; `mechanismLimits` and `residualRisk` in particular have no equivalent anywhere in "we are secure because we use TLS," because a mechanism-only slogan does not admit that it has limits at all. A SecureCollab catalogue row is a single mapping with the following required keys, each answering one question the mechanism-only slogan left open: `property` (the bounded rule itself, stated so that "must," "only," "never," or "remain" appears and a listed asset is named inside it), `assets`, `attackers`, `trust`, `untrusted` (a component the design explicitly refuses to trust), `timeHorizon`, `preconditions`, `mechanisms`, `mechanismLimits` (what the chosen mechanism cannot do — a field with no equivalent in the vulnerable document at all), `forbiddenOutcomes`, `evidence` (a mapping with `normal`, `negative`, `abuse`, and `failure` keys, which [05-forbidden-outcomes.md](05-forbidden-outcomes.md) covers in full), `detection`, `recovery`, `residualRisk`, `nonGoals`, and `reviewTriggers`. Every one of those keys traces back to a specific gap the previous lesson's failing test named; the schema did not invent new requirements, it gave the requirements the model lesson already stated a place to be checked mechanically instead of trusted to an author's memory.

## Two honest candidate mechanisms, and where the weaker one breaks

A shape-only validator — one that checks that every required key is present and every required list is non-empty, and stops there — is the mechanism a reasonable engineer would build first, and it is genuinely better than no validator at all: it would have caught the vulnerable fixture's missing `attackers`, `trust`, and `evidence` keys outright. Where it breaks is exactly the case this module's own lab review turned up while deepening this content: five rows that each fill every required key with generic, interchangeable text — "a bad actor," "the server," "notes leak somehow," "thing works" — pass a shape-only check completely, because every key is present and every list has an item in it, and nothing about presence distinguishes a SecureCollab-specific claim from a claim that would validate equally well against a claim about a payroll system or a photo app. `catalogue_validator.py`'s actual behavior goes one step further than shape: `is_mechanism_only` rejects a fixed list of slogan phrases, the asset-term check in `validate_catalogue` requires the property text to contain a word drawn from the claim's own `assets` list, and — added specifically to close the padding gap just described — a signature built from each claim's normalized `property` and `forbiddenOutcomes` text is compared across all five rows, so two rows that restate the same generic claim under two different ids are now flagged as one claim wearing two identifiers rather than two system-specific ones. Run the padded five-row fixture from [02-securecollab-catalogue.md](02-securecollab-catalogue.md) against the validator yourself and confirm which check catches it; the point of doing this by hand once is to see that "the fields are all filled in" and "the claim is bounded" are different properties, and only the second one is what this module is actually about.

## Where the chosen mechanism itself stops working

Say plainly what the validator cannot do, because a reader who believes it proves more than it does has learned the exact mistake this module exists to correct. It cannot tell whether a claim's content is *true* of SecureCollab — a fluent, well-shaped, entirely fictional claim about a mechanism SecureCollab does not actually have would pass every check here, because nothing in `catalogue_validator.py` inspects the product's actual code, which does not exist yet in Phase 1. It cannot detect a paraphrased duplicate; five rows using five different sentence structures to say the same generic thing would each carry a different signature and slip past the check just added. And it cannot replace the independent semantic review the module's publishability decision requires — a human reviewer asking "would a concrete SecureCollab-specific event actually falsify this?" is doing work no regular-expression check in this file can do for them. The lab's own README states this limit directly: the validator "catches selected reasoning defects but cannot prove an application secure or replace independent review," and believing otherwise about your own catalogue is the mechanism-only mistake recurring one level up, this time about the checker instead of the claim.

## Framework default versus application guarantee, made concrete

"The YAML parsed and pytest exited zero" is a framework default — PyYAML correctly read the bytes into a Python mapping, and pytest correctly reported that no assertion raised. Neither of those facts is the application guarantee this module is teaching toward, which is: a reviewer who has never seen this specific catalogue could read one row and construct a concrete SecureCollab event that would prove it false, and could not construct that event if the row were actually true as scoped. A catalogue that syntax-validates and then gets rubber-stamped because "the tests passed" has repeated, at the level of tooling, exactly the substitution [01-property-vs-mechanism.md](01-property-vs-mechanism.md) opened by warning against at the level of prose: presence of a mechanism standing in for proof of an outcome.

## Practice

Run this only inside `labs/1.1/1.1-invariant-catalogue/`. The data is synthetic.

Take one row from `fixed/security_claim.yaml`, copy it to a scratch file, and delete exactly one field: `mechanismLimits`, `untrusted`, or one evidence mode. Predict which check fails before running the validator, then confirm. Repeat once more, this time leaving every field present but replacing the `property` and `forbiddenOutcomes` text with generic wording that keeps the same structure — confirm that the duplicate-signature check, not a missing-field check, is what catches it if you copy that same generic wording into a second row.

## Check yourself

Explain why a shape-only validator would have caught the original vulnerable fixture but not the padded-rows fixture, and name the one thing about SecureCollab this module's validator can never verify no matter how it is extended. [05-forbidden-outcomes.md](05-forbidden-outcomes.md) takes this same mechanism and asks what "verified" actually requires across four distinct kinds of evidence.

## What this page is not doing

This lesson does not claim the validator proves SecureCollab secure, and it does not run against any file outside `labs/1.1/1.1-invariant-catalogue/`. Answer keys are not on this site.
