# 1.3-LO-03 — Break the forged worker-provenance boundary locally

**Kind:** break-fix-lab

**Loop step:** 3 Break

**Authorized scope:** only the in-process synthetic fixture under `labs/1.3/1.3-trust-boundaries`. Do not adapt these calls or observations to any public, employer, classroom, or third-party system.

## The question is causal, not “can I make pytest red?”

The vulnerable fixture claims two layers protect a worker-only export:

1. an illustrative edge check recognizes an internal-looking field;
2. the application repeats the same recognition before exporting.

Both layers consume requester-controlled metadata. They are two checks but one trust assumption. The fixture also gives the resulting worker path a broad, reusable ability instead of binding the protected effect to current tenant, action, object, expiry, and use state.

The property under test is:

> A public caller cannot become a worker by choosing metadata. Only a trusted worker adapter may establish worker provenance, and the export effect requires a current, single-use grant bound to worker, tenant, action, and exact object set. Missing, unknown, malformed, expired, replayed, or evidence-failed context denies before output.

The local fixture is designed to make that property observable without a network target, real credential, real personal data, or harmful payload.

## Prepare an evidence worksheet

Before running anything, create one row per observed case:

| Test / flow | Required property | Preconditions | Trigger | Root cause | Impact / forbidden effect | Structural prevention | Detection | Recovery | Residual limit |
|---|---|---|---|---|---|---|---|---|---|

Keep these columns distinct:

- A **precondition** is a state that makes the failure reachable: a public entry exists, a grant exists, a shared export function accepts the call.
- A **trigger** is the specific local input or transition that exercises the failure.
- The **root cause** is the violated trust or enforcement assumption—not the input string and not the failed assertion.
- **Impact** is the forbidden effect on a property: unauthorized summary release, cross-tenant reach, use outside action/object/time scope, replay, or unobserved effect.
- **Prevention** changes how the system derives provenance, represents authority, or mediates the effect.
- **Detection** makes a boundary crossing visible but does not retroactively prevent release.
- **Recovery** contains authority, repairs every path sharing the assumption, reconciles outputs/state, and retests.

“Header spoofing” is a trigger label, not a complete diagnosis. “Validate the header” is not a structural repair when the public caller still controls the asserted fact.

## Read tests before implementations

From the repository root, inspect:

- `labs/1.3/1.3-trust-boundaries/README.md`
- `labs/1.3/1.3-trust-boundaries/tests/test_boundary.py`
- `labs/1.3/1.3-trust-boundaries/vulnerable/SECURITY.md`

Do not open the fixed implementation or examiner key yet. For each test, mark:

- diagram flow and entry point;
- attacker/failure capability;
- exact protected effect and oracle;
- evidence mode: normal, negative, abuse, failure, or counterfactual;
- whether the case tests provenance, authority scope, enforcement coverage, lifecycle, or evidence behavior.

An environment/import error is not security evidence. A test that passes on both variants may be a valuable valid-input regression, an ordinary denial, or a safety constraint rather than an intended vulnerability.

## Run the vulnerable variant

Use the command in the lab README from the repository root:

```text
python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl vulnerable
```

Expected shape: selected forbidden-outcome assertions fail while valid worker behavior, ordinary public denial, malformed requests, output projection, and fixture-safety checks continue to pass. Record the exact totals produced by your checkout; do not invent totals from this paragraph.

For every intended failure, answer three layers of “why”:

1. **Why did the assertion fail?** Describe the returned decision/output/state.
2. **Why could the implementation produce that result?** Identify the missing or untrusted model element.
3. **Why did the design allow that implementation?** Identify the false boundary, ambient capability, missing lifecycle, incomplete mediation, or common-mode claim.

## Failure family 1 — forged provenance

The public caller may choose an internal-looking marker and service label. If those values create a worker-equivalent context, the client has become part of the authority TCB.

Trace it:

```text
public field chosen
  -> edge interprets field as internal
     -> application interprets same field as internal
        -> shared export effect accepts effective worker
           -> protected summaries released
```

The two layers do not give independent depth because one attacker-controlled fact drives both. Even perfect TLS only protects the attacker’s chosen field in transit.

Your causal row should say that **provenance was derived from an assertion made by the party whose provenance was in question**. The minimal structural direction is separate trusted and untrusted adapters or an equivalent production mechanism that establishes service identity outside public fields. This local course does not claim to implement production workload identity.

## Failure family 2 — authority widening

A genuine worker identity is still not authority for every export. Challenge tenant, action, and object-set dimensions separately.

Examples of distinct forbidden outcomes:

- a Tenant A grant exports a Tenant B object;
- a grant for `{A1, A2}` exports `{A1, A2, A3}`;
- a grant for `export_summary` is used for another action;
- a broad process credential substitutes for the product’s grant.

Do not merge these into “authorization missing.” Each points to a different absent binding. The identity boundary can be correct while the authorization boundary remains wrong.

The impact is the scope actually released or mutated, not “the worker is compromised.” A worker with an all-tenant store credential may have a larger mechanism capability than product authority. The enforcement point must consume the product authority before the effect.

## Failure family 3 — lifecycle and replay

A scoped grant can become unsafe if its time and use state are ignored. Test expired and already-used grants independently.

Reason in transitions:

```text
issued -> usable -> consumed
              \-> expired
```

Only `usable` may authorize the modeled effect. Unknown transitions deny. In this sequential in-memory fixture, a successful effect consumes the grant. That demonstrates lifecycle reasoning; it does not prove transactionality or race safety. A production queue with duplicate delivery would require atomic consumption, idempotency, cancellation, and retry analysis in later modules.

## Failure family 4 — evidence failure

The lab models the export as high impact and chooses a conservative exercise rule: if the required evidence record cannot be produced, the effect denies. That is not a universal rule for every event. Some low-risk operations may buffer or degrade; some availability-critical operations may proceed with alternate evidence.

The design must be explicit. “We log exports” is false assurance if the operation proceeds silently whenever the shared sink fails. Test both:

- unavailable evidence produces no export effect under this exercise policy;
- an allowed export record omits note bodies, raw grant material, and other unnecessary sensitive fields.

The evidence sink is therefore part of the accountability TCB and, under this exercise rule, part of export availability. That consequence belongs on the model.

## Failure family 5 — alternate enforcement and correlated claims

Check whether every exported output must pass through the same scoped decision. A policy function can be correct while a wrapper, helper, retry, or administrative path bypasses it.

Also inspect the vulnerable `SECURITY.md`. A document may claim “edge plus application” as two layers even when source inspection shows a shared requester-controlled input. Evidence includes code/data dependencies, not the number of boxes in prose.

Your analysis must distinguish:

- **policy correctness:** when called with trustworthy context, does the decision enforce scope?
- **enforcement coverage:** can any in-scope effect occur without consuming that decision?
- **control independence:** can one false input or shared failure defeat the claimed layers together?

## Compare plausible non-fixes

For at least three of these, explain which failure remains:

- strip one exact header spelling at an edge;
- check a private source address;
- rename the route `/internal/export`;
- add a second check that reads the same field;
- sign a message that still grants all tenants/actions/objects indefinitely;
- hide the worker operation in the UI;
- give the worker a broad store credential and promise it will choose the correct tenant;
- log after release but silently skip the log when the sink fails.

The exercise is not asking which mechanism is always wrong. It asks why the proposed change does not establish the stated provenance, authority, lifecycle, mediation, independence, or evidence property.

## Safe mutation practice

After recording the baseline, make only a disposable copy outside the course fixture. Choose one simple mutation, such as removing an action comparison or changing a used-state transition. Predict exactly which property test should fail and which valid regressions should remain green. Run only the local test command.

If more tests change than predicted, record the coupling as a model finding. Restore by deleting the disposable copy—not by resetting the repository or editing a live target.

## Break-phase deliverable

Submit:

1. exact vulnerable command, environment, exit code, and totals;
2. a test-to-flow/evidence-mode trace;
3. one complete causal row for every intended failure;
4. grouping by forged provenance, scope widening, lifecycle/replay, evidence failure, alternate enforcement, or correlated control;
5. at least three rejected repairs with the remaining forbidden outcome;
6. one safe mutation prediction/result;
7. a bounded statement of what the fixture cannot prove.

### Success criteria

- Root causes name violated assumptions and enforcement structure, not only inputs or weakness labels.
- Valid behavior is preserved in the analysis; “deny every export” is not accepted as a functional repair.
- Detection and recovery are not presented as prevention.
- Worker identity and worker authority remain separate.
- The local type/adapter model is not called production authentication.
- No step reaches a network, real tenant, credential, or public system.

## Transfer hook

PreviewForge’s hostile influence may arrive as stored document bytes long after the upload request. “The upload endpoint validated it” can become the same kind of false boundary as “the edge stripped the header.” In LO-07 you will trace provenance, parser capability, queue lifecycle, egress, and evidence through an asynchronous system rather than repeating this fixture’s field names.
