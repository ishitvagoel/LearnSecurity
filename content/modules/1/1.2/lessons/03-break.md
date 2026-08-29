# 1.2-LO-03 — Break ambient authority and incomplete mediation locally

**Kind:** mechanism-lab
**Loop step:** 3 Break
**Lab:** `labs/1.2/1.2-authority-matrix` — local course files and synthetic data only
**Standards:** Saltzer and Schroeder complete mediation, fail-safe defaults, least privilege, and separation of privilege (1975, seminal); OWASP ASVS 5.0.0 `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.3.1`, and `v5.0.0-8.4.1`.

## Which forbidden effects can a valid identity still cause?

The lab deliberately gives legitimate synthetic users too much ambient authority. It contains no HTTP server and no real account. The security failure occurs inside a small Python model, which lets you see policy cause and effect without turning the exercise into a target walkthrough.

The invariant under test is:

> Every in-scope operation must obtain a current positive decision over subject, object, action, tenant, and relevant authority state. Unknown cases deny.

The vulnerable implementation violates that invariant in several ways. Do not reduce them to “missing if statements.” Group them by authority failure.

## Authorized boundary

Only files under `labs/1.2/1.2-authority-matrix/` are in scope. The users, tenants, notes, approvals, and timestamps are synthetic. No socket is opened, no credential is used, and no outbound request is needed.

Do not adapt the exercise to a public site, employer system, classmate deployment, or real tenant. The in-process calls provide all evidence required by this lesson.

## Run the two selected implementations

From the repository root, create a disposable environment and install the pinned lab dependency if needed:

```text
python -m venv .venv-1-2
. .venv-1-2/bin/activate
python -m pip install -r labs/1.2/1.2-authority-matrix/requirements.txt
```

Then run:

```text
python -m pytest labs/1.2/1.2-authority-matrix/tests --impl vulnerable

python -m pytest labs/1.2/1.2-authority-matrix/tests --impl fixed
```

The vulnerable run must fail selected forbidden-outcome tests. The fixed run must pass. A syntax error, missing package, import failure, or wrong path is an environment problem, not successful security evidence.

## Read failures as matrix counterexamples

The suite contains both allow and deny cells. Expected allow cells matter: a policy that denies everyone is fail-closed but does not implement the product. Expected deny cells reveal overbroad or stale authority.

The vulnerable fixture is designed to expose these failure shapes:

| Failure shape | Authority question |
|---|---|
| Cross-tenant direct read | Why did authentication become permission on this object? |
| Cross-tenant aggregate listing | Which alternate release path skipped object/field mediation? |
| Cross-tenant administrator delete | Where was tenant scope lost when a role compressed the matrix? |
| Revoked member read | Which stale identity or cached fact survived the authority transition? |
| One-person bulk-export approval | Are the claimed independent conditions actually required and distinct? |
| Unknown action allowed | Why did absence of a positive rule become success? |

Do not open the fixed implementation immediately. First map each failing test to a cell:

```text
subject × action × object × state/time -> expected decision
```

Then identify the attribute source. A decision can have the right shape and still fail if the tenant, role, or object classification came from the requester.

## Build a causal diagnosis

For each failed test, complete this table.

| Layer | Question |
|---|---|
| Required property | Which exact effect should have been forbidden? |
| Root cause | Which authority relation was absent, ambient, overbroad, stale, or default-allow? |
| Preconditions | Which legitimate identity, object state, role, or approval already existed? |
| Trigger | Which operation and input caused the effect? |
| Impact | Which confidentiality, integrity, accountability, or tenant-isolation invariant failed? |
| Prevention | Which positive current rule and enforcement point would restore the cell? |
| Detection | Which privacy-safe decision evidence could reveal the attempt or success? |
| Recovery | Which authority, data, alternate paths, and tests must be repaired or revisited? |

“The test expected `None`” is not the root cause. “The function did not compare tenants” is closer, but still incomplete if the larger issue is that each operation invents its own policy. State why the missing comparison represented authority, where it belongs, and which other paths need the same meaning.

## Trace one example without jumping to the patch

Suppose Admin A deletes Note B-4.

- Admin A is correctly authenticated.
- The role `admin` may legitimately allow selected high-impact actions.
- The object belongs to Tenant B.
- The vulnerable decision expands `admin` without tenant scope.
- The forbidden state change occurs because the role became ambient global authority.

A denylist for Admin A would block this one fixture but fail for Admin A2 or a future tenant. A client-supplied `tenant_id` comparison would let the caller choose the authority context. Hiding the delete control would leave the operation reachable. The structural rule must bind the current server-resolved admin membership to the stored object tenant and exact action.

## Compare the fixed decision path

After completing your diagnosis, inspect the fixed implementation. For each repaired case, find:

1. where the current subject is resolved;
2. where the stored object or target tenant is resolved;
3. where the action is explicitly matched;
4. where state such as active membership is checked;
5. where an unknown or invalid case denies;
6. where the operation consumes the decision before exposing or mutating state.

The fixed file is intentionally small. It is not a production policy framework. It does not prove that a FastAPI route, PostgreSQL query, worker, cache, or mobile client would use the same rule.

## Why the illustrative export case exists

The lab models a high-impact tenant export that requires two distinct current Tenant A administrators. This is an exercise policy chosen to make separation of privilege observable. It does not assert that every export in every product needs two people.

The vulnerable implementation accepts one approval. The fixed implementation requires the documented conditions and rejects duplicate, inactive, cross-tenant, or insufficient approvers. The lesson is that “two-person approval” must become a testable authority relation; a second button, second field, or repeated identity is not independent authority.

## Practice modification

Copy the fixed directory to a temporary location outside the fixture directories. Make one change at a time:

1. remove the active-membership check;
2. treat all admins as global;
3. change the final unknown-action branch to allow;
4. make `list_notes` return storage results before policy filtering;
5. count duplicate approver IDs as separate approvals.

Run the suite after each change and record which property test detects it. If a meaningful defect is not detected, record a coverage gap. Do not add a superficial assertion merely to turn the suite green; add a matrix cell and a property oracle.

## Lab limits and transfer

The fixture has no cryptographic capability, no network boundary, no session cache, no transaction, and no distributed worker. A process with full access to the in-memory dictionaries remains powerful. Passing the suite shows that selected service operations consume the modeled policy correctly.

For transfer, imagine the same decision is made once, placed in a queue, and used ten minutes later by a worker. Which subject is acting? Which authority version applies? What if membership was revoked in the interval? A signed queue message may establish message integrity, but it does not by itself answer those authority questions.
