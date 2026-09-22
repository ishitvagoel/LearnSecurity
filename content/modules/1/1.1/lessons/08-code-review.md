# Review a security document as an engineering claim

**Kind:** code-review
**Loop step:** 7 Generalize

## What you are reviewing, and why order matters

You are reviewing a change that adds `labs/1.1/1.1-invariant-catalogue/vulnerable/SECURITY.md` and its companion `vulnerable/security_claim.yaml` to a repository, proposed as SecureCollab's first security statement. A short document is not the same thing as a safe one, and a reviewer who reads top to bottom and reacts to whatever catches the eye first will spend the review budget on the loudest issue instead of the one that actually decides whether the document is mergeable. Read in a fixed order instead: the property statement first, then the envelope fields around it, then the evidence, then the scope and safety fields, and only after all four are settled, the cosmetic details that do not change any of them. That order exists because each later category can look fine in isolation while the earlier one has already failed, and a reviewer who starts at the bottom of that list can spend an entire review approving formatting on a document whose central claim was never checkable to begin with.

## Step one: is the property a rule or a mechanism?

Here is the whole claim under review, in full, before this lesson interprets any of it:

```yaml
catalogueVersion: 1
system: SecureCollab
authorizedScope: Check https://production.example.org because it is only a demo
syntheticDataOnly: false
secure: true
because:
  - Passwords are hashed
  - We use TLS
  - The scanner is green
claims:
  - id: claim-1
    property: We are secure because we use TLS
    assets:
      - data
```

Thirteen lines are the entire proposed security statement for a product whose Phase 1 model already names six or more distinct assets. Read `property: We are secure because we use TLS` before reading anything else in the file. Ask the question [01-property-vs-mechanism.md](01-property-vs-mechanism.md) built this whole module around: does this sentence name an asset, an attacker, and an observable outcome that a concrete event could falsify, or does it name a tool and stop? This one names TLS, stops, and — worse — the same sentence is applied by the surrounding `because` list to passwords and to a scanner result as well, meaning one unfalsifiable sentence is doing the work three mechanisms and six-plus SecureCollab assets would each need their own bounded row to cover. This is the finding that decides everything else in the review; if the property fails this test, no amount of correct YAML syntax below it rescues the document, and you can say so in one sentence without yet reading further.

## Step two: are the envelope fields present, and do they say anything?

Only after the property fails or passes step one does it make sense to check for `assets`, `attackers`, `trust`, `untrusted`, `timeHorizon`, `forbiddenOutcomes`, `mechanismLimits`, `nonGoals`, and `reviewTriggers`. In this fixture, `claims[0]` has exactly two keys — `id` and `property` — so every one of those fields is simply absent, not merely thin. Note that absence is a different, easier finding than the padded-but-present failure [04-smallest-mechanism.md](04-smallest-mechanism.md) and [05-forbidden-outcomes.md](05-forbidden-outcomes.md) described, where every field exists and says nothing specific; a reviewer trained only to check "is the field there" would catch this document and then wave through that harder case, so name explicitly, in your review, which of the two failures you are looking at.

## Step three: does the evidence observe an outcome, or a control?

This claim has no `evidence` key at all, so the check `catalogue_validator.py` runs — rejecting phrases like "middleware exists" or "scanner is green" as evidence — never even gets a chance to run; the document fails one level earlier, at "evidence is missing," rather than at "evidence exists but only observes a control." Both are real defects, and conflating them in a review comment ("no evidence") loses the information a repair author needs to know which one they are fixing.

## Step four: scope and safety, checked last on purpose

`authorizedScope: Check https://production.example.org because it is only a demo` and `syntheticDataOnly: false` are the two fields this lab's validator treats as safety-relevant rather than merely semantic, and they are checked last in this reading order because they would be just as wrong on a well-bounded claim as on this mechanism-only one — they are independent of whether the property itself is a rule. Flag both explicitly: a public URL inside a course fixture, even one the validator is specifically built to reject rather than visit, is the kind of detail that should never survive into a merged document, and a `syntheticDataOnly: false` flag on a claim about fixture data is either a copy-paste error or a genuine claim that real data is involved, and a reviewer has to find out which before approving anything.

## The plausible non-issue

`vulnerable/security_claim.yaml` also carries two top-level keys that appear nowhere in the schema `catalogue_validator.py` actually checks: `secure: true` and a `because` list duplicating the property's mechanism names. These look like exactly the kind of clutter a tidy reviewer wants to flag — "remove the stray `secure` flag and the redundant `because` list" is an easy, satisfying comment to write. Resist writing it as if it were the fix. Deleting both keys changes nothing about the four real defects above: the property is still a mechanism slogan, the envelope fields are still absent, the evidence is still missing, and the scope is still unsafe. A review that spends its comment budget on `secure: true` and calls the document improved has cleaned the room without touching the reason the document fails, and a competent reviewer says so — name the two keys as unused clutter worth removing eventually, and say explicitly that removing them is not what makes this document mergeable, so the repair author does not mistake a cosmetic pass for a real one.

## Writing the review comment itself

A useful comment on any of the four real findings names four things in order: the unsupported conclusion the document currently makes, which specific envelope or evidence element is missing that would let a reader check that conclusion, the concrete consequence of merging the document as written — design and review work on note confidentiality, session security, and account recovery could each be marked "covered" by a claim that touches none of them — and the smallest change that would address it, which for this document is not a longer paragraph but the structured five-row catalogue [02-securecollab-catalogue.md](02-securecollab-catalogue.md) and [04-smallest-mechanism.md](04-smallest-mechanism.md) built together. "This needs more detail" identifies none of those four things and teaches the repair author nothing about what to change.

## Practice

Run this only inside `labs/1.1/1.1-invariant-catalogue/`. The data is synthetic.

Write the review comment you would post for `vulnerable/SECURITY.md` and `vulnerable/security_claim.yaml`, covering all four real findings from this lesson's reading order and explicitly naming the `secure`/`because` clutter as a non-blocking cosmetic note rather than a finding. Then write the shorter review you would post for `fixed/security_claim.yaml`: two sentences, one naming the evidence you actually ran, one naming the residual risk the fixed catalogue still records rather than closes.

## Check yourself

Explain why checking the property before the envelope fields, and the envelope fields before the evidence, changes what a review comment says compared to reading the document in file order. Name the exact reason `secure: true` is not one of this document's four real defects, and contrast that with a change to `mechanismLimits` or `evidence.negative`, which would be.

## What this page is not doing

This lesson reviews course fixtures only; no real product's SECURITY.md is involved, and no exploit or live target appears anywhere in this exercise. Answer keys, including the intended findings for this document, live only under `content/assessment/keys/1.1.md`.
