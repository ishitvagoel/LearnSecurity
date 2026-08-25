# 1.1-LO-05 — Verify forbidden outcomes, not control presence

**Kind:** verification-lab  
**Loop step:** 5 Verify

## Turn the property into an oracle

A security test needs an oracle: a rule that decides whether the observed result violates the invariant. “The middleware ran” is a mechanism oracle. “Tenant B received zero bytes derived from Tenant A’s note body” is a property oracle.

For each catalogue row, write the forbidden outcome before choosing a test tool.

| Invariant shape | Forbidden outcome | Property evidence | Misleading evidence |
|---|---|---|---|
| Cross-tenant confidentiality | A B principal obtains any A note-body value through an in-scope route | Negative tests over every read/export route and captured logs | Authentication middleware is installed |
| Membership integrity | A non-admin or stale admin changes membership | State-transition tests with current and revoked authority | The UI hides the button |
| Accountability | A role grant completes without privacy-safe actor, tenant, action, target, decision, and correlation evidence | Assert an event is emitted and survives the stated failure | “Logging enabled” configuration |
| Bounded availability | One tenant’s abusive workload prevents ordinary reads outside the stated budget | Load/failure experiment with per-tenant observations and recovery timing | A single health check returns 200 |
| Privacy deletion | Data remains accessible beyond declared retention or restore behavior | Live, cache, export, and restore-path evidence | DELETE returned success |

The later modules implement many of these tests. In Module 1.1, your task is to specify evidence precisely enough that implementation can be judged.

## Four evidence modes

Every important row needs more than a happy path.

1. **Normal:** an authorized action succeeds and produces the intended state and evidence.
2. **Negative:** a clearly unauthorized or invalid action is denied without partial effect.
3. **Abuse:** a capable adversary varies identifiers, order, volume, or context within the lab model.
4. **Failure:** dependencies time out, retries occur, evidence storage fails, or state is restored.

These modes expose different assumptions. A negative test may prove that one route denies Tenant B while a failure test reveals that a cache or restore path leaks stale Tenant A data.

## Trace one evidence argument

For a proposed cross-tenant read test, record:

- **Initial state:** Tenant A and Tenant B exist; each has a member; note N belongs to A.
- **Attacker capability:** B’s member has a valid session and can choose any note identifier and request shape.
- **Action:** request N through each in-scope read path.
- **Oracle:** no response body, status detail, timing-class claim, log accessible to B, or export contains N’s body. Be precise about which side channels are in scope.
- **Expected state:** N and membership remain unchanged; a privacy-safe denial event may exist.
- **Counterfactual:** removing tenant binding from the policy would make at least one test fail.
- **Limits:** this evidence does not cover operator database access or future offline caches.

The counterfactual is important. If the test passes with the enforcement mechanism removed, it may not exercise the property.

## Evidence quality ladder

Classify each proposed item:

| Level | Evidence | Value |
|---|---|---|
| 0 | “We follow best practices” | No observable claim |
| 1 | Configuration or control presence | Shows intent, not outcome |
| 2 | Test observes a property under stated preconditions | Useful but bounded |
| 3 | Independent evidence spans alternate paths and failure modes | Stronger assurance, still not universal proof |

Do not call Level 1 evidence useless; configuration review can expose defects. Do not call it proof of the invariant.

## Practice: build a forbidden-outcome matrix

Add a table to your catalogue with one row per invariant:

| ID | Normal | Negative | Abuse | Failure | Oracle | Residual gap |
|---|---|---|---|---|---|---|

Requirements:

- at least one case must change time or retained state;
- at least one must challenge an alternate route or component;
- at least one must verify privacy-safe detection evidence;
- at least one must describe what happens if evidence collection itself fails;
- no case may target a public or third-party system.

For each case, say whether it is executable now, executable in a later named module, or a review-only claim. Future evidence is not current proof.

## Common verification errors

- **Testing a label:** asserting a function called authorize was invoked.
- **One-object sampling:** testing only a random object that happens to belong to the caller.
- **No state oracle:** checking a status code while a forbidden write partially commits.
- **No alternate path:** testing the UI but not the API, export, retry, or restore route.
- **Secret-bearing evidence:** logging the protected value so a test can find it.
- **Universal conclusion:** turning one passing test into “tenant isolation is guaranteed.”
- **Mocking away the property:** replacing the actual policy or persistence boundary with a permissive mock.

## Review checkpoint

A reviewer should be able to answer three questions from your matrix:

1. What observation would falsify the invariant?
2. Which assumptions are not exercised?
3. Which future product change invalidates the evidence?

If any answer is missing, the row remains developing.
