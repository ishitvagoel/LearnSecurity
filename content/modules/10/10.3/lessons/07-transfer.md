# Same idea: clinic app SA is cluster-admin

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

The notes-app scaffolding goes away. You get a **clinic app ServiceAccount that is cluster-admin**. Your job is to rewrite the loop, not to name a bug-list code.

The notes-app sentence was: `pod_ok("cluster-admin")` must be false. Rewrite it for a clinic without changing the fork: cluster-admin denied, app may run. A private namespace is still a name, not isolation.

**Product sketch:** an EHR-lite "the API namespace is private so ClusterRole is fine," plus "we attached a network policy and a CIS Kubernetes scan."

## Picture: same admission loop, clinical object

Renaming "note" to "chart" is not transfer. Rule, allow-list, and leftover change. Putting the app in a private namespace does not put `"app"` in `ALLOWED_ROLES`.

| Notes app this week | Clinic sketch |
|---|---|
| App pod must not be cluster-admin | Clinic API SA must not be cluster-admin |
| `pod_ok("cluster-admin")` false | Same call — cluster-admin still denied |
| Namespaced `"app"` may run | Same allow-list — local practice files only |
| Compromised container / malicious chart | Same actors — **not** a live clinic cluster |
| Namespace / network policy / CIS scan | Same inputs — not the admission decision |

```mermaid
flowchart LR
  Ns[private namespace] --> Belief[isolated]
  Sa[cluster-admin SA] --> Reality[control plane]
```

If the namespace is "private" while `pod_ok` is always true, the rule is gone. A network policy, a restricted pod profile, and a CIS scan do not put `"app"` in `ALLOWED_ROLES`. Serverless IAM `*` is the same god-mode grain on a different object — name it, do not attack a live cloud account here. A container-stack guide names five layers; it does not make a managed cluster secure by default. Documented cluster-API retry is extra, advanced work, not this check.

The clinic rewrite still has to keep the notes-app fork: cluster-admin denied, app may run. Adding a namespace without an allow-list leaves `pod_ok("cluster-admin")` true. The local pytest analogue is `test_cluster_admin_pod_is_denied` — on a practice, not a live cluster.

## Prompt — clinic app SA is cluster-admin

Rewrite the notes-app sentence. Include:

1. who can act (compromised container / malicious chart — not a live clinic cluster);
2. what you trust (allow-listed namespaced role is the promise; namespace, network policy, restricted pod profile, and CIS are not);
3. what must not happen (`pod_ok("cluster-admin")` true, not a legal label);
4. a test idea on a **local** practice files only (no live kube-apiserver);
5. leftover (break-glass elective, metadata hop, documented cluster-API retry);
6. whether engineers read the denial (say cluster-admin refused, not color only).

Use fake labels. Do not use real patient names.

Also name serverless IAM `*`.

## What is not good enough

| Reject | Why |
|---|---|
| "we have a network policy" | Egress, not who-is-allowed on the API |
| Live cluster / cloud takeover tutorial | Course rules |
| "restricted pod profile so who-is-allowed is done" | Pod spec is not API authorization |
| "CIS scan green" | Benchmark, not the predicate |
| "assurance gate complete" | Forbidden stamp |

## Practice

One page. No answer keys. `labs/10.3/10.3-lab` is the only running system you may break. Do not apply manifests to a live cluster.

## What this page is not doing

Live-cluster attacks. Real cloud-account takeover. Claiming you finished an assurance gate from this page.
