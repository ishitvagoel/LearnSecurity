# A broken admission must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## If you cannot test it, it is still a slogan

"We use Kubernetes" is not evidence. "CIS is green" is a tool observation. The check is: `pod_ok("cluster-admin")` is false and `"app"` may run. That cluster-admin observation must be **false** on the broken files and **true** on the repaired files. Do not apply manifests to a live cluster.

## Picture: a broken admission must fail the check

A test that only counts passing tests can pass while `pod_ok("cluster-admin")` still returns true. This check asks whether an app pod granted cluster-admin still counts as a passing control. Broken must fail that question. Repaired must pass it.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: cluster-admin runs]
  X["repaired files --impl fixed"] --> P[Must pass: cluster-admin denied]
```

If both pass, the test is not looking at cluster-admin. If both fail, the fix is not structural or the check is wrong.

## Four modes, even for a role string

| Mode | Must show for this topic |
|---|---|
| Normal | `app` → may run (may pass on both) |
| Wrong input | cluster-admin → cannot run; broken files must fail |
| Abuse | Unknown roles still deny (fail closed) |
| Not claimed | A live managed cluster; a CIS score; an assurance gate; that `"app"` is least privilege |

The file is `labs/10.3/10.3-lab/tests/test_property.py`. The test `test_cluster_admin_pod_is_denied` is a **what-must-not-happen** test: always-true `pod_ok` is not allowed to count as a passing control.

Honest `"app"` may pass on both implementations. That does not excuse the cluster-admin deny test. If the broken files do not fail `test_cluster_admin_pod_is_denied`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/10.3/10.3-lab/tests --impl vulnerable
python3 -m pytest labs/10.3/10.3-lab/tests --impl fixed
```

A test that only greps `namespace:` in a chart without calling `pod_ok("cluster-admin")` is not this topic's evidence. This practice never opens a live cluster.

## What the tests do not prove

- A restricted pod profile on the real spec
- Network-policy egress
- Instance metadata blocked
- Helm chart supply chain
- Documented cluster-API retry (extra, advanced)
- An assurance gate complete

Record those as leftover or later topics, not as silent passes.

## Practice

Run both this session from the lab directory if needed:

```text
python3 -m pytest labs/10.3/10.3-lab/tests --impl vulnerable
python3 -m pytest labs/10.3/10.3-lab/tests --impl fixed
```

Paste nothing from answer keys. Write fail/pass into your notes next to the cluster-admin row. Reject a "test" that only greps `namespace:` in a chart without calling `pod_ok("cluster-admin")`.

## Use it somewhere new

A clinic example: a test that only asserts "namespace exists" is not this topic. A live kube-apiserver is out of scope.

## What this page is not doing

Do not treat a live cluster screenshot as proof. Do not log kubeconfig. Answer keys are not on this site. This page does not mark you as finished.
