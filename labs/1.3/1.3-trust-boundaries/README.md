# Module 1.3 lab — trusted provenance and bounded worker export

This local fixture makes a trust-boundary failure observable without a web server or external target. The vulnerable variant lets a public caller promote requester-controlled metadata into worker provenance, then treats a registered worker plus any known grant as broad export ability. The fixed variant separates the public and worker adapters and consumes a current grant bound to worker, tenant, action, exact object set, expiry, and one successful use.

The lesson is not “block one header.” It is that provenance, authority, effect mediation, lifecycle, evidence, and control independence are separate claims.

## Authorized scope

Only the files under this lab directory are in scope. Tenants, workers, registrations, grants, notes, summaries, bodies, times, and events are synthetic. Fixture execution:

- runs in one Python process;
- starts no server and opens no socket;
- makes no outbound request;
- reads no environment variable, credential, or external data;
- performs no application file or database write; Python/pytest may create ignored bytecode and test-cache files;
- invokes no shell or subprocess;
- contains no harmful document, exploit payload, or production identifier.

Do not adapt the calls, metadata, identifiers, or findings to a public site, employer or classroom system, cloud account, API, queue, converter, or other third-party target. The dependency-install command may contact the package index configured for `pip`; use an approved mirror or pre-populated cache when installation must remain offline. The fixture/test runs themselves perform no outbound action.

## Security property

For the modeled SecureCollab Phase 1 summary export:

> A public requester cannot establish worker provenance by choosing request metadata. Only the trusted local worker adapter may resolve a registered worker, and the export effect requires a current, single-use server-held grant bound to that worker, tenant, action, and exact object set. Missing, unknown, malformed, expired, replayed, mismatched, or evidence-failed context denies before output.

The exercise policy treats this export as high impact and blocks it when decision evidence cannot be recorded. That is a deliberate availability/accountability trade-off for this fixture, not a universal logging rule.

## Modeled boundaries and flows

```text
public mapping -> public_export -> public context only -> deny worker export

server-held registration handle -> worker_export -> resolved worker identity
    -> server-held scoped grant -> effect enforcement -> summary-only output
                                           |
                                           -> bounded decision event
```

- A request mapping is wholly requester-controlled even if it contains internal-looking names.
- The public adapter cannot create worker caller kind or identity in the fixed variant.
- The registration handle is a local stand-in for a trusted adapter selecting server-held registry state. It is not a password, token, cryptographic workload identity, or production authentication mechanism.
- Worker provenance proves only modeled caller kind/identity. The grant separately decides action, tenant, objects, expiry, and use state.
- The protected effect is the construction and release of exact summary fields, not merely a boolean policy result.

## Vulnerable root causes

The vulnerable variant intentionally contains several related but distinguishable failures:

1. **Forged provenance:** edge and application both read `X-SecureCollab-Internal` from the same public mapping; a known service label is also supplied by that caller.
2. **False depth:** the two checks share decision input, parser/representation, routing configuration, runtime, and operator assumptions, yet the fixture labels them independent.
3. **Ambient worker authority:** any registered worker presenting any known grant can select tenant, action, and object IDs.
4. **Missing subject binding:** another registered worker can use Worker A’s grant.
5. **Missing tenant/action/object binding:** a grant can cross tenants, change action, or add same-tenant objects.
6. **Missing lifecycle:** expired grants and repeated uses remain accepted.
7. **Silent evidence failure:** a high-impact effect proceeds when its required decision record cannot be emitted.

These are not nine spellings of one bug. The tests isolate provenance, identity binding, authority dimensions, lifecycle, evidence, and the honesty of the defense-depth claim.

## Structural repair

The fixed variant:

- makes `public_export` unconditionally remain on the public side of the worker-only boundary;
- resolves worker identity only through a separate registration adapter backed by fixture state;
- rejects unknown worker or grant;
- binds grant to worker, exact action, tenant, and exact object set;
- resolves stored notes and confirms the tenant relation before release;
- rejects malformed duplicate object identifiers;
- rejects expired and consumed grants;
- consumes the grant on one successful sequential use;
- projects only `id` and `summary` fields;
- requires bounded evidence before the high-impact effect;
- describes adapter and grant controls as partially independent while naming their shared runtime/operator failure domain.

Header filtering, private addressing, an internal route name, UI hiding, another identical check, or a reusable global signed assertion would not alone restore this property.

## Setup

Use Python 3.11 or newer in a disposable virtual environment:

```text
python -m venv .venv-1-3
. .venv-1-3/bin/activate
python -m pip install -r labs/1.3/1.3-trust-boundaries/requirements.txt
```

On Windows PowerShell, activate the environment from its `Scripts` directory. Installation is setup, not lab evidence.

## Run the vulnerable/fixed pair

From the repository root:

```text
python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl vulnerable

python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl fixed
```

Expected results for the authored fixture with Python 3.12.13 and pytest 9.1.1:

- vulnerable: **10 intended failures, 10 passes**;
- fixed: **20 passes**.

The vulnerable failures are expected property evidence. An import error, syntax error, missing dependency, unexpected collection total, or unrelated failure is an environment/fixture problem and must be resolved before analysis.

## Evidence map

| Test family | Mode | Property / oracle | Expected vulnerable behavior |
|---|---|---|---|
| Exact scoped worker export | Normal | Allow exact A1/A2 summaries | Passes; keeps valid function visible |
| Ordinary public / service label alone | Negative | Deny and return no summaries | Passes; isolates the triggering conjunction |
| Public internal metadata | Abuse | Public cannot become worker; no output | Fails; requester metadata creates worker effect |
| Unknown registration / grant | Negative | Unknown denies | Passes; vulnerable variant is selective, not random |
| Worker binding | Abuse | Worker B cannot use Worker A grant | Fails |
| Tenant / object / action binding | Negative and abuse | No widening; empty output | Three distinct failures |
| Expiry instant / later expiry / replay | Failure-state and abuse | Only a grant strictly before expiry and not yet consumed works | Three distinct failures |
| Evidence unavailable | Failure | Effect denies; grant remains unused | Fails; vulnerable effect silently proceeds |
| Duplicate IDs or non-collection scope | Negative | Malformed scope denies cleanly | Passes |
| Summary projection / safe evidence | Normal and privacy regression | No bodies or bearer material | Passes |
| Dependency analysis | Counterfactual/design evidence | Shared failure named; no false independence | Fails |
| AST safety boundary | Safety | No network/file/process execution path | Passes |

## Learner workflow

1. Read this file and `tests/test_boundary.py`; do not read `fixed/surface.py` or the examiner key.
2. Draw the public and worker entry paths, trusted sources, enforcement point, output, and evidence flow.
3. Predict which tests should pass and fail on the vulnerable variant and why.
4. Run the vulnerable command. Record exact environment, exit code, totals, and names.
5. For every intended failure, separate invariant, preconditions, trigger, root cause, impact, prevention, detection, recovery, and residual.
6. Group failures by provenance, worker binding, tenant/action/object scope, lifecycle, evidence, and common-mode claim.
7. Propose the minimum structural repair and at least three plausible non-fixes before opening the fixed tree.
8. Read `fixed/surface.py` and both `SECURITY.md` files. Map each changed assumption to tests and diagram flows.
9. Run the fixed command and explain why each previously forbidden effect is now absent while normal export remains usable.
10. In a disposable copy, remove one protection, predict the exact changed oracle, and run the local tests. Never edit the course variants in place.
11. Record what the lab still does not prove.

## Causal worksheet

For each intended failure, complete:

| Flow/test | Required property | Preconditions | Trigger | Root cause | Impact | Structural prevention | Detection | Recovery | Residual |
|---|---|---|---|---|---|---|---|---|---|

Reject these shallow diagnoses:

- “The test failed because it returned true.”
- “The header is spoofable, so block it.”
- “Authorization bug.”
- “Use zero trust.”
- “Add a WAF/mTLS/container.”

A competent row identifies the false trusted source or missing scope/lifecycle/mediation rule, the exact forbidden output/state, the trusted structural replacement, an oracle, and where the local proof stops.

## Five evidence modes

- **Normal:** exact registered worker/grant/tenant/action/object scope; summary-only output; bounded event.
- **Negative:** ordinary public, service label alone, unknown registration/grant, malformed duplicates, wrong action/tenant/object scope.
- **Abuse:** public metadata promotion, another worker’s grant, same-tenant widening, cross-tenant use, replay.
- **Failure/state:** expiry and evidence-sink outage. Persistent race, crash, queue, and clock behavior are deferred.
- **Counterfactual:** dependency-classification assertion plus learner mutation of adapter, scope, lifecycle, or evidence behavior.

Every denial should produce empty output. The evidence-failure test also asserts that the unused grant remains unused. Allowed output is checked for exact fields. A status-only oracle would miss these effects.

## Safe counterfactual examples

Use a temporary copy and change only one thing:

- remove worker-to-grant equality;
- replace exact object-set comparison with tenant-only scope;
- skip the `used` transition;
- let `public_export` call the worker helper;
- proceed when `evidence_available` is false.

Before changing code, state which test must change and which unrelated tests must remain stable. If the prediction is wrong, update the dependency model rather than adding an indiscriminate assertion.

## Reset and cleanup

The pytest fixture imports a fresh selected module for every test, so in-memory grant consumption and events do not leak across tests. A replay case performs both uses inside one test intentionally.

Delete disposable practice copies and the disposable virtual environment when finished. If you accidentally edited a course variant, restore only this lab directory from version control or re-download the repository. Do not perform a destructive repository-wide reset.

## Operations and recovery

A production design would correlate worker registration, grant issue/use/revoke, adapter, action, tenant, object count, decision reason, enforcement point, model version, and effect completion without copying note bodies or bearer grants.

If public-to-worker confusion were observed:

1. disable the affected export adapter/path and revoke implicated grant/registration scope;
2. enumerate every public, worker, administrative, retry, restore, and alternate helper sharing the provenance or broad credential assumption;
3. determine tenants, objects, fields, time window, egress, and evidence gaps actually reachable;
4. repair provenance construction and effect mediation, not only the observed metadata;
5. rotate/revoke affected abilities and reconcile released outputs/state;
6. restore trustworthy evidence and run all five modes;
7. update the invariant, authority matrix, flows, surface inventory, TCB, blast radius, signals, and review triggers.

Confidentiality recovery cannot undo a prior release. Say what remains uncertain.

## Limits and review triggers

Passing this lab does not prove:

- HTTP, proxy, TLS, DNS, private-network, routing, or header normalization behavior;
- cryptographic workload identity, secret storage, certificate/key rotation, or cloud IAM;
- queue authenticity, duplication, retry, ordering, cancellation, or dead-letter behavior;
- persistent/atomic grant consumption, transaction isolation, concurrency, or clock correctness;
- database roles, row security, cache keys, backups, restore paths, or cross-tenant storage isolation;
- process/container/sandbox isolation, host compromise resistance, or network egress control;
- durable, ordered, tamper-resistant, privacy-compliant evidence;
- operator, build, dependency, provider, or control-plane compromise resistance;
- complete SecureCollab or ASVS compliance.

Reopen the model when any of those mechanisms is introduced, when a new export/aggregate/admin path appears, when worker authority expands, when evidence failure behavior changes, or when an incident/test shows an unmodeled path.
