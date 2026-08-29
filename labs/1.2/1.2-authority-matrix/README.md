# Module 1.2 lab — authority matrix under pressure

This lab teaches how valid identity becomes unsafe ambient authority when policy omits object, tenant, action, state, time, or independent approval. It uses two small local Python modules so the learner can trace exact subject–action–object decisions without a web target.

## Authorized scope

Only files under this lab directory are in scope. All tenants, users, notes, roles, approvals, and values are synthetic. Running the fixture and its tests starts no server, opens no socket, reads no credential, and performs no outbound action. The separate dependency-install command may contact the package index configured for `pip`; use an approved mirror or pre-populated cache when your environment requires offline installation.

Do not adapt the calls to a public site, employer system, classmate deployment, cloud account, repository, CI provider, or real tenant. No exploit payload is needed.

## Security invariant

Every in-scope security-relevant operation obtains a current, positive decision over server-resolved subject, object, action, tenant, and relevant authority state. Missing or unknown authority denies.

The modeled operations are:

- read a note body;
- list note summaries;
- delete a note as a tenant-scoped administrator;
- decide whether an illustrative high-impact tenant export has the documented approvals;
- reject an action the policy does not know.

The export rule requiring two distinct current tenant administrators is an exercise policy chosen to make separation of privilege observable. It is not a universal product recommendation.

## Root causes in the vulnerable variant

The vulnerable policy:

- treats any known identity as current read and list authority;
- releases every tenant’s summaries from the aggregate path;
- expands `admin` without preserving tenant scope;
- ignores revoked membership state;
- accepts one or duplicate approval as if independent conditions existed;
- defaults an unknown action to allow.

These are related but distinct failures: ambient authority, incomplete mediation, overbroad role compression, stale authority, cosmetic separation of privilege, and fail-open policy.

## Structural fix

The fixed policy:

- resolves active subject state independently from authentication;
- resolves the stored note before deciding;
- matches explicit actions and denies unknown ones;
- binds read, list, and delete effects to the server-resolved tenant;
- preserves action scope when applying the admin role;
- requires two distinct current administrators of the target tenant for the illustrative export decision;
- makes every modeled operation consume the decision before release or mutation.

A denylist of fixture usernames, random note IDs, hidden buttons, authentication middleware, route naming, or a second approval field without identity/scope checks would not restore the invariant.

## Setup

Use Python 3.11 or newer in a disposable virtual environment:

```text
python -m venv .venv-1-2
. .venv-1-2/bin/activate
python -m pip install -r labs/1.2/1.2-authority-matrix/requirements.txt
```

On Windows PowerShell, activate the environment using its `Scripts` directory.

## Run the vulnerable and fixed pair

From the repository root:

```text
python -m pytest labs/1.2/1.2-authority-matrix/tests --impl vulnerable

python -m pytest labs/1.2/1.2-authority-matrix/tests --impl fixed
```

Expected result:

- vulnerable: selected forbidden-outcome tests fail while valid same-tenant operations still pass;
- fixed: the entire suite passes.

The intended observation is not “red versus green.” Record which matrix cells fail, why the vulnerable rule permits them, which structural rule repairs them, and what the fixture still does not prove. A missing package, bad path, syntax error, or import failure is an environment failure.

## Learner workflow

1. Read the module invariant and the tests, but not the fixed implementation or examiner key.
2. Run the vulnerable variant and translate each failure into `subject × action × object × state -> decision`.
3. Group failures by root cause: ambient identity, alternate path, unscoped role, stale state, insufficient separation, or fail-open default.
4. Propose one structural policy and enforcement change per group.
5. Inspect the fixed implementation and compare its trusted attribute sources, explicit rules, and enforcement order with your proposal.
6. Copy the fixed file to a temporary location, remove one protection at a time, and check whether the relevant property test fails.
7. Record undetected defects as assurance gaps rather than adding unsupported claims.

Do not edit the vulnerable or fixed course fixtures in place for the practice modification.

## Evidence modes represented

- **Normal:** same-tenant member read, scoped admin delete, and documented two-approver export decision.
- **Negative:** cross-tenant read/delete, revoked subject, unknown identity/object/action, and insufficient approval.
- **Abuse:** aggregate list leakage, duplicate approval, cross-tenant approval, and retired approval.
- **Failure/state:** inactive current membership and unknown policy state. Distributed outage, transaction, cache, and clock failures are explicit later-module gaps.

## Operations and recovery

A real product would record privacy-safe decision metadata such as subject, action, object ID, tenant, policy/authority version, decision reason, enforcement point, timestamp, and correlation ID. It must not copy note bodies, passwords, tokens, raw authorization headers, or unnecessary personal attributes.

If an over-authority failure were found, containment would revoke the implicated authority and affected path; investigation would enumerate every direct, aggregate, admin, cached, background, retry, export, and restore effect sharing the rule; recovery would repair the root cause, reconcile state and exposed outputs, and rerun the matrix and lifecycle evidence.

## Reset

The test loader imports a fresh selected module for each test, so mutations to in-memory notes do not persist between tests. Delete temporary practice copies and the disposable virtual environment when finished. If a fixture file was edited accidentally, restore only this lab directory from version control or re-download the repository; do not perform a destructive repository-wide reset.

## Limits and review triggers

Passing this lab does not establish complete authorization for a web application. Reopen the model when adding:

- FastAPI routes, GraphQL, serialization, PostgreSQL, row policies, or transactions;
- sessions, cached decisions, self-contained claims, capabilities, or clock-based expiry;
- workers, queues, retries, exports, caches, webhooks, or restore paths;
- files, external sharing, support impersonation, mobile offline state, or public resources;
- production identities, real data, cloud administrators, or emergency access.

Each change adds subjects, objects, paths, state, time, or common mechanisms that the local fixture does not cover.
