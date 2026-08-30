# 1.3-LO-05 — Prove the boundary claim across five evidence modes

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP Threat Modeling Project’s “Did we do a good enough job?” question and lifecycle review. Standards references shape evidence questions; passing this fixture is not an ASVS assessment.

## Verification must be able to make the claim fail

An architecture diagram can be internally consistent and still be false. Verification connects each boundary claim to an observation that would contradict it.

For the lab property:

> Public input cannot establish worker provenance, and only a current single-use grant bound to worker, tenant, action, and exact object set permits the summary export effect.

Useful oracles observe more than an HTTP-like status:

- `allowed` decision and reason;
- exact returned note IDs and exact allowed fields;
- absence of Tenant B or note-body data;
- capability use state before and after;
- evidence presence and sanitized schema;
- unchanged state/output after denial;
- whether every effect path invokes enforcement.

A `403` alone is weak if output was already constructed, a side effect occurred, a retry remains queued, or sensitive data entered logs.

## Use five evidence modes

### 1. Normal

Show that the intended function remains usable. A registered worker presents its own unexpired, unused grant for the exact Tenant A action and object set. The expected result is one allowed summary-only output, a consumed grant, and a bounded evidence record.

Normal evidence prevents “deny everything” from masquerading as security. It also checks that the repair does not silently broaden output fields for convenience.

### 2. Negative

Use a valid or plausible caller that lacks one required condition:

- ordinary public call with no internal-looking metadata;
- unknown worker;
- missing/unknown grant;
- wrong action, tenant, or object set;
- missing object or tenant relation.

Vary one condition at a time where possible. Assert denied decision, empty output, unconsumed unrelated grants, and bounded evidence. A case with five invalid fields may pass while hiding which rule works.

### 3. Abuse

Exercise the attacker capability or misuse pattern that motivated the property:

- public input supplies internal-looking caller/service metadata;
- a valid worker tries to widen from Tenant A to Tenant B;
- a valid worker adds an ungranted same-tenant object;
- an already-consumed grant is replayed;
- an alternate export helper is called without the adapter/policy path, if such a path exists.

The fixture uses benign synthetic strings and function calls. No network evasion, production identifier, or harmful payload is needed.

### 4. Failure/state

Exercise non-malicious or operational failure:

- grant is expired;
- evidence sink is unavailable under the exercise’s high-impact policy;
- registry or stored relation is missing/unknown;
- representation is malformed;
- later, queue duplication, reordering, clock skew, transaction failure, and partial output would be required.

Unknown/failure behavior is part of the boundary contract. A control that works only while every dependency is healthy is incomplete.

### 5. Counterfactual

Remove or bypass one claimed protection in a disposable copy and predict the precise oracle that must change. Examples:

- let the public adapter construct worker context;
- remove exact object-set comparison;
- skip used-state transition;
- call output construction before policy;
- make evidence failure silently continue.

If no test changes, the control may be decorative, the test may not reach it, or another correlated control may mask its absence. Counterfactual evidence is stronger than accumulating green tests because it asks whether the claimed mechanism is causally connected to the property.

## Build the traceability matrix

Use a matrix that joins design and execution:

| Claim / flow | Property dimension | Initial state | Capability / failure | Entry and enforcement path | Oracle | Normal | Negative | Abuse | Failure | Counterfactual | Residual |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Public context cannot be worker | Provenance | Public adapter reachable | Caller chooses all metadata | F1–F3; worker-only export denies | No output; public caller kind in evidence | — | Plain public deny | Internal metadata still denies | Malformed metadata denies | Permit worker context in public adapter; abuse test must fail | No production routing/identity proof |
| Grant binds exact objects | Authority scope | Grant `{A1,A2}` usable | Worker adds A3 | F8–F9 | Deny; no summaries; grant remains usable | Exact set allows | Wrong set denies | Same-tenant widening denies | Missing object denies | Remove set equality; widening test must fail | No database row-policy proof |
| Grant is single use | Lifecycle | Grant usable | Repeat after success | F8–F9 | First allow, second deny; one effect | First use allows | Consumed denies | Replay denies | Atomic failure deferred | Remove consumption; replay test must fail | Sequential memory only |
| Evidence required | Accountability/availability | Sink unavailable | Operational outage | F6 before F9 | Deny and no output under exercise rule | Available sink allows | — | — | Unavailable sink denies | Continue on sink failure; failure test must fail | No durable/tamper-resistant sink |

Every critical claim needs at least one executable case and a residual. Not every mode applies to every row, but the evidence pack as a whole must cover all five modes.

## Distinguish decision tests from effect tests

A pure function test may prove:

```text
policy(worker, grant, request) == deny
```

It does not prove:

- every export route calls the policy;
- output is constructed only after allow;
- a retry or admin helper cannot bypass it;
- the grant is consumed atomically;
- the database credential cannot read broader data;
- evidence is emitted and sanitized;
- production caller identity is trustworthy.

The lab therefore observes wrapper behavior and output/state as well as decision logic. Its structural tests inspect the fixed public adapter and safety boundary. Even then, it proves only the small in-process fixture.

## Test the attack-surface inventory for closure

For each inventory row, define one of four closure states:

- **Executable evidence now:** a local test reaches the entry/effect and asserts an oracle.
- **Reviewed structural evidence:** source/model inspection supports the claim but a runtime path is absent.
- **Deferred with trigger:** component is not implemented; later module and activating change are named.
- **Residual/unknown:** the assumption remains trusted or unverified and has an owner.

Never mark “closed” because a control name appears in the diagram. A surface can be reduced, mediated, detected, transferred, accepted, or removed; every verb needs evidence and scope.

Example:

| Surface | State | Evidence | Honest conclusion |
|---|---|---|---|
| Public metadata promotes worker | Executable | Forged-metadata abuse tests plus public-adapter inspection | Closed in local API fixture; production routing/workload identity unproved |
| Worker grant crosses tenant | Executable | Tenant mismatch and exact-output oracle | Closed for fixture state and sequential call |
| Queue replay | Deferred | Trigger: first persistent/asynchronous worker | No queue assurance claim |
| Cloud operator changes registry | Residual/later | Owner and Phase 10 trigger | Operator remains transitively trusted |
| Evidence sink tampering | Residual/later | Only in-memory schema/outage test | Durability/integrity unproved |

## Verify control independence with fault hypotheses

Do not write “independent” without a named fault. Use hypotheses:

- If the public parser accepts an ambiguous field, do both edge and application accept it?
- If the worker registry is wrong, can capability scope still prevent cross-tenant export?
- If policy code is bypassed, can output projection or evidence prevent release? Usually evidence only detects after the fact.
- If the shared process is compromised, do context types and policy remain trustworthy? No; they share a failure domain.
- If the evidence sink fails, does prevention still work and is the failure visible elsewhere?

Classify each pair for that fault as **independent**, **partially independent**, **correlated**, or **unknown**. A local test can establish some logical separation. It cannot establish production operational independence.

## Run both variants

From the repository root, use the README commands:

```text
python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl vulnerable

python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl fixed
```

Record environment, exact command, exit code, totals, and intended failure names. The vulnerable run should preserve valid/regression cases while failing selected forbidden-outcome cases. The fixed suite should pass completely. Treat syntax/import/setup errors as environment defects, not lesson evidence.

For each intended vulnerable failure, compare:

- expected property oracle;
- actual vulnerable effect and state;
- fixed effect and state;
- implementation decision that changed;
- inventory row and diagram flow;
- remaining assurance gap.

## Design a counterfactual safely

Copy `fixed/surface.py` to a temporary learner directory. Do not edit course variants in place. Choose one protection and write the prediction before modifying:

```text
If exact object-set binding is removed,
then the same-tenant scope-widening test will change from denied to allowed,
while the exact authorized export and public-provenance denial remain unchanged,
because the mutation affects authority scope but not caller provenance.
```

Run the smallest relevant local test selection and then the full fixed suite against your disposable copy if your harness supports it. If the observed effects differ, revise the dependency model. Delete the temporary copy afterward.

## Verification deliverable

Submit:

1. five-mode traceability matrix covering every module invariant;
2. exact vulnerable/fixed results and environment;
3. diagram-flow and attack-surface row for each test;
4. explicit output, state, and evidence oracles—not only statuses;
5. one counterfactual prediction, mutation, result, and interpretation;
6. independence classifications for at least three control pairs and faults;
7. closure state and residual for each surface row;
8. a boundary on the conclusion.

A suitable conclusion is:

> The local evidence shows that the fixed in-process public adapter cannot construct worker provenance, and that the modeled export wrapper enforces the fixture’s worker/tenant/action/object/expiry/use/evidence rules for the covered cases. It does not prove production workload identity, HTTP/proxy behavior, persistent atomicity, queue semantics, database isolation, sandboxing, egress control, or durable audit integrity.

### Success criteria

- All five modes are present and trace to claims.
- At least one oracle checks exact allowed fields and one checks unchanged state after denial.
- Counterfactual evidence demonstrates a causal link to a claimed control.
- Policy correctness and enforcement coverage are separately addressed.
- Control independence is relative to named failures and shared dependencies.
- Deferred and residual surfaces are not counted as closed.
- The conclusion is narrower than “secure” or “ASVS compliant.”

## Transfer hook

PreviewForge needs different oracles: no parser escape, no unexpected network/file-system effect, bounded CPU/time/output, exact object-to-job binding, safe preview publication, idempotent retry, and evidence that excludes hostile content. The five modes stay; their observations change with the system.
