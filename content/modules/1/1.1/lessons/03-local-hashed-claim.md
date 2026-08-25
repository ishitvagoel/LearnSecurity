# 1.1-LO-03 — Break a mechanism-only security claim

**Kind:** mechanism-lab
**Loop step:** 3 Break  
**Lab:** labs/1.1/1.1-invariant-catalogue — authorized local files and synthetic SecureCollab data only.

## What this lab breaks

The vulnerable fixture says the product is secure because it names familiar mechanisms. It is not an intentionally exploitable web service. The failure is a review and assurance failure: an unbounded slogan is allowed to stand in for a testable system property.

That distinction is deliberate. This module occurs before SecureCollab features exist. Later modules break running authorization, parser, browser, and state-transition mechanisms. Here you learn to reject a false claim before code makes it expensive.

## Safety boundary

You may inspect and validate only the files in this lab directory. Do not test a public site, employer system, classmate deployment, or real account. The fixtures contain synthetic tenants and notes; no credentials or personal data are needed.

## Run the two variants

From the repository root, create an isolated environment if needed and install pytest and PyYAML. Then run:

```text
python -m pytest labs/1.1/1.1-invariant-catalogue/tests   --claim labs/1.1/1.1-invariant-catalogue/vulnerable/security_claim.yaml

python -m pytest labs/1.1/1.1-invariant-catalogue/tests   --claim labs/1.1/1.1-invariant-catalogue/fixed/security_claim.yaml
```

The vulnerable run must fail the catalogue-validation test. The fixed run must pass. A failure caused by a missing dependency, unreadable path, or invalid test setup is not the intended observation.

## Read the failure as evidence

The validator checks more than whether certain field names exist. It asks whether the catalogue:

- identifies SecureCollab and a local synthetic scope;
- contains several stable, unique invariant IDs;
- names specific assets and adversary capabilities;
- identifies trusted and untrusted components;
- bounds the claim in time;
- separates properties from mechanisms and records mechanism limits;
- names module-specific forbidden outcomes;
- proposes normal, negative, abuse, and failure evidence;
- includes privacy-safe detection and concrete recovery;
- states residual risk, non-goals, and review triggers;
- avoids live-target URLs, credentials, personal data, and universal “we are secure” language.

A document can be valid YAML and still be invalid security reasoning. Syntax is necessary for the tool, not sufficient for the claim.

## Diagnose the vulnerable fixture

Do not jump directly to the fixed file. Annotate the vulnerable SECURITY.md and YAML using this causal chain:

| Layer | Question |
|---|---|
| Root cause | Which property was replaced by a mechanism label or universal conclusion? |
| Preconditions | What must a reviewer assume for the slogan to be accepted? |
| Trigger | Which line or missing field permits the false conclusion? |
| Impact | Which security decisions could be incorrectly marked complete? |
| Prevention | What structure would force a bounded property and assumptions? |
| Detection | What review or test should reject the claim? |
| Recovery | After false assurance has influenced a design, what must be reopened and retested? |

The important observation is not merely “required keys are missing.” A claim can contain attacker and trust fields while still saying nothing testable. Look for semantics: named actors, objects, actions, channels, time, and counterexamples.

## Compare the fixed fixture

After you have written your diagnosis, inspect the fixed version. Trace one invariant from property to forbidden outcome to evidence. Then ask:

- Does the proposed evidence observe the property, or only the control?
- Which trusted component could still invalidate the result?
- Which channel or time period remains a residual risk?
- Which product change forces review?

The fixed fixture is a model of claim quality, not proof that a SecureCollab implementation is secure. There is no implementation here to prove.

## Practice modification

Copy the fixed fixture to a temporary file outside the fixed directory. Make one change at a time:

1. replace a property with “we use encryption”;
2. remove the time horizon;
3. provide only happy-path evidence;
4. add the reserved example-domain URL from the vulnerable fixture as inert text;
5. put a note body into the proposed detection signal.

Run the validator after each change and record whether the failure message points to the reasoning defect. If a defect is not detected, note it as a validator limitation rather than claiming the catalogue is safe.

## Transfer prompt

Choose a different mechanism slogan—JWT, TLS, framework validation, encrypted storage, or a green scanner. Write:

- one bounded property it might support;
- one unrelated property it cannot establish;
- one assumption under which even the bounded property fails.

That three-part answer is the conceptual “break” for this lesson.
